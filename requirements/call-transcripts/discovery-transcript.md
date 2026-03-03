# Discovery Call Transcript — Relay Logic

> **Context:** This is the follow-up discovery call after the initial sales handoff from the AE (see `onboarding/sales-transcript.md`). The consultant already knows the basics — company, team size, tier structure, and high-level pain points. This call digs into the specifics needed for implementation.

**Date:** March 2, 2026
**Client:** Relay Logic (B2B SaaS — workflow automation platform)
**Attendees:**
- **Lisa Chen** — VP of Customer Success, Relay Logic
- **Marcus Webb** — Support Team Lead, Relay Logic
- **Consultant** — Salesforce Consultant

---

**Consultant:** Thanks for making the time today, Lisa and Marcus. The goal here is to understand how your support team works right now and what you need from Salesforce. I'll ask a lot of questions — some might seem obvious, but it helps me get the full picture. Sound good?

**Lisa:** Absolutely. We're excited to get this going. We've been running support out of a shared Gmail inbox for about two years now, and it's… held together with duct tape at this point.

**Consultant:** Ha, I hear that a lot. Let's start there — tell me about the team. Who's involved in support today?

**Lisa:** So we have six people total on the support side. Four are frontline agents — they're the ones in the inbox every day handling customer issues. Then we have two team leads who manage those agents. And then there's me — I oversee the whole customer success function, support included.

**Consultant:** Got it. Can you give me the names and how they're organized?

**Marcus:** Sure. I'm one of the two team leads. The other lead is Priya Sharma. Under me I have two agents — Jake Torres and Anika Patel. Under Priya, she has Sam Okafor and Rachel Kim.

**Consultant:** And Lisa, you're above both Marcus and Priya?

**Lisa:** Right. Marcus and Priya both report to me. I don't handle cases day-to-day, but I need to see everything — all the cases, all the metrics. The leads need to see their team's cases plus anything unassigned. But the agents should really only see their own stuff and cases in their team's queue.

**Consultant:** That makes sense. So the agents shouldn't be able to see cases assigned to the other team?

**Lisa:** Correct. We actually split things by product line — Marcus's team handles our core platform issues, and Priya's team handles our integrations product. We don't want agents accidentally working cases that belong to the other team.

**Marcus:** Yeah, that's burned us a couple times with the shared inbox. Someone replies to the wrong thread and the customer gets conflicting answers.

**Consultant:** Okay, that's really clear. What about editing and deleting — should agents be able to delete cases?

**Lisa:** No. Absolutely not. Nobody deletes anything. Leads and agents can update cases, close them, but no deleting. I've seen too many "oops" moments.

**Consultant:** Smart. And for the leads — Marcus and Priya — they'd need to see all cases across both teams, or just their team's?

**Marcus:** Just my team's for me. Priya sees hers. Lisa's the only one who sees everything.

**Consultant:** Perfect. Now let's talk about the cases themselves. When a case comes in today, what information do you track?

**Marcus:** Right now it's pretty informal. We tag emails in Gmail with labels. But what we really need is — first, which product the case is about. Like I said, we have the core platform and the integrations product. Oh, and we just launched a third one — our analytics module. So three products.

**Lisa:** That's a must-have. Every single case needs to have a product tagged on it. We can't have cases floating around with no product — it throws off all our reporting and routing.

**Consultant:** So you'd want it required — no saving a case without selecting the product?

**Lisa:** Exactly.

**Consultant:** What else do you track, or wish you could track?

**Marcus:** Customer tier would be huge. We have three tiers — Silver, Gold, and Platinum. Right now we check the account record manually to figure out what tier they're on, and half the time people don't bother. If it was right there on the case, it'd change how we prioritize.

**Lisa:** And honestly, it's not just nice-to-have. Our SLAs are different by tier. Platinum customers expect a response within two hours. Gold gets four hours. Silver is next business day. If agents can't see the tier at a glance, they can't prioritize correctly.

**Consultant:** Got it. Would the tier be set automatically based on the account, or would agents pick it manually?

**Lisa:** Ideally it'd pull from the account automatically. But even if agents have to pick it, having the field is step one.

**Consultant:** We can probably do both — have it default from the account and still allow override. Let me note that down. What about how the case came in — phone, email, web form?

**Marcus:** Yeah, we definitely need that. Right now everything comes through email, but we're planning to add a web form on our help center. And some customers just call us. We need to track the channel.

**Consultant:** Salesforce has a standard field for that — Case Origin. We'll just make sure it's configured with the right values for you.

**Marcus:** Oh, nice. That's easy then.

**Consultant:** Now this is the part I'm most curious about — Lisa, you mentioned SLAs differ by tier. Tell me more about how you want cases handled, especially for your higher-tier customers.

**Lisa:** Okay, so this is the big one for me. Our Gold and Platinum customers — we call them VIP internally. If one of them opens a case and they've already got open tickets with us, that's a red flag. It means something's going wrong with their experience. I want those flagged immediately — bumped to critical priority and routed to our senior agents.

