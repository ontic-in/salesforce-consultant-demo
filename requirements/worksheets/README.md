# Requirements Worksheet System

## Purpose

AI-accelerated requirements gathering for Salesforce Starter Pack discovery sessions. Works across **multiple clouds** (Sales, Service, etc.) and **multiple tiers** (Enable, Elevate, Transform).

## The Problem

- Requirements gathering is manual and time-consuming
- Clients (greenfield Salesforce implementations) don't understand SF terminology
- Consultants spend time explaining concepts before getting answers

## The Solution: Hybrid Approach

```
┌──────────────────┐     ┌──────────────────────┐     ┌─────────────────┐
│ Cloud + Tier     │     │ Agent loads scope,   │     │ STANDARD        │
│ Transcript +     │ --> │ reads context,       │ --> │ worksheet with  │
│ Client docs      │     │ suggests answers     │     │ pre-filled      │
└──────────────────┘     │ (Perplexity grounded)│     │ suggestions     │
                         └──────────────────────┘     └─────────────────┘
                                                             │
                                                             ▼
                                                      Consultant + Client
                                                      review/adjust together
                                                      (screen share)
                                                             │
                                                             ▼
                                                      Implementation Agent
                                                      (existing system)
```

## Key Design Principles

1. **Worksheet structure is FIXED** - Consultants always know what sections to expect
2. **Agent ASSISTS, doesn't create** - Reads transcript, suggests answers in the fixed template
3. **Scope-aware** - Loads cloud + tier scope file to know what's in/out of scope
4. **Suggestions are clearly marked** - "Based on your conversation, we think X... is this correct?"
5. **Client validates** - Nothing goes in without client confirmation
6. **Business-friendly language** - Simple explanations, no Salesforce jargon

## Files

| File | Purpose |
|------|---------|
| `agent.md` | **The AI agent** - cloud/tier agnostic, uses Perplexity for grounding |
| `enable-tier-worksheet-template.md` | Worksheet template (Sales Cloud Enable) |
| `process.md` | How to use the worksheet (for consultants) |

## Scope Documentation

Scope files live in the `tiers/` directory:

```
tiers/
├── README.md
├── sales-cloud/
│   ├── enable.md      ← What's in/out for $15K tier
│   ├── elevate.md     ← What's in/out for $45K tier
│   └── transform.md   ← What's in/out for $75K tier
└── service-cloud/
    └── ...
```

See [tiers/README.md](../tiers/README.md) for scope file structure.

## Quick Start

To generate a pre-filled worksheet for a client:

```
1. Identify: Cloud (sales-cloud, service-cloud) + Tier (enable, elevate, transform)
2. Gather: Fathom transcript + any client docs
3. Invoke: Provide materials to agent (see agent.md)
4. Review: Agent returns pre-filled worksheet with AI suggestions
5. Collaborate: Walk through with client via screen share
6. Finalize: Confirm all suggestions, feed to implementation agent
```

**Example invocation:**
```markdown
## Cloud & Tier
Cloud: sales-cloud
Tier: enable

## Client Context
Acme Corp - B2B software company, 15 person sales team

## Discovery Transcript
[Paste Fathom transcript here]

## Client Documents
[Any org charts, process docs, etc.]
```

---

## Worksheet Creation Process

### Sources of Truth

1. **Scope files** - `tiers/[cloud]/[tier].md` defines what's in/out
2. **questionnaire.csv** - Comprehensive technical questions (123 questions)
3. **Perplexity research** - Validate Salesforce features and best practices

### Process

1. Load the correct scope file for cloud + tier
2. Use `questionnaire.csv` as the base for what info we need
3. Validate/research via Perplexity for accuracy
4. Translate technical questions to business-friendly language
5. Group by conversation flow (not technical category)
6. Route out-of-scope items to Parking Lot with tier upgrade suggestions

### Future Updates

- When `questionnairev2.csv` is completed, update templates to match
- Add worksheet templates for Service Cloud and other clouds
- Add scope files for Elevate and Transform tiers (currently placeholders)

## Related

- **ClickUp Task:** [86d1r6yy5](https://app.clickup.com/t/86d1r6yy5)
- **Tiers documentation:** `tiers/` directory
- **questionnaire.csv:** Technical questions source
- **questionnairev2.csv:** Enable-tier focused questions (in progress)
