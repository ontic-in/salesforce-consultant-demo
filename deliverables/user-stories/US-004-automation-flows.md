# US-004: Automation Flows (3 Flows)

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs three record-triggered flows to automate case handling — all confirmed in the discovery call. These use all 3 Enable tier flow slots:

1. **VIP Detection & Alert** — When a Gold/Platinum customer opens a case and already has 1+ other open cases (2+ total), bump to Critical priority, route to Senior Support Queue, and post a Chatter alert.
2. **New Customer Prioritization** — When a case is created on an account less than 30 days old, auto-set priority to High. VIP rule takes precedence if both apply.
3. **Auto-Task Creation** — When a case is assigned to an agent, create an "Initial Response Required" task with a priority-based due date.

Additionally, this story includes creation of the **Senior Support Queue** (members: Marcus Webb, Priya Sharma, Jake Torres) since it is required by Flow 1 and queue setup is not covered in other selected stories.

## Worksheet References
- Section 10, Automation 1 (VIP): *"✅ Confirmed: Gold or Platinum customer opens a case AND already has 1+ other open cases (2+ total including the new one)"*
- Section 10, Automation 1 Actions: *"✅ Confirmed: 1. Bump case to Critical priority 2. Route to Senior Support Queue 3. Post Chatter alert"*
- Section 10, Automation 2 (New Customer): *"✅ Confirmed: Case created on an account that is less than 30 days old (regardless of tier)"*
- Section 10, Automation 2 Actions: *"✅ Confirmed: Auto-set case priority to High"*
- Section 10, Automation 2 Precedence: *"✅ Confirmed: VIP rule takes precedence. If customer is both new AND VIP with multiple cases, VIP rule wins → Critical priority."*
- Section 10, Automation 3 (Auto-Task): *"✅ Confirmed: Case is assigned to an agent"*
- Section 10, Automation 3 Actions: *"✅ Confirmed: Auto-create task 'Initial Response Required' assigned to case owner. Due date based on priority: Critical = same day, High = next business day, Normal = 3 business days"*
- Section 6, Senior Support Queue: *"✅ Confirmed: Senior Support Queue (members: Marcus, Priya, Jake)"*

## Solution Design

**Senior Support Queue (prerequisite for Flow 1):**

| Queue | DeveloperName | Object | Members |
|-------|---------------|--------|---------|
| Senior Support Queue | Senior_Support_Queue | Case | Marcus Webb, Priya Sharma, Jake Torres |

**Flow 1: VIP Detection & Alert**

| Attribute | Value |
|-----------|-------|
| Type | Record-Triggered Flow (After Save) |
| Object | Case |
| Trigger | After Insert |
| Entry Condition | Account.Customer_Tier__c IN (Gold, Platinum) |
| Logic | Query open cases for same Account (Status != Closed). If count >= 2 (including new case): update Priority to Critical, update Owner to Senior Support Queue, post Chatter FeedItem. |
| Chatter Message | "VIP Alert: [Tier] customer [Account Name] with [X] open cases — routed to senior queue" |

**Flow 2: New Customer Prioritization**

| Attribute | Value |
|-----------|-------|
| Type | Record-Triggered Flow (Before Save) |
| Object | Case |
| Trigger | Before Insert |
| Entry Condition | Account.Account_Start_Date__c != null AND Account.Account_Start_Date__c > (TODAY - 30) |
| Logic | Set Priority = "High". Before Save runs before After Save, so VIP flow (After Save) can override to Critical if VIP conditions also apply. |
| Precedence | Before Save sets High; After Save VIP flow overrides to Critical if VIP conditions met. Natural execution order handles precedence. |

**Flow 3: Auto-Task Creation**

| Attribute | Value |
|-----------|-------|
| Type | Record-Triggered Flow (After Save) |
| Object | Case |
| Trigger | After Insert, After Update |
| Entry Condition | OwnerId is changed AND OwnerId is a User (not a Queue) |
| Logic | Create Task: Subject = "Initial Response Required", WhoId = Case Contact, WhatId = Case, OwnerId = Case Owner, ActivityDate = based on Priority: Critical = TODAY, High = TODAY + 1, Medium/Low = TODAY + 3 |

**Design Decisions:**
> **Decision:** Flow 2 (New Customer) uses Before Save; Flows 1 and 3 use After Save.
> **Rationale:** Before Save is ideal for same-record field updates (no DML needed). Flow 1 needs After Save because it performs cross-record updates (Chatter post, Owner change via DML). Flow 3 needs After Save to create a related Task record. The natural Before→After execution order means Flow 2 sets High first, then Flow 1 can override to Critical — this handles the VIP precedence requirement without explicit checks.

> **Decision:** Flow 1 VIP detection counts open cases via a Get Records element, not a Roll-Up Summary.
> **Rationale:** Roll-Up Summary fields require Master-Detail relationships. Case→Account is a standard Lookup. A Get Records + count in the flow is the correct approach for Enable tier.

