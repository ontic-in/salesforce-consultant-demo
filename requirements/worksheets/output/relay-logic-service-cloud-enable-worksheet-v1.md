# Service Cloud Starter Pack: Enable Tier Requirements Worksheet

**Client:** Relay Logic
**Cloud:** Service Cloud
**Tier:** Enable ($20,000 | 6-8 weeks)
**Date:** 2026-03-02
**Version:** 1 (AI Pre-filled from Sales Handoff Transcript)
**Consultant:** [Consultant Name]

---

## AI Analysis Summary

**Client:** Relay Logic
**Cloud:** Service Cloud
**Tier:** Enable ($20,000)
**Industry:** B2B SaaS (Workflow Automation)
**Team Size:** ~200 employees (~8 Salesforce users)
**Version:** 1 (Initial — 2026-03-02)

### Worksheet Completion Status
- Sections complete (Confirmed): 0 of 14
- Sections partially filled (AI suggestions): 12
- Sections needing discussion: 2
- Sections not started: 0

### Key Findings from Discovery
1. **Shared Gmail inbox is the current system** — No CRM, no case tracking, no structure. Everything runs through email. This is a greenfield implementation. *(AE handoff call)*
2. **VIP customer handling is the #1 priority** — Lisa Chen (VP Customer Success) specifically cited a Platinum customer with 3 open tickets that went unnoticed until churn threat. Tiered routing is critical. *(AE handoff call)*
3. **Product and channel tracking on cases is required** — Lisa was "emphatic" about tracking which product a case relates to and how it came in. These are must-have custom fields. *(AE handoff call)*
4. **Team is ~8 users (within Enable tier limit of 10)** — 6 support agents + 2 managers. Well within capacity. *(AE handoff call)*
5. **Speed is a priority** — Lisa wants the team using Salesforce "within a couple weeks, not a couple months." Keep implementation practical and focused. *(AE handoff call)*

### Recommended Focus Areas
1. **Case management structure** — Moving from unstructured email to structured cases with proper fields, types, and statuses is the foundational win.
2. **Tier-based routing and escalation** — Assignment rules that route by customer tier (Silver/Gold/Platinum) with escalation rules that enforce different SLAs per tier.
3. **Email-to-Case from Gmail** — Since the team already lives in Gmail, Email-to-Case provides the smoothest transition path. Cases created from email with threading preserved.

### Industry-Specific Recommendations
Based on Perplexity research for B2B SaaS:
- **Tiered SLAs are standard** — B2B SaaS companies commonly use Silver (8h response) / Gold (2-4h) / Platinum (30-60 min) response time tiers. Relay Logic's tiered approach is well-aligned.
- **Common case types for SaaS support** — Bug reports, integration issues, billing inquiries, feature requests, and onboarding questions. Map these to Relay Logic's specific product areas.
- **Multi-case escalation** — Industry best practice is to auto-escalate when a single account has 3+ open cases. This directly addresses Lisa's Platinum customer incident.

### Items for Elevate/Transform Discussion
| Feature | Context from Call | Why Out of Scope |
|---------|-------------------|------------------|
| Customer Portal | "Lisa asked about a customer portal — somewhere customers could log in and see their tickets" | Customer Community/Portal requires Transform tier ($60K) |
| Stripe Integration | "They use Stripe for billing, so she mentioned wanting to see subscription data in Salesforce" | External system integration beyond Enable scope. Consider Elevate ($35K) or Transform. |

### Assumptions Made
| Assumption | Confidence | Verify With Client |
|------------|------------|-------------------|
| Team uses Gmail (not Outlook) | High | AE said "shared Gmail inbox" — confirm all agents use Gmail |
| ~8 Salesforce users total | Medium | AE said "half a dozen support folks plus a couple of managers" — get exact headcount |
| US-based, single time zone | Low | Not mentioned in transcript — confirm time zone and business hours |
| No historical cases to migrate | Medium | Current system is email — unclear if they want to import email threads as cases |
| Customer tiers are on the Account level | Medium | Confirm how Silver/Gold/Platinum is determined (contract, revenue, manual?) |
| Standard business hours (M-F) | Low | Not discussed — confirm if they offer weekend/after-hours support |

