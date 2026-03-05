# Service Cloud Starter Pack: Enable Tier Requirements Worksheet

**Client:** Relay Logic
**Date:** 2026-03-05
**Cloud:** Service Cloud
**Tier:** Enable ($20,000 / 6-8 weeks)
**Version:** 1 (Initial AI Pre-fill)

---

## AI Analysis Summary

**Client:** Relay Logic
**Cloud:** Service Cloud
**Tier:** Enable ($20,000)
**Industry:** B2B SaaS (Workflow Automation Platform)
**Team Size:** ~200 employees (7 Salesforce users)

### Worksheet Completion Status
- Sections complete (✅ Confirmed): 0 of 15
- Sections partially filled (📝 AI suggestions): 13
- Sections needing discussion (❓): 2
- Sections not started: 0

### Key Findings from Discovery
1. **Shared Gmail inbox is the primary pain point** — Cases are being dropped, customers getting conflicting answers from wrong-team replies (Sales transcript + Discovery transcript)
2. **Tiered SLA model is critical** — Platinum (2hr), Gold (4hr), Silver (next business day) response times drive prioritization (Discovery transcript, Lisa Chen)
3. **VIP detection with smart routing** — Gold/Platinum customers with 2+ open cases must be flagged as Critical and routed to Senior Queue (Discovery transcript, Lisa Chen)
4. **Product-based team split** — Marcus's team handles Core Platform, Priya's team handles Integrations; agents must NOT see cross-team cases (Discovery transcript, Marcus Webb)
5. **New customer prioritization** — Accounts <30 days old auto-bump to High priority to protect first impressions (Discovery transcript, Lisa Chen)

### Recommended Focus Areas
1. **Security & Access (OWD + Sharing)** — Private case visibility with role-based sharing is foundational; must be configured first to enforce team separation
2. **Case Data Structure** — Product field (required), Customer Tier, and Case Origin fields are prerequisites for routing and automation
3. **Smart Routing Automation** — 3 flows (VIP detection, new customer priority, auto-task creation) use the full Enable tier allocation; design carefully

### Industry-Specific Recommendations
Based on industry research for B2B SaaS:
- SLA compliance tracking is critical — target >95% compliance rate; B2B SaaS customers expect sub-1-hour acknowledgment for critical issues
- First Contact Resolution (FCR) is a key differentiator — track it from day one
- Tiered SLA model aligns with B2B SaaS best practices where premium subscribers receive priority assistance

### Items for Elevate/Transform Discussion
| Feature | Context from Discovery | Why Out of Scope |
|---------|----------------------|------------------|
| Customer Portal | Lisa: "We want a customer portal eventually. Somewhere customers can log in, see their cases" | Transform tier feature (Customer Community/Portal) |
| Stripe Integration | Lisa: "Our billing system — we use Stripe — it'd be great if we could see subscription info" | Custom integration, not included in any standard tier |

### Assumptions Made
| Assumption | Confidence | Verify With Client |
|------------|------------|-------------------|
| Business hours are US business hours (9-5 M-F) | Medium | Confirm time zone and exact hours |
| Products are: Core Platform, Integrations, Analytics Module | High | Confirm — 3 products mentioned in discovery |
| No historical cases to migrate (Gmail inbox) | Medium | Ask if they want to import any email threads as cases |
| Email system is Gmail (shared inbox mentioned) | High | Confirm agent email client preference |
| Calendar fiscal year | Low | Not discussed — confirm |
| SLA timing is business hours | Medium | Lisa was unsure — flagged as needs discussion |

### Questions to Clarify in Next Session
1. **SLA timing — business hours vs clock hours?** — Lisa was unsure; this affects escalation rule configuration
2. **Time zone and business hours?** — Needed for escalation rule timing and business hours calendar
3. **Customer tier auto-populate from Account?** — Lisa prefers auto-populate; need to confirm Account field exists or will be created
4. **Data migration scope?** — Are there existing accounts/contacts to import, or starting fresh?
5. **Holiday schedule?** — Which holidays to observe for SLA/escalation pausing?

---

## How to Use This Worksheet

This worksheet captures everything we need to set up your Service Cloud system. We'll go through it together section by section.

