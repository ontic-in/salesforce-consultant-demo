# Exowork Onboarding — Experience Guide

How a senior Salesforce consultant experiences their first hands-on session with the Exowork pipeline.

---

## Overview

The consultant walks through the full Exowork lifecycle using a realistic client scenario: Relay Logic, a B2B SaaS company moving from shared inboxes to Salesforce Service Cloud. Starting from a sales handoff transcript, they produce an initial requirements worksheet with gaps, then refine it with a discovery call transcript to see the system's iterative merge capability. From the completed worksheet, they break it into user stories, then plan → implement → QA three stories against a live scratch org.

No slides. No training deck. Just real work with real tooling. By the end, they have a working Salesforce org, complete documentation, and captured learnings — all produced through the system they'll use on actual engagements.

**What gets built:**
- 7 users with role hierarchy and OWD
- 3 custom fields on Case (1 required, with validation rule)
- Record-Triggered Flow with cross-object lookups, conditional routing, task creation, and Chatter notifications

---

## Pre-Session Setup

Before the consultant arrives, ensure:

**Environment:**
- [ ] Fresh scratch org spun up and authenticated (`sf org login`)
- [ ] Repo cloned, Claude Code installed and working
- [ ] Slash commands functional (`/salesforce-coe:sp:plan`, `/salesforce-coe:sp:implement`, `/salesforce-coe:sp:qa`, `/salesforce-coe:sp:feedback`)
- [ ] Consultant has terminal access (their machine or shared screen)

**Materials:**
- [ ] `onboarding/sales-transcript.md` ready in the repo (AE handoff — used first)
- [ ] `onboarding/discovery-transcript.md` ready in the repo (detailed discovery — used second)
- [ ] Feature guides up to date (especially: user-management, field-management, automations-flows)

**Facilitator prep:**
- Read through the transcript so you know what requirements are embedded
- Know the three stories and their expected scope (admin → fields → automation)
- Have the Salesforce org open in a browser to show results visually after each implementation

---

## The Experience, Step by Step

### Task 1: Transcripts → Requirements Worksheet (Two-Pass)

The consultant's first interaction with the system. They produce a requirements worksheet iteratively — first from a sales handoff (partial, with gaps), then refined with a full discovery call. This mirrors real engagement flow: you always get a sales handoff before you do your own discovery.

#### Task 1a: Sales Transcript → Initial Worksheet (v1)

**What they do:**
1. Open the sales handoff transcript (`onboarding/sales-transcript.md`)
2. Run `/salesforce-coe:sp:create-or-update-requirements-worksheet` pointed at the sales transcript
3. Review the generated worksheet — notice the gaps, AI guesses, and `❓ Needs Discussion` items
4. Don't fix anything yet — just observe what the system knows and doesn't know

**What makes this impressive:**
- The system extracts what it can from a casual, relationship-focused call
- Gaps are surfaced honestly — no team names, no specific thresholds, no field requirements
- AI-inferred values are marked with confidence levels so you know what's solid vs guessed
- The worksheet is already structured and usable, even with gaps

**Facilitator notes:**
- Set expectations: "This is from the AE handoff — it's intentionally incomplete. Watch what happens when we add the discovery call."
- Point out specific gaps: no individual agent names, no org structure, no automation thresholds, vague SLA references. These are the things the discovery call will fill in.
- Point out the `❓ Needs Discussion` items and AI confidence markers. This is where the system shows it knows its limits.
- Don't let them fix things manually — the point is to see the second pass fill the gaps automatically.

#### Task 1b: Discovery Transcript → Updated Worksheet (v2)

**What they do:**
1. Open the discovery transcript (`onboarding/discovery-transcript.md`)
2. Run `/salesforce-coe:sp:create-or-update-requirements-worksheet` again — pointed at the discovery transcript, against the existing worksheet
3. Review the updated worksheet — watch gaps fill in, confidence levels upgrade, and `❓ Needs Discussion` items resolve
4. Make any final corrections or clarifications

**What makes this impressive:**
- The system merges new information with the existing worksheet — it doesn't start over
- Previously vague items ("about half a dozen support folks") become specific (6 named users with reporting structure)
- AI guesses from v1 are either confirmed or corrected by discovery call specifics
- Parking lot items and ambiguities carry forward and get refined
- Transcript line references tie every requirement back to its source across both transcripts

**Facilitator notes:**
- This is the "wow" moment. Walk through the before/after: "Remember this was a gap? Look at it now."
- Point out confidence upgrades — items that were `Medium` confidence from the sales call should now be `High` from the discovery call
- If some gaps remain (like SLA business hours vs clock hours), that's realistic — not everything gets answered in one call
- This is also a good time to explain: "On a real engagement, you'd run this after every client touchpoint. The worksheet gets better each time."

---

### Task 2: Requirements Worksheet → User Stories

Now they take the validated worksheet and break it into sequenced, implementation-ready user stories.

