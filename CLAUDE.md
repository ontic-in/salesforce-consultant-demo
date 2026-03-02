# Claude Instructions for Service Cloud Starter Pack Optimization

## Template Repository

This is a **template repository**. It is cloned once per client engagement and then personalized using `/sp:setup`. Until `/sp:setup` is run, all files contain generic placeholders (e.g., `[CLIENT_INDUSTRY]`). If a consultant starts working without running setup first, nudge them to run `/sp:setup` before proceeding.

## 🎯 Salesforce Consultant Interface

### Primary Commands

`/sp:setup` is a local command. All other commands come from the **`salesforce-coe` grimoire plugin** (installed during setup).

| Command | Source | Purpose | When to Use |
|---------|--------|---------|-------------|
| **`/sp:setup`** | Local | Initialize project | First thing to run on a new engagement |
| **`/salesforce-coe:sp:plan US-XXX`** | Plugin | Generate implementation plan | Start of any user story |
| **`/salesforce-coe:sp:implement US-XXX`** | Plugin | Execute the plan | After plan is approved |
| **`/salesforce-coe:sp:qa US-XXX`** | Plugin | Validate implementation | After implementation completes |
| **`/salesforce-coe:sp:feedback`** | Plugin | Capture learnings | Anytime you discover something new |

### Key Features

**Context-Aware Automation:**
- Auto-authenticates to Salesforce org
- Queries actual org state before planning
- Pre-fills known information (reduces questions)
- Captures deviations automatically
- Updates feature guides with learnings

**Intelligent Planning:**
- Maps requirements to feature guides
- Generates CLI commands grounded in org state
- Identifies known gotchas from past learnings
- Creates timestamped plan documents

**Safe Implementation:**
- Follows approved plan step-by-step
- Runs verification queries after each step
- Captures deviations in real-time
- Commits changes with proper attribution

**Quality Assurance:**
- Tests against acceptance criteria
- Runs SOQL verification queries
- Documents evidence of success/failure
- Suggests next user story

**Learning Capture:**
- Detects context (current story, feature)
- Asks only necessary questions (3-5)
- Shows preview before updating guides
- Commits with proper source attribution

### Example Session

```bash
# Initialize project (run once)
User: /sp:setup
Claude: [Asks client name, project name, tier, materials — installs salesforce-coe plugin]

# Consultant starts US-001
User: /salesforce-coe:sp:plan US-001
Claude: [Authenticates to org, retrieves users/roles, generates plan]

# After reviewing plan
User: /salesforce-coe:sp:implement US-001
Claude: [Executes steps, captures deviations, commits changes]

# After implementation
User: /salesforce-coe:sp:qa US-001
Claude: [Runs tests, verifies acceptance criteria, documents results]

# Optional: Capture specific learning
User: /salesforce-coe:sp:feedback
Claude: [Context-aware questions, updates guide, commits]
```

---

## Project Overview

This is a template repository for Salesforce Service Cloud engagements. Consultants clone it for each new client, run `/sp:setup` to personalize it (client name, scope tier, existing materials), then follow the structured user story workflow. The project uses a feature-driven approach with a 3-phase workflow per user story.

## Repository Structure

### Feature Guides (via Plugin)
Feature guides are provided by the `salesforce-coe` grimoire plugin as supporting prompts. They are organized hierarchically:
- Top-level features (e.g., email-integration, security)
- Sub-features under parent features (e.g., user-management/profile-management)
- Each feature/sub-feature contains `guide.md` with implementation patterns and learnings
- These are loaded automatically when the plugin is installed — no local `features/` directory needed

### Logs Directory
The `logs/` directory contains timestamped phase documentation for each story:
- Each user story has its own directory named by story ID
- Three phase files per story: plan, implementation, and qa
- All phase files are timestamped using ISO 8601 format

### Automation Directory (`.claude/`)
The `.claude/` directory contains:
- `commands/sp:setup.md` — `/sp:setup` slash command for project initialization (installs the `salesforce-coe` plugin)

All other commands, skills, and resources are provided by the **`salesforce-coe` grimoire plugin** which is installed during `/sp:setup`. The plugin provides:
- Slash commands: `plan`, `implement`, `qa`, `feedback`, `create-user-stories`, `create-or-update-requirements-worksheet`
- Skills: `learning-loop` (automatic learning capture on deviations)
- Resources: plan template, implementation template, QA template, Salesforce authentication guide

## Workflow Instructions

### Automated Workflow Commands

The repository provides one local command (`/sp:setup`) and the rest come from the `salesforce-coe` grimoire plugin.

#### `/sp:setup` — Project Initialization (Local)
**What it does:**
- Asks for client name, project name, and scope tier
- Asks about existing materials (transcripts, worksheets, user stories)
- Updates all template files (README, CLAUDE.md, workflow YAML, user stories)
- Installs (or enables) the `salesforce-coe` grimoire plugin
- Personalizes the generic starter pack into a project-specific repository

**Output:**
- Updates: `README.md`, `CLAUDE.md`, `.exo/workflows/primary_workflow.yaml`, `user-stories.md`, `user-story-template.md`
- Auto-commits with message: `[setup] Initialize project: [Client Name] - [Tier] tier`

#### `/salesforce-coe:sp:plan <story-id>` — Planning Phase (Plugin)
**What it does:**
- Authenticates to Salesforce org (or verifies existing connection)
- Queries actual org state (users, roles, profiles, fields, etc.)
- Reads user story from `user-stories.md`
- Maps requirements to relevant feature guide files (provided by the salesforce-coe plugin)
- Generates implementation plan with CLI patterns from guides
- **Plans are grounded in actual org data, not assumptions**

