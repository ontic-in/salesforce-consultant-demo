# US-008: Automation Flows

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs three record-triggered flows to automate critical support operations:
1. **VIP Case Detection** — Gold/Platinum customers with 2+ open cases get bumped to Critical and routed to Senior Queue with Chatter notification
2. **New Customer Priority Boost** — Cases from accounts less than 30 days old auto-set to High priority (unless already Critical from VIP)
3. **Auto-Create Follow-Up Task** — Every new case generates a task for the assigned agent with a priority-based due date

These 3 flows use the full Enable tier allocation (max 3 record-triggered flows).

## Worksheet References
- Section 10, Flow 1 (VIP Detection): *"New case where Account Customer Tier = Gold/Platinum AND 2+ open cases → Critical priority, Senior Queue, Chatter post"*
- Section 10, Flow 2 (New Customer): *"New case where Account Created Date within 30 days → High priority (VIP takes precedence)"*
- Section 10, Flow 3 (Auto Task): *"New case after assignment → Task 'Initial Response Required', due date by priority: Critical=today, High=tomorrow, Medium=3 days, Low=5 days"*
- Section 10, VIP Precedence: *"If both new AND VIP with multiple cases, the VIP rule should win"*

## Solution Design

### Flow 1: VIP Case Detection

| Setting | Value |
|---|---|
| Type | Record-Triggered Flow (After Save) |
| Object | Case |
| Trigger | Create |
| Entry Criteria | Account.Customer_Tier__c IN (Gold, Platinum) |

**Flow Logic:**
1. Get Records: Count open Cases on same Account where Status != Closed
2. Decision: If count >= 2 (including current case)
3. Update Record: Set Priority = Critical
4. Update Record: Set Owner = Senior_Support_Queue (Queue ID)
5. Post to Chatter: "VIP Alert: {Account.Customer_Tier__c} customer {Account.Name} with {count} open cases — routed to Senior Queue"

> **Design Decision:** After-Save trigger (not Before-Save)
> **Rationale:** Flow needs to query other Cases on the Account (Get Records), which requires the current Case to be saved first. Also needs to post to Chatter (side effect), which is only allowed in After-Save context.

### Flow 2: New Customer Priority Boost

| Setting | Value |
|---|---|
| Type | Record-Triggered Flow (Before Save) |
| Object | Case |
| Trigger | Create |
| Entry Criteria | None (evaluate all new cases) |

**Flow Logic:**
1. Get Records: Get Account.CreatedDate for the Case's Account
2. Decision: If Account.CreatedDate > (TODAY - 30 days) AND Priority != Critical
3. Update Record (trigger record): Set Priority = High

> **Design Decision:** Before-Save trigger with "Priority != Critical" guard
> **Rationale:** VIP Detection (After-Save) runs after this flow. However, on initial creation, if the case would be both VIP and new customer, VIP's After-Save will override to Critical. The guard prevents this flow from downgrading Critical back to High on any subsequent re-evaluation.

### Flow 3: Auto-Create Follow-Up Task

| Setting | Value |
|---|---|
| Type | Record-Triggered Flow (After Save) |
| Object | Case |
| Trigger | Create |
| Entry Criteria | None (all new cases) |

**Flow Logic:**
1. Decision: Check Case Priority
   - Critical → Due Date = TODAY
   - High → Due Date = TODAY + 1
   - Medium → Due Date = TODAY + 3
   - Low → Due Date = TODAY + 5
2. Create Record: Task
   - Subject: "Initial Response Required"
   - WhatId: Case ID
   - OwnerId: Case Owner
   - ActivityDate: Due Date (from decision)
   - Priority: matches Case priority

### Execution Order

| Order | Flow | Trigger Type | Why This Order |
|---|---|---|---|
| 1 | New Customer Priority Boost | Before Save | Sets High priority before record saves |
| 2 | VIP Case Detection | After Save | Overrides to Critical + reassigns (needs saved record for Get Records) |
| 3 | Auto-Create Follow-Up Task | After Save | Creates task with FINAL priority (after VIP override) |

