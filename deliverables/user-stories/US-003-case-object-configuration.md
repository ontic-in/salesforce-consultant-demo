# US-003: Case Object Configuration

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs the Case object configured to track support requests with product tagging, customer tier visibility, and priority-based workflows. Every case must have a product tagged (Core Platform, Integrations, or Analytics Module). Customer Tier should be visible on the case for agent context. Standard priorities (Low, Medium, High, Critical) are confirmed. Case statuses need to support a "Waiting on Customer" state beyond the standard set.

## Worksheet References
- Section 4, Case Types: *"📝 AI (Perplexity): Technical Issue / Bug Report, Integration / API Issue, Billing Question, Feature Request, General Inquiry"* — Confirmed by consultant
- Section 4, Case Statuses: *"📝 AI (Perplexity): New, In Progress, Waiting on Customer, Escalated, Resolved, Closed"*
- Section 4, Case Priorities: *"✅ Confirmed: Yes — standard (Low, Medium, High, Critical)"*
- Section 4, Product Field: *"✅ Confirmed: Product / Module (picklist: Core Platform, Integrations, Analytics Module) — REQUIRED"*
- Section 4, Customer Tier on Case: *"✅ Confirmed: Customer Tier (picklist: Silver, Gold, Platinum — from Account)"*
- Section 4, Case Origin: *"✅ Confirmed: Case Origin (standard field — Email, Phone, Web)"*
- Section 4, Required Fields: *"✅ Confirmed: Product / Module (required), Case Type, Priority, Customer Contact, Description"*

## Solution Design

**Custom Case Fields:**

| Field | API Name | Type | Values | Required | Purpose |
|-------|----------|------|--------|----------|---------|
| Product / Module | Product_Line__c | Picklist | Core Platform, Integrations, Analytics Module | Yes | Product-based routing, reporting, queue assignment |
| Customer Tier | Customer_Tier__c | Formula (Text) | — | N/A (formula) | Pulls tier from Account automatically. Lisa: "Ideally it'd pull from the account automatically." |

**Design Decisions:**
> **Decision:** Customer Tier on Case is a formula field (`Account.Customer_Tier__c`) rather than a picklist.
> **Rationale:** Lisa wants it to "pull from the account automatically." A formula field ensures tier is always in sync with the Account and agents cannot override it on cases. This also simplifies data integrity — no risk of mismatched tier values between Account and Case.

> **Decision:** Use `Product_Line__c` as the API name (not `Product__c`).
> **Rationale:** `Product` is a standard Salesforce object name. Using `Product_Line__c` avoids potential naming conflicts and is more descriptive of Relay Logic's use case (product lines, not products in the CPQ sense).

> **Decision:** Case statuses include "Waiting on Customer" and "Resolved" beyond the standard set.
> **Rationale:** "Waiting on Customer" is standard for B2B SaaS to pause SLA timers (Perplexity-validated). "Resolved" separates agent resolution from formal closure, allowing for customer confirmation before closing.

> **Decision:** No Record Types for Case — single case process for all product lines.
> **Rationale:** Product differentiation is handled by the `Product_Line__c` picklist and assignment rules. Record Types add complexity without a clear business need at this stage.

**Case Statuses:**

| Status | Category | Notes |
|--------|----------|-------|
| New | New | Default for new cases |
| In Progress | Working | Agent is actively working |
| Waiting on Customer | Working | Awaiting customer response |
| Escalated | Working | Case has been escalated |
| Resolved | Closed | Agent resolved, pending confirmation |
| Closed | Closed | Fully closed |

**Case Types:**

| Type | Notes |
|------|-------|
| Technical Issue / Bug Report | Core platform and product bugs |
| Integration / API Issue | Integration product issues |
| Billing Question | Billing inquiries (Stripe-related) |
| Feature Request | Enhancement requests |
| General Inquiry | Catch-all |

**Page Layout — Key sections:**
- Case Information: Subject, Status, Priority, Product_Line__c, Customer_Tier__c (formula, read-only), Case Origin, Type
- Contact Information: Contact Name, Account Name
- Description: Description
- Related Lists: Activities, Case Comments, Emails

**List Views:**

| List View | Filter | Shared To | Purpose |
|-----------|--------|-----------|---------|
| My Open Cases | Owner = current user, Status != Closed | All Internal Users | Agent's personal queue |
| All Open Cases | Status != Closed | All Internal Users | Manager overview (visibility controlled by OWD + sharing rules) |
| Core Platform Cases | Product_Line__c = "Core Platform", Status != Closed | All Internal Users | Core Platform team view |
| Integrations Cases | Product_Line__c = "Integrations", Status != Closed | All Internal Users | Integrations team view |
| High Priority Cases | Priority = High OR Critical, Status != Closed | All Internal Users | Escalation monitoring |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---------|-----------|
| Affected Workflow ID field | `📝 AI (Perplexity)` suggestion from v1. Not discussed in discovery. |
| Record Types for Case | Not required — single case process for all product lines. Confirmed by consultant. |
| Business Process for Case | Not needed without Record Types |
| Validation Rules | Not confirmed as needed. Required fields handle data quality for now. |
| Compact Layout | Using default compact layout |

## Implementation Checklist

**Deploy Custom Fields:**
- [ ] Retrieve existing Case object metadata for XML reference
- [ ] Create `Product_Line__c` picklist field (values: Core Platform, Integrations, Analytics Module; required)
- [ ] Create `Customer_Tier__c` formula field (Text): `TEXT(Account.Customer_Tier__c)` — read-only by nature
- [ ] Deploy both fields to org

**Configure Case Statuses:**
- [ ] Retrieve `StandardValueSet:CaseStatus` to see existing values
- [ ] Add "Waiting on Customer" status (category: Working) if not present
- [ ] Add "Resolved" status (category: Closed) if not present
- [ ] Deploy StandardValueSet update (note: deploy is FULL REPLACEMENT — include all existing values)

**Configure Case Types:**
- [ ] Retrieve `StandardValueSet:CaseType` to see existing values
- [ ] Set case type values: Technical Issue / Bug Report, Integration / API Issue, Billing Question, Feature Request, General Inquiry
- [ ] Deploy StandardValueSet update

**Secure & Make Usable:**
- [ ] Deploy Permission Set `Case_Custom_Fields` with FLS: read/edit on `Product_Line__c`; read-only on `Customer_Tier__c` (formula fields must be `editable: false`)
- [ ] Assign Permission Set to all 7 users
- [ ] Retrieve Case page layout
- [ ] Add `Product_Line__c`, `Customer_Tier__c`, Case Origin, Type to Case page layout
- [ ] Set `Product_Line__c` behavior to `Required` on page layout
- [ ] Deploy updated page layout

**Create List Views:**
- [ ] Create 5 list views: My Open Cases, All Open Cases, Core Platform Cases, Integrations Cases, High Priority Cases
- [ ] Set `<sharedTo><allInternalUsers>` on all list views
- [ ] Deploy list views to org

**Verify:**
- [ ] Query `SELECT Product_Line__c, Customer_Tier__c FROM Case LIMIT 1` to confirm fields exist
- [ ] Verify FLS via `FieldPermissions` SOQL query
- [ ] Test: Create a Case on an Account with Customer Tier = Gold — confirm formula shows "Gold" on Case
- [ ] Test: Confirm Product / Module is required when creating a case
- [ ] Test: Verify all 5 list views appear and filter correctly
- [ ] User verification with client