**Consultant:** When you say "already got open tickets" — how many? Any open case, or a threshold?

**Lisa:** If they have two or more open cases including the new one. One open case is normal. Two or more means there's a pattern.

**Consultant:** And "senior agents" — is that Marcus and Priya, or specific people?

**Marcus:** We have a senior support queue — it's me and Priya, basically, plus Jake who's been here the longest. We handle the escalated stuff.

**Lisa:** Right. Route it to the senior queue, not a specific person. Whoever's available picks it up.

**Consultant:** Makes sense. What about new customers? You mentioned prioritization earlier.

**Lisa:** Yes! This is the other thing. When an account is brand new — say within their first 30 days — and they open a case, I want that treated as high priority automatically. First impressions matter. If a new customer hits a wall in their first month and doesn't get help fast, we lose them.

**Consultant:** So any case from an account less than 30 days old gets bumped to high priority, regardless of tier?

**Lisa:** Exactly. And if they're both new AND VIP with multiple cases, the VIP rule should win — that goes to critical.

**Consultant:** Got it — VIP detection takes precedence over new customer. What happens after a case gets triaged? Any follow-up actions?

**Marcus:** Biggest thing is making sure the agent actually follows up. We've had cases sit for days because someone got busy. If there was a task or a reminder created automatically — like "Hey, you need to respond to this" — that'd be amazing.

**Lisa:** Yes. Auto-create a task for the assigned agent. Something like "Initial Response Required." And make the due date reflect the priority. Critical cases — that task should be due today. High priority — maybe tomorrow. Normal — a few days out.

**Consultant:** And notifications? How does the team find out about these VIP or new customer cases?

**Lisa:** We use Chatter internally — well, we will once we're in Salesforce. I'd love a Chatter post when a case gets flagged as VIP. Something like "VIP Alert: Gold customer with 3 open cases — routed to senior queue." That way the leads can see it in their feed without digging through reports.

**Marcus:** That'd be great. We talked about maybe doing email notifications too, but honestly Chatter might be enough to start. We can always add email later.

**Consultant:** Noted. Let me ask about a couple more things. Anything else on your wishlist?

**Lisa:** Actually, yes — two things. First, we want a customer portal eventually. Somewhere customers can log in, see their cases, maybe submit new ones. Second, our billing system — we use Stripe — it'd be great if we could see subscription info right in Salesforce.

**Consultant:** Both great ideas. For this phase, I'd recommend we park those. The portal is a bigger build, and the Stripe integration needs its own scoping. Let me add them to the parking lot so we don't lose them. For now, let's get your team set up, your case data structured, and the smart routing working. Sound fair?

**Lisa:** Totally fair. Those are phase two items.

**Consultant:** A couple of quick clarifications before we wrap up. The SLA timing you mentioned — two hours for Platinum, four for Gold — is that business hours or clock hours?

**Lisa:** Hmm. Good question. I'd say business hours for now? But honestly, I'm not sure. We haven't formalized it yet. Can we decide that later?

**Consultant:** Absolutely. I'll flag it as a discussion item. And for the Chatter notifications versus email — you said Chatter is probably enough. Should we skip email alerts for now, or do you want both?

**Marcus:** Let's start with Chatter. If people miss things, we'll add email. But I don't want people drowning in notifications on day one.

**Consultant:** Smart approach. Last thing — the senior queue. Is that something that already exists, or do we need to create it?

**Marcus:** We'll need to create it. It's a concept we have — not something that exists in any system today.

**Consultant:** Got it. I have a really clear picture now. Let me summarize what I'm hearing as three main areas: First, getting your team set up with the right access — six users, two teams, leads see their team's cases, Lisa sees everything. Second, structuring your case data — product field that's required, customer tier, and case origin. Third, smart case routing — VIP detection, new customer prioritization, auto-tasks, and Chatter notifications. Does that cover it?

**Lisa:** That's it. That's exactly what we need.

**Marcus:** Yeah, that's spot on. When do we get started?

**Consultant:** We'll turn this into a detailed requirements doc, break it into stories, and start building. You'll see working results fast. Thanks, both of you — this was a great call.

**Lisa:** Thank you! Looking forward to it.

---

## Parking Lot

| Item | Notes | Priority |
|------|-------|----------|
| Customer Portal | Self-service case submission and tracking | Phase 2 |
| Stripe Integration | Surface billing/subscription data in Salesforce | Phase 2 |

## Needs Discussion

| Item | Context |
|------|---------|
| ❓ SLA timing — business hours vs clock hours | Lisa unsure, needs internal discussion before formalizing |
| ❓ Chatter vs email notifications for VIP alerts | Starting with Chatter only; revisit if adoption is low |
| ❓ Customer tier — auto-populate from Account vs manual entry | Prefer auto-populate, but need to confirm Account field exists |
