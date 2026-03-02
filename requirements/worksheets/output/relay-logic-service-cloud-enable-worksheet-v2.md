# Service Cloud Starter Pack: Enable Tier Requirements Worksheet

**Client:** Relay Logic
**Cloud:** Service Cloud
**Tier:** Enable ($20,000 | 6-8 weeks)
**Date:** 2026-03-02
**Version:** 2 (Updated from Discovery Call with Lisa Chen & Marcus Webb)
**Consultant:** [Consultant Name]

---

## AI Analysis Summary

**Client:** Relay Logic
**Cloud:** Service Cloud
**Tier:** Enable ($20,000)
**Industry:** B2B SaaS (Workflow Automation)
**Team Size:** ~200 employees (7 Salesforce users)
**Version:** 2 (Iteration 2 — 2026-03-02)

### Worksheet Completion Status
- Sections complete (✅ Confirmed): 5 of 14 (partially — many fields within sections confirmed)
- Sections partially filled (📝 AI suggestions): 8
- Sections needing discussion (❓): 1 (Branding)
- Sections not started: 0

### Key Findings from Discovery
1. **Team is split by product line** — Marcus's team (Jake, Anika) handles Core Platform; Priya's team (Sam, Rachel) handles Integrations. This drives queue structure, case routing, and visibility. Agents should NOT see the other team's cases. *(Discovery call — Lisa & Marcus)*
2. **VIP detection threshold is 2+ open cases for Gold/Platinum customers** — Lower threshold than initially assumed (was 3+ in v1). Lisa: "Two or more means there's a pattern." VIP includes both Gold AND Platinum (not just Platinum). *(Discovery call — Lisa)*
3. **Three products confirmed: Core Platform, Integrations, Analytics Module** — Product field is required on every case. Analytics Module is newly launched (third product). *(Discovery call — Marcus & Lisa)*
4. **SLAs confirmed: Platinum 2h, Gold 4h, Silver next business day** — Business hours vs clock hours still TBD. Lisa: "I'd say business hours for now? But honestly, I'm not sure." *(Discovery call — Lisa)*
5. **Cases OWD must be Private, not Public Read Only** — Lisa was explicit: agents only see their own cases and team queue. Leads see their team. Lisa sees everything. This is a significant change from v1. *(Discovery call — Lisa)*

### Recommended Focus Areas
1. **Private OWD security model with role-based sharing** — The team split by product line requires Private case visibility with sharing rules granting leads access to their team's cases and Lisa access to all. This is more complex than the Public Read Only model in v1 but is the right approach.
2. **Three automation flows (uses all 3 Enable tier slots)** — VIP detection + Chatter notification, new customer prioritization, and auto-task creation. These are client-driven requirements, not AI suggestions. All 3 slots are committed.
3. **Product-based queue routing** — Core Platform Queue and Integrations Queue with a Senior Support Queue for escalated VIP cases. Assignment rules route by product; VIP detection overrides to Senior Queue.

### Industry-Specific Recommendations
Based on Perplexity research for B2B SaaS:
- **2+ open case threshold is validated** — Perplexity confirms 2 is appropriate for premium B2B SaaS; waiting for 3 risks delayed intervention for high-value customers.
- **30-day new customer window is standard** — Aligns with B2B SaaS onboarding phase where churn risk is highest. Consider shortening to 14-21 days if early retention data shows faster drop-off.
- **Private OWD with sharing rules is recommended** for small product-segmented teams — prevents cross-team confusion (which Marcus flagged as a current problem).

### Items for Elevate/Transform Discussion
| Feature | Context from Call | Why Out of Scope |
|---------|-------------------|------------------|
| Customer Portal | Lisa: "We want a customer portal eventually. Somewhere customers can log in, see their cases, maybe submit new ones." | Customer Community/Portal requires Transform tier ($60K) |
| Stripe Integration | Lisa: "Our billing system — we use Stripe — it'd be great if we could see subscription info right in Salesforce." | External system integration beyond Enable scope |

### Assumptions Made
| Assumption | Confidence | Verify With Client |
|------------|------------|-------------------|
| Team uses Gmail (not Outlook) | ✅ Confirmed | Lisa confirmed shared Gmail inbox |
| 7 Salesforce users total | ✅ Confirmed | Lisa: 4 agents + 2 leads. Plus Lisa herself = 7 |
| US-based, single time zone | Low | Not discussed — confirm time zone and business hours |
| No historical cases to migrate | Medium | Not discussed in discovery. Current system is Gmail — confirm if they want email threads imported |
| Customer Tier is on the Account object | ✅ Confirmed | Lisa: "Ideally it'd pull from the account automatically." |
| Standard business hours (M-F) | Low | Not discussed — confirm business hours and holiday schedule |
| SLAs measured in business hours | Medium | Lisa: "business hours for now" but unsure — flag for follow-up |

