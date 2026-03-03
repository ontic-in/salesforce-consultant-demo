# US-002: Account & Contact Data Model

**Status:** [ ] Not Started

## Business Requirement

Relay Logic uses a tiered customer model (Silver, Gold, Platinum) that drives SLA response times, case priority, VIP detection, and escalation rules. The Customer Tier field must exist on the Account object and be required — it's the foundation for downstream automation and routing. An Account Start Date is also needed to power the "new customer within 30 days" auto-prioritization flow (US-004).

## Worksheet References
- Section 7, Customer Tier: *"✅ Confirmed: Customer Tier (picklist: Silver, Gold, Platinum)"*
- Section 7, Required Fields: *"✅ Confirmed: Customer Tier, Account Name"*
- Section 7, Account Start Date: *"📝 AI (Medium): Account Start Date (date — for 'new customer' 30-day rule)"*
- Section 7, Contacts to Multiple Accounts: *"✅ Confirmed: No"*
- Section 4, SLA by Tier: *"✅ Confirmed: Platinum 2h, Gold 4h, Silver next business day"*
- Section 10, Automation 2: *"✅ Confirmed: Case created on an account that is less than 30 days old"*

## Solution Design

**Custom Account Fields:**

| Field | API Name | Type | Values | Required | Purpose |
|-------|----------|------|--------|----------|---------|
| Customer Tier | Customer_Tier__c | Picklist | Silver, Gold, Platinum | Yes | Drives SLAs, VIP detection, escalation rules, case priority |
| Account Start Date | Account_Start_Date__c | Date | — | No | Powers 30-day new customer prioritization (US-004 Automation 2) |

**Design Decisions:**
> **Decision:** Use a custom `Account_Start_Date__c` field rather than the standard `CreatedDate` on Account.
> **Rationale:** `CreatedDate` reflects when the record was created in Salesforce, not when the customer relationship started. Since Relay Logic is migrating from Gmail, accounts will be created during setup — `CreatedDate` would make every account look "new." A custom date field lets them backfill actual start dates.

> **Decision:** Make Customer Tier required on Account but NOT on Contact.
> **Rationale:** Lisa: "It's not just nice-to-have." Tier drives routing, SLAs, and VIP logic — missing tier data would break downstream automation. Contact fields don't drive any confirmed business rules.

> **Decision:** Skip custom Contact fields (Preferred Contact Method, Role/Department) for now.
> **Rationale:** These were `📝 AI (Low)` suggestions not discussed in discovery. No confirmed business requirement depends on them. Can add later if needed.

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---------|-----------|
| Subscription Plan field on Account | Overlaps with future Stripe integration (parking lot). Not confirmed as needed now. |
| Custom Contact fields | AI suggestion only — no confirmed business requirement |
| Account Hierarchy (parent-child) | Not discussed; Relay Logic sells to mid-market ops teams, unlikely to need parent/subsidiary tracking |
| Contacts to Multiple Accounts | ✅ Confirmed not needed |
| Duplicate Management rules | `📝 AI (Low)` suggestion only — defer to a later story or post-launch |

## Implementation Checklist

**Deploy Custom Fields:**
- [ ] Retrieve existing Account object metadata for XML reference
- [ ] Create `Customer_Tier__c` picklist field (values: Silver, Gold, Platinum; required, default: none)
- [ ] Create `Account_Start_Date__c` date field (not required)
- [ ] Deploy both fields to org

**Secure & Make Usable:**
- [ ] Deploy Permission Set `Account_Custom_Fields` with FLS: read/edit on both fields for all 3 profiles (Support Manager, Support Lead, Support Agent)
- [ ] ❓ Confirm: Should Customer Tier be editable by agents, or restricted to leads/manager only? (Worksheet Section 13: *"📝 AI (Medium): Customer Tier field on Account — editable only by leads and Lisa"*). If restricted, create a second Permission Set for leads/manager with edit access, and agent Permission Set with read-only.
- [ ] Assign Permission Set(s) to all 7 users
- [ ] Add `Customer_Tier__c` and `Account_Start_Date__c` to Account page layout

**Verify:**
- [ ] Query `SELECT Customer_Tier__c, Account_Start_Date__c FROM Account LIMIT 1` to confirm fields exist
- [ ] Verify FLS via `FieldPermissions` SOQL query
- [ ] Test: Create an Account — confirm Customer Tier is required and picklist shows 3 values (Silver, Gold, Platinum)
- [ ] User verification with client
