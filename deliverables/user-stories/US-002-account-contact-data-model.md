# US-002: Account & Contact Data Model

**Status:** [ ] Not Started

## Business Requirement

Relay Logic needs a Customer Tier field on Accounts to drive SLA prioritization, VIP detection, and routing logic. The tier (Silver/Gold/Platinum) is the source of truth for case priority and queue assignment automation. Basic duplicate prevention is needed for Accounts (by name) and Contacts (by email) to maintain data quality as the team transitions from a shared Gmail inbox.

## Worksheet References
- Section 7, Custom Account Fields: *"Customer Tier (Picklist: Silver, Gold, Platinum) — source for case tier auto-populate"*
- Section 7, Required Account Fields: *"Customer Tier — Critical for SLA and routing logic"*
- Section 7, Required Contact Fields: *"Email — Standard best practice for case communication"*
- Section 7, Custom Contact Fields: *"Standard fields sufficient (Name, Email, Phone, Title)"*
- Section 3, Duplicate Prevention: *"Block duplicate Contacts by email, Alert on duplicate Accounts by name"*
- Section 7, Account Hierarchy: *"Unlikely — not required"*
- Section 7, Contacts to Multiple Accounts: *"No — standard single-account relationship sufficient"*

## Solution Design

### Custom Account Fields

| Field API Name | Label | Type | Values | Required | Purpose |
|---|---|---|---|---|---|
| Customer_Tier__c | Customer Tier | Picklist | Silver, Gold, Platinum | Yes (page layout) | Source of truth for SLA tiers; auto-populates on Cases via Flow (US-008); drives VIP detection |

> **Design Decision:** Make Customer Tier required via page layout, not field metadata
> **Rationale:** Metadata-level `<required>true</required>` conflicts with FLS deployment (cannot deploy FLS for required fields). Page layout required achieves the same UX enforcement without the deployment conflict.

### Custom Contact Fields

No custom Contact fields needed. Standard fields (Name, Email, Phone, Title) are sufficient per worksheet.

### Duplicate Prevention

**Org Analysis Findings:**

| Rule | Current State | Gap | Action |
|---|---|---|---|
| Account duplicate rule | `Standard_Account_Duplicate_Rule` — Active (Alert mode, fuzzy name match) | Already provides Alert on name match | **No Gap** — standard rule meets requirement |
| Contact duplicate rule | `Contact_Name_Email_Duplicate_Rule` — Active + `Standard_Contact_Duplicate_Rule` — Active | Worksheet says "Block" for contacts; standard rules use "Alert" | **Evaluate** — may need to update action to Block |

> **Design Decision:** Keep standard duplicate rules as-is (Alert mode for both)
> **Rationale:** Standard rules are already active and configured. The worksheet's "Block" suggestion is AI (Low) confidence. Recommend starting with Alert mode and upgrading to Block after the team has used the system and confirmed the matching is accurate. Blocking prematurely can frustrate agents trying to create legitimate records.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Customer_Tier__c on Account | No custom Account fields exist | Field needs to be created | Create |
| Account standard fields | Standard fields exist | No gap | — |
| Contact standard fields | Standard fields exist | No gap | — |
| Account duplicate rule | Standard rule active (Alert on name) | Meets requirement | No Gap |
| Contact duplicate rule | Standard + custom rules active (Alert on email+name) | Meets requirement (Alert vs Block — recommend Alert) | No Gap |
| Account hierarchy | Not needed per worksheet | N/A | — |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Account hierarchy (parent-child) | Worksheet: "Unlikely — not required" |
| Contacts to Multiple Accounts | Worksheet: "No — standard single-account relationship sufficient" |
| Custom Contact fields | Worksheet: "Standard fields sufficient" |
| Custom duplicate matching rules | Standard rules already active and sufficient |
| Account record types | Not discussed; single account type sufficient |
| Contact record types | Not discussed; single contact type sufficient |

## Implementation Checklist

### Phase 1: Custom Field Creation

- [ ] Create `Customer_Tier__c` picklist field metadata: `force-app/main/default/objects/Account/fields/Customer_Tier__c.field-meta.xml` with values: Silver, Gold, Platinum
- [ ] Deploy field: `sf project deploy start --source-dir force-app/main/default/objects/Account/fields/Customer_Tier__c.field-meta.xml`
- [ ] Verify field exists: `SELECT Customer_Tier__c FROM Account LIMIT 1`

### Phase 2: Field-Level Security (Required — new fields get zero FLS by default)

- [ ] Create Permission Set `Account_Customer_Tier_Access` with FLS for `Account.Customer_Tier__c` (read + edit)
- [ ] Deploy permission set: `sf project deploy start --source-dir force-app/main/default/permissionsets/Account_Customer_Tier_Access.permissionset-meta.xml`
- [ ] Assign to all Relay Logic users: `sf org assign permset --name Account_Customer_Tier_Access`
- [ ] Verify FLS: `SELECT Field, PermissionsRead, PermissionsEdit FROM FieldPermissions WHERE Field = 'Account.Customer_Tier__c'`

### Phase 3: Page Layout — Add Field & Make Required

- [ ] Retrieve Account page layout: `sf project retrieve start --metadata "Layout:Account-Account Layout"`
- [ ] Add `Customer_Tier__c` to Account page layout in a prominent position (Details section)
- [ ] Mark field as required on layout (`<required>true</required>` in layout item)
- [ ] Deploy updated layout: `sf project deploy start --source-dir force-app/main/default/layouts/Account-Account*`
- [ ] Verify layout assignment to Service_Cloud_Agent profile

### Phase 4: Duplicate Rules — Verify Existing

- [ ] Verify standard Account duplicate rule is active: `SELECT DeveloperName, IsActive FROM DuplicateRule WHERE SobjectType = 'Account'`
- [ ] Verify standard Contact duplicate rules are active: `SELECT DeveloperName, IsActive FROM DuplicateRule WHERE SobjectType = 'Contact'`
- [ ] Test Account duplicate detection: create two Accounts with same name → confirm Alert appears
- [ ] Test Contact duplicate detection: create two Contacts with same email → confirm Alert appears

### Secure & Make Usable

- [ ] Verify Customer_Tier__c visible and editable for all Relay Logic users
- [ ] Verify field appears on Account page layout as required
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Contact duplicate action** — Standard rules use Alert mode. Should we upgrade to Block (prevents saving duplicate contacts), or is Alert (warns but allows save) acceptable to start?