### Questions to Clarify in Next Session
1. **What time zone and business hours does the support team operate?** — Needed for escalation rule timing and SLA calculation.
2. **Business hours vs clock hours for SLAs?** — Lisa was unsure. This affects escalation rule configuration.
3. **Do you want to import any historical data from Gmail?** — Or start with a clean slate in Salesforce?
4. **What email address should appear as the sender?** — Likely support@relaylogic.com but need to confirm.
5. **Do you need the web form (Web-to-Case) in this phase?** — Marcus mentioned "planning to add" but it wasn't committed.
6. **Branding details** — Logo file, brand colors (hex codes).

---

## How to Use This Worksheet

This worksheet has been updated with information from the discovery call with Lisa Chen and Marcus Webb (March 2, 2026), building on the initial pre-fill from the AE handoff call.

- **✅ Confirmed** — Client validated in the discovery call
- **📝 AI (High)** — Directly stated in the discovery or handoff transcript
- **📝 AI (Medium)** — Inferred from context in the transcripts
- **📝 AI (Low)** — Best practice suggestion from industry research (no client input)
- **📝 AI (Perplexity)** — Validated against B2B SaaS industry best practices
- **❓ Needs Discussion** — Unknown or unclear — ask in next session
- **N/A** — Not applicable to this client

---

## Section 1: About Your Business

*Let's start with the basics about how your company operates.*

### Time Zones & Business Hours

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What time zone is your main office in? | ❓ Needs Discussion | Not discussed in either call |
| Do you have support teams in multiple time zones? | ❓ Needs Discussion | Company is ~200 employees, team is 7 people — likely single location but confirm |
| What are your support team's business hours? | ❓ Needs Discussion | 📝 AI (Low): B2B SaaS typical is M-F 8AM-6PM. Lisa mentioned "business hours" re: SLAs but didn't specify. |
| Do you observe holidays? | ❓ Needs Discussion | Affects escalation rule timing |
| If yes, which holidays? | ❓ Needs Discussion | 📝 AI (Low): US federal holidays typical for mid-market SaaS |

---

## Section 2: Your Support Team

*Tell us about the people who will use the system.*

### Team Structure

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How many people will use the support system? | ✅ Confirmed: 7 users (4 agents + 2 team leads + 1 VP/Manager) | Lisa: "We have six people total on the support side. Four are frontline agents... two team leads." Plus Lisa herself who needs full visibility. Max 10 for Enable tier — well within limit. |

### User List

*All names and roles confirmed in discovery call:*

| Name | Email | Role | Manager | Team / Product Line |
|------|-------|------|---------|---------------------|
| Lisa Chen | ❓ Needs Discussion | Manager (VP Customer Success) | — | Oversees all; doesn't handle cases day-to-day |
| Marcus Webb | ❓ Needs Discussion | Team Lead | Lisa Chen | Core Platform team |
| Priya Sharma | ❓ Needs Discussion | Team Lead | Lisa Chen | Integrations team |
| Jake Torres | ❓ Needs Discussion | Agent (Senior) | Marcus Webb | Core Platform team |
| Anika Patel | ❓ Needs Discussion | Agent | Marcus Webb | Core Platform team |
| Sam Okafor | ❓ Needs Discussion | Agent | Priya Sharma | Integrations team |
| Rachel Kim | ❓ Needs Discussion | Agent | Priya Sharma | Integrations team |

*Need email addresses for all 7 users.*

### Support Team Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the reporting relationships for your support team? | ✅ Confirmed: Multi-level. Lisa → Marcus & Priya (leads) → Agents. Teams split by product line. | Marcus: "I'm one of the two team leads. The other lead is Priya Sharma. Under me I have two agents — Jake Torres and Anika Patel. Under Priya, she has Sam Okafor and Rachel Kim." |
| Do managers need to see their team's cases automatically? | ✅ Confirmed: Yes — but only their own team. Lisa sees all. | Lisa: "The leads need to see their team's cases plus anything unassigned. But the agents should really only see their own stuff and cases in their team's queue." Marcus: "Just my team's for me. Priya sees hers. Lisa's the only one who sees everything." |
| Do any users need special permissions beyond standard case management? | ✅ Confirmed: No deletion for anyone. Lisa needs full reporting access. | Lisa: "No. Absolutely not. Nobody deletes anything. Leads and agents can update cases, close them, but no deleting." |
| If yes, what special permissions? | ✅ Confirmed: Lisa — full visibility and reporting. Leads — view team's cases + unassigned. Agents — own cases + team queue only. No delete for any role. | |