### Questions to Clarify in Discovery Session
1. **What are the exact SLA response times per tier?** — Jordan mentioned "different response times by tier" but didn't have specifics. Need numbers from Lisa/Marcus.
2. **What products/modules does Relay Logic offer?** — They want to track "product" on cases. Need the actual product list for picklist values.
3. **How are customer tiers determined?** — Silver/Gold/Platinum — is this contract-based, revenue-based, or manually assigned?
4. **What is the team's exact structure?** — Need names, emails, roles, and reporting lines for all 8 users.
5. **Do they need a web form for case submission?** — Transcript focused on email, but Web-to-Case is in scope if they want it.
6. **What does "smart routing" mean specifically?** — Lisa wants high-tier multi-case customers flagged. Need to define the exact routing logic.

---

## How to Use This Worksheet

This worksheet has been pre-filled using information from the AE handoff call with Jordan Park (Feb 25, 2026). Review each section and bring this to your discovery call with Lisa Chen and Marcus.

- **📝 AI (High)** — Directly stated in the handoff transcript
- **📝 AI (Medium)** — Inferred from context in the transcript
- **📝 AI (Low)** — Best practice suggestion from industry research (no client input)
- **📝 AI (Perplexity)** — Validated against B2B SaaS industry best practices
- **❓ Needs Discussion** — Unknown or unclear — ask in discovery session
- **N/A** — Not applicable to this client

---

## Section 1: About Your Business

*Let's start with the basics about how your company operates.*

### Time Zones & Business Hours

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What time zone is your main office in? | ❓ Needs Discussion | Not mentioned in handoff call |
| Do you have support teams in multiple time zones? | ❓ Needs Discussion | Company is ~200 employees, may have distributed team |
| What are your support team's business hours? | ❓ Needs Discussion | 📝 AI (Low): B2B SaaS typical is M-F 8AM-6PM with extended hours for Platinum |
| Do you observe holidays? | ❓ Needs Discussion | Affects escalation rule timing |
| If yes, which holidays? | ❓ Needs Discussion | 📝 AI (Low): US federal holidays typical for mid-market SaaS |

---

## Section 2: Your Support Team

*Tell us about the people who will use the system.*

### Team Structure

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How many people will use the support system? | 📝 AI (High): ~8 users (6 agents + 2 managers) | AE: "About half a dozen support folks, plus a couple of managers." Max 10 for Enable tier — within limit. |

### User List

*Please list each user who needs access:*

| Name | Email | Role | Manager |
|------|-------|------|---------|
| Lisa Chen | ❓ Needs Discussion | Manager (VP Customer Success) | 📝 AI (High): Main sponsor |
| Marcus [Last Name] | ❓ Needs Discussion | Team Lead | 📝 AI (High): Reports to Lisa |
| Agent 1 | ❓ Needs Discussion | Agent | ❓ Marcus or Lisa |
| Agent 2 | ❓ Needs Discussion | Agent | ❓ Marcus or Lisa |
| Agent 3 | ❓ Needs Discussion | Agent | ❓ Marcus or Lisa |
| Agent 4 | ❓ Needs Discussion | Agent | ❓ Marcus or Lisa |
| Agent 5 | ❓ Needs Discussion | Agent | ❓ Marcus or Lisa |
| Agent 6 | ❓ Needs Discussion | Agent | ❓ Marcus or Lisa |

*Need exact headcount, names, emails, and reporting lines from discovery call.*

### Support Team Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the reporting relationships for your support team? | 📝 AI (Medium): Multi-level (Lisa → Marcus → Agents) | AE mentioned Lisa as VP and Marcus as team lead — implies 3-level hierarchy |
| Do managers need to see their team's cases automatically? | 📝 AI (Medium): Yes | Lisa needs visibility into VIP cases across the team. Role hierarchy grants upward visibility. |
| Do any users need special permissions beyond standard case management? | ❓ Needs Discussion | Lisa likely needs admin/reporting access. Marcus may need bulk operations. |
| If yes, what special permissions? | ❓ Needs Discussion | |

