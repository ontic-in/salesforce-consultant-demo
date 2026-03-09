# US-009: Reports & Dashboards

**Status:** [ ] Not Started

## Business Requirement

Lisa Chen needs a dashboard with visibility into support operations — case volume, product distribution, SLA compliance, VIP alerts, and agent workload. The Enable tier includes 1 custom dashboard with 5 custom reports. Standard out-of-the-box reports (case volume, aging, resolution times, queue status, agent productivity) are also available.

## Worksheet References
- Section 11, Top 5 Metrics: *"1. Open Cases by Priority 2. Cases by Product 3. Average First Response Time by Tier 4. VIP Alert Cases (This Week) 5. Cases by Agent"*

## Solution Design

### Custom Dashboard: Relay Logic Support Operations

| Component # | Report | Chart Type | Purpose |
|---|---|---|---|
| 1 | Open Cases by Priority | Bar/Column chart | Real-time view of Critical/High/Medium/Low backlog |
| 2 | Cases by Product | Pie/Donut chart | Volume split across Core Platform, Integrations, Analytics Module |
| 3 | Average First Response Time by Tier | Table/Bar chart | SLA compliance: Platinum <2hr, Gold <4hr, Silver <NBD |
| 4 | VIP Alert Cases This Week | Table | Cases that triggered VIP detection (Priority=Critical + Customer_Tier__c IN Gold,Platinum) |
| 5 | Cases by Agent | Bar chart | Workload distribution across team |

### Custom Reports (5 of 5 allowed)

| Report Name | Report Type | Filters | Groupings | Columns |
|---|---|---|---|---|
| Open_Cases_by_Priority | Cases | Status != Closed | Priority | Count, Case Number, Subject, Owner |
| Cases_by_Product | Cases | Created Date = THIS_QUARTER | Product__c | Count, Priority, Status |
| First_Response_Time_by_Tier | Cases with Activities | Created Date = THIS_MONTH | Customer_Tier__c | Avg Response Time, Case Number |
| VIP_Alert_Cases_This_Week | Cases | Priority=Critical, Customer_Tier__c IN (Gold,Platinum), Created Date = THIS_WEEK | Owner | Case Number, Account, Priority, Status |
| Cases_by_Agent | Cases | Created Date = THIS_MONTH | Owner | Count, Priority, Status, Avg Age |

> **Design Decision:** First Response Time uses Cases with Activities report type
> **Rationale:** Need to calculate time between case creation and first activity (email/task). Standard "Cases with Activities" report type provides this join. Note: precise SLA tracking requires Entitlements (Elevate tier) — this report is an approximation.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Custom dashboard | SDO dashboards exist; none for RL | Create 1 custom dashboard | Create |
| Custom reports | SDO reports exist; none for RL | Create 5 custom reports | Create |
| Report folder | No RL folder | Create "Relay Logic Reports" folder | Create |
| Dashboard folder | No RL folder | Create "Relay Logic Dashboards" folder | Create |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Scheduled reports | Not discussed; Enable tier doesn't include scheduled reports |
| Einstein Analytics | Out of scope — Transform tier feature |
| Additional dashboards | Enable tier: 1 custom dashboard (standard dashboards available) |
| Report subscriptions | Not discussed; can be configured by users in self-service |
| Custom report types | Standard report types sufficient |
| Dashboard filters | Consider adding in Phase 2 for dynamic filtering |

## Implementation Checklist

### Phase 1: Report Folders

- [ ] Create report folder "Relay_Logic_Reports" accessible to all Relay Logic users
- [ ] Create dashboard folder "Relay_Logic_Dashboards" accessible to all Relay Logic users

### Phase 2: Custom Reports

- [ ] Create report: Open_Cases_by_Priority
- [ ] Create report: Cases_by_Product
- [ ] Create report: First_Response_Time_by_Tier
- [ ] Create report: VIP_Alert_Cases_This_Week
- [ ] Create report: Cases_by_Agent
- [ ] Deploy reports: `sf project deploy start --source-dir force-app/main/default/reports`
- [ ] Verify all 5 reports run successfully with test data

### Phase 3: Custom Dashboard

- [ ] Create dashboard: Relay_Logic_Support_Operations
  - Running user: Lisa Chen (VP — sees all data)
  - Add 5 components mapped to the 5 reports
  - Arrange in logical layout (priority overview at top, details below)
- [ ] Deploy dashboard: `sf project deploy start --source-dir force-app/main/default/dashboards`
- [ ] Verify dashboard renders correctly

### Secure & Make Usable

- [ ] Verify all Relay Logic users can access reports and dashboard
- [ ] Verify Lisa can see data across both teams (VP role visibility)
- [ ] Verify agents see only their own data in reports (respects OWD/sharing)
- [ ] User verification with client
