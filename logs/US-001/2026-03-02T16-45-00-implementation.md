# Implementation Summary: US-001 — Team Setup (Users, Roles, Profiles & OWD)

**Story ID:** US-001
**Plan File:** `logs/US-001/2026-03-02T16-28-48-plan.md`
**Implementation Date:** 2026-03-02T16:45:00 UTC
**Target Org:** deborah@realfast.ai.deb-testing (Org ID: 00DdN00000tuRVmUAM)

---

## Actions Taken

### Step 1: Deploy Role Hierarchy (5 roles)
- **Attempt 1**: Failed — `caseAccessForAccountOwner` invalid element in Role XML
- **Fix Applied**: Corrected element names to `caseAccessLevel`, `contactAccessLevel`, `opportunityAccessLevel`, and `name` (per Metadata API reference)
- **Attempt 2**: Success — 5 roles deployed via Metadata API
- **Final Result**: PASS (2 attempts, 1 fix applied)
- **Key Learning**: Role XML uses `caseAccessLevel` / `contactAccessLevel` / `opportunityAccessLevel` / `name`, NOT `caseAccessForAccountOwner` / `contactAccessForAccountOwner` / `opportunityAccessForAccountOwner` / `label`

**Roles created:**

| Role | DeveloperName | Parent |
|------|---------------|--------|
| VP Customer Success | VP_Customer_Success | (none — top level) |
| Core Platform Lead | Core_Platform_Lead | VP_Customer_Success |
| Integrations Lead | Integrations_Lead | VP_Customer_Success |
| Core Platform Agent | Core_Platform_Agent | Core_Platform_Lead |
| Integrations Agent | Integrations_Agent | Integrations_Lead |

### Step 2: Retrieve Standard User Profile as Base Template
- **Attempt 1**: Success — Retrieved `Profile:Standard` into `force-app/main/default/profiles/Standard.profile-meta.xml`
- **Final Result**: PASS

### Step 3: Create and Deploy 3 Custom Profiles
- **Attempt 1**: Success — 3 custom profiles created by cloning Standard User profile XML, setting `<custom>true</custom>`, and adding `<objectPermissions>` blocks
- **Final Result**: PASS

**Profiles created:**

| Profile | Case Delete | Case View All | Account Delete | Contact Delete |
|---------|-------------|---------------|----------------|----------------|
| Support Manager | false | true | true | true |
| Support Lead | false | false | true | true |
| Support Agent | false | false | false | false |

### Step 4: Deploy OWD Changes
- **Step 4a**: Retrieved Case and Account object metadata
- **Step 4b**: Changed Case `<sharingModel>` from `ReadWriteTransfer` to `Private`
- **Step 4c**: Deployed Case OWD — Success
- **Step 4d**: Waited 30 seconds for sharing recalculation
- **Step 4e**: Changed Account `<sharingModel>` from `ReadWrite` to `Read`
- **Step 4f**: Deployed Account OWD — Success (recalculation took ~30 seconds to propagate)
- **Final Result**: PASS

**OWD values confirmed:**

| Object | Before | After (XML) | After (SOQL) |
|--------|--------|-------------|--------------|
| Case | ReadWriteTransfer | Private | None |
| Account | ReadWrite | Read | Read |
| Contact | ControlledByParent | ControlledByParent | ControlledByParent |

### Step 5: Create 7 Users via Data API
- Created in dependency order (managers before reports)
- All 7 users created successfully on first attempt
- **Final Result**: PASS

**Users created:**

| Name | Email | Profile | Role | Manager | User ID |
|------|-------|---------|------|---------|---------|
| Lisa Chen | lisa.chen@relaylogic.com | Support Manager | VP_Customer_Success | — | 005dN00000ABd6jQAD |
| Marcus Webb | marcus.webb@relaylogic.com | Support Lead | Core_Platform_Lead | Lisa Chen | 005dN00000ABdEnQAL |
| Priya Sharma | priya.sharma@relaylogic.com | Support Lead | Integrations_Lead | Lisa Chen | 005dN00000ABdGPQA1 |
| Jake Torres | jake.torres@relaylogic.com | Support Agent | Core_Platform_Agent | Marcus Webb | 005dN00000ABdI1QAL |
| Anika Patel | anika.patel@relaylogic.com | Support Agent | Core_Platform_Agent | Marcus Webb | 005dN00000ABdJdQAL |
| Sam Okafor | sam.okafor@relaylogic.com | Support Agent | Integrations_Agent | Priya Sharma | 005dN00000ABVPKQA5 |
| Rachel Kim | rachel.kim@relaylogic.com | Support Agent | Integrations_Agent | Priya Sharma | 005dN00000ABdLFQA1 |