- **✅ Confirmed** - You've confirmed this is correct
- **📝 AI (High)** - Directly stated in discovery transcript
- **📝 AI (Medium)** - Inferred from context across multiple data points
- **📝 AI (Low)** - Best practice suggestion from industry research
- **📝 AI (Perplexity)** - Validated via industry research
- **❓ Needs Discussion** - We need to talk through this together
- **N/A** - Not applicable to your business

---

## Section 1: About Your Business

*Let's start with the basics about how your company operates.*

### Time Zones & Business Hours

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What time zone is your main office in? | ❓ Needs Discussion | Not mentioned in discovery |
| Do you have support teams in multiple time zones? | 📝 AI (Medium): No | Single team described; no mention of distributed support |
| What are your support team's business hours? | ❓ Needs Discussion | Lisa was unsure about business hours vs clock hours for SLAs |
| Do you observe holidays? | ❓ Needs Discussion | Not discussed; affects escalation rule timing |
| If yes, which holidays? | ❓ Needs Discussion | |

---

## Section 2: Your Support Team

*Tell us about the people who will use the system.*

### Team Structure

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How many people will use the support system? | 📝 AI (High): 7 users | Lisa (VP) + Marcus & Priya (leads) + 4 agents. Within 10-user Enable tier limit. |

### User List

| Name | Email | Role | Manager | Notes |
|------|-------|------|---------|-------|
| Lisa Chen | ❓ Needs Discussion | Manager (VP Customer Success) | — | 📝 AI (High): Oversees all of customer success; needs full case visibility |
| Marcus Webb | ❓ Needs Discussion | Team Lead | Lisa Chen | 📝 AI (High): Leads Core Platform support team |
| Priya Sharma | ❓ Needs Discussion | Team Lead | Lisa Chen | 📝 AI (High): Leads Integrations support team |
| Jake Torres | ❓ Needs Discussion | Agent | Marcus Webb | 📝 AI (High): Core Platform team; also in Senior Queue (longest tenure) |
| Anika Patel | ❓ Needs Discussion | Agent | Marcus Webb | 📝 AI (High): Core Platform team |
| Sam Okafor | ❓ Needs Discussion | Agent | Priya Sharma | 📝 AI (High): Integrations team |
| Rachel Kim | ❓ Needs Discussion | Agent | Priya Sharma | 📝 AI (High): Integrations team |

*7 of 10 maximum users for Enable tier.*

### Support Team Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the reporting relationships? | 📝 AI (High): Multi-level (Lisa → Team Leads → Agents) | 3-level hierarchy: VP → 2 Team Leads → 4 Agents |
| Do managers need to see their team's cases automatically? | 📝 AI (High): Yes — with restrictions | Lisa sees ALL cases. Marcus sees his team only. Priya sees her team only. Agents see only their own + team queue. |
| Do any users need special permissions beyond standard? | 📝 AI (High): No deletions for anyone | Lisa: "Nobody deletes anything." Leads and agents can update/close but not delete. |

---

## Section 3: Your Existing Customer Data

*Let's plan how to bring your current data into the new system.*

### Data Sources

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Where is your customer data currently stored? | 📝 AI (High): Email (shared Gmail inbox) | Lisa: "We've been running support out of a shared Gmail inbox for about two years" |
| Approximately how many customer accounts? | ❓ Needs Discussion | Not mentioned; B2B SaaS with ~200 employees suggests mid-market customer base |
| Approximately how many contacts? | ❓ Needs Discussion | Not mentioned |
| Do you have historical cases to bring over? | 📝 AI (Medium): Unlikely — email threads | Gmail threads don't map cleanly to cases; recommend starting fresh |

### Data Quality

| Question | Your Answer | Notes |
|----------|-------------|-------|
| How clean is your current data? | 📝 AI (Medium): Some cleanup needed | Email-based system likely has inconsistent data; no structured records |
| What cleanup is needed? | ❓ Needs Discussion | Need to understand what customer/account data exists outside Gmail |

### Duplicate Prevention

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What duplicate prevention do you need? | 📝 AI (Low): Block duplicate Contacts by email, Alert on duplicate Accounts by name | Standard B2B SaaS best practice (Perplexity) |

---

## Section 4: Case Management & Tracking

*How you track and manage support requests.*