---

## Section 3: Your Existing Customer Data

*Let's plan how to bring your current data into the new system.*

### Data Sources

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Where is your customer data currently stored? | 📝 AI (High): Email (shared Gmail inbox) | AE: "running everything through a shared Gmail inbox." May also have customer data in other systems (billing via Stripe mentioned). |
| Approximately how many customer accounts do you have? | ❓ Needs Discussion | Company is mid-market B2B SaaS with ~200 employees — could be hundreds to thousands of accounts |
| Approximately how many contacts (people) do you have? | ❓ Needs Discussion | |
| Do you have historical cases to bring over? | ❓ Needs Discussion | 📝 AI (Medium): Unlikely — current "cases" are email threads in Gmail. May want a clean start. Confirm with client. |

### Data Quality

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How clean is your current data? | ❓ Needs Discussion | 📝 AI (Medium): Likely "significant cleanup needed" given unstructured Gmail inbox |
| What cleanup is needed before migration? | ❓ Needs Discussion | Will depend on what data sources exist beyond email |

### Duplicate Prevention

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What duplicate prevention do you need going forward? | 📝 AI (Low): Block duplicate Contacts by email, Alert on duplicate Accounts by name | Standard B2B SaaS best practice |

---

## Section 4: Case Management & Tracking

*How you track and manage support requests.*

### Case Types

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the 3-5 main types of support requests you handle? | 📝 AI (Perplexity): 1. Technical Issue / Bug Report 2. Integration / API Issue 3. Billing Question 4. Feature Request 5. General Inquiry | Perplexity: Common B2B SaaS case types. Relay Logic is a workflow automation platform — integration issues are likely high volume. Confirm with Lisa/Marcus which categories match their reality. |

### Case Statuses

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need additional case statuses beyond standard (New, In Progress, Escalated, Closed)? | 📝 AI (Perplexity): Yes — add "Waiting on Customer" and "Resolved" | Perplexity: "Waiting on Customer" is standard for B2B SaaS to pause SLA timers. "Resolved" separates agent resolution from formal closure. Full set: New, In Progress, Waiting on Customer, Escalated, Resolved, Closed. |

### Case Priorities

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you use the standard priorities (Low, Medium, High, Critical)? | 📝 AI (Low): Yes — use standard (Low, Medium, High, Critical) | Standard priorities work well. Priority + Customer Tier together drive escalation timing. |

### Escalation Rules

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should High priority cases escalate immediately or after a time period? | ❓ Needs Discussion | 📝 AI (Perplexity): For B2B SaaS, High priority Platinum cases should escalate after 1 hour; Gold after 2-3 hours; Silver after 6-8 hours |
| Should Medium priority cases escalate? | ❓ Needs Discussion | 📝 AI (Perplexity): Yes — Platinum after 2 hours, Gold after 4-6 hours, Silver after 12-18 hours |
| Should Low priority cases escalate? | ❓ Needs Discussion | 📝 AI (Perplexity): Yes — Platinum after 4 hours, Gold after 8 hours, Silver after 24+ hours |
| How long should a case stay in "New" status before escalating? | ❓ Needs Discussion | Lisa needs to define SLAs per tier. AE: "She mentioned different response times by tier too, but I don't have the specifics." |
| Who should receive notifications when cases escalate? | 📝 AI (Medium): Lisa Chen (VP) and/or Marcus (Team Lead) | AE: Lisa was "livid" about the Platinum case that slipped through. She needs escalation visibility. |

### Custom Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do agents need to track on cases? | 📝 AI (High): 1. Product / Module (picklist) 2. Case Channel / Origin (picklist) 3. Customer Tier (Silver/Gold/Platinum — from Account) | AE: "They want to track product and channel on every case. Lisa was pretty emphatic about that." Customer Tier drives routing and escalation logic. |
| | 📝 AI (Perplexity): 4. Affected Workflow ID (text — for linking to specific customer workflows) 5. Software Version (picklist — for tracking version-specific issues) | Perplexity: B2B SaaS support teams commonly track product-specific identifiers. Relay Logic likely needs a way to reference customer workflows. ❓ Confirm with client. |