---

## Section 3: Your Existing Customer Data

*Let's plan how to bring your current data into the new system.*

### Data Sources

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Where is your customer data currently stored? | ✅ Confirmed: Email (shared Gmail inbox) | Lisa: "We've been running support out of a shared Gmail inbox for about two years now." Stripe for billing (parking lot). |
| Approximately how many customer accounts do you have? | ❓ Needs Discussion | Company is mid-market B2B SaaS with ~200 employees — could be hundreds to thousands of accounts |
| Approximately how many contacts (people) do you have? | ❓ Needs Discussion | |
| Do you have historical cases to bring over? | ❓ Needs Discussion | 📝 AI (Medium): Unlikely — current "cases" are email threads in Gmail. Consultant suggested "clean start" approach. Confirm with client. |

### Data Quality

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How clean is your current data? | 📝 AI (Medium): Likely "significant cleanup needed" given unstructured Gmail inbox | Two years of unstructured email |
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
| What are the 3-5 main types of support requests you handle? | 📝 AI (Perplexity): 1. Technical Issue / Bug Report 2. Integration / API Issue 3. Billing Question 4. Feature Request 5. General Inquiry | Not specifically discussed in discovery call. Perplexity: Common B2B SaaS case types. Now that we know there are 3 products (Core Platform, Integrations, Analytics), integration issues are likely high-volume. ❓ Confirm with Lisa/Marcus which categories match their reality. |

### Case Statuses

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need additional case statuses beyond standard (New, In Progress, Escalated, Closed)? | 📝 AI (Perplexity): Yes — add "Waiting on Customer" and "Resolved" | Full set: New, In Progress, Waiting on Customer, Escalated, Resolved, Closed. "Waiting on Customer" is standard for B2B SaaS to pause SLA timers. Not specifically discussed in discovery — confirm. |

### Case Priorities

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you use the standard priorities (Low, Medium, High, Critical)? | ✅ Confirmed: Yes — standard (Low, Medium, High, Critical) | Lisa and Marcus referenced "high priority" and "critical" in discovery call. VIP detection bumps to Critical. New customer rule bumps to High. |

### SLA Response Times by Customer Tier

| Customer Tier | First Response SLA | Notes |
|---------------|-------------------|-------|
| ✅ Confirmed: Platinum | ✅ Confirmed: 2 hours | Lisa: "Platinum customers expect a response within two hours." |
| ✅ Confirmed: Gold | ✅ Confirmed: 4 hours | Lisa: "Gold gets four hours." |
| ✅ Confirmed: Silver | ✅ Confirmed: Next business day | Lisa: "Silver is next business day." |
| ❓ SLA timing basis | ❓ Needs Discussion: Business hours vs clock hours | Lisa: "I'd say business hours for now? But honestly, I'm not sure. Can we decide that later?" |

### Escalation Rules

| Question | Your Answer | Notes |
|----------|-------------|-------|
| When should cases escalate based on tier + priority? | 📝 AI (Medium): Use SLA times above as escalation triggers. If case is in "New" status past the SLA window, escalate. | Specific escalation timing TBD once business hours vs clock hours is decided. |
| Who should receive notifications when cases escalate? | ✅ Confirmed: Chatter notification to team feed. Start with Chatter only, add email later if needed. | Marcus: "Let's start with Chatter. If people miss things, we'll add email. But I don't want people drowning in notifications on day one." |

### Custom Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do agents need to track on cases? | ✅ Confirmed: 1. **Product / Module** (picklist: Core Platform, Integrations, Analytics Module) — REQUIRED | Lisa: "Every single case needs to have a product tagged on it. We can't have cases floating around with no product." Marcus confirmed 3 products. |
| | ✅ Confirmed: 2. **Customer Tier** (picklist: Silver, Gold, Platinum — from Account) | Lisa: "Ideally it'd pull from the account automatically." Consultant: "We can probably do both — have it default from the account and still allow override." |
| | ✅ Confirmed: 3. **Case Origin** (standard field — Email, Phone, Web) | Marcus: "We definitely need that." Consultant: "Salesforce has a standard field for that — Case Origin." |
| | 📝 AI (Perplexity): 4. Affected Workflow ID (text — for linking to specific customer workflows) | Perplexity suggestion from v1. Not discussed in discovery. ❓ Confirm if needed — may be valuable for a workflow automation platform. |

