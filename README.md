# Starter Pack Agent Testing Template

A template repository for Salesforce Service Cloud engagements. Clone this repo for each new client engagement, then run `/sp:setup` to personalize it.

## 🚀 Quick Start

### 1. Clone the template

```bash
# Create a new repo from this template (via GitHub UI or CLI)
gh repo create <client>-service-cloud --template <this-repo> --private
git clone <new-repo-url>
cd <client>-service-cloud
```

### 2. Initialize the project

```bash
/sp:setup
```

This asks you 5-6 questions (client name, scope tier, existing materials) and updates all template files. Run it once at the start of every engagement.

### 3. Start the workflow

```bash
# If you have discovery call transcripts:
/salesforce-coe:sp:create-or-update-requirements-worksheet

# If you have a finalized requirements worksheet:
/salesforce-coe:sp:create-user-stories

# If you have user stories ready:
/salesforce-coe:sp:plan US-001
```

---

## Commands

`/sp:setup` is a local command in this repo. All other commands come from the **`salesforce-coe` grimoire plugin**, which is installed during setup.

| Command | Source | Purpose | When to Use |
|---------|--------|---------|-------------|
| **`/sp:setup`** | Local | Initialize project | First thing — sets client name, tier, imports materials, installs plugin |
| **`/salesforce-coe:sp:create-or-update-requirements-worksheet`** | Plugin | Generate requirements worksheet | After discovery calls — processes transcripts, SOWs, client docs |
| **`/salesforce-coe:sp:create-user-stories`** | Plugin | Generate user stories | After worksheet is finalized — creates sequenced implementation stories |
| **`/salesforce-coe:sp:plan <story-id>`** | Plugin | Create implementation plan | Start of each user story — authenticates to org, queries state, generates plan |
| **`/salesforce-coe:sp:implement <story-id>`** | Plugin | Execute implementation | After plan is approved — deploys changes, captures deviations |
| **`/salesforce-coe:sp:qa <story-id>`** | Plugin | Quality assurance | After implementation — tests against acceptance criteria, documents results |
| **`/salesforce-coe:sp:feedback`** | Plugin | Capture learning | Anytime — updates feature guides with gotchas and best practices |

### Typical Engagement Flow

```
/sp:setup → /salesforce-coe:sp:create-or-update-requirements-worksheet → /salesforce-coe:sp:create-user-stories
    ↓
/salesforce-coe:sp:plan US-001 → /salesforce-coe:sp:implement US-001 → /salesforce-coe:sp:qa US-001
    ↓
/salesforce-coe:sp:plan US-002 → /salesforce-coe:sp:implement US-002 → /salesforce-coe:sp:qa US-002
    ↓
  ... repeat for each user story ...
```

### What These Commands Do

- **Auto-authenticate** to your Salesforce org before execution
- **Query actual org state** to ground plans in reality
- **Capture deviations** automatically when implementation differs from guides
- **Update feature guides** with your learnings
- **Commit and push** changes automatically
- **Post to ClickUp** for team visibility

---

## Scope Tiers

Each engagement maps to one of three scope tiers. `/sp:setup` asks which tier applies and sets the active scope reference.

| Tier | Budget | Duration | Scope Reference |
|------|--------|----------|----------------|
| **Enable** | $20K | 6-8 weeks | `tiers/service-cloud/enable.md` |
| **Elevate** | $35K | 10-12 weeks | `tiers/service-cloud/elevate.md` |
| **Transform** | $60K | 16-18 weeks | `tiers/service-cloud/transform.md` |

---

## Repository Structure

```
.claude/
├── commands/
│   └── sp:setup.md                          # /sp:setup — project initialization (installs salesforce-coe plugin)
├── settings.json                            # Permission and tool configuration
└── settings.local.json                      # Local-only settings

tiers/service-cloud/
├── enable.md              # Enable tier scope definition
├── elevate.md             # Elevate tier scope definition
└── transform.md           # Transform tier scope definition

# Feature guides are provided by the salesforce-coe grimoire plugin
# (not stored locally — loaded automatically when plugin is installed)

requirements/
├── call-transcripts/      # Place discovery call transcripts here
└── worksheets/            # Generated and refined requirements worksheets

user-stories.md            # User story definitions (generated or imported via /sp:setup)
user-story-template.md     # Template format for user stories

logs/                      # Auto-generated during implementation
└── <story-id>/
    ├── <timestamp>-plan.md
    ├── <timestamp>-implementation.md
    └── <timestamp>-qa.md
```

---

## How It Works

### Per-Story Workflow

Each user story goes through three phases with automatic learning capture:

```
/salesforce-coe:sp:plan US-004  →  /salesforce-coe:sp:implement US-004  →  /salesforce-coe:sp:qa US-004
```

**`/salesforce-coe:sp:plan`** — Authenticates to the org, queries current state, maps requirements to feature guides, generates an implementation plan with CLI commands and verification checkpoints.

**`/salesforce-coe:sp:implement`** — Loads the approved plan, executes each step (Salesforce CLI deployments, SOQL verification), captures any deviations as learnings.

**`/salesforce-coe:sp:qa`** — Runs test cases from the plan, captures evidence with actual query results, validates acceptance criteria.

### Learning Loop

Every phase includes an automatic learning loop. When something deviates from the feature guides:

1. The deviation is detected (plan disagreement, deployment error, QA failure)
2. The learning is mapped to the relevant feature guide (provided by the salesforce-coe plugin)
3. A proposed update is shown to the user for approval
4. After approval, the guide is updated

This means every engagement makes the guides better for the next one.

---

## Prerequisites

1. Salesforce CLI installed (`sf`)
2. Git repository cloned locally
3. ClickUp ticket ID (format: `86dxxxxxxx`)

Org authentication is handled by the commands — they'll guide you through it if needed.

---

## Guide Philosophy

Guides in this repo are **opinionated playbooks, not reference manuals.** They should:

- **Be high-level** — Focus on the workflow and the gotchas, not every XML attribute or config option
- **Prioritize speed over perfection** — A short guide that gets someone 80% there fast is better than an exhaustive doc nobody reads
- **Lead with hard-won learnings** — The real value is what burned us in practice (FLS gotchas, CLI quirks, SDO traps)
- **Follow the CLI-first principle** — Use SF CLI for everything possible. Only fall back to Setup UI when the Metadata API genuinely doesn't support it

A good guide answers: "What's the workflow? What will bite me? What commands do I copy-paste?" — and stops there.
