# Service Cloud Starter Pack: Enable Tier Requirements Worksheet

**Client:** [Client Name]
**Date:** [Date]
**Session Duration:** 90 minutes
**Consultant:** [Consultant Name]

---

## Table of Contents

1. [About Your Business](#section-1-about-your-business) - Time zones, business hours, holidays
2. [Your Support Team](#section-2-your-support-team) - Users, roles, hierarchy, permissions
3. [Your Existing Customer Data](#section-3-your-existing-customer-data) - Data sources, migration, cleanup, duplicates
4. [Case Management & Tracking](#section-4-case-management--tracking) - Case types, statuses, priorities, escalations, custom fields
5. [Case Capture](#section-5-case-capture) - Web-to-Case, Email-to-Case, auto-response, origins
6. [Case Assignment & Routing](#section-6-case-assignment--routing) - Assignment rules, queues, default owners
7. [Contact & Account Management](#section-7-contact--account-management) - Custom fields, hierarchy, required fields
8. [Email Integration](#section-8-email-integration) - Email system, templates, org-wide addresses, signatures
9. [Activity Management](#section-9-activity-management) - Task types, reminders
10. [Automation](#section-10-automation) - Automated actions beyond assignment/escalation
11. [Reports & Dashboards](#section-11-reports--dashboards) - Key metrics to track
12. [Mobile Access](#section-12-mobile-access) - Mobile app requirements
13. [Security & Access](#section-13-security--access) - OWD, sharing rules, field-level security
14. [Branding](#section-14-branding) - Logo, colors, visual identity
15. [Parking Lot](#parking-lot) - Out of scope items for future consideration

---

## How to Use This Worksheet

This worksheet captures everything we need to set up your Service Cloud system. We'll go through it together section by section.

- **✅ Confirmed** - You've confirmed this is correct
- **📝 AI Suggestion** - Our system suggested this based on your discovery session (please verify)
- **❓ Needs Discussion** - We need to talk through this together
- **N/A** - Not applicable to your business

---

## Section 1: About Your Business

*Let's start with the basics about how your company operates.*

### Time Zones & Business Hours

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What time zone is your main office in? | _____________ | Used for case timestamps |
| Do you have support teams in multiple time zones? | ☐ Yes ☐ No | |
| What are your support team's business hours? | Monday-Friday from: _____ to: _____ | Example: 9 AM - 5 PM Eastern Time |
| Do you observe holidays? | ☐ Yes ☐ No | Affects escalation rule timing |
| If yes, which holidays? | _____________ | Example: Federal holidays, company holidays |

---

## Section 2: Your Support Team

*Tell us about the people who will use the system.*

### Team Structure

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How many people will use the support system? | _______ users | Full users who log in daily (max 10 for Enable tier) |

### User List

*Please list each user who needs access:*

| Name | Email | Role | Manager |
|------|-------|------|---------|
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |
| | | ☐ Agent ☐ Team Lead ☐ Manager | |

*Maximum 10 users for Enable tier.*

### Support Team Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the reporting relationships for your support team? | ☐ Flat (all report to one manager) ☐ Multi-level (manager → team lead → agents) | Determines case visibility |
| Do managers need to see their team's cases automatically? | ☐ Yes ☐ No | Role hierarchy grants automatic access |
| Do any users need special permissions beyond standard case management? | ☐ Yes ☐ No | Examples: Bulk deletion, modify all cases, admin access |
| If yes, what special permissions? | _____________ | |

---

## Section 3: Your Existing Customer Data

*Let's plan how to bring your current data into the new system.*

### Data Sources

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Where is your customer data currently stored? | ☐ Excel/Spreadsheets ☐ Another system (specify: _____) ☐ Email ☐ Other: _____ | |
| Approximately how many customer accounts do you have? | _______ | Companies/Organizations |
| Approximately how many contacts (people) do you have? | _______ | Individual people at customer accounts |
| Do you have historical cases to bring over? | ☐ Yes (_____ cases) ☐ No | |

### Data Quality

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How clean is your current data? | ☐ Very clean ☐ Some cleanup needed ☐ Significant cleanup needed | |
| What cleanup is needed before migration? | ☐ Remove duplicates ☐ Fix incomplete records ☐ Remove outdated data ☐ Other: _____ | |

### Duplicate Prevention

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What duplicate prevention do you need going forward? | ☐ Block duplicate Contacts by email ☐ Alert on duplicate Accounts by name ☐ Prevent duplicate Cases ☐ Other: _____ | |

---

## Section 4: Case Management & Tracking

*How you track and manage support requests.*

### Case Types

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the 3-5 main types of support requests you handle? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ 5. _____________ | Examples: Technical Issue, Billing Question, General Inquiry, Complaint |

### Case Statuses

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need additional case statuses beyond standard (New, In Progress, Escalated, Closed)? | ☐ No, use standard ☐ Yes, add: _____________ | Example: "Waiting on Customer" |

### Case Priorities

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you use the standard priorities (Low, Medium, High, Critical)? | ☐ Yes ☐ No, we use: _____________ | |

### Escalation Rules

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should High priority cases escalate immediately or after a time period? | ☐ Immediately ☐ After _____ hours | |
| Should Medium priority cases escalate? | ☐ Yes, after _____ hours ☐ No | |
| Should Low priority cases escalate? | ☐ Yes, after _____ hours ☐ No | |
| How long should a case stay in "New" status before escalating to a manager? | High priority: _____ hours Medium priority: _____ hours Low priority: _____ hours | Based on business hours |
| Who should receive notifications when cases escalate? | ☐ Case owner's direct manager ☐ Support manager (name: _____) ☐ Escalation queue ☐ Other: _____ | |

### Custom Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do agents need to track on cases? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ 5. _____________ | Limit 5-10 fields max. Examples: Order Number, Product Category, Issue Severity |

### Required Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which fields should be required when creating a case? | ☐ Case Type ☐ Priority ☐ Customer Contact ☐ Description ☐ Other: _____ | Agents cannot save case without these |

---

## Section 5: Case Capture

*How customers submit support requests.*

### Web-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want customers to submit cases via a form on your website? | ☐ Yes ☐ No | |
| What information should customers provide on the web form? | ☐ Name ☐ Email ☐ Phone ☐ Subject ☐ Description ☐ Product Category ☐ Other: _____ | Limit 5-10 fields for good UX |
| Should the web form include spam protection (reCAPTCHA)? | ☐ Yes ☐ No | Recommended for public-facing forms |

### Email-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want customers to create cases by emailing a support address? | ☐ Yes ☐ No | |
| What email address(es) should customers use? | 1. _____________ 2. _____________ 3. _____________ | Example: support@company.com, billing@company.com |

### Auto-Response

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What should the automatic confirmation email say when a case is created? | _____________ | Example: "Thank you for contacting us. Your case number is {Case Number}. We will respond within 24 hours." |

### Email Threading

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should email conversations stay threaded on the case (customer replies go to same case)? | ☐ Yes ☐ No | Recommended: Yes |

### Case Origin Tracking

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What sources can cases come from? | ☐ Web form ☐ Email ☐ Phone call ☐ Walk-in ☐ Chat ☐ Other: _____ | Used for reporting (how many cases from web vs email?) |

---

## Section 6: Case Assignment & Routing

*How cases get to the right agent.*

### Assignment Approach

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want cases automatically assigned when created or will agents claim them from a queue? | ☐ Automatic assignment ☐ Manual claiming from queue ☐ Combination | |

### Assignment Criteria

*If using automatic assignment:*

| Criteria | Assigned To | Notes |
|----------|-------------|-------|
| Example: Case Type = Billing | Billing team queue | |
| Example: Case Type = Technical AND Priority = High | Senior tech agent (name: _____) | |
| _____________ | _____________ | |
| _____________ | _____________ | |
| _____________ | _____________ | |

### Queues

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need shared queues where multiple agents can claim cases? | ☐ Yes ☐ No | |
| What queues do you need? | 1. _____________ (members: _____) 2. _____________ (members: _____) 3. _____________ (members: _____) | Example: General Support Queue, Billing Queue, Technical Queue |
| Should agents be notified when cases are added to their queue? | ☐ Yes ☐ No | Without notification, agents must manually check queue |

### Default Case Owner

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who should be assigned cases that don't match any assignment rules? | ☐ Support Manager (name: _____) ☐ Unassigned Cases queue ☐ Other: _____ | Required fallback for unmatched cases |

---

## Section 7: Contact & Account Management

*Customer information tracking.*

### Custom Account Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do you need to track for customer accounts? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ 5. _____________ | Examples: Industry, Account Type, Annual Revenue. Standard fields: Name, Phone, Website, Billing Address |

### Custom Contact Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do you need to track for contacts? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ 5. _____________ | Examples: Department, Role, Preferred Contact Method. Standard fields: Name, Email, Phone, Title |

### Account Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you have parent company and subsidiary relationships that need to be tracked? | ☐ Yes ☐ No | Example: Regional office under global headquarters |

### Contacts to Multiple Accounts

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Can one contact work with multiple customer accounts? | ☐ Yes ☐ No | Example: Consultant works with 3 different client companies |

### Required Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which Account fields should be required? | ☐ Industry ☐ Phone ☐ Account Type ☐ Other: _____ | |
| Which Contact fields should be required? | ☐ Email ☐ Phone ☐ Title ☐ Other: _____ | |

---

## Section 8: Email Integration

*How agents communicate with customers via email.*

### Email System

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email system do your agents use? | ☐ Outlook ☐ Gmail ☐ Other: _____ | Outlook/Gmail integration included in Service Cloud |

### Email Templates

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email templates should be available to agents? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ 5. _____________ | Limit 10 templates. Examples: Case resolved, Request more info, Escalation notification |

### Organization-Wide Email Address

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email address should appear as the sender when agents email customers from Salesforce? | _____________ | Example: support@company.com. Requires domain verification with IT team |

### Email Signature

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need a standard email signature on all outbound emails? | ☐ Yes ☐ No | |
| If yes, what should it include? | _____________ | Example: Company name, address, legal disclaimer |

---

## Section 9: Activity Management

*Tracking tasks, events, and calls.*

### Task Types

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What types of tasks do agents typically create? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ | Examples: Follow up call, Send quote, Request information, Escalate to manager |

### Activity Reminders

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should agents receive automatic reminders before tasks are due? | ☐ Yes ☐ No | Example: Popup reminder 15 minutes before task due time |

---

## Section 10: Automation

*Business rules that happen automatically.*

### Automated Actions

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Beyond automatic assignment and escalation, do you need any other automated actions on cases? | ☐ Yes ☐ No | Limit up to 3 automations for Enable tier |

*If yes, describe each automation:*

| Automation 1 | Details |
|--------------|---------|
| What triggers it? | Example: Case has no customer response for 7 days |
| What happens? | Example: Auto-close case and send notification to customer |

| Automation 2 | Details |
|--------------|---------|
| What triggers it? | Example: Agent hasn't updated case in 24 hours |
| What happens? | Example: Update status to "Waiting on Agent" and notify manager |

| Automation 3 | Details |
|--------------|---------|
| What triggers it? | Example: Case marked as Resolved |
| What happens? | Example: Create follow-up task for agent to check in after 3 days |

---

## Section 11: Reports & Dashboards

*Tracking key metrics and performance.*

### Dashboard Metrics

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the top 5 metrics your support team needs to track daily? | 1. _____________ 2. _____________ 3. _____________ 4. _____________ 5. _____________ | Examples: Open cases by priority, Average resolution time by agent, Escalated cases count, New cases this week, Cases waiting on customer |

*Note: Standard reports (case volume, aging, resolution times, queue status, agent productivity) are included out-of-the-box. This question identifies the 5 custom reports for your dashboard.*

---

## Section 12: Mobile Access

*Support agents working away from their desk.*

### Mobile Needs

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do your support agents need to access and update cases while away from their desk? | ☐ Yes ☐ No | Examples: Field technicians, remote agents |

*Note: Mobile app is out-of-the-box. Agents download app and sign in to view/edit cases, log activities, add comments. This question determines if we include mobile training and setup in scope.*

---

## Section 13: Security & Access

*Who can see and do what.*

### Organization-Wide Defaults (Record Access)

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who should be able to see cases by default? | ☐ Only case owner (Private) ☐ All agents can view (Public Read Only) ☐ All agents can view and edit (Public Read/Write) | Most restrictive = Private |
| Who should be able to see accounts by default? | ☐ Only owner (Private) ☐ All agents can view (Public Read Only) ☐ All agents can view and edit (Public Read/Write) | |
| Who should be able to see contacts by default? | ☐ Only owner (Private) ☐ All agents can view (Public Read Only) ☐ All agents can view and edit (Public Read/Write) | |

### Sharing Rules

*If any of the above are set to Private:*

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How should private records be shared across the team? | ☐ Share all High Priority cases with manager role ☐ Share cases from VIP accounts with senior agents ☐ Share regional cases with regional team ☐ Other: _____ | Only needed if OWD is Private |

### Field-Level Security

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Are there any sensitive fields that certain users should not see or edit? | ☐ Yes ☐ No | |
| If yes, which fields and for which users? | Example: Hide Social Security Number from agents / Make billing information read-only for support reps / Hide internal notes from contractors | |

---

## Section 14: Branding

*Make Salesforce look like your company.*

### Company Branding

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What branding should be applied to the Salesforce interface? | ☐ Company logo ☐ Brand colors ☐ Both | Logo appears in header and login page. Theme colors customize Lightning interface. |
| Do you have a logo file ready? | ☐ Yes ☐ No ☐ Need help creating one | PNG or SVG format preferred |
| What are your primary brand colors? | Primary: _____________ Secondary: _____________ | Hex codes preferred (e.g., #FF5733) |

---

---

## Parking Lot

*Items that came up but are out of scope for Enable tier. We'll discuss tier upgrades if needed.*

| Item | Why It's Out of Scope | Suggested Tier |
|------|----------------------|----------------|
| | | ☐ Elevate ($35K) ☐ Transform ($60K) |
| | | ☐ Elevate ($35K) ☐ Transform ($60K) |
| | | ☐ Elevate ($35K) ☐ Transform ($60K) |