> **Decision:** Flow 3 triggers on Owner change (not just creation) to handle reassignment scenarios.
> **Rationale:** If a case is reassigned from a queue to an agent (or between agents), the new owner should get a fresh "Initial Response Required" task. The entry condition filters out queue ownership to avoid creating tasks when cases are routed to queues.

> **Decision:** Auto-Task due dates use calendar days (TODAY + N), not business days.
> **Rationale:** Flow Builder doesn't natively support business day calculations without complex formulas. Calendar days are acceptable for initial rollout. Confirmed by consultant.

> **Decision:** Senior Support Queue created in this story rather than a separate queue story.
> **Rationale:** Queue setup (Section 6) is not one of the 4 selected stories. The Senior Support Queue is a hard dependency for Flow 1 (VIP routing). Creating it here keeps the story self-contained.

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---------|-----------|
| Auto-close stale cases | No automation capacity — all 3 flow slots committed. Parking lot item. |
| Post-resolution follow-up task | No automation capacity — all 3 flow slots committed. Parking lot item. |
| Email notifications on VIP detection | Marcus: "Let's start with Chatter. If people miss things, we'll add email." |
| SLA timer pausing on "Waiting on Customer" | Requires Entitlement/Milestone features (Elevate tier) |
| Business day calculation for task due dates | Flow Builder limitation — using calendar days. Confirmed acceptable. |
| Core Platform Queue & Integrations Queue | Part of Section 6 queue setup, not in scope for selected stories. Only Senior Support Queue is created here. |
| Assignment Rules (product-based routing) | Part of Section 6, not in scope for selected stories. |

## Implementation Checklist

**Prerequisites (from other stories):**
- [ ] Confirm US-001 is complete (users and roles exist — needed for queue members)
- [ ] Confirm US-002 is complete (Account_Start_Date__c and Customer_Tier__c fields exist on Account)
- [ ] Confirm US-003 is complete (Product_Line__c, Customer_Tier__c formula on Case, case statuses exist)

**Create Senior Support Queue:**
- [ ] Create Queue metadata XML: Senior_Support_Queue, object = Case
- [ ] Deploy Queue to org
- [ ] Add queue members via Data API: Marcus Webb, Priya Sharma, Jake Torres
- [ ] Verify queue exists: `SELECT Id, Name, DeveloperName FROM Group WHERE Type = 'Queue' AND DeveloperName = 'Senior_Support_Queue'`

**Flow 1: VIP Detection & Alert (After Save):**
- [ ] Create Flow XML: Record-Triggered, Case, After Insert
- [ ] Entry Condition: Account.Customer_Tier__c IN ("Gold", "Platinum")
- [ ] Get Records: Open Cases where AccountId = {!$Record.AccountId} AND Status != "Closed" AND Id != {!$Record.Id}
- [ ] Decision: If count >= 1 (meaning 2+ total including current case)
- [ ] Update Record: Set Priority = "Critical"
- [ ] Update Record: Set OwnerId = Senior Support Queue ID
- [ ] Create Record: FeedItem (Chatter post) on Case with VIP alert message
- [ ] Set `<status>Active</status>` in XML
- [ ] Deploy Flow: `sf project deploy start --metadata "Flow:VIP_Detection_Alert"`

**Flow 2: New Customer Prioritization (Before Save):**
- [ ] Create Flow XML: Record-Triggered, Case, Before Insert
- [ ] Entry Condition: Account.Account_Start_Date__c != null
- [ ] Decision: If Account.Account_Start_Date__c > (TODAY - 30 days)
- [ ] Update Record (same record, no DML): Set Priority = "High"
- [ ] Set `<status>Active</status>` in XML
- [ ] Deploy Flow: `sf project deploy start --metadata "Flow:New_Customer_Priority"`

**Flow 3: Auto-Task Creation (After Save):**
- [ ] Create Flow XML: Record-Triggered, Case, After Insert + After Update
- [ ] Entry Condition: OwnerId isChanged AND Owner is User (not Queue)
- [ ] Decision: Priority-based due date calculation (Critical=TODAY, High=+1, Medium/Low=+3)
- [ ] Create Record: Task with Subject="Initial Response Required", OwnerId=Case Owner, ActivityDate=calculated date
- [ ] Set `<status>Active</status>` in XML
- [ ] Deploy Flow: `sf project deploy start --metadata "Flow:Auto_Task_Creation"`

**Verify:**
- [ ] Query `FlowDefinitionView` to confirm all 3 flows are active (`ActiveVersionId != null`)
- [ ] Test Flow 1: Create a case on a Gold account that already has 1 open case → confirm priority bumps to Critical, owner changes to Senior Queue, Chatter post appears
- [ ] Test Flow 2: Create a case on an account with Account_Start_Date__c = today → confirm priority is set to High
- [ ] Test Flow 2 + 1 precedence: Create a case on a new Gold account with 1+ open cases → confirm priority is Critical (VIP overrides new customer)
- [ ] Test Flow 3: Assign a case to an agent → confirm "Initial Response Required" task is created with correct due date
- [ ] Test Flow 3: Assign a case to a queue → confirm NO task is created
- [ ] User verification with client