### Required Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which fields should be required when creating a case? | 📝 AI (Medium): Case Type, Priority, Customer Contact, Description, Product/Module | Product tracking is a top priority for Lisa — making it required ensures agents always capture it. |

---

## Section 5: Case Capture

*How customers submit support requests.*

### Web-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want customers to submit cases via a form on your website? | ❓ Needs Discussion | Not mentioned in handoff call. Current support is via email. May want this as an additional channel. |
| What information should customers provide on the web form? | 📝 AI (Perplexity): Name, Email, Company, Subject, Description, Product/Feature, Severity | Perplexity: Limit to 7-10 fields for good UX. Include product dropdown to auto-categorize. |
| Should the web form include spam protection (reCAPTCHA)? | 📝 AI (Low): Yes | Standard best practice for public-facing forms |

### Email-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want customers to create cases by emailing a support address? | 📝 AI (High): Yes | AE: Team currently uses shared Gmail inbox. Email-to-Case is the natural migration path. |
| What email address(es) should customers use? | 📝 AI (Medium): support@relaylogic.com (or current shared Gmail address) | ❓ Need to confirm actual email address. Transition plan: forward existing Gmail to Salesforce Email-to-Case routing address. |

### Auto-Response

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What should the automatic confirmation email say when a case is created? | 📝 AI (Perplexity): "Thank you for contacting Relay Logic Support. We've received your request and created Case #{Case Number}: {Subject}. Expected response time: [based on your support tier]. Track your case status or check our help docs at [link]. If urgent, reply directly to this email." | Perplexity: B2B SaaS auto-responses should confirm receipt, set SLA expectations, and offer self-service. |

### Email Threading

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should email conversations stay threaded on the case? | 📝 AI (High): Yes | Critical for Gmail migration — team is used to threaded email conversations. Threading keeps context together. |

### Case Origin Tracking

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What sources can cases come from? | 📝 AI (High): Email, Phone | AE: Lisa wants to track "how it came in." Start with Email (primary) and Phone. 📝 AI (Perplexity): Also consider Web (if Web-to-Case enabled) and Chat (future/parking lot). |

---

## Section 6: Case Assignment & Routing

*How cases get to the right agent.*

### Assignment Approach

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want cases automatically assigned when created or will agents claim from a queue? | 📝 AI (Medium): Combination — auto-assign Platinum/Critical cases directly to senior agents; other cases go to team queue for claiming | AE: Lisa wants "smart routing" for VIP customers. Combination approach gives VIP priority while keeping flexibility for the team. |

### Assignment Criteria

*If using automatic assignment:*

| Criteria | Assigned To | Notes |
|----------|-------------|-------|
| 📝 AI (High): Customer Tier = Platinum | Senior agent or dedicated queue | AE: "if a high-tier customer has multiple issues going on, that should get flagged and routed to someone senior" |
| 📝 AI (Medium): Customer Tier = Platinum AND Priority = High/Critical | Marcus (Team Lead) or escalation queue | VIP high-priority cases get immediate senior attention |
| 📝 AI (Low): Customer Tier = Gold | General Support Queue (priority handling) | Gold customers go to general queue but with elevated priority |
| 📝 AI (Low): Customer Tier = Silver (or unmatched) | General Support Queue | Standard queue, standard SLA |

### Queues

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need shared queues where multiple agents can claim cases? | 📝 AI (Medium): Yes | Team of 6 agents needs a shared queue for workload distribution |
| What queues do you need? | 📝 AI (Perplexity): 1. General Support Queue (all agents) 2. VIP / Platinum Queue (senior agents only) 3. Escalation Queue (managers) | Perplexity: B2B SaaS teams of 6-10 typically use 2-3 queues. VIP queue is critical for Relay Logic given the Platinum churn incident. |
| Should agents be notified when cases are added to their queue? | 📝 AI (Low): Yes | Without notification, agents must manually check — not ideal for SLA enforcement |