### Case Types

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What are the main types of support requests? | 📝 AI (Medium): 1. Technical Issue 2. Product Question 3. Feature Request 4. Bug Report | Not explicitly listed in discovery; inferred from B2B SaaS workflow automation context. 📝 AI (Perplexity): B2B SaaS typically categorizes as Technical, Product, Billing, Feature Request, Bug |

### Case Statuses

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need additional statuses beyond standard? | 📝 AI (Perplexity): Yes — add "Waiting on Customer" | Standard: New, In Progress, Escalated, Closed. Industry best practice adds "Waiting on Customer" to pause SLA timers. Marcus mentioned cases sitting because agents get busy — status tracking helps. |

### Case Priorities

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you use standard priorities? | 📝 AI (High): Yes — Low, Medium, High, Critical | Lisa described Critical for VIP cases, High for new customers. Standard set aligns with their needs. |

### Escalation Rules

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should Critical priority cases escalate immediately? | 📝 AI (High): Immediately via VIP detection flow | Lisa: VIP cases go straight to Critical and Senior Queue |
| Should High priority cases escalate? | 📝 AI (Perplexity): After 2 hours with no response | Industry standard for B2B SaaS: escalate High within 2-4 hours if unworked |
| Should Medium priority cases escalate? | 📝 AI (Low): After 8 business hours | Perplexity: Mid-priority B2B SaaS cases typically escalate within 1 business day |
| Should Low priority cases escalate? | 📝 AI (Low): After 24 business hours | Perplexity: Low-priority cases escalate if untouched for >1 business day |
| How long should a case stay in "New" before escalating? | ❓ Needs Discussion | Depends on SLA timing decision (business hours vs clock hours) |
| Who should receive escalation notifications? | 📝 AI (High): Case owner's direct manager (Marcus or Priya) + Lisa for Critical | Follows role hierarchy |

### Custom Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What custom fields do agents need? | 📝 AI (High): 1. **Product** (Picklist: Core Platform, Integrations, Analytics Module) — REQUIRED 2. **Customer Tier** (Picklist: Silver, Gold, Platinum) 3. **Case Origin** (Standard field — Email, Phone, Web) | Lisa: "Every single case needs to have a product tagged on it." Marcus: "Customer tier would be huge." Case Origin is a standard Salesforce field — just needs configured values. |

### Required Case Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Which fields should be required? | 📝 AI (High): Product, Contact, Description | Lisa was "emphatic" about Product being required. Contact and Description are standard best practices. |

---

## Section 5: Case Capture

*How customers submit support requests.*

### Web-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want a web form for case submission? | 📝 AI (High): Yes — planned | Marcus: "We're planning to add a web form on our help center" |
| What fields on the web form? | 📝 AI (Perplexity): Name, Email, Company, Product (dropdown), Subject, Description | Keep lean — 5-7 fields max for good UX. B2B SaaS best practice: include product selector to enable auto-routing. |
| Include reCAPTCHA? | 📝 AI (Low): Yes | Recommended for public-facing forms to prevent spam |

### Email-to-Case

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you want email-based case creation? | 📝 AI (High): Yes — primary channel | Currently all support runs through shared Gmail inbox |
| What support email address(es)? | 📝 AI (Medium): support@relaylogic.com (or similar) | ❓ Needs Discussion: Need actual email address. Transitioning from shared Gmail. |

### Auto-Response

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Auto-response email content? | 📝 AI (Perplexity): "Thank you for contacting Relay Logic Support. Your case number is {Case.CaseNumber} has been received. We'll respond within [SLA window based on your plan]. In the meantime, visit our help center at [URL] for common solutions." | Best practice: 3-5 sentences, include case number, set response time expectation, offer self-service link |

### Email Threading

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should email replies stay threaded on the case? | 📝 AI (Low): Yes | Recommended standard configuration |

### Case Origin Tracking

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What sources can cases come from? | 📝 AI (High): Email, Phone, Web | Marcus: "Everything comes through email, but we're planning to add a web form... And some customers just call us" |

---

## Section 6: Case Assignment & Routing

*How cases get to the right agent.*

### Assignment Approach

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Automatic assignment or manual queue claiming? | 📝 AI (High): Combination | VIP/Critical cases auto-route to Senior Queue. Product-based cases route to product team queues. Agents claim from their team queue. |

### Assignment Criteria

