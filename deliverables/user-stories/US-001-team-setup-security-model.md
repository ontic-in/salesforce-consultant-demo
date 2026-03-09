# US-001: Team Setup & Security Model

**Status:** [ ] Not Started

## Business Requirement

Relay Logic's 7-person support team needs to be set up in Salesforce with appropriate roles, profiles, and security controls. The team is split into two product-based groups — Core Platform (led by Marcus Webb) and Integrations (led by Priya Sharma) — under VP Lisa Chen. Agents must only see their own cases and their team's queue; team leads see only their team's cases; Lisa sees everything. Nobody can delete cases.

## Worksheet References
- Section 2, Team Structure: *"7 users — Lisa (VP) + Marcus & Priya (leads) + 4 agents"*
- Section 2, Hierarchy: *"3-level hierarchy: VP → 2 Team Leads → 4 Agents"*
- Section 2, Special Permissions: *"Nobody deletes anything."*
- Section 13, Case OWD: *"Private — agents should only see their own stuff and cases in their team's queue"*
- Section 13, Account OWD: *"Public Read Only — all agents need to see account info for case context"*
- Section 13, Sharing Rules: *"Role-based — Team Leads see their team's cases. Lisa sees ALL cases."*
- Section 13, Delete Prevention: *"No. Absolutely not. Nobody deletes anything."*

## Solution Design

### Role Hierarchy (5 Roles, 3 Levels)

| Role (DeveloperName) | Level | Parent Role | Users | Purpose |
|---|---|---|---|---|
| VP_Support | 1 | CEO (existing) | Lisa Chen | Full case visibility via hierarchy |
| Core_Platform_Lead | 2 | VP_Support | Marcus Webb | Sees Core Platform team cases only |
| Integrations_Lead | 2 | VP_Support | Priya Sharma | Sees Integrations team cases only |
| Core_Platform_Agent | 3 | Core_Platform_Lead | Jake Torres, Anika Patel | Sees own cases + queue |
| Integrations_Agent | 3 | Integrations_Lead | Sam Okafor, Rachel Kim | Sees own cases + queue |

> **Design Decision:** Separate lead/agent roles per team (not shared "Support Manager" / "Support Agent" roles)
> **Rationale:** With Case OWD = Private, role hierarchy controls vertical visibility. Shared roles would let Marcus see Priya's team cases and vice versa. Separate role branches enforce the team separation requirement from discovery.

### User List (7 Users)

| Name | Email | Profile | Role | Notes |
|---|---|---|---|---|
| Lisa Chen | ❓ Needs email | Service Cloud Agent (custom) | VP_Support | VP Customer Success — full visibility |
| Marcus Webb | ❓ Needs email | Service Cloud Agent (custom) | Core_Platform_Lead | Core Platform team lead |
| Priya Sharma | ❓ Needs email | Service Cloud Agent (custom) | Integrations_Lead | Integrations team lead |
| Jake Torres | ❓ Needs email | Service Cloud Agent (custom) | Core_Platform_Agent | Core Platform agent; also Senior Queue member |
| Anika Patel | ❓ Needs email | Service Cloud Agent (custom) | Core_Platform_Agent | Core Platform agent |
| Sam Okafor | ❓ Needs email | Service Cloud Agent (custom) | Integrations_Agent | Integrations agent |
| Rachel Kim | ❓ Needs email | Service Cloud Agent (custom) | Integrations_Agent | Integrations agent |

### Profile Strategy

| Profile | Based On | Key Differences | Assigned To |
|---|---|---|---|
| Service_Cloud_Agent (custom) | Clone of standard "Service Cloud User" | Remove `ModifyAllData`, `ViewAllData`, and dependents. Remove `PermissionsDelete` on Case object. | All 7 users |

> **Design Decision:** Single custom profile for all 7 users, not separate profiles per role level
> **Rationale:** Delete prevention applies to everyone (including Lisa). Feature-level differences (if any emerge in later stories) will be handled via Permission Sets, per Salesforce best practices. Profile provides the baseline; Permission Sets add features.

### Organization-Wide Defaults

| Object | Current OWD | Target OWD | Change Required |
|---|---|---|---|
| Case | Public Read/Write | **Private** | Yes — deploy `<sharingModel>Private</sharingModel>` |
| Account | Public Read/Write | **Public Read Only** | Yes — deploy `<sharingModel>Read</sharingModel>` |
| Contact | Controlled By Parent | Controlled By Parent | No change needed |

> **Design Decision:** Account OWD = Public Read Only (not Private)
> **Rationale:** All agents need to see Account info (Customer Tier, etc.) for case context. Private Accounts would block agents from viewing customer details on cases they're working.

### Sharing Rules

With Case OWD = Private, the role hierarchy automatically provides upward visibility:
- Lisa (VP_Support) sees all cases below her in the hierarchy
- Marcus (Core_Platform_Lead) sees Jake and Anika's cases
- Priya (Integrations_Lead) sees Sam and Rachel's cases

Queue-based sharing (configured in US-004) will handle team queue visibility.