### Default Case Owner

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who should be assigned cases that don't match any assignment rules? | 📝 AI (Medium): General Support Queue | Fallback for unmatched cases. Queue ensures nothing gets lost (addresses the "dropping things" problem). |

---

## Section 7: Contact & Account Management

*Customer information tracking.*

### Custom Account Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do you need to track for customer accounts? | 📝 AI (High): 1. Customer Tier (picklist: Silver, Gold, Platinum) | AE: Tiered customers are core to the routing/escalation model. This field drives assignment rules. |
| | 📝 AI (Perplexity): 2. Subscription Plan (text or picklist) 3. Contract Start Date / Renewal Date | Perplexity: B2B SaaS companies commonly track subscription info on accounts. ❓ May overlap with future Stripe integration (parking lot). Confirm what's needed now vs. later. |

### Custom Contact Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do you need to track for contacts? | 📝 AI (Low): 1. Preferred Contact Method (picklist: Email, Phone) 2. Role/Department at customer company | Standard B2B contact fields. ❓ Needs Discussion — may not be priority for initial rollout. |

### Account Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you have parent company and subsidiary relationships that need to be tracked? | ❓ Needs Discussion | 📝 AI (Medium): Likely not critical for initial setup. Relay Logic sells to mid-market ops teams — probably direct accounts, not complex hierarchies. |

### Contacts to Multiple Accounts

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Can one contact work with multiple customer accounts? | ❓ Needs Discussion | 📝 AI (Low): Unlikely for B2B SaaS — contacts usually belong to one company. |

### Required Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which Account fields should be required? | 📝 AI (Medium): Customer Tier, Account Name | Customer Tier is required for routing logic to work |
| Which Contact fields should be required? | 📝 AI (Low): Email | Email is required for Email-to-Case matching |

---

## Section 8: Email Integration

*How agents communicate with customers via email.*

### Email System

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email system do your agents use? | 📝 AI (High): Gmail | AE: "running everything through a shared Gmail inbox." Gmail Integration and Sync included in Enable tier. |

### Email Templates

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email templates should be available to agents? | 📝 AI (Perplexity): 1. Case Acknowledgment (auto-response) 2. Request More Information 3. Case Resolved / Solution Provided 4. Escalation Notification (internal) 5. Case Follow-Up (post-resolution) | Perplexity: Top 5 templates for B2B SaaS support. Limit of 10 for Enable tier — start with 5 core templates, add more as needed. ❓ Confirm with Lisa/Marcus which templates they use most often via email today. |

### Organization-Wide Email Address

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email address should appear as the sender when agents email customers from Salesforce? | 📝 AI (Medium): support@relaylogic.com | ❓ Confirm actual email address. This should match their current support email for customer continuity. Requires domain verification with IT. |

### Email Signature

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need a standard email signature on all outbound emails? | 📝 AI (Low): Yes | Standard practice for professional B2B communication |
| If yes, what should it include? | ❓ Needs Discussion | Typically: Company name, support hours, help center link |

---

## Section 9: Activity Management

*Tracking tasks, events, and calls.*

### Task Types

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What types of tasks do agents typically create? | 📝 AI (Low): 1. Follow up with customer 2. Escalate to engineering 3. Internal review / investigation 4. Post-resolution check-in | Standard support task types. ❓ Confirm with Marcus what follow-up actions the team performs today. |

### Activity Reminders

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should agents receive automatic reminders before tasks are due? | 📝 AI (Low): Yes | Helps prevent dropped follow-ups — directly addresses their current pain point of "things getting dropped." |

---

## Section 10: Automation

*Business rules that happen automatically.*

### Automated Actions

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Beyond automatic assignment and escalation, do you need any other automated actions? | 📝 AI (Medium): Yes — see below | Limit of 3 automations for Enable tier |

*Suggested automations based on discovery:*