**Output:**
- Creates: `logs/<story-id>/<timestamp>-plan.md`
- Auto-commits with message: `[<ticket-id>] Create plan for <story-id>`

#### `/salesforce-coe:sp:implement <story-id>` — Implementation Phase (Plugin)
**What it does:**
- Loads the most recent plan file for the story
- Executes steps with Salesforce CLI deployments and verification queries
- Captures deviations in real-time via the learning loop
- Commits metadata and implementation summary

**Output:**
- Creates: `logs/<story-id>/<timestamp>-implementation.md`
- Auto-commits all artifacts (metadata + summary + guide updates)

#### `/salesforce-coe:sp:qa <story-id>` — QA Phase (Plugin)
**What it does:**
- Loads implementation summary and acceptance criteria
- Generates test checklist and runs SOQL verification queries
- Documents pass/fail results with evidence
- Marks story as verified and suggests next story

**Output:**
- Creates: `logs/<story-id>/<timestamp>-qa.md`
- Auto-commits QA report and any guide updates

#### `/salesforce-coe:sp:feedback` — Learning Capture (Plugin)
**What it does:**
- Auto-detects context (current user story, feature area, recent files)
- Asks only 3-5 questions (skips redundant questions)
- Maps feedback to the correct feature guide (provided by the salesforce-coe plugin)
- Shows preview before updating guides
- Supports multiple feedback types: gotcha, best practice, missing docs, CLI issue

**Output:**
- Updates appropriate guide sections (Troubleshooting, Best Practices, Learnings)
- Auto-commits guide updates with proper attribution
- Offers to capture more feedback in same session

### Learning Loop (Automatic)

The `learning-loop` skill automatically captures knowledge when implementations deviate from documented patterns. It activates during any phase when:

- User disagrees with a proposed plan approach
- Deployment or configuration behaves differently than documented
- New gotchas or workarounds are discovered during QA

**Learning capture workflow:**
1. **Detect** — Compare expected vs actual behavior
2. **Map** — Identify which feature guide (from the salesforce-coe plugin) should capture the learning
3. **Propose** — Show the user the proposed guide update (formatted as: `**[Title]** — [Explanation]. *(Source: <story-id>)*`)
4. **Approve** — Wait for explicit user approval before updating any guide
5. **Update** — Append learning to the appropriate section (Troubleshooting, Best Practices, or Learnings Captured)

### Manual Workflow (Without Commands)

The commands can also be run manually by following the same 3-phase pattern:

#### 1. Plan Phase
- Create `logs/<story-id>/<timestamp>-plan.md`
- Document implementation strategy, approach, and considerations
- Present plan to user for approval
- Capture any disagreements as learnings (see below)

#### 2. Implementation Phase
- Create `logs/<story-id>/<timestamp>-implementation.md`
- Document all changes, code modifications, and configurations
- Link to relevant feature guides

#### 3. QA Phase
- Create `logs/<story-id>/<timestamp>-qa.md`
- Document testing approach, test cases, and results
- Capture any issues found and resolutions

### Capturing Learnings

When new learnings emerge (including plan disagreements):

1. **Identify Feature Mapping**
   - Determine which feature or sub-feature the learning relates to
   - Map to the appropriate directory structure

2. **Propose Update**
   - Show the user which file will be updated (guide.md)
   - Present the proposed learning/change
   - Explain the mapping rationale

3. **Wait for Approval**
   - DO NOT update feature documentation without explicit user approval
   - User may suggest alternative mapping or wording

4. **Update Documentation**
   - Only after approval, update the relevant guide.md
   - Maintain consistency with existing documentation style

### Plan Disagreements

When a user disagrees with a proposed plan:
1. Capture the disagreement and the reason
2. Identify which feature area it relates to
3. Propose adding it as a learning in the relevant feature documentation
4. Get user approval before updating

## Feature Hierarchy Reference

Based on the provided diagram, the feature structure is:

- **Email Integration** (top-level)
- **User Management** (top-level)
  - Profile Management
  - Org Wide Defaults
  - Role Hierarchy
  - Sharing Rules
  - Permission Management
- **Security** (top-level)
- **Object Management** (top-level)
  - List Views
  - Field Management
  - Record Types
  - Page Layouts
- **Reports & Dashboards** (top-level)
- **Assignment and Escalation Rules** (top-level)
- **Automations (Flows)** (top-level)
- **Web to Case** (top-level)
- **Email to Case** (top-level)

## File Naming Conventions

- Timestamps: Use ISO 8601 format `YYYY-MM-DDTHH-MM-SS` (e.g., `2024-02-10T15-30-00`)
- Feature directories: Use kebab-case (e.g., `assignment-and-escalation-rules`)
- Phase files: `<timestamp>-<phase>.md` (e.g., `2024-02-10T15-30-00-plan.md`)

## Documentation Standards

### guide.md
Contains:
- Implementation patterns and best practices
- Step-by-step instructions
- Common use cases and examples
- Troubleshooting tips
- Governance rules and constraints
- Naming conventions and compliance requirements

## Key Principles

1. **User Approval Required**: Never update feature documentation without explicit user approval
2. **Proper Mapping**: Always verify feature/sub-feature mapping with the user
3. **Timestamps**: All phase documents must be timestamped
4. **Capture Everything**: Disagreements and alternative approaches are valuable learnings
5. **Structured Learning**: Knowledge captured in feature guides (via the salesforce-coe plugin) persists across user stories