### Required Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which fields should be required when creating a case? | ✅ Confirmed: Product / Module (required), Case Type, Priority, Customer Contact, Description | Lisa: "Exactly" when asked if Product should be required. Product tracking is the #1 data requirement. |

---

## Section 5: Case Capture

*How customers submit support requests.*

### Web-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want customers to submit cases via a form on your website? | 📝 AI (High): Yes — planning to add | Marcus: "We're planning to add a web form on our help center." Not yet committed for this phase — ❓ confirm if this is in scope for phase 1 or a later add. |
| What information should customers provide on the web form? | 📝 AI (Perplexity): Name, Email, Company, Subject, Description, Product/Feature, Severity | Perplexity: Limit to 7-10 fields for good UX. Include product dropdown to auto-categorize. |
| Should the web form include spam protection (reCAPTCHA)? | 📝 AI (Low): Yes | Standard best practice for public-facing forms |

### Email-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want customers to create cases by emailing a support address? | ✅ Confirmed: Yes | Primary channel. Team currently uses shared Gmail inbox. |
| What email address(es) should customers use? | ❓ Needs Discussion | 📝 AI (Medium): Likely support@relaylogic.com or their current shared Gmail address. Need to confirm actual address. |

### Auto-Response

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What should the automatic confirmation email say when a case is created? | 📝 AI (Perplexity): "Thank you for contacting Relay Logic Support. We've received your request and created Case #{Case Number}: {Subject}. Expected response time: [based on your support tier]. Track your case status or check our help docs at [link]. If urgent, reply directly to this email." | Now that SLAs are confirmed (Platinum 2h, Gold 4h, Silver next business day), auto-response can set tier-specific expectations. |

### Email Threading

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should email conversations stay threaded on the case? | ✅ Confirmed: Yes | Critical for Gmail migration — team is used to threaded email conversations. |

### Case Origin Tracking

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What sources can cases come from? | ✅ Confirmed: Email, Phone, Web | Marcus: "Right now everything comes through email, but we're planning to add a web form on our help center. And some customers just call us." |

---

## Section 6: Case Assignment & Routing

*How cases get to the right agent.*

### Assignment Approach

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want cases automatically assigned when created or will agents claim from a queue? | ✅ Confirmed: Combination — product-based routing to team queues (agents claim); VIP auto-assigned to Senior Queue | Lisa's team is split by product line. Standard cases route to the product-specific queue. VIP cases (Gold/Platinum + 2+ open) override to Senior Queue. |

### Assignment Criteria

*Based on discovery call:*

| Criteria | Assigned To | Notes |
|----------|-------------|-------|
| ✅ Confirmed: Product = Core Platform | Core Platform Queue | Marcus's team handles core platform issues |
| ✅ Confirmed: Product = Integrations | Integrations Queue | Priya's team handles integrations product |
| 📝 AI (Medium): Product = Analytics Module | ❓ Needs Discussion — Core Platform Queue or new queue? | Analytics is a newly launched third product. Not discussed who handles it. Likely one of the existing teams for now. |
| ✅ Confirmed: VIP case (Gold/Platinum + 2+ open cases) | Senior Support Queue | Lisa: "If one of them opens a case and they've already got open tickets with us... I want those flagged immediately — bumped to critical priority and routed to our senior agents." VIP rule overrides product routing. |

### Queues

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need shared queues where multiple agents can claim cases? | ✅ Confirmed: Yes | |
| What queues do you need? | ✅ Confirmed: 1. **Core Platform Queue** (members: Marcus, Jake, Anika) 2. **Integrations Queue** (members: Priya, Sam, Rachel) 3. **Senior Support Queue** (members: Marcus, Priya, Jake) | Lisa: "Route it to the senior queue, not a specific person. Whoever's available picks it up." Marcus: "We have a senior support queue — it's me and Priya, basically, plus Jake who's been here the longest." |
| Should agents be notified when cases are added to their queue? | 📝 AI (Medium): Yes — via Chatter for VIP cases. Standard queue notifications for others. | Marcus: "Let's start with Chatter" for VIP alerts. Standard Salesforce queue notifications for regular case routing. |

### Default Case Owner

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who should be assigned cases that don't match any assignment rules? | 📝 AI (Medium): Core Platform Queue (as general fallback) | Cases without a matching product should land somewhere safe. ❓ Confirm with client — could also be a general "Unassigned" queue. |

---

## Section 7: Contact & Account Management

*Customer information tracking.*