| Automation 1 | Details |
|--------------|---------|
| What triggers it? | 📝 AI (High): Platinum customer has 3+ open cases simultaneously |
| What happens? | 📝 AI (High): Flag account, notify Marcus (Team Lead) and Lisa (VP), escalate all open cases to VIP queue |
| Notes | AE: "if a high-tier customer has multiple issues going on, that should get flagged and routed to someone senior." This is Lisa's #1 request — the Platinum churn incident. Uses 1 of 3 flow slots. |

| Automation 2 | Details |
|--------------|---------|
| What triggers it? | 📝 AI (Perplexity): Case status is "Waiting on Customer" for 7+ days with no response |
| What happens? | 📝 AI (Perplexity): Auto-close case, send notification to customer, create follow-up task for agent |
| Notes | Perplexity: Standard B2B SaaS auto-close workflow. Prevents stale cases from cluttering queues. |

| Automation 3 | Details |
|--------------|---------|
| What triggers it? | 📝 AI (Perplexity): Case marked as "Resolved" |
| What happens? | 📝 AI (Perplexity): Create follow-up task for agent to check in with customer after 3 business days |
| Notes | Perplexity: Post-resolution follow-up improves CSAT and catches re-opened issues early. |

---

## Section 11: Reports & Dashboards

*Tracking key metrics and performance.*

### Dashboard Metrics

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the top 5 metrics your support team needs to track daily? | 📝 AI (Perplexity): 1. Open cases by priority and customer tier 2. Average first response time by tier (SLA compliance) 3. Escalated cases count (current) 4. Cases by product/module (volume distribution) 5. Agent caseload / cases per agent | Perplexity: Top metrics for a VP of Customer Success at B2B SaaS. #1 and #2 directly address Lisa's VIP handling concern. #4 addresses her product tracking requirement. |

*Note: Standard reports (case volume, aging, resolution times, queue status, agent productivity) are included out-of-the-box. The 5 custom reports above go on the 1 custom dashboard included in Enable tier.*

---

## Section 12: Mobile Access

*Support agents working away from their desk.*

### Mobile Needs

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do your support agents need to access and update cases while away from their desk? | ❓ Needs Discussion | Not mentioned in handoff call. 📝 AI (Low): Likely yes for managers (Lisa/Marcus) to monitor escalations on the go. |

---

## Section 13: Security & Access

*Who can see and do what.*

### Organization-Wide Defaults (Record Access)

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who should be able to see cases by default? | 📝 AI (Medium): Public Read Only — all agents can view all cases, but only owner/assigned agent can edit | Team of 6 agents working from shared queue — they need visibility to claim and collaborate. Read-only prevents accidental edits. |
| Who should be able to see accounts by default? | 📝 AI (Medium): Public Read Only | Agents need to see customer tier and account info to handle cases properly. |
| Who should be able to see contacts by default? | 📝 AI (Medium): Public Read Only | Same rationale — agents need contact info for case handling. |

### Sharing Rules

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How should private records be shared across the team? | 📝 AI (Medium): N/A if OWD is Public Read Only | If OWD stays Public Read Only, sharing rules are not needed. If client wants Private OWD, we'll need role-based sharing rules (managers see all, agents see their own + queue). |

### Field-Level Security

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Are there any sensitive fields that certain users should not see or edit? | ❓ Needs Discussion | 📝 AI (Low): Possible — internal notes field visible only to managers. Customer tier field editable only by managers (prevents agents from changing tier). |
| If yes, which fields and for which users? | ❓ Needs Discussion | |

---

## Section 14: Branding

*Make Salesforce look like your company.*

### Company Branding

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What branding should be applied to the Salesforce interface? | ❓ Needs Discussion | Standard: company logo + brand colors |
| Do you have a logo file ready? | ❓ Needs Discussion | PNG or SVG format preferred |
| What are your primary brand colors? | ❓ Needs Discussion | Hex codes needed |

---

## Parking Lot

*Items that came up but are out of scope for Enable tier. We'll discuss tier upgrades if needed.*