**What they do:**
1. Run `/salesforce-coe:sp:create-user-stories` against the requirements worksheet
2. Review the generated stories — acceptance criteria, sequencing, dependencies
3. Approve, reorder, or modify stories interactively
4. Confirm the final story set

**What makes this impressive:**
- Stories come out sequenced correctly (admin foundations first, automation last)
- Each story has clear acceptance criteria tied to specific client requirements
- Dependencies between stories are explicit (e.g., "fields must exist before automation can reference them")
- The consultant is the decision-maker — the system proposes, they approve

**Facilitator notes:**
- The system should produce ~3 stories that map to the three requirement areas. If it produces more (splitting admin into users + OWD, for example), that's fine — the consultant can merge or keep them.
- Watch for how the automation story gets scoped. It should capture: VIP detection, new customer prioritization, task creation, Chatter post. If anything is missing, have the consultant add it.
- This is a good moment to explain the story → plan → implement → QA lifecycle they're about to experience three times.

---

### Task 3: Story 1 — Admin & Team Setup (Full Lifecycle)

The first full cycle. This story covers users, roles, profiles, OWD, and sharing rules — the foundation everything else builds on.

**Scope:**
- 7 users: 4 agents, 2 team leads, 1 VP (Lisa)
- Role hierarchy: VP → Team Leads → Agents (two teams)
- OWD: Cases set to Private
- Sharing rules or role hierarchy grants: leads see their team's cases, Lisa sees all
- No delete permission for anyone

**What they do:**

*Plan:*
1. Run `/salesforce-coe:sp:plan` for the admin story
2. System authenticates to org, queries current state (existing users, roles, profiles)
3. Review the generated plan — CLI commands, metadata changes, verification queries
4. Approve or adjust the plan

*Implement:*
1. Run `/salesforce-coe:sp:implement` for the same story
2. Watch the system execute the plan step by step
3. See real-time verification queries confirming each step worked
4. If something deviates from the plan, the learning loop activates — they see it capture the deviation

*QA:*
1. Run `/salesforce-coe:sp:qa` for the story
2. System runs acceptance criteria checks against the live org
3. Review pass/fail results with SOQL evidence
4. Open the Salesforce org in a browser — see the users, roles, and hierarchy visually

**What makes this impressive:**
- The plan is grounded in actual org state, not generic templates
- Implementation uses real Salesforce CLI commands — not screenshots of UI clicks
- Verification is automated — SOQL queries prove the work is correct
- Full documentation is generated as a side effect of doing the work

**Facilitator notes:**
- This is the longest story but also the most foundational. Don't rush it.
- The consultant may want to adjust the plan (different role names, different profile assignments). Encourage this — it's how the system is designed to work.
- If OWD or sharing rules behave unexpectedly, use `/salesforce-coe:sp:feedback` to capture the learning. This demonstrates the feedback loop naturally.
- After QA, pull up the Salesforce org and show the role hierarchy visually. The "it actually works" moment lands harder when they can see it in the UI.

---

### Task 4: Story 2 — Custom Fields on Case (Full Lifecycle)

Shorter story, but compound impact — the fields they create here become inputs for the automation story.

**Scope:**
- Custom picklist field: `Product__c` (Core Platform, Integrations, Analytics) — **required**
- Custom picklist field: `Customer_Tier__c` (Silver, Gold, Platinum)
- Validation rule: Case cannot be saved without Product__c populated
- Verify Case Origin standard field has correct values (Phone, Email, Web)

**What they do:**

*Plan:*
1. Run `/salesforce-coe:sp:plan` — system sees the users and roles from Story 1 already in the org
2. Plan references field metadata, validation rule XML, and page layout assignments

*Implement:*
1. Run `/salesforce-coe:sp:implement` — fields deployed via metadata API
2. Validation rule deployed and tested
3. Page layout updated to include new fields

*QA:*
1. Run `/salesforce-coe:sp:qa` — verify fields exist, picklist values are correct, validation rule fires
2. Try creating a case without a product — see it fail (validation rule working)
3. Confirm fields appear on the page layout

**What makes this impressive:**
- The system knows the org already has users and roles — plan builds on existing state
- Metadata deployment is precise — no manual UI field creation
- Validation rule is tested automatically, not just deployed and hoped for
- Fields are ready for the automation story — the pipeline compounds

**Facilitator notes:**
- This is where the consultant starts to feel the rhythm: plan → implement → QA is becoming familiar.
- Point out that the system's plan references the actual org state — it doesn't re-propose creating users or roles. It knows what's already done.
- If the field API names come out differently than expected (e.g., `Product_Name__c` vs `Product__c`), that's a learning capture moment.
- The validation rule is a good test of guide quality. If the guide handles it cleanly, great. If not, the consultant captures the gap via `/salesforce-coe:sp:feedback`.

---

### Task 5: Story 3 — Case Triage Automation (Full Lifecycle)

The showpiece. A Record-Triggered Flow that demonstrates why this isn't just a deployment script — it's a system that handles complex, cross-object Salesforce logic.

