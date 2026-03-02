# US-002: Account & Contact Data Model — Implementation Summary

**Story ID:** US-002
**Title:** Account & Contact Data Model
**Plan File:** `logs/US-002/2026-03-02T18-00-00-plan.md`
**Implementation Date:** 2026-03-02T19:00:00
**Target Org:** deborah@realfast.ai.deb-testing

---

## Actions Taken

### Step 1: Retrieve Account Object Metadata (Template Reference)
- **Action:** Retrieved full Account object metadata for XML reference
- **Command:** `sf project retrieve start --metadata "CustomObject:Account" --output-dir retrieve-temp`
- **Result:** PASS — 24 standard field XML files retrieved
- **Attempts:** 1 (first attempt used `--output-dir /tmp/...` which failed with `OutputDirOutsideProjectError`; corrected to project-relative path)

### Step 2: Create Custom Field Metadata XML
- **Action:** Created two field XML files in `force-app/main/default/objects/Account/fields/`
- **Files Created:**
  - `Customer_Tier__c.field-meta.xml` — Picklist (Silver, Gold, Platinum), required=true, restricted=true
  - `Account_Start_Date__c.field-meta.xml` — Date, required=false
- **Result:** PASS

### Step 3: Deploy Custom Fields
- **Command:** `sf project deploy start --source-dir force-app/main/default/objects/Account/fields`
- **Deploy ID:** `0AfdN00000Fog9tSAB`
- **Result:** PASS — Status: Succeeded, 26 components (2 Created, 24 Unchanged)
- **Verification:** Tooling API query confirmed both fields exist:
  - `Account_Start_Date` (ID: `00NdN00000NJjPBUA1`)
  - `Customer_Tier` (ID: `00NdN00000NJjPCUA1`)

### Step 4: Create and Deploy Permission Set with FLS
- **Deviation from plan:** Plan included FLS for both fields in the permission set. Field-management guide states: *"Required fields and FLS are mutually exclusive — `<required>true</required>` auto-grants visibility; deploying FLS for it fails."* Removed `Customer_Tier__c` from permission set FLS. Only `Account_Start_Date__c` gets FLS via permission set.
- **File Created:** `force-app/main/default/permissionsets/Account_Custom_Fields.permissionset-meta.xml`
- **Command:** `sf project deploy start --source-dir force-app/main/default/permissionsets/Account_Custom_Fields.permissionset-meta.xml`
- **Deploy ID:** `0AfdN00000FogBVSAZ`
- **Result:** PASS — Status: Succeeded, 1 component Created
- **Verification:** `SELECT Id, Name, Label FROM PermissionSet WHERE Name = 'Account_Custom_Fields'` → 1 row (Label: "Account Custom Fields")