| Item | Why It's Out of Scope | Notes | Suggested Tier |
|------|----------------------|-------|----------------|
| Customer Portal | Customer Community/Portal is a Transform tier feature. Requires Experience Cloud setup, guest user profiles, and ongoing maintenance. | AE: "Lisa asked about a customer portal — somewhere customers could log in and see their tickets." Lisa was fine parking this for phase 2. | Transform ($60K) |
| Stripe Billing Integration | External system integration (API/middleware) is beyond Enable scope. Would require custom Apex or middleware like MuleSoft. | AE: "they use Stripe for billing, so she mentioned wanting to see subscription data in Salesforce at some point." Lisa was fine with phase 2. | Elevate ($35K) or Transform ($60K) |
| Skills-Based Routing | Requires Omni-Channel, which is an Elevate+ feature. Enable tier uses criteria-based assignment rules. | Not explicitly requested, but "smart routing" aspirations may evolve into this need. | Elevate ($35K) |
| Knowledge Base / Help Center | Knowledge Management is an Elevate+ feature. Includes articles, categories, publishing workflows. | Not mentioned in handoff call, but common request once support is structured. May come up in discovery. | Elevate ($35K) |

---

## Version History

| Version | Date | Inputs | Key Changes |
|---------|------|--------|-------------|
| v1 | 2026-03-02 | AE handoff transcript (Jordan Park, Feb 25, 2026) | Initial AI pre-fill from sales handoff call |

## Research Notes (Perplexity)

### Industry Context: B2B SaaS (Workflow Automation)

**Typical Support Characteristics:**
- B2B SaaS support teams commonly use tiered models (Silver/Gold/Platinum) with differentiated SLAs
- Common case types: Bug reports (highest volume), integration/API issues, billing questions, feature requests, onboarding
- Mid-market SaaS companies (200 employees) typically have 6-10 support agents
- Average first response time targets: Platinum 30-60 min, Gold 2-4 hours, Silver 8-24 hours

**Industry-Specific Considerations:**
- Workflow automation products generate high integration-related support volume (API errors, connector issues)
- B2B SaaS customers expect email-based support as primary channel
- Multi-case detection (3+ open per account) is a standard escalation trigger
- Post-resolution follow-up (3-5 business days) is standard practice for SaaS retention

### Section-Specific Validation

**Case Management (Section 4):**
- Query: "Salesforce case types and statuses for B2B SaaS workflow automation companies"
- Key findings: Standard case types (Technical, Integration, Billing, Feature Request, General) align with SaaS norms. "Waiting on Customer" status is essential for SLA timer pausing.

**Case Capture (Section 5):**
- Query: "Web-to-Case and Email-to-Case best practices for B2B SaaS companies"
- Key findings: Email-to-Case is primary channel for B2B. Web form should have 7-10 fields max. Auto-response should include case number, SLA expectation, and self-service link.

**Case Assignment & Routing (Section 6):**
- Query: "Case assignment and queue structure for mid-market SaaS support teams"
- Key findings: 2-3 queues optimal for 6-10 agents. Tier-based routing (Platinum direct to VIP queue, others to general). Combination of auto-assign (VIP) and queue claiming (standard).

**Escalation Rules (Section 4):**
- Query: "Escalation rules and SLA best practices for B2B SaaS tiered support"
- Key findings: Escalation thresholds scale by both priority and customer tier. Platinum Critical: 15-30 min. Gold High: 2-3 hours. Multi-case detection (3+ per account) should auto-escalate.

**Reports & Dashboards (Section 11):**
- Query: "Support dashboard KPIs for B2B SaaS VP of Customer Success"
- Key findings: Top 5 metrics: Open cases by priority/tier, first response time by tier (SLA compliance), escalated case count, cases by product, agent caseload. CSAT/NPS important but may not be tracked in Enable tier.

---

**Document Status:** AI Pre-filled (Ready for Consultant Review)
**Generated:** 2026-03-02
**Sources:** AE Handoff Transcript — Jordan Park to Consultant (Feb 25, 2026)
**Template Used:** service-cloud-enable-worksheet-template.md
**Scope File:** service-cloud/tiers/enable.md
