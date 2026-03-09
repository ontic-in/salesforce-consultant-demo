# US-005: Escalation Rules

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs time-based escalation rules to ensure cases don't sit unworked. Cases should escalate based on priority — Critical cases get immediate attention (handled by VIP flow in US-008), while High, Medium, and Low cases escalate after specific time thresholds. Escalation notifications go to the case owner's manager (Marcus or Priya) and Lisa for Critical cases. Business hours configuration is needed to drive escalation timing.

## Worksheet References
- Section 4, Critical Escalation: *"Immediately via VIP detection flow"*
- Section 4, High Escalation: *"After 2 hours with no response"*
- Section 4, Medium Escalation: *"After 8 business hours"*
- Section 4, Low Escalation: *"After 24 business hours"*
- Section 4, Notification Recipients: *"Case owner's direct manager (Marcus or Priya) + Lisa for Critical"*
- Section 1, Business Hours: *"❓ Needs Discussion — time zone and exact hours"*
- Section 1, SLA Timing: *"❓ Needs Discussion — business hours vs clock hours"*

## Solution Design

### Business Hours

| Setting | Value | Notes |
|---|---|---|
| Name | Relay Logic Support Hours | |
| Time Zone | ❓ Needs Discussion | US timezone assumed — need confirmation |
| Monday–Friday | ❓ 9:00 AM – 5:00 PM (assumed) | Needs confirmation |
| Saturday–Sunday | Closed | |
| Holidays | ❓ Needs Discussion | Which holidays to observe |

> **Design Decision:** Configure business hours first; escalation rules reference them
> **Rationale:** Worksheet says escalation times are in "business hours" (Medium: 8 business hours, Low: 24 business hours). Business hours calendar determines when the clock runs.

### Escalation Rules

| Rule Name | Entry # | Criteria | Escalation Time | Action | Notes |
|---|---|---|---|---|---|
| Relay_Logic_Escalation | 1 | Priority = High AND Status = New | 2 business hours | Reassign to Senior_Support_Queue + Notify manager | High priority unworked |
| | 2 | Priority = Medium AND Status = New | 8 business hours | Notify manager (no reassignment) | Medium priority unworked |
| | 3 | Priority = Low AND Status = New | 24 business hours | Notify manager (no reassignment) | Low priority unworked |

> **Design Decision:** Critical priority NOT in escalation rules
> **Rationale:** Critical cases are handled by the VIP Detection Flow (US-008) which immediately routes to Senior_Support_Queue and posts Chatter notification. Adding an escalation rule for Critical would be redundant.

> **Design Decision:** Only escalate cases in "New" status
> **Rationale:** If an agent has started working a case (In Progress, Waiting on Customer), the timer should not escalate it. Only "New" (untouched) cases need escalation.

### Email Templates for Escalation

| Template Name | Purpose | Recipients |
|---|---|---|
| Escalation_High_Priority | High priority case unworked for 2+ hours | Case owner's manager |
| Escalation_Medium_Priority | Medium priority case unworked for 8+ hours | Case owner's manager |
| Escalation_Low_Priority | Low priority case unworked for 24+ hours | Case owner's manager |

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Business Hours | Default 24/7 exists | Need Relay Logic-specific hours | Create |
| Escalation Rules | No Relay Logic rules | Create all 3 entries | Create |
| Escalation email templates | None for RL | Create 3 templates | Create |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Multi-level escalation (escalate twice) | Enable tier — single escalation action per entry |
| SLA Milestones / Entitlements | Out of scope — Elevate tier feature |
| Auto-close after inactivity | Not discussed; could be Phase 2 |
| Weekend/holiday coverage | Not discussed; business hours exclude weekends |
| Escalation for "Waiting on Customer" | Customer-caused delay — SLA timer pauses conceptually |

## Implementation Checklist

### Phase 1: Business Hours Configuration

- [ ] Configure Business Hours in Salesforce Setup (UI-only — no metadata API support for BusinessHours)
  - Name: Relay Logic Support Hours
  - Time Zone: ❓ (confirm with client)
  - Hours: ❓ Mon–Fri 9:00 AM – 5:00 PM (confirm with client)
  - Set as default business hours
- [ ] Verify: `SELECT Id, Name, TimeZoneSidKey, IsDefault FROM BusinessHours`

### Phase 2: Email Templates

- [ ] Create email template folder "Relay_Logic_Templates"
- [ ] Create `Escalation_High_Priority` email template with case details merge fields
- [ ] Create `Escalation_Medium_Priority` email template
- [ ] Create `Escalation_Low_Priority` email template
- [ ] Deploy templates: `sf project deploy start --source-dir force-app/main/default/email`
- [ ] Verify templates exist in org

### Phase 3: Escalation Rules

- [ ] Create escalation rule metadata: `force-app/main/default/escalationRules/Case.escalationRules-meta.xml`
  - Entry 1: Priority=High, Status=New → 2 hours → reassign to Senior_Support_Queue + notify manager
  - Entry 2: Priority=Medium, Status=New → 8 hours → notify manager
  - Entry 3: Priority=Low, Status=New → 24 hours → notify manager
  - Reference Business Hours and email templates
- [ ] Deploy: `sf project deploy start --source-dir force-app/main/default/escalationRules`
- [ ] Set as active escalation rule
- [ ] Verify rules are active and referencing correct business hours

### Secure & Make Usable

- [ ] Test: Create High priority case in New status → verify escalation fires after 2 business hours
- [ ] Test: Verify escalation email is received by manager
- [ ] Test: Verify In Progress cases do NOT escalate
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Time zone** — What time zone for business hours? (US Eastern, Central, Pacific?)
2. **Business hours** — Exact start/end times? (9-5? 8-6?)
3. **Holidays** — Which holidays should pause escalation timers?
4. **SLA timing** — Business hours or clock hours for escalation? (Worksheet says Lisa was unsure)