### Custom Account Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do you need to track for customer accounts? | ✅ Confirmed: 1. **Customer Tier** (picklist: Silver, Gold, Platinum) | Lisa: "Our SLAs are different by tier." Marcus: "If it was right there on the case, it'd change how we prioritize." Drives assignment rules, escalation, and SLA enforcement. |
| | 📝 AI (Medium): 2. **Account Start Date** (date — for "new customer" 30-day rule) | Needed for the new customer auto-prioritization automation. If standard "Created Date" on Account is sufficient, no custom field needed. ❓ Confirm if they track onboarding start separately from Account creation date. |
| | 📝 AI (Perplexity): 3. Subscription Plan (text or picklist) | Perplexity v1 suggestion. May overlap with future Stripe integration (parking lot). ❓ Confirm if needed now vs. later. |

### Custom Contact Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What information beyond standard fields do you need to track for contacts? | 📝 AI (Low): 1. Preferred Contact Method (picklist: Email, Phone) 2. Role/Department at customer company | Standard B2B contact fields. Not discussed in discovery call. ❓ May not be priority for initial rollout. |

### Account Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you have parent company and subsidiary relationships that need to be tracked? | 📝 AI (Medium): Likely not critical for initial setup | Relay Logic sells to mid-market ops teams. Not discussed in discovery. |

### Contacts to Multiple Accounts

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Can one contact work with multiple customer accounts? | ✅ Confirmed: No | Contacts are only associated to one account. (Confirmed in v1) |

### Required Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which Account fields should be required? | ✅ Confirmed: Customer Tier, Account Name | Customer Tier is required for routing and SLA logic to work. Lisa: "It's not just nice-to-have." |
| Which Contact fields should be required? | 📝 AI (Low): Email | Email is required for Email-to-Case contact matching |

---

## Section 8: Email Integration

*How agents communicate with customers via email.*

### Email System

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email system do your agents use? | ✅ Confirmed: Gmail | Lisa: "We've been running support out of a shared Gmail inbox for about two years now." Gmail Integration and Sync included in Enable tier. |

### Email Templates

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email templates should be available to agents? | 📝 AI (Perplexity): 1. Case Acknowledgment (auto-response) 2. Request More Information 3. Case Resolved / Solution Provided 4. Escalation Notification (internal) 5. Case Follow-Up (post-resolution) | Perplexity: Top 5 templates for B2B SaaS support. Limit of 10 for Enable tier — start with 5. ❓ Confirm with Lisa/Marcus which templates they use most often via email today. |

### Organization-Wide Email Address

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email address should appear as the sender when agents email customers from Salesforce? | ❓ Needs Discussion | 📝 AI (Medium): Likely support@relaylogic.com. Requires domain verification with IT. |

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
| What types of tasks do agents typically create? | ✅ Confirmed: 1. **Initial Response Required** (auto-created — see Automation section) | Lisa: "Auto-create a task for the assigned agent. Something like 'Initial Response Required.'" |
| | 📝 AI (Medium): 2. Follow up with customer 3. Escalate to engineering 4. Internal review / investigation | Standard support task types. Marcus mentioned follow-up as a pain point: "We've had cases sit for days because someone got busy." |

### Activity Reminders

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should agents receive automatic reminders before tasks are due? | ✅ Confirmed: Yes | Marcus: "If there was a task or a reminder created automatically — like 'Hey, you need to respond to this' — that'd be amazing." |

---

## Section 10: Automation

*Business rules that happen automatically.*

### Automated Actions

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Beyond automatic assignment and escalation, do you need any other automated actions? | ✅ Confirmed: Yes — 3 automations (uses all 3 Enable tier flow slots) | All 3 automations are client-driven requirements from the discovery call. |

*Client-confirmed automations:*

| Automation 1: VIP Detection & Alert | Details |
|--------------------------------------|---------|
| What triggers it? | ✅ Confirmed: Gold or Platinum customer opens a case AND already has 1+ other open cases (2+ total open cases including the new one) |
| What happens? | ✅ Confirmed: 1. Bump case to Critical priority 2. Route to Senior Support Queue 3. Post Chatter alert: "VIP Alert: [Tier] customer [Account Name] with [X] open cases — routed to senior queue" |
| Notes | Lisa: "If one of them opens a case and they've already got open tickets with us, that's a red flag... I want those flagged immediately — bumped to critical priority and routed to our senior agents." Lisa: "If they have two or more open cases including the new one." Marcus: Senior queue = Marcus, Priya, Jake. Chatter notification only (no email for now). 📝 AI (Perplexity): 2+ threshold is validated — appropriate for premium B2B SaaS customers. Uses 1 of 3 flow slots. |