| Criteria | Assigned To | Notes |
|----------|-------------|-------|
| 📝 AI (High): Product = Core Platform | Core Platform Queue | Marcus's team handles platform issues |
| 📝 AI (High): Product = Integrations | Integrations Queue | Priya's team handles integrations |
| 📝 AI (Medium): Product = Analytics Module | ❓ Needs Discussion | New product — which team handles it? |
| 📝 AI (High): VIP Detection triggered (Gold/Platinum + 2+ open cases) | Senior Support Queue | Override: Critical priority, Senior Queue regardless of product |
| 📝 AI (High): New Customer (<30 days) | ❓ Needs Discussion — same queue or separate? | Override: High priority, but routing TBD |

### Queues

| Queue Name | Members | Notes |
|------------|---------|-------|
| 📝 AI (High): Core Platform Queue | Marcus Webb, Jake Torres, Anika Patel | Product-based queue for core platform cases |
| 📝 AI (High): Integrations Queue | Priya Sharma, Sam Okafor, Rachel Kim | Product-based queue for integrations cases |
| 📝 AI (High): Senior Support Queue | Marcus Webb, Priya Sharma, Jake Torres | Escalated/VIP cases — Lisa: "Route it to the senior queue, not a specific person" |

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Should agents be notified when cases are added to their queue? | 📝 AI (Perplexity): Yes | Industry best practice — without notification, agents must manually check queue |

### Default Case Owner

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who gets cases that don't match any rules? | 📝 AI (Medium): Unassigned Cases queue or Lisa Chen | ❓ Needs Discussion: Need fallback owner for unmatched cases |

---

## Section 7: Contact & Account Management

*Customer information tracking.*

### Custom Account Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What custom Account fields do you need? | 📝 AI (High): 1. **Customer Tier** (Picklist: Silver, Gold, Platinum) — source for case tier auto-populate 2. **Account Created Date** (Standard field — used for new customer detection <30 days) | Customer Tier on Account is the source of truth. Lisa: "Ideally it'd pull from the account automatically." |

### Custom Contact Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What custom Contact fields do you need? | 📝 AI (Low): Standard fields sufficient (Name, Email, Phone, Title) | No specific contact field requirements mentioned in discovery |

### Account Hierarchy

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need parent-child account relationships? | 📝 AI (Medium): Unlikely | Not mentioned; B2B SaaS selling to mid-market ops teams doesn't typically require hierarchy |

### Contacts to Multiple Accounts

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Can one contact work with multiple accounts? | 📝 AI (Low): No | Not mentioned; standard single-account relationship sufficient |

### Required Fields

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Required Account fields? | 📝 AI (Medium): Customer Tier | Critical for SLA and routing logic |
| Required Contact fields? | 📝 AI (Low): Email | Standard best practice for case communication |

---

## Section 8: Email Integration

*How agents communicate with customers via email.*

### Email System

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What email system do agents use? | 📝 AI (High): Gmail | Currently using shared Gmail inbox; Gmail integration included in Service Cloud |

### Email Templates

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What templates should be available? | 📝 AI (Perplexity): 1. Case Auto-Response (new case acknowledgment) 2. Case Resolved (resolution notification) 3. Request More Information (ask customer for details) 4. Escalation Notification (internal — VIP alert) 5. Initial Response (first agent reply) | B2B SaaS standard templates. Up to 10 allowed; start with 5 essential ones. |

### Organization-Wide Email Address

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What sender email address? | ❓ Needs Discussion | Need to determine the support@ address. Currently using shared Gmail — may reuse or create new. |

### Email Signature

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Standard email signature? | 📝 AI (Low): Yes | Recommended: Company name, support hours, help center link |
| What should it include? | ❓ Needs Discussion | |

---

## Section 9: Activity Management

*Tracking tasks, events, and calls.*

### Task Types

| Question | Your Answer | Notes |
|----------|-------------|-------|
| What task types do agents create? | 📝 AI (High): 1. Initial Response Required 2. Follow-Up Required 3. Escalation Follow-Up | Lisa: "Auto-create a task for the assigned agent. Something like 'Initial Response Required.'" Marcus: "If there was a task or a reminder created automatically... that'd be amazing." |

### Activity Reminders

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Automatic reminders before tasks are due? | 📝 AI (Medium): Yes | Aligns with Lisa's emphasis on timely follow-up and SLA compliance |

---

## Section 10: Automation