No additional owner-based or criteria-based sharing rules are needed for the initial team separation requirement. The role hierarchy alone enforces the correct visibility model.

> **Design Decision:** No custom sharing rules — rely on role hierarchy + queue membership
> **Rationale:** The 5-role hierarchy with team branches already provides the exact visibility matrix described in the worksheet. Adding sharing rules would be redundant. Queue membership (US-004) will provide queue-level case visibility.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Relay Logic users | None exist in org | Create all 7 | Create |
| Role hierarchy | Existing SDO roles (Executive → Support Manager → Agent) | Need team-separated branches | Create 5 new roles under existing CEO |
| Case OWD | Public Read/Write | Must be Private | Update |
| Account OWD | Public Read/Write | Must be Public Read Only | Update |
| Contact OWD | Controlled By Parent | Already correct | No Gap |
| Custom profile | `Service_Cloud_Agent` exists from prior engagement | Clone standard profile fresh for Relay Logic | Create |
| Sharing rules | No Relay Logic-specific rules | Role hierarchy is sufficient | No rules needed |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Criteria-based sharing rules | Not needed — role hierarchy provides correct visibility |
| Field-level security restrictions | No sensitive fields identified in worksheet (Section 13) |
| Permission Set Groups | Not needed until multiple permission sets exist (later stories) |
| Public Groups | Not needed — queue membership handles team grouping |
| Login restrictions (IP/hours) | Not discussed in discovery; out of scope for Enable tier |
| Two-factor authentication | Not discussed; org-level security setting, not per-user |

## Implementation Checklist

### Phase 1: Identity & Access

- [ ] Verify Salesforce license availability (need 7 licenses): `SELECT TotalLicenses, UsedLicenses FROM UserLicense WHERE Name = 'Salesforce'`
- [ ] Retrieve existing CEO role to confirm DeveloperName for parent reference
- [ ] Create 5 role metadata files: `VP_Support`, `Core_Platform_Lead`, `Integrations_Lead`, `Core_Platform_Agent`, `Integrations_Agent`
- [ ] Deploy roles: `sf project deploy start --source-dir force-app/main/default/roles`
- [ ] Verify role hierarchy: `SELECT Id, Name, DeveloperName, ParentRoleId FROM UserRole WHERE DeveloperName IN ('VP_Support','Core_Platform_Lead','Integrations_Lead','Core_Platform_Agent','Integrations_Agent')`

### Phase 2: Profile Setup

- [ ] Retrieve standard "Service Cloud User" profile: `sf project retrieve start --metadata "Profile:ServiceCloud"`
- [ ] Clone to custom `Service_Cloud_Agent` profile:
  - Set `<custom>true</custom>`
  - Set `<userLicense>Salesforce</userLicense>`
  - Remove `ModifyAllData`, `ViewAllData`, and dependent user permissions
  - Set `<permissionsDelete>false</permissionsDelete>` on Case `<objectPermissions>`
- [ ] Deploy custom profile: `sf project deploy start --source-dir force-app/main/default/profiles/Service_Cloud_Agent.profile-meta.xml`
- [ ] Verify profile: `SELECT Id, Name FROM Profile WHERE Name = 'Service Cloud Agent'`

### Phase 3: User Creation

- [ ] Create 7 users via Data API with role and profile assignments (❓ need email addresses from client)
- [ ] Verify all users active and assigned: `SELECT Name, Email, Profile.Name, UserRole.Name FROM User WHERE UserRole.DeveloperName IN ('VP_Support','Core_Platform_Lead','Integrations_Lead','Core_Platform_Agent','Integrations_Agent')`

### Phase 4: Security — OWD Changes

- [ ] Retrieve Account and Case object metadata for OWD edit
- [ ] Update Case `.object-meta.xml`: `<sharingModel>Private</sharingModel>`
- [ ] Update Account `.object-meta.xml`: `<sharingModel>Read</sharingModel>`
- [ ] Deploy OWD changes (deploy Account first, wait 30s for sharing recalc, then deploy Case — Case OWD cannot be more restrictive than Account)
- [ ] Verify OWD: `SELECT DefaultAccountAccess, DefaultContactAccess, DefaultCaseAccess FROM Organization`
- [ ] Note: SOQL may show old value temporarily due to async sharing recalculation; use metadata retrieve to confirm

### Secure & Make Usable

- [ ] Verify delete prevention: log in as test agent user → confirm Case delete button is not available
- [ ] Verify role hierarchy visibility: log in as Marcus → confirm he can see Jake's and Anika's cases but NOT Sam's or Rachel's
- [ ] Verify Lisa can see all cases across both teams
- [ ] User verification with client

---

❓ **Open Questions:**
1. **User email addresses** — Needed for all 7 users (Lisa, Marcus, Priya, Jake, Anika, Sam, Rachel)
2. **Lisa Chen — System Administrator profile?** — Should Lisa have System Administrator profile instead of the custom agent profile, since she's VP and may need admin access? Or keep her on the restricted profile with additional Permission Sets?
