# US-001: Team Setup — Users, Roles, Profiles & OWD

**Status:** [ ] Not Started

## Business Requirement

Relay Logic's support team of 7 people needs to be set up in Salesforce with a role hierarchy that mirrors their product-line team structure. The VP of Customer Success (Lisa Chen) oversees two team leads — Marcus Webb (Core Platform) and Priya Sharma (Integrations) — each managing two agents. Cases must be Private so agents only see their own cases and their team's queue. No user should have delete permissions on cases.

## Worksheet References
- Section 2, Team Size: *"✅ Confirmed: 7 users (4 agents + 2 team leads + 1 VP/Manager)"*
- Section 2, Hierarchy: *"✅ Confirmed: Multi-level. Lisa → Marcus & Priya (leads) → Agents. Teams split by product line."*
- Section 2, Visibility: *"✅ Confirmed: Leads see their team's cases + unassigned. Agents — own cases + team queue only."*
- Section 2, Deletion: *"✅ Confirmed: No. Absolutely not. Nobody deletes anything."*
- Section 13, OWD: *"✅ Confirmed: Private — Only case owner and their team via sharing rules"*
- Section 13, Accounts OWD: *"📝 AI (Medium): Public Read Only"*
- Section 13, Contacts OWD: *"✅ Confirmed: Controlled By Parent"*

## Solution Design

**Role Hierarchy:**
```
VP_Customer_Success (Lisa Chen)
├── Core_Platform_Lead (Marcus Webb)
│   ├── Core_Platform_Agent (Jake Torres)
│   └── Core_Platform_Agent (Anika Patel)
└── Integrations_Lead (Priya Sharma)
    ├── Integrations_Agent (Sam Okafor)
    └── Integrations_Agent (Rachel Kim)
```

**Users:**

| Name | Email | Role | Profile | Manager | Team |
|------|-------|------|---------|---------|------|
| Lisa Chen | lisa.chen@relaylogic.com | VP_Customer_Success | Support Manager | — | All |
| Marcus Webb | marcus.webb@relaylogic.com | Core_Platform_Lead | Support Lead | Lisa Chen | Core Platform |
| Priya Sharma | priya.sharma@relaylogic.com | Integrations_Lead | Support Lead | Lisa Chen | Integrations |
| Jake Torres | jake.torres@relaylogic.com | Core_Platform_Agent | Support Agent | Marcus Webb | Core Platform |
| Anika Patel | anika.patel@relaylogic.com | Core_Platform_Agent | Support Agent | Marcus Webb | Core Platform |
| Sam Okafor | sam.okafor@relaylogic.com | Integrations_Agent | Support Agent | Priya Sharma | Integrations |
| Rachel Kim | rachel.kim@relaylogic.com | Integrations_Agent | Support Agent | Priya Sharma | Integrations |

**Profiles (3 custom profiles cloned from Standard User):**

| Profile | Based On | Key Permissions |
|---------|----------|-----------------|
| Support Manager | Standard User | Full CRUD on Cases, Accounts, Contacts. View All Cases. Run Reports. No Delete on Cases. |
| Support Lead | Standard User | CRUD on Cases, Accounts, Contacts. No Delete on Cases. No View All (handled by sharing rules). |
| Support Agent | Standard User | Create/Read/Edit on Cases, Accounts, Contacts. No Delete on Cases. |

**Organization-Wide Defaults:**

| Object | OWD | Rationale |
|--------|-----|-----------|
| Case | Private | Lisa: "Agents should only see their own stuff and cases in their team's queue." |
| Account | Public Read Only | Agents need to see customer tier and account info across all accounts for case handling. |
| Contact | Controlled By Parent | Standard — follows Account access. Feature guide warns: do not change from ControlledByParent. |

**Design Decisions:**
> **Decision:** Use 5 distinct roles (VP, 2 Lead roles, 2 Agent roles per team) rather than 3 generic roles (Manager, Lead, Agent).
> **Rationale:** Distinct roles per team enable team-based sharing rules (Core Platform Lead/Agent roles share Core Platform cases). A generic "Lead" role wouldn't support product-line visibility separation.

> **Decision:** Clone custom profiles from Standard User rather than using Standard Profile directly.
> **Rationale:** Standard profiles have locked permissions that can't be removed (e.g., ModifyAllData on some). Custom profiles give full control over delete restrictions. Feature guide confirms: "Standard 'Service Cloud' profile has locked ModifyAllData — must clone to a custom profile."

> **Decision:** Contact OWD set to Controlled By Parent (not Public Read Only).
> **Rationale:** Feature guide warns: "Do not change Contact OWD from ControlledByParent." Since Account is Public Read Only, contacts will inherit read access.

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---------|-----------|
| Permission Set Groups | Not needed at this scale (7 users, 3 profiles covers all needs) |
| Login IP Restrictions | Not discussed in worksheet Section 13 |
| Password Policies | Not discussed — using Salesforce defaults |
| Single Sign-On (SSO) | Not discussed; out of Enable tier scope |
| Territory Management | Not applicable — team segmentation handled by roles |

## Implementation Checklist

**Create Identity & Access Foundation:**
- [ ] Audit existing roles, profiles, and users in the org via SOQL
- [ ] Create 5 roles: VP_Customer_Success, Core_Platform_Lead, Integrations_Lead, Core_Platform_Agent, Integrations_Agent (deploy as metadata)
- [ ] Retrieve Standard User profile as base template
- [ ] Create 3 custom profiles: Support_Manager, Support_Lead, Support_Agent (clone from Standard User)
- [ ] Remove Delete permission on Case from all 3 profiles
- [ ] Grant "View All" on Cases for Support_Manager profile only
- [ ] Deploy profiles to org

**Configure Organization-Wide Defaults:**
- [ ] Retrieve Case, Account object metadata
- [ ] Set Case `<sharingModel>` to `Private`
- [ ] Set Account `<sharingModel>` to `Read` (Public Read Only)
- [ ] Verify Contact is `ControlledByParent` (do not change)
- [ ] Deploy OWD changes (Account first, then Case — wait 30 seconds between deploys)

**Create Users:**
- [ ] Verify license availability (need 7 Service Cloud licenses)
- [ ] Create 7 users via Data API with placeholder emails (@relaylogic.com), assigning correct profiles and roles
- [ ] Assign manager relationships (ManagerId) for each user

**Verify:**
- [ ] Query `UserRole` to confirm 5 roles exist with correct hierarchy
- [ ] Query `User` to confirm 7 users with correct profiles and roles
- [ ] Query `Organization` to confirm OWD values (Case=None/Private, Account=Read)
- [ ] Test: Log in as agent — confirm cannot see other team's cases
- [ ] Test: Log in as lead — confirm can see own cases only (sharing rules come later)
- [ ] User verification with client