*Business rules that happen automatically. Enable tier allows up to 3 record-triggered flows.*

### Automated Actions

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do you need automated actions beyond assignment/escalation? | 📝 AI (High): Yes — 3 automations (at Enable tier limit) | All 3 flow slots used |

**Flow 1: VIP Case Detection**

| Detail | Value | Notes |
|--------|-------|-------|
| What triggers it? | 📝 AI (High): New case created where Account Customer Tier = Gold or Platinum AND Account has 2+ open cases (including the new one) | Lisa: "If they have two or more open cases including the new one" |
| What happens? | 📝 AI (High): 1. Set Priority = Critical 2. Reassign to Senior Support Queue 3. Post Chatter notification: "VIP Alert: [Tier] customer [Account Name] with [X] open cases — routed to Senior Queue" | Lisa: "Bumped to critical priority and routed to our senior agents" + Chatter post request |

**Flow 2: New Customer Priority Boost**

| Detail | Value | Notes |
|--------|-------|-------|
| What triggers it? | 📝 AI (High): New case created where Account Created Date is within last 30 days | Lisa: "When an account is brand new — say within their first 30 days" |
| What happens? | 📝 AI (High): Set Priority = High (unless already Critical from VIP detection — VIP takes precedence) | Lisa: "If they're both new AND VIP with multiple cases, the VIP rule should win" |

**Flow 3: Auto-Create Follow-Up Task**

| Detail | Value | Notes |
|--------|-------|-------|
| What triggers it? | 📝 AI (High): New case created (after assignment) | Lisa: "Auto-create a task for the assigned agent" |
| What happens? | 📝 AI (High): Create Task "Initial Response Required" assigned to case owner. Due date based on priority: Critical = today, High = tomorrow, Medium = 3 business days, Low = 5 business days | Lisa: "Make the due date reflect the priority. Critical cases — that task should be due today. High priority — maybe tomorrow. Normal — a few days out." |

⚠️ **Note:** All 3 flow slots for Enable tier are used. Any additional automation would require an Elevate tier upgrade.

---

## Section 11: Reports & Dashboards

*Tracking key metrics and performance. Enable tier includes 1 custom dashboard with 5 custom reports.*

### Dashboard Metrics

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Top 5 metrics to track? | 📝 AI (Perplexity): 1. **Open Cases by Priority** — Real-time view of Critical/High/Medium/Low backlog 2. **Cases by Product** — Volume split across Core Platform, Integrations, Analytics Module 3. **Average First Response Time by Tier** — SLA compliance tracking (Platinum <2hr, Gold <4hr, Silver <NBD) 4. **VIP Alert Cases (This Week)** — Count of cases that triggered VIP detection 5. **Cases by Agent** — Workload distribution across team | Industry best practice for B2B SaaS: focus on SLA compliance, volume by segment, and agent productivity. Lisa needs full visibility as VP. |

*Standard reports (case volume, aging, resolution times, queue status, agent productivity) are included out-of-the-box.*

---

## Section 12: Mobile Access

*Support agents working away from their desk.*

### Mobile Needs

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Do agents need mobile case access? | 📝 AI (Medium): Yes — basic access | Not explicitly discussed, but B2B SaaS teams typically need mobile for off-hours incident response. Standard mobile app is out-of-the-box. |

---

## Section 13: Security & Access

*Who can see and do what. This section is critical for Relay Logic's team separation requirement.*

### Organization-Wide Defaults (Record Access)

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Case OWD | 📝 AI (High): **Private** | Lisa: Agents should "only see their own stuff and cases in their team's queue." Marcus: "We don't want agents accidentally working cases that belong to the other team." |
| Account OWD | 📝 AI (Medium): Public Read Only | All agents need to see account info (customer tier, etc.) for case context, but ownership stays with assigned rep |
| Contact OWD | 📝 AI (Medium): Public Read Only | Same reasoning as Accounts — agents need contact info for cases |

### Sharing Rules

*Since Case OWD is Private, sharing rules grant access:*

| Sharing Rule | What It Does | Notes |
|--------------|--------------|-------|
| 📝 AI (High): Role-based — Team Leads see their team's cases | Marcus sees cases owned by Jake & Anika; Priya sees Sam & Rachel's cases | Marcus: "Just my team's for me. Priya sees hers." |
| 📝 AI (High): Role-based — Lisa (VP) sees ALL cases | VP role at top of hierarchy grants full visibility | Lisa: "I need to see everything — all the cases, all the metrics" |
| 📝 AI (High): Queue-based sharing | Queue members can see/claim cases in their queue | Enables agents to work from their team queue |