**Scope:**
- Record-Triggered Flow on Case (After Save — new records)
- **Decision 1 — VIP Detection:**
  - Get Contact from Case → Get Account from Contact
  - Check: `Customer_Tier__c` = Gold or Platinum
  - Get open cases for same Contact (count ≥ 2)
  - If both true: Set Priority = Critical, assign to Senior Support Queue
- **Decision 2 — New Customer:**
  - Check: Account `CreatedDate` < 30 days ago
  - If true and not already Critical: Set Priority = High
- **Action — Follow-up Task:**
  - Create Task: "Initial Response Required"
  - Due date: Critical = today, High = tomorrow, Normal = 3 days
  - Assigned to case owner
- **Action — Chatter Post:**
  - Post triage summary to Case feed
  - Include: tier, open case count, priority set, queue routed to

**What they do:**

*Plan:*
1. Run `/salesforce-coe:sp:plan` — this is the most complex plan in the session
2. System maps flow logic to metadata structure
3. Plan should outline: trigger configuration, Get Records elements, Decision elements, Assignment elements, Create Records elements
4. Consultant reviews for correctness — does the logic match what Lisa described?

*Implement:*
1. Run `/salesforce-coe:sp:implement` — flow metadata deployed
2. This is where things get interesting. Flow XML is complex, cross-object lookups need the right relationship paths, and the queue from Story 1 must be referenced correctly
3. If deployment fails or flow has errors, the system captures what went wrong and adjusts
4. Verification queries confirm flow is active and elements are correctly configured

*QA:*
1. Run `/salesforce-coe:sp:qa` — test scenarios against the live org
2. Test case 1: Gold customer with 2+ open cases → should route to senior queue, priority Critical
3. Test case 2: New account (< 30 days) → should set priority High
4. Test case 3: Silver customer, established account → should stay normal priority
5. Verify tasks are created with correct due dates
6. Verify Chatter posts appear on case feed

**What makes this impressive:**
- The system handles a genuinely complex flow — not a toy example
- Cross-object lookups (Case → Contact → Account), aggregate queries, conditional branching — real Salesforce architecture
- If something doesn't work on first deploy, the error handling and retry cycle demonstrates resilience
- The flow references fields and queues created in previous stories — the whole session compounds

**Facilitator notes:**
- This is the story most likely to hit guide gaps or unexpected behavior. That's by design.
- If the flow fails to deploy or activate, don't panic. Walk through the error together, use `/salesforce-coe:sp:feedback` to capture the learning. The consultant seeing the system handle failure gracefully is more impressive than a perfect run.
- If time is running short, the Chatter post action can be deferred. VIP detection + task creation is the must-have.
- After QA, show the flow in Flow Builder visually. Let the consultant see that a complex, multi-path flow was built and deployed without touching the UI.
- This is also where the consultant usually "gets it" — they see how transcript → requirements → stories → working automation is a real pipeline, not a demo.

---

## What They Walk Away With

By end of session, the consultant has:

**A working Salesforce org containing:**
- 7 configured users with proper role hierarchy and access controls
- 3 custom fields on Case with validation rules
- A production-grade Record-Triggered Flow handling VIP detection, new customer prioritization, auto-task creation, and Chatter notifications

**Complete documentation trail:**
- Requirements worksheet traced to transcript lines
- Sequenced user stories with acceptance criteria
- Plan, implementation, and QA docs for each story (timestamped in `logs/`)
- Any learnings captured in feature guides

**Hands-on experience with:**
- The full `/salesforce-coe:sp:plan` → `/salesforce-coe:sp:implement` → `/salesforce-coe:sp:qa` lifecycle
- The `/salesforce-coe:sp:feedback` learning capture loop
- How the system queries actual org state and builds on previous work
- How errors and deviations are handled (not hidden)

**A clear path to continue:**
- Remaining stories from the worksheet (parking lot items, refinements)
- Understanding of how to start a new engagement from scratch
- Confidence that the system handles real complexity, not just demos

---

## Why This Order

The three stories are sequenced deliberately:

**Story 1 — Admin & Team Setup (first)**
- Foundation that everything else depends on
- Lowest risk — creating users and roles is well-understood territory
- Lets the consultant learn the plan → implement → QA rhythm on something familiar
- Creates the queue that Story 3 needs for routing

**Story 2 — Custom Fields (second)**
- Builds on Story 1 (page layouts, profiles are already configured)
- Demonstrates compound effect — the system knows what's already in the org
- Creates the fields that Story 3 needs for its decision logic
- Short enough to reinforce the lifecycle without fatigue

**Story 3 — Automation (last)**
- Depends on both Story 1 (queues, users) and Story 2 (fields)
- Most impressive technically — cross-object lookups, conditional routing, record creation
- Most likely to surface real-world complexity (guide gaps, deployment issues)
- Ends the session on the highest note — they've seen a complex flow built from a client conversation

The progression is: safe → intermediate → impressive. Each story builds confidence while raising the stakes. By the time they hit the automation story, they trust the system enough to push it on something genuinely hard.