### Step 5: Assign Permission Set to All Users
- **Deviation from plan:** Plan used email-only usernames (e.g., `lisa.chen@relaylogic.com`). Actual usernames have `.deb-testing` suffix (e.g., `lisa.chen@relaylogic.com.deb-testing`). First attempt failed; corrected and retried.
- **Additional assignment:** Also assigned to admin user `deborah@realfast.ai.deb-testing` — required for CLI verification queries (admin profile doesn't auto-grant FLS on custom fields).
- **Result:** PASS — 8 assignments total (7 RL users + 1 admin)
- **Verification:** `SELECT Assignee.Name, PermissionSet.Label FROM PermissionSetAssignment WHERE PermissionSet.Name = 'Account_Custom_Fields'` → 7 RL users confirmed (admin also assigned but not counted in RL total)

### Step 6: Retrieve Account Page Layout
- **Command:** `sf project retrieve start --metadata "Layout:Account-Account Layout"`
- **Result:** PASS — Layout retrieved to `force-app/main/default/layouts/Account-Account Layout.layout-meta.xml`
- **Observation:** `Customer_Tier__c` was already on the layout with `Required` behavior (auto-added by Salesforce when a required field is deployed). Only `Account_Start_Date__c` needed to be added.

### Step 7: Add Account_Start_Date__c to Layout and Deploy
- **Action:** Added `Account_Start_Date__c` with `Edit` behavior to the Account Information section, after `Customer_Tier__c`
- **Command:** `sf project deploy start --source-dir "force-app/main/default/layouts/Account-Account Layout.layout-meta.xml"`
- **Deploy ID:** `0AfdN00000FogD7SAJ`
- **Result:** PASS — Status: Succeeded, 1 component Changed

### Step 8: Final Verification
- **8a. Fields queryable:** `SELECT Id, Customer_Tier__c, Account_Start_Date__c FROM Account LIMIT 1` → PASS (query succeeds, returns null values for existing account)
- **8b. FLS grants:** `SELECT Field, PermissionsRead, PermissionsEdit, Parent.Label FROM FieldPermissions WHERE Field IN (...)` → PASS (Account_Start_Date__c: Read=true, Edit=true via Account Custom Fields. Customer_Tier__c not in FieldPermissions because required fields auto-grant visibility.)
- **8c. Picklist verification:** Retrieved `Customer_Tier__c` field XML and confirmed: 3 values (Silver, Gold, Platinum), restricted=true, required=true

---

## Deployments

| Deploy ID | Components | Status | Step |
|-----------|-----------|--------|------|
| `0AfdN00000Fog9tSAB` | 26 (2 Created) | Succeeded | Step 3 — Custom Fields |
| `0AfdN00000FogBVSAZ` | 1 (Created) | Succeeded | Step 4 — Permission Set |
| `0AfdN00000FogD7SAJ` | 1 (Changed) | Succeeded | Step 7 — Account Layout |

---

## Artifacts Created

### Metadata Deployed
| File | Purpose | Deploy Step |
|------|---------|-------------|
| `force-app/main/default/objects/Account/fields/Customer_Tier__c.field-meta.xml` | Customer Tier picklist (Silver/Gold/Platinum, required, restricted) | Step 3 |
| `force-app/main/default/objects/Account/fields/Account_Start_Date__c.field-meta.xml` | Account Start Date (date, optional) | Step 3 |
| `force-app/main/default/permissionsets/Account_Custom_Fields.permissionset-meta.xml` | FLS: Read/Edit on Account_Start_Date__c | Step 4 |
| `force-app/main/default/layouts/Account-Account Layout.layout-meta.xml` | Updated layout with both custom fields | Step 7 |

### Scripts Created
*None — all operations used metadata deployment and CLI commands.*

### Learnings Captured
*No new learnings — all deviations were covered by existing guide documentation.*

**Total artifacts**: 4 files created/modified

---

## Retry Summary

| Step | Total Attempts | Failures | Final Result | Key Learning |
|------|---------------|----------|--------------|--------------|
| 1 | 2 | 1 | Success | `--output-dir` must be inside project root, not `/tmp/` |
| 5 | 2 | 1 | Success | Usernames use `.deb-testing` suffix in sandbox orgs |
| 8a | 2 | 1 | Success | Admin user needs Permission Set assignment for FLS on non-required custom fields |

**Total retries**: 3
**Success rate**: 8/8 steps succeeded

---

## Deviations from Plan

| # | Deviation | Reason | Impact |
|---|-----------|--------|--------|
| 1 | Removed `Customer_Tier__c` from Permission Set FLS | Required fields auto-grant visibility; deploying FLS for them would fail per field-management guide | No impact — field is visible to all users via required flag |
| 2 | Added admin user (Deborah) to Permission Set assignment | Admin needs FLS for `Account_Start_Date__c` to run verification queries and manage data | 8 total assignments instead of 7 |
| 3 | `Customer_Tier__c` already on layout after field deploy | Salesforce auto-adds required fields to the default layout | Only `Account_Start_Date__c` needed manual layout addition |

---

## Open Items
*None — all implementation steps completed successfully.*