### Field-Level Security

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Sensitive fields to restrict? | 📝 AI (Medium): No specific restrictions identified | Lisa's main concern was delete prevention, not field visibility. No sensitive fields mentioned. |

### Delete Prevention

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Who can delete cases? | 📝 AI (High): Nobody — no case deletion | Lisa: "No. Absolutely not. Nobody deletes anything." Configure via Profile permissions. |

---

## Section 14: Branding

*Make Salesforce look like your company.*

### Company Branding

| Question | Your Answer | Notes |
|----------|-------------|-------|
| Branding to apply? | ❓ Needs Discussion | Not discussed in discovery |
| Logo file ready? | ❓ Needs Discussion | |
| Brand colors? | ❓ Needs Discussion | |

---

## Parking Lot

*Items that came up but are out of scope for Enable tier.*

| Item | Notes | Source | Suggested Tier |
|------|-------|--------|----------------|
| Customer Portal | Self-service case submission and tracking. Lisa: "Somewhere customers can log in, see their cases, maybe submit new ones" | Discovery transcript — Lisa Chen | Transform ($60K) |
| Stripe Integration | Surface billing/subscription data in Salesforce. Lisa: "We use Stripe — it'd be great if we could see subscription info" | Discovery transcript — Lisa Chen | Custom Integration (separate scoping) |
| Email Notifications for VIP | Marcus suggested starting with Chatter only; revisit email alerts if Chatter adoption is low | Discovery transcript — Marcus Webb | Phase 2 (same tier) |
| Advanced SLA Tracking | Formal entitlements with milestones and SLA violation workflows | Not requested, but may emerge as SLA needs mature | Elevate ($35K) |

---

## Version History

| Version | Date | Inputs | Key Changes |
|---------|------|--------|-------------|
| v1 | 2026-03-05 | Sales handoff transcript (2026-02-25), Discovery call transcript (2026-03-02) | Initial AI pre-fill from two transcripts |

---

## Research Notes (Perplexity)

### Industry Context: B2B SaaS (Workflow Automation)

**Typical Support Characteristics:**
- B2B SaaS support teams typically serve tiered customer segments with differentiated SLAs
- First Response Time (FRT) is the most critical metric — sub-1-hour for critical issues is industry standard
- Customer Retention Rate and Churn Rate are closely tied to support quality
- CSAT benchmark for B2B SaaS is >85%
- Tiered support models (Silver/Gold/Platinum) are common and align with Relay Logic's structure

**Key Metrics That Matter:**
- SLA Compliance Rate (target >95%)
- First Response Time by tier
- Average Resolution Time
- First Contact Resolution Rate
- Case Volume by Product/Channel
- Customer Satisfaction Score (CSAT)

### Section-Specific Validation

**Case Management (Section 4):**
- Query: "Salesforce case management stages and SLA best practices for B2B SaaS"
- Key findings applied: Added "Waiting on Customer" status to pause SLA timers; validated Critical/High/Medium/Low priority alignment; escalation thresholds based on B2B SaaS norms

**Case Capture (Section 5):**
- Query: "Web-to-Case form fields best practices B2B SaaS"
- Key findings applied: Recommended lean form (5-7 fields); auto-response template with case number, expected response time, and self-service link

**Case Assignment & Routing (Section 6):**
- Query: "Case assignment routing best practices B2B SaaS"
- Key findings applied: Product-based routing + tier-based escalation is standard; queue structure should match team specialization; recommended queue notification

**Reports & Dashboards (Section 11):**
- Query: "Service Cloud dashboard KPIs for B2B SaaS support teams"
- Key findings applied: Prioritized SLA compliance, volume by product, first response time by tier, VIP alerts, and agent workload distribution

---

**Document Status:** AI Pre-filled (Ready for Consultant Review)
**Generated:** 2026-03-05
**Sources:** Sales handoff transcript (2026-02-25), Discovery call transcript (2026-03-02)
**Template Used:** service-cloud-enable-worksheet-template.md
**Scope File:** service-cloud/tiers/enable.md
