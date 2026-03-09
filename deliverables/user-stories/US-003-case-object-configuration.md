# US-003: Case Object Configuration

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs the Case object configured with the right statuses, priorities, custom fields, and page layouts to support their product-based support model. Every case must have a Product tagged, and Customer Tier should auto-populate from the Account. The "Critical" priority level is needed for VIP detection, and "Waiting on Customer" status is needed to pause SLA tracking.

## Worksheet References
- Section 4, Case Types: *"Technical Issue, Product Question, Feature Request, Bug Report"*
- Section 4, Case Statuses: *"Add 'Waiting on Customer' to pause SLA timers"*
- Section 4, Case Priorities: *"Low, Medium, High, Critical — Critical for VIP cases"*
- Section 4, Custom Fields: *"Product (Picklist: Core Platform, Integrations, Analytics Module) — REQUIRED. Customer Tier (Picklist: Silver, Gold, Platinum)"*
- Section 4, Required Fields: *"Product, Contact, Description — Lisa was emphatic about Product being required"*
- Section 5, Case Origin: *"Email, Phone, Web"*

## Solution Design

### Case Statuses (StandardValueSet: CaseStatus)

| Status | IsClosed | Exists in Org | Action |
|---|---|---|---|
| New | No | Yes | No change |
| In Progress | No | Yes | No change |
| Waiting on Customer | No | Yes | **No Gap** — already configured |
| Escalated | No | Yes | No change |
| Closed | Yes | Yes | No change |

> **Org Analysis:** All required statuses already exist. No SVS deployment needed.

### Case Priorities (StandardValueSet: CasePriority)

| Priority | Exists in Org | Action |
|---|---|---|
| Low | Yes | No change |
| Medium | Yes (default) | No change |
| High | Yes | No change |
| Critical | **No** | **Create** — needed for VIP detection flow |

> **Gap:** Critical priority must be added. SVS deploy is full replacement — retrieve first, add Critical, redeploy.

### Custom Case Fields

| Field API Name | Label | Type | Values | Required | Purpose |
|---|---|---|---|---|---|
| Product__c | Product | Picklist | Core Platform, Integrations, Analytics Module | Yes (page layout) | Product routing, queue assignment, reporting |
| Customer_Tier__c | Customer Tier | Picklist | Silver, Gold, Platinum | No | Auto-populated from Account via Flow (US-008); used for VIP detection |

> **Design Decision:** Use `Product__c` (new field) instead of existing `Product_Line__c`
> **Rationale:** `Product_Line__c` contains manufacturing values (Fiber, Chemical, Base, Coating) from SDO data. Creating a clean `Product__c` field avoids value conflicts and confusion.

> **Design Decision:** Case Type as a picklist field, not Record Types
> **Rationale:** All case types follow the same process (statuses, layouts). Record types add complexity (business processes, layout assignments) with no benefit for Relay Logic's needs. A simple Type picklist achieves categorization without overhead.

### Case Origin (Standard Field)

Standard Case Origin field already exists with Email, Phone, Web values. Verify values are present; add if missing.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Case statuses | New, In Progress, Waiting on Customer, Escalated, Closed | No gap | — |
| Case priorities | High, Medium (default), Low | Missing Critical | Add via SVS deploy |
| Product__c | Does not exist | Create | Create custom picklist |
| Customer_Tier__c (Case) | Does not exist | Create | Create custom picklist |
| Product_Line__c | Exists (SDO data — Fiber, Chemical, etc.) | Not usable | Ignore — create Product__c |
| Case page layout | Default SDO layout exists | Needs customization | Update |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Case Record Types | Not needed — single process for all case types; picklist field sufficient |
| Business Processes | Not needed — no record types |
| Case Teams | Not discussed in discovery |
| Case Milestones/Entitlements | Out of scope — Elevate tier feature |
| Validation Rules | Not discussed; may add in future stories if needed |
| Compact Layouts | Standard compact layout sufficient for now |
| Case Comments custom fields | Standard case comments sufficient |

## Implementation Checklist

### Phase 1: Standard Value Sets

- [ ] Retrieve current CasePriority SVS: `sf project retrieve start --metadata "StandardValueSet:CasePriority"`
- [ ] Add "Critical" value to CasePriority SVS XML (preserve existing High, Medium, Low values — SVS deploy is full replacement)
- [ ] Deploy updated CasePriority: `sf project deploy start --source-dir force-app/main/default/standardValueSets/CasePriority.standardValueSet-meta.xml`
- [ ] Verify: `SELECT MasterLabel, SortOrder FROM CasePriority ORDER BY SortOrder`
- [ ] Verify Case Origin has Email, Phone, Web values (retrieve and check)

### Phase 2: Custom Fields

- [ ] Create `Product__c` picklist field metadata at `force-app/main/default/objects/Case/fields/Product__c.field-meta.xml` with values: Core Platform, Integrations, Analytics Module
- [ ] Create `Customer_Tier__c` picklist field metadata at `force-app/main/default/objects/Case/fields/Customer_Tier__c.field-meta.xml` with values: Silver, Gold, Platinum
- [ ] Deploy both fields: `sf project deploy start --source-dir force-app/main/default/objects/Case/fields`
- [ ] Verify fields exist: `SELECT Product__c, Customer_Tier__c FROM Case LIMIT 1`

### Phase 3: Field-Level Security (Required — new fields get zero FLS)

- [ ] Create Permission Set `Case_Custom_Fields_Access` with FLS for both `Case.Product__c` and `Case.Customer_Tier__c` (read + edit)
- [ ] Deploy permission set: `sf project deploy start --source-dir force-app/main/default/permissionsets/Case_Custom_Fields_Access.permissionset-meta.xml`
- [ ] Assign to all Relay Logic users: `sf org assign permset --name Case_Custom_Fields_Access`
- [ ] Verify FLS: `SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE Field IN ('Case.Product__c','Case.Customer_Tier__c')`

### Phase 4: Page Layout

- [ ] Retrieve current Case page layout: `sf project retrieve start --metadata "Layout:Case-Case Layout"`
- [ ] Add `Product__c` to Case Information section — mark as required on layout
- [ ] Add `Customer_Tier__c` to Case Information section — read-only (auto-populated by Flow)
- [ ] Ensure standard fields are present: Contact, Subject, Description, Status, Priority, Case Origin, Type
- [ ] Deploy updated layout: `sf project deploy start --source-dir force-app/main/default/layouts`
- [ ] Verify layout assignment to Service_Cloud_Agent profile

### Secure & Make Usable

- [ ] Test: Create a Case → verify Product is required, Customer Tier is visible
- [ ] Test: Verify Critical priority appears in picklist
- [ ] Test: Verify all 5 statuses appear in Status picklist
- [ ] User verification with client
