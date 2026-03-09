# US-006: Email Integration & Email-to-Case

**Status:** [ ] Not Started

## Business Requirement

Relay Logic's primary support channel is email — they're transitioning from a shared Gmail inbox (support@relaylogic.com or similar) to Salesforce Email-to-Case. Incoming emails should automatically create cases, route them via assignment rules (US-004), and send auto-response confirmations. Agents need email templates for common responses. Email replies should thread back to the originating case.

## Worksheet References
- Section 5, Email-to-Case: *"Yes — primary channel. Currently all support runs through shared Gmail inbox"*
- Section 5, Support Email: *"support@relaylogic.com (or similar) — ❓ Needs Discussion"*
- Section 5, Auto-Response: *"Thank you for contacting Relay Logic Support. Your case number is {Case.CaseNumber}..."*
- Section 5, Email Threading: *"Yes — recommended standard configuration"*
- Section 8, Email System: *"Gmail — shared inbox"*
- Section 8, Email Templates: *"5 templates: Case Auto-Response, Case Resolved, Request More Information, Escalation Notification, Initial Response"*
- Section 8, Org-Wide Email: *"❓ Needs Discussion — support@ address"*
- Section 8, Email Signature: *"❓ Needs Discussion"*

## Solution Design

### Email-to-Case Configuration

| Setting | Value | Notes |
|---|---|---|
| Routing Address | ❓ support@relaylogic.com (confirm) | Forwarding from Gmail to Salesforce Email Services address |
| Case Origin | Email | Auto-set on email-created cases |
| Case Priority | Medium (default) | VIP flow (US-008) may override |
| Run Assignment Rules | Yes | Routes to correct queue via US-004 |
| Auto-Response | Yes | Sends confirmation email |
| Threading | Enabled | Replies append to existing case |

> **Design Decision:** Standard Email-to-Case (not On-Demand)
> **Rationale:** Standard Email-to-Case is simpler and sufficient for Enable tier. Relay Logic forwards their support@ address to the Salesforce routing address.

### Org-Wide Email Address

| Setting | Value | Notes |
|---|---|---|
| Display Name | Relay Logic Support | Shown in "From" field |
| Email Address | ❓ support@relaylogic.com | Needs client confirmation |
| Allow All Profiles | Yes | All agents send from this address |

### Email Templates (5 of 10 allowed)

| Template Name | Type | Purpose | Key Merge Fields |
|---|---|---|---|
| Case_Auto_Response | Auto-response | New case acknowledgment | {!Case.CaseNumber}, {!Case.Subject} |
| Case_Resolved | Agent-sent | Resolution notification | {!Case.CaseNumber}, {!Case.Subject}, {!Case.Resolution} |
| Request_More_Information | Agent-sent | Ask customer for details | {!Case.CaseNumber}, {!Contact.FirstName} |
| Escalation_Notification | Internal | Manager alert for escalated case | {!Case.CaseNumber}, {!Case.Priority}, {!Account.Name} |
| Initial_Response | Agent-sent | First agent reply template | {!Case.CaseNumber}, {!Contact.FirstName}, {!Case.Subject} |

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Email-to-Case | Not configured for Relay Logic | Create routing configuration | Create |
| Org-Wide Email Address | None for Relay Logic | Create with support@ address | Create |
| Email templates | SDO templates exist; none for RL | Create 5 RL templates | Create |
| Auto-response rules | None for RL | Create for Email-to-Case | Create |
| Gmail integration | Not configured | Standard Gmail integration (Chrome extension) | Configure |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Einstein Activity Capture | Requires separate license — out of scope |
| Salesforce Inbox | Requires separate license — out of scope |
| Multiple routing addresses | Single support@ address sufficient |
| Email-to-Case with IMAP | Using standard forwarding approach |
| Advanced email parsing | Not discussed; standard subject/body parsing |
| Custom email signature per user | ❓ Needs Discussion — may add org-wide signature |

## Implementation Checklist

### Phase 1: Org-Wide Email Address

- [ ] Create Org-Wide Email Address in Setup (UI configuration):
  - Display Name: Relay Logic Support
  - Email Address: ❓ (confirm with client)
  - Allow All Profiles to use this address
- [ ] Verify email address (confirmation email sent to the address)
- [ ] Verify: `SELECT Id, DisplayName, Address FROM OrgWideEmailAddress`

### Phase 2: Email Templates

- [ ] Create email template folder: "Relay_Logic"
- [ ] Create 5 email templates with merge fields:
  - Case_Auto_Response
  - Case_Resolved
  - Request_More_Information
  - Escalation_Notification (internal — also used by US-005)
  - Initial_Response
- [ ] Deploy templates: `sf project deploy start --source-dir force-app/main/default/email`
- [ ] Verify templates are available to agents

### Phase 3: Email-to-Case Setup

- [ ] Enable Email-to-Case in Setup → Email-to-Case Settings
- [ ] Create Email-to-Case routing address:
  - Routing Address: ❓ support@relaylogic.com
  - Case Origin: Email
  - Case Priority: Medium
  - Case Owner: ❓ Default queue or Lisa Chen
  - Run Assignment Rules: Yes
  - Save Email Headers: Yes
  - Enable Email Threading: Yes
- [ ] Configure email forwarding from Gmail to Salesforce routing address
- [ ] Verify: send test email to support address → confirm case created

### Phase 4: Auto-Response Rules

- [ ] Create Auto-Response Rule for Cases:
  - Criteria: Case Origin = Email
  - Template: Case_Auto_Response
  - From: Org-Wide Email Address (Relay Logic Support)
- [ ] Deploy: `sf project deploy start --source-dir force-app/main/default/autoResponseRules`
- [ ] Verify: send email → confirm auto-response received

### Phase 5: Gmail Integration

- [ ] Enable Gmail Integration in Setup → Gmail Integration and Sync
- [ ] Provide agents with Chrome extension installation instructions
- [ ] Verify: agent can view Salesforce records from Gmail

### Secure & Make Usable

- [ ] Test: Send email to support address → case created with correct Origin, Priority, Queue assignment
- [ ] Test: Reply to auto-response → reply threads on original case
- [ ] Test: Agent sends email from case feed using Org-Wide Email Address
- [ ] Test: Agent uses email templates from case feed
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Support email address** — What is the exact address? (support@relaylogic.com?)
2. **Email signature** — What should be included? (Company name, support hours, help center link?)
3. **Gmail forwarding** — Does client have admin access to configure Gmail forwarding to Salesforce?