| Automation 2: New Customer Prioritization | Details |
|--------------------------------------------|---------|
| What triggers it? | ✅ Confirmed: Case created on an account that is less than 30 days old (regardless of tier) |
| What happens? | ✅ Confirmed: Auto-set case priority to High |
| Precedence | ✅ Confirmed: VIP rule (Automation 1) takes precedence. If customer is both new AND VIP with multiple cases, VIP rule wins → Critical priority. |
| Notes | Lisa: "When an account is brand new — say within their first 30 days — and they open a case, I want that treated as high priority automatically. First impressions matter." 📝 AI (Perplexity): 30-day threshold is validated — aligns with B2B SaaS onboarding churn window. Uses 1 of 3 flow slots. |

| Automation 3: Auto-Task Creation | Details |
|-----------------------------------|---------|
| What triggers it? | ✅ Confirmed: Case is assigned to an agent |
| What happens? | ✅ Confirmed: Auto-create task "Initial Response Required" assigned to case owner. Due date based on priority: Critical = same day, High = next business day, Normal = 3 business days |
| Notes | Lisa: "Auto-create a task for the assigned agent... make the due date reflect the priority. Critical cases — that task should be due today. High priority — maybe tomorrow. Normal — a few days out." 📝 AI (Perplexity): These timing standards are validated for mid-market B2B SaaS. Uses 1 of 3 flow slots. |

### ⚠️ Automation Capacity Note

All 3 Enable tier flow slots are now committed to client-confirmed automations. The following v1 suggestions (Perplexity-based) are deferred:
- **Auto-close stale cases** (Waiting on Customer 7+ days) — consider for post-launch optimization or Elevate tier
- **Post-resolution follow-up task** (check in after 3 days) — consider for post-launch optimization or Elevate tier

---

## Section 11: Reports & Dashboards

*Tracking key metrics and performance.*

### Dashboard Metrics

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the top 5 metrics your support team needs to track daily? | 📝 AI (Perplexity): 1. Open cases by priority and customer tier 2. Average first response time by tier (SLA compliance) 3. Escalated cases count (current) 4. Cases by product/module (volume distribution) 5. Agent caseload / cases per agent | Perplexity: Top metrics for VP of Customer Success at B2B SaaS. #1 and #2 directly address Lisa's VIP handling concern. #4 addresses her product tracking requirement. Now that we know the product split (Core Platform / Integrations / Analytics), #4 is even more relevant for Lisa to see volume per product team. ❓ Confirm with Lisa — these are AI suggestions, not discussed in discovery. |

*Note: Standard reports (case volume, aging, resolution times, queue status, agent productivity) are included out-of-the-box. The 5 custom reports above go on the 1 custom dashboard included in Enable tier.*

---

## Section 12: Mobile Access

*Support agents working away from their desk.*

### Mobile Needs

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do your support agents need to access and update cases while away from their desk? | ❓ Needs Discussion | Not mentioned in either call. 📝 AI (Low): Likely yes for managers (Lisa/Marcus/Priya) to monitor escalations and VIP alerts on the go. |

---

## Section 13: Security & Access

*Who can see and do what.*

### Organization-Wide Defaults (Record Access)

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who should be able to see cases by default? | ✅ Confirmed: **Private** — Only case owner and their team via sharing rules | Lisa: "The agents should really only see their own stuff and cases in their team's queue." Marcus confirmed leads only see their own team's cases. This is a change from v1 (was Public Read Only). |
| Who should be able to see accounts by default? | 📝 AI (Medium): Public Read Only | Agents need to see customer tier and account info for any customer to handle cases properly, even if they can't see the other team's cases. |
| Who should be able to see contacts by default? | 📝 AI (Medium): Public Read Only | Same rationale — agents need contact info for case handling across all accounts. |

### Sharing Rules

*Required because Cases OWD is Private:*

| Rule | Type | Access Level | Notes |
|------|------|-------------|-------|
| ✅ Confirmed: Core Platform team → Core Platform Queue cases | Role-based | Read/Write | Marcus's team (Marcus, Jake, Anika) can view/edit Core Platform cases |
| ✅ Confirmed: Integrations team → Integrations Queue cases | Role-based | Read/Write | Priya's team (Priya, Sam, Rachel) can view/edit Integrations cases |
| ✅ Confirmed: Lisa → All cases | Role hierarchy | Read/Write | Lisa: "I need to see everything — all the cases, all the metrics." Role hierarchy automatically grants upward visibility. |
| 📝 AI (Medium): Senior Queue members → Senior Queue cases | Criteria-based | Read/Write | Marcus, Priya, Jake need access to VIP-escalated cases regardless of product line |