> **Design Decision:** Flow 3 should run AFTER Flow 1 (VIP Detection) in After-Save
> **Rationale:** Task due date depends on final priority. If VIP flow changes priority to Critical, the task should be due today (not based on the original priority). Configure Flow 3 with a higher trigger order number than Flow 1.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Record-triggered flows | SDO flows exist (not for RL) | Create 3 new flows | Create |
| Account.Customer_Tier__c | Created in US-002 | Dependency | US-002 must complete first |
| Case.Product__c | Created in US-003 | Dependency | US-003 must complete first |
| Senior_Support_Queue | Created in US-004 | Dependency | US-004 must complete first |
| Case.Customer_Tier__c | Created in US-003 | Dependency | US-003 must complete first |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Email notification for VIP | Parking lot — Marcus: "start with Chatter only; revisit if adoption low" |
| Auto-close after inactivity | Not discussed; potential Phase 2 |
| Scheduled flows | Not needed; all flows are record-triggered |
| Approval processes | Out of scope — Elevate tier |
| Flow-based email alerts (beyond Chatter) | Escalation emails handled by escalation rules (US-005) |
| Additional flows | All 3 Enable tier flow slots used |

## Implementation Checklist

### Phase 1: Flow 2 — New Customer Priority Boost (Before Save)

- [ ] Create Flow metadata for New_Customer_Priority_Boost:
  - Record-Triggered Flow on Case, Before Save, on Create
  - Get Account.CreatedDate
  - Decision: CreatedDate > (TODAY - 30) AND Priority != Critical
  - Assignment: Priority = High
- [ ] Deploy: `sf project deploy start --source-dir force-app/main/default/flows/New_Customer_Priority_Boost*`
- [ ] Verify: Create case on account created <30 days ago → priority auto-set to High

### Phase 2: Flow 1 — VIP Case Detection (After Save)

- [ ] Create Flow metadata for VIP_Case_Detection:
  - Record-Triggered Flow on Case, After Save, on Create
  - Entry Criteria: Account.Customer_Tier__c IN (Gold, Platinum)
  - Get Records: Count open cases on Account
  - Decision: If count >= 2
  - Update: Priority = Critical, Owner = Senior_Support_Queue
  - Post to Chatter on Case record
- [ ] Deploy flow
- [ ] Verify: Create 2nd case for Gold account → priority = Critical, owner = Senior_Support_Queue, Chatter post visible

### Phase 3: Flow 3 — Auto-Create Follow-Up Task (After Save)

- [ ] Create Flow metadata for Auto_Create_Follow_Up_Task:
  - Record-Triggered Flow on Case, After Save, on Create
  - Trigger order: AFTER VIP_Case_Detection
  - Decision on Priority → set due date
  - Create Task: "Initial Response Required", assigned to Case Owner, due date by priority
- [ ] Deploy flow
- [ ] Verify: Create case → task created with correct due date based on final priority

### Phase 4: Integration Testing

- [ ] Test VIP + New Customer scenario: Gold account <30 days old with 2+ cases → Priority=Critical (not High), routed to Senior Queue, task due=today
- [ ] Test normal new case: Standard account, Medium priority → task due in 3 days
- [ ] Test new customer: Account <30 days, no VIP → Priority=High, task due tomorrow
- [ ] Verify Chatter post appears on VIP cases

### Secure & Make Usable

- [ ] Verify all 3 flows are active
- [ ] Confirm flow execution order (Before Save → After Save, ordered correctly)
- [ ] Verify no conflicting SDO flows on Case object
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Chatter notification text** — Is the proposed format acceptable? "VIP Alert: {Tier} customer {Account} with {X} open cases — routed to Senior Queue"
2. **Task due dates** — Are business days or calendar days for task due dates? (Critical=today, High=tomorrow, Medium=3 days, Low=5 days)
