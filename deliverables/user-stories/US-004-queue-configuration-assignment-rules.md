# US-004: Queue Configuration & Assignment Rules

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs product-based case routing with three queues: Core Platform (Marcus's team), Integrations (Priya's team), and Senior Support (for VIP/escalated cases). Cases should auto-route to the correct queue based on the Product field, and agents should be notified when cases land in their queue. A fallback owner is needed for unmatched cases.

## Worksheet References
- Section 6, Assignment Approach: *"Combination — VIP/Critical auto-route to Senior Queue. Product-based cases route to product team queues. Agents claim from their team queue."*
- Section 6, Core Platform Queue: *"Marcus Webb, Jake Torres, Anika Patel"*
- Section 6, Integrations Queue: *"Priya Sharma, Sam Okafor, Rachel Kim"*
- Section 6, Senior Support Queue: *"Marcus Webb, Priya Sharma, Jake Torres"*
- Section 6, Queue Notification: *"Yes — without notification, agents must manually check queue"*
- Section 6, Default Case Owner: *"Unassigned Cases queue or Lisa Chen — needs discussion"*
- Section 6, Analytics Module Assignment: *"❓ Needs Discussion — which team handles it?"*

## Solution Design

### Queues

| Queue Name (DeveloperName) | Supported Object | Members | Purpose |
|---|---|---|---|
| Core_Platform_Queue | Case | Marcus Webb, Jake Torres, Anika Patel | Core Platform product cases |
| Integrations_Queue | Case | Priya Sharma, Sam Okafor, Rachel Kim | Integrations product cases |
| Senior_Support_Queue | Case | Marcus Webb, Priya Sharma, Jake Torres | VIP/escalated cases (cross-team) |

> **Design Decision:** 3 queues aligned with the team structure — not per-product
> **Rationale:** Analytics Module doesn't have a dedicated team yet. Assignment rules will route Analytics Module cases to a queue based on client decision (likely Core Platform as default). Senior Support Queue is cross-team for escalated/VIP cases.

### Assignment Rules

| Rule Name | Entry # | Criteria | Assign To | Notes |
|---|---|---|---|---|
| Relay_Logic_Case_Assignment | 1 | Product__c = "Core Platform" | Core_Platform_Queue | Product-based routing |
| | 2 | Product__c = "Integrations" | Integrations_Queue | Product-based routing |
| | 3 | Product__c = "Analytics Module" | ❓ Core_Platform_Queue (default) | Needs client confirmation |
| | (default) | No criteria match | ❓ Lisa Chen or dedicated queue | Fallback for unmatched cases |

> **Note:** VIP routing to Senior_Support_Queue is handled by Flow (US-008), not assignment rules. The flow overrides the initial queue assignment after case creation.

### Queue List Views

Each queue gets a dedicated list view so agents can see and claim cases from their queue.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Core_Platform_Queue | Does not exist | Create | Create |
| Integrations_Queue | Does not exist | Create | Create |
| Senior_Support_Queue | Does not exist | Create | Create |
| Case Assignment Rules | No Relay Logic rules exist | Create | Create |
| Queue list views | None for RL queues | Create | Create with each queue |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Round-robin assignment | Out of scope — Elevate tier feature; agents claim from queue |
| Skills-based routing | Out of scope — Transform tier feature |
| Omni-Channel routing | Out of scope — Elevate tier feature |
| Assignment rule email templates | Will use standard notification; custom templates in US-006 |
| Multiple assignment rule sets | Only one active assignment rule set at a time; single rule sufficient |

## Implementation Checklist

### Phase 1: Queue Creation

- [ ] Create queue metadata for `Core_Platform_Queue` (Case object, email notification enabled)
- [ ] Create queue metadata for `Integrations_Queue`
- [ ] Create queue metadata for `Senior_Support_Queue`
- [ ] Deploy queues: `sf project deploy start --source-dir force-app/main/default/queues`
- [ ] Verify queues: `SELECT Id, Name, DeveloperName FROM Group WHERE Type = 'Queue' AND DeveloperName IN ('Core_Platform_Queue','Integrations_Queue','Senior_Support_Queue')`

### Phase 2: Queue Members

- [ ] Add queue members via Data API (users must exist from US-001):
  - Core_Platform_Queue: Marcus Webb, Jake Torres, Anika Patel
  - Integrations_Queue: Priya Sharma, Sam Okafor, Rachel Kim
  - Senior_Support_Queue: Marcus Webb, Priya Sharma, Jake Torres
- [ ] Verify membership: `SELECT GroupId, Group.Name, UserOrGroupId FROM GroupMember WHERE Group.Type = 'Queue'`

### Phase 3: Assignment Rules

- [ ] Create Case Assignment Rule metadata: `force-app/main/default/assignmentRules/Case.assignmentRules-meta.xml`
  - Entry 1: Product__c = "Core Platform" → Core_Platform_Queue
  - Entry 2: Product__c = "Integrations" → Integrations_Queue
  - Entry 3: Product__c = "Analytics Module" → ❓ Core_Platform_Queue (confirm with client)
- [ ] Deploy assignment rules: `sf project deploy start --source-dir force-app/main/default/assignmentRules`
- [ ] Set as active assignment rule
- [ ] Verify: create test cases with different Product values → confirm correct queue assignment

### Phase 4: Queue List Views

- [ ] Create queue-specific list view for Core_Platform_Queue with `<filterScope>Queue</filterScope>`
- [ ] Create queue-specific list view for Integrations_Queue
- [ ] Create queue-specific list view for Senior_Support_Queue
- [ ] Deploy list views: `sf project deploy start --source-dir force-app/main/default/objects/Case/listViews`

### Secure & Make Usable

- [ ] Verify queue members can see and claim cases from their queue
- [ ] Verify assignment rules route cases correctly for each Product value
- [ ] Verify queue notification emails are sent when cases are assigned
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Analytics Module routing** — Which team handles Analytics Module cases? Suggest Core Platform as default.
2. **Default case owner** — Lisa Chen or a dedicated "Unassigned" queue for cases that don't match any rule?