### Step 6: Final Verification
- 5 roles with correct hierarchy — PASS
- 7 users with correct profiles, roles, managers — PASS
- OWD: Account=Read, Contact=ControlledByParent, Case=None — PASS
- Case Delete blocked on all 3 profiles — PASS
- View All Cases only on Support Manager — PASS
- No duplicate roles — PASS
- License count: 9/20 used — PASS

---

## Deployments

| # | Command | Deploy ID | Result |
|---|---------|-----------|--------|
| 1 | `sf project deploy start --source-dir force-app/main/default/roles` (attempt 1) | 0AfdN00000FoYXJSA3 | Failed — invalid XML elements |
| 2 | `sf project deploy start --source-dir force-app/main/default/roles` (attempt 2) | 0AfdN00000FoJF6SAN | Succeeded — 5 roles created |
| 3 | `sf project deploy start --source-dir "Support Manager/Lead/Agent profiles"` | 0AfdN00000FoYdlSAF | Succeeded — 3 profiles created |
| 4 | `sf project deploy start --source-dir force-app/main/default/objects/Case` | 0AfdN00000FoYfNSAV | Succeeded — Case OWD → Private |
| 5 | `sf project deploy start --source-dir force-app/main/default/objects/Account` | 0AfdN00000FoXzSSAV | Succeeded — Account OWD → Read |

---

## Retry Summary

| Step | Total Attempts | Failures | Final Result | Key Learning |
|------|---------------|----------|--------------|--------------|
| 1 | 2 | 1 | Success | Role XML uses `caseAccessLevel` not `caseAccessForAccountOwner` |

**Total retries**: 1
**Success rate**: 6/6 steps passed

---

## Artifacts Created

### Metadata Deployed
| File | Purpose | Deploy Step |
|------|---------|-------------|
| force-app/main/default/roles/VP_Customer_Success.role-meta.xml | VP Customer Success role | Step 1 |
| force-app/main/default/roles/Core_Platform_Lead.role-meta.xml | Core Platform Lead role | Step 1 |
| force-app/main/default/roles/Integrations_Lead.role-meta.xml | Integrations Lead role | Step 1 |
| force-app/main/default/roles/Core_Platform_Agent.role-meta.xml | Core Platform Agent role | Step 1 |
| force-app/main/default/roles/Integrations_Agent.role-meta.xml | Integrations Agent role | Step 1 |
| force-app/main/default/profiles/Support Manager.profile-meta.xml | Support Manager custom profile | Step 3 |
| force-app/main/default/profiles/Support Lead.profile-meta.xml | Support Lead custom profile | Step 3 |
| force-app/main/default/profiles/Support Agent.profile-meta.xml | Support Agent custom profile | Step 3 |
| force-app/main/default/objects/Case/Case.object-meta.xml | Case OWD → Private | Step 4 |
| force-app/main/default/objects/Account/Account.object-meta.xml | Account OWD → Read | Step 4 |

### Scripts Created
None.

### Learnings Captured
None — no deviations required learning loop activation.

**Total artifacts**: 10 metadata files deployed, 7 users created via Data API

---

## Deviations

| # | Expected (Plan) | Actual | Root Cause | Resolution |
|---|-----------------|--------|------------|------------|
| 1 | Role XML uses `caseAccessForAccountOwner`, `contactAccessForAccountOwner`, `opportunityAccessForAccountOwner`, `label` | Invalid XML elements — deploy rejected | Plan used incorrect element names from the plan template, not from the Metadata API reference | Corrected to `caseAccessLevel`, `contactAccessLevel`, `opportunityAccessLevel`, `name` per reference docs |
| 2 | Account OWD visible immediately after deploy | SOQL showed `Edit` for ~30 seconds after successful deploy | Sharing recalculation lag — OWD changes take time to propagate in SOQL queries | Waited additional 30 seconds; second query confirmed `Read` |

---

## Open Items

None — all implementation steps completed and verified.