### Record Deletion

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who can delete cases? | ✅ Confirmed: Nobody | Lisa: "No. Absolutely not. Nobody deletes anything." Remove Delete permission from all profiles/permission sets. |

### Field-Level Security

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Are there any sensitive fields that certain users should not see or edit? | 📝 AI (Medium): Customer Tier field on Account — editable only by leads and Lisa (prevents agents from changing tier) | Lisa wants tier to "pull from the account automatically" — agents shouldn't be able to override it on cases. Tier on Account should be restricted to leads/manager. |
| If yes, which fields and for which users? | ❓ Needs Discussion | Confirm: Should agents see but not edit Customer Tier? Any other sensitive fields? |

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
| Customer Portal | Customer Community/Portal is a Transform tier feature. Requires Experience Cloud setup, guest user profiles, and ongoing maintenance. | Lisa (discovery): "We want a customer portal eventually. Somewhere customers can log in, see their cases, maybe submit new ones." Consultant parked it — Lisa agreed: "Those are phase two items." | Transform ($60K) |
| Stripe Billing Integration | External system integration (API/middleware) is beyond Enable scope. Would require custom Apex or middleware like MuleSoft. | Lisa (discovery): "Our billing system — we use Stripe — it'd be great if we could see subscription info right in Salesforce." Lisa agreed to park for phase 2. | Elevate ($35K) or Transform ($60K) |
| Skills-Based Routing | Requires Omni-Channel, which is an Elevate+ feature. Enable tier uses criteria-based assignment rules. | Not explicitly requested, but "smart routing" aspirations may evolve. Current product-based + VIP routing covers immediate needs. | Elevate ($35K) |
| Knowledge Base / Help Center | Knowledge Management is an Elevate+ feature. Includes articles, categories, publishing workflows. | Not mentioned in either call, but Marcus referenced adding a "help center" for Web-to-Case. May come up once support is structured. | Elevate ($35K) |
| Auto-Close Stale Cases | All 3 Enable tier automation slots are committed to client-confirmed flows (VIP detection, new customer priority, auto-task). | Was a v1 Perplexity suggestion. Good automation but no capacity in current tier. Consider post-launch or Elevate. | Post-launch or Elevate ($35K) |
| Post-Resolution Follow-Up Automation | Same — all 3 flow slots are committed. | Was a v1 Perplexity suggestion. Could be handled manually via task creation for now. | Post-launch or Elevate ($35K) |

---

## Version History

| Version | Date | Inputs | Key Changes |
|---------|------|--------|-------------|
| v1 | 2026-03-02 | AE handoff transcript (Jordan Park, Feb 25, 2026) | Initial AI pre-fill from sales handoff call |
| v2 | 2026-03-02 | Discovery call transcript (Lisa Chen & Marcus Webb, Mar 2, 2026) | Major update — team structure confirmed, VIP rules refined, automations confirmed, security model changed to Private OWD |

## Iteration 2 Change Log

### Newly Confirmed (from discovery call)
- Section 2, Team Size: ~8 users → **7 users** (4 agents + 2 leads + 1 VP)
- Section 2, User List: All 7 names, roles, and reporting lines confirmed
- Section 2, Hierarchy: Multi-level with product-line split confirmed
- Section 4, Products: **3 products** (Core Platform, Integrations, Analytics Module)
- Section 4, Product field: Required on every case — confirmed
- Section 4, SLAs: Platinum 2h, Gold 4h, Silver next business day — confirmed
- Section 4, Priorities: Standard (Low/Medium/High/Critical) — confirmed
- Section 5, Email-to-Case: Yes (primary channel) — confirmed
- Section 5, Case Origins: Email, Phone, Web — confirmed
- Section 5, Email Threading: Yes — confirmed
- Section 6, Queues: Core Platform Queue, Integrations Queue, Senior Support Queue — confirmed with members
- Section 7, Customer Tier on Account: Required — confirmed
- Section 8, Gmail: Confirmed
- Section 9, Auto-task: "Initial Response Required" with priority-based due dates — confirmed
- Section 10, All 3 automations: VIP detection, new customer priority, auto-task — confirmed
- Section 13, Cases OWD: **Private** — confirmed
- Section 13, No deletion: Confirmed for all roles

### AI Suggestions Upgraded
- Section 4, Custom fields (Product, Tier, Origin): Was AI (High) → Now ✅ Confirmed with specific values
- Section 6, Assignment approach: Was AI (Medium) → Now ✅ Confirmed (product-based + VIP override)

### Previously Unknown → Now Answered
- Section 2, Priya Sharma: New team lead — not known from AE handoff
- Section 2, All agent names: Jake Torres, Anika Patel, Sam Okafor, Rachel Kim
- Section 4, Analytics Module: Third product — not known from AE handoff
- Section 4, SLA numbers: Specific hours per tier
- Section 10, New customer 30-day rule: Entirely new requirement
- Section 10, Chatter notifications: Confirmed as notification method
- Section 13, Private OWD: Changed from AI suggestion of Public Read Only

### New Parking Lot Items
- Auto-close stale cases: Bumped from Automation section (no capacity — all 3 flow slots committed)
- Post-resolution follow-up: Bumped from Automation section (same reason)

### Still Open (Needs Discussion)
- Section 1: Time zone, business hours, holidays
- Section 3: Account/contact counts, historical data migration
- Section 4: SLA business hours vs clock hours
- Section 5: Org-wide email address, Web-to-Case commitment
- Section 6: Analytics Module queue assignment
- Section 8: Email templates confirmation, org-wide email address, email signature
- Section 12: Mobile access needs
- Section 13: Field-level security details
- Section 14: Branding (logo, colors)

## Research Notes (Perplexity)

### Industry Context: B2B SaaS (Workflow Automation)

**From v1 research (still valid):**
- B2B SaaS support teams commonly use tiered models (Silver/Gold/Platinum) with differentiated SLAs
- Common case types: Bug reports (highest volume), integration/API issues, billing questions, feature requests, onboarding
- Mid-market SaaS companies (200 employees) typically have 6-10 support agents
- Average first response time targets: Platinum 30-60 min, Gold 2-4 hours, Silver 8-24 hours

**New v2 research findings:**
- **VIP 2+ case threshold validated** — Perplexity confirms 2 is appropriate for premium B2B SaaS; waiting for 3 risks delayed intervention for high-value customers
- **30-day new customer window validated** — Aligns with B2B SaaS onboarding phase where churn risk is highest. Could consider shortening to 14-21 days if data shows faster drop-off.
- **Auto-task due date timing validated** — Critical same-day, High next-day, Normal 3-day is reasonable for mid-market B2B SaaS
- **Private OWD with sharing rules validated** — Common and recommended for small product-segmented teams. Prevents cross-team data confusion (directly addresses Marcus's pain point of "conflicting answers").

### Section-Specific Validation

**Case Management (Section 4):**
- Query: "Salesforce case types and statuses for B2B SaaS workflow automation companies"
- Key findings: Standard case types (Technical, Integration, Billing, Feature Request, General) align with SaaS norms. "Waiting on Customer" status is essential for SLA timer pausing.

**Case Capture (Section 5):**
- Query: "Web-to-Case and Email-to-Case best practices for B2B SaaS companies"
- Key findings: Email-to-Case is primary channel for B2B. Web form should have 7-10 fields max.

**Case Assignment & Routing (Section 6):**
- Query: "Case assignment and queue structure for mid-market SaaS support teams"
- Key findings: Product-based queues with escalation queue is a validated pattern.

**Escalation Rules (Section 4):**
- Query: "Escalation rules and SLA best practices for B2B SaaS tiered support"
- Key findings: Client's SLAs (Platinum 2h, Gold 4h, Silver NBD) are within industry norms.

**Automation (Section 10):**
- Query: "Salesforce Service Cloud VIP detection, new customer prioritization, and auto-task best practices for B2B SaaS 2026"
- Key findings: All 3 automation patterns validated. 2+ case threshold appropriate. 30-day onboarding window standard. Priority-based task due dates aligned with industry.

**Reports & Dashboards (Section 11):**
- Query: "Support dashboard KPIs for B2B SaaS VP of Customer Success"
- Key findings: Top 5 metrics validated — open cases by tier, first response time, escalated count, cases by product, agent caseload.

---

**Document Status:** In Progress (Iteration 2)
**Generated:** 2026-03-02
**Sources:** AE Handoff Transcript — Jordan Park (Feb 25, 2026); Discovery Call Transcript — Lisa Chen & Marcus Webb (Mar 2, 2026)
**Template Used:** service-cloud-enable-worksheet-template.md
**Scope File:** /home/exo/.claude/plugins/cache/grimoire/salesforce-coe/0.4.1/supporting_prompts/service-cloud/tiers/enable.md
