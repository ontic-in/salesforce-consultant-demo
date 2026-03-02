---
description: Initialize project with client name, tier, and existing materials
---

## User Input

```text
$ARGUMENTS
```

You MAY consider the user input above. It is optional — the command will prompt for all required information interactively.

## Outline

Initialize a new Service Cloud engagement by collecting project details and personalizing all template files. This is the **first command** a consultant runs when starting a new engagement. It transforms the generic starter pack into a project-specific repository.

### Execution Steps

1. **Check If Already Set Up**: Detect whether this project has already been initialized
   - Read `README.md` and check if the title is still "Service Cloud Starter Pack Optimization"
   - If already customized (title has been changed):
     - Warn: "This project appears to already be set up as **[current title]**. Running setup again will overwrite the current configuration."
     - Ask: "Do you want to re-run setup?" (Yes/No)
     - If No: Exit gracefully with message "Setup cancelled. Your existing configuration is preserved."
     - If Yes: Continue with setup (will overwrite existing values)

2. **Ask Question 1: Client Name** (Required)
   - Prompt: "What is the client's name?"
   - Example: "Acme Manufacturing", "GlobalTech Industries"
   - This is used in README title, CLAUDE.md title, workflow welcome message, user stories header
   - Validate: Must be non-empty

3. **Ask Question 2: Project Name** (Required, with default)
   - Prompt: "What is the project name?"
   - Default: "[Client Name] Service Cloud Implementation" (derive from client name)
   - Example: "Acme Service Cloud Implementation"
   - Show the default and let user accept or override
   - This is used in README title, CLAUDE.md title

4. **Ask Question 3: Scope/Tier** (Required, multiple choice)
   - Prompt: "Which scope tier is this engagement?"
   - Options:
     - **Enable** — $20K, 6-8 weeks, foundational Service Cloud setup
     - **Elevate** — $35K, 10-12 weeks, intermediate Service Cloud with integrations
     - **Transform** — $60K, 16-18 weeks, full enterprise Service Cloud transformation
   - This determines which `tiers/service-cloud/<tier>.md` is the active scope reference
   - Store the selected tier name (lowercase: enable, elevate, or transform)

5. **Ask Question 4: Call Transcripts?** (Yes/No)
   - Prompt: "Do you have discovery call transcripts to add?"
   - If Yes:
     - Tell user: "Place your transcript files in `requirements/call-transcripts/` — supported formats: .txt, .md, .pdf"
     - Tell user: "You can add them now or later. When ready, run `/salesforce-coe:sp:create-or-update-requirements-worksheet` to generate a requirements worksheet from them."
     - Do NOT block setup waiting for files
   - If No:
     - Tell user: "No problem — after your first discovery call, place the transcript in `requirements/call-transcripts/` and run `/salesforce-coe:sp:create-or-update-requirements-worksheet`."

6. **Ask Question 5: Existing Worksheets?** (Yes/No)
   - Prompt: "Do you have an existing requirements worksheet?"
   - If Yes:
     - Ask: "Please paste the path to the worksheet file, or place it in `requirements/worksheets/output/`"
     - If user provides a path: Note it for the summary
     - Tell user: "If you have raw transcripts instead of a finished worksheet, run `/salesforce-coe:sp:create-or-update-requirements-worksheet` to generate one."
   - If No:
     - Tell user: "You can generate one from call transcripts using `/salesforce-coe:sp:create-or-update-requirements-worksheet`."

7. **Ask Question 6: Existing User Stories?** (Yes/No)
   - Prompt: "Do you have existing user stories to import?"
   - If Yes:
     - Ask: "Please paste the user stories content below, or provide a file path."
     - If user pastes content: Store it for writing to `user-stories.md`
     - If user provides a file path: Read the file and store content
   - If No:
     - Tell user: "You can generate user stories from a requirements worksheet using `/salesforce-coe:sp:create-user-stories`."

8. **Update Files**: Apply all collected information to project files

   **a. Update `README.md`:**
   - Replace title `# Service Cloud Starter Pack Optimization` → `# [Client Name] - [Project Name]`
   - In the "Getting Started" section (near bottom of file), update step 1:
     - From: `1. Review the user stories in \`user-stories.md\` (US-001 through US-013)`
     - To: `1. Review the user stories in \`user-stories.md\`` (remove the specific count since stories may differ)
   - In the Repository Structure section, update the `user-stories.md` description line:
     - From: `user-stories.md                # All 13 user story definitions (US-001 to US-013)`
     - To: `user-stories.md                # User story definitions for [Client Name]`

   **b. Update `CLAUDE.md`:**
   - Replace title `# Claude Instructions for Service Cloud Starter Pack Optimization` → `# Claude Instructions for [Project Name]`
   - After the title line, insert a project context block:
     ```
     > **Client:** [Client Name]
     > **Tier:** [Tier Name] ($[amount], [duration])
     > **Initialized:** [YYYY-MM-DD]
     > **Scope Reference:** `tiers/service-cloud/[tier].md`
     ```

   **c. Update `.exo/workflows/primary_workflow.yaml`:**
   - Replace `[CLIENT_INDUSTRY]` in `system_prompt` → client name (both occurrences)
   - Replace `[CLIENT_INDUSTRY]` in `welcome_message` → client name (both occurrences)
   - Update `name:` field from `Service Cloud - Enable Tier` → `Service Cloud - [Tier] Tier`

   **d. Update `user-stories.md`:**
   - If user provided stories: Replace entire file content with their stories
   - If no stories provided: Update the header from `# User Stories` → `# [Client Name] - User Stories`

   **e. Update `user-story-template.md`:**
   - Replace `[Engagement Name]` → client name

9. **Show Summary**: Display what was configured

   ```
   ## Setup Complete

   **Client:** [Client Name]
   **Project:** [Project Name]
   **Tier:** [Tier] ($[amount], [duration])
   **Scope Reference:** tiers/service-cloud/[tier].md

   ### Files Updated
   - README.md — title and project references
   - CLAUDE.md — title and project context
   - .exo/workflows/primary_workflow.yaml — system prompt and welcome message
   - user-stories.md — [imported N stories / header updated]
   - user-story-template.md — engagement name

   ### Materials Status
   - Call transcripts: [Added / Not yet — add to requirements/call-transcripts/]
   - Requirements worksheet: [Provided / Not yet — run /salesforce-coe:sp:create-or-update-requirements-worksheet]
   - User stories: [Imported / Not yet — run /salesforce-coe:sp:create-user-stories]

   ### Plugin
   - Salesforce COE: [Will be installed in next step]
   ```

10. **Suggest Next Step**: Based on what the user provided, recommend the next action

    | Has | Doesn't Have | Recommendation |
    |-----|-------------|----------------|
    | Transcripts | Worksheet | Run `/salesforce-coe:sp:create-or-update-requirements-worksheet` to generate a requirements worksheet |
    | Worksheet | User stories | Run `/salesforce-coe:sp:create-user-stories` to generate sequenced user stories |
    | User stories | — | Run `/salesforce-coe:sp:plan US-001` to start planning the first user story |
    | Nothing yet | Everything | Schedule your discovery call, then place the transcript in `requirements/call-transcripts/` and run `/salesforce-coe:sp:create-or-update-requirements-worksheet` |

    Show the single most relevant next step clearly.

11. **Install Salesforce COE Grimoire Plugin**: Install (or enable) the `salesforce-coe` plugin to provide the agent with the COE knowledge base, workflows, and capability tooling.

    **a. Check if already installed:**
    ```bash
    claude plugin list
    ```
    - If `salesforce-coe` appears in the output and is **enabled**: Skip to step 11d — report `✅ Salesforce COE plugin already installed and enabled`.
    - If `salesforce-coe` appears but is **disabled**: Go to step 11b (enable it).
    - If `salesforce-coe` is **not listed**: Go to step 11c (install it).

    **b. Enable the plugin (if installed but disabled):**
    ```bash
    claude plugin enable salesforce-coe
    ```
    - Skip to step 11d.

    **c. Install the plugin (if not installed):**
    ```bash
    # Register the grimoire marketplace (if not already registered)
    claude plugin marketplace add https://github.com/ontic-in/grimoire

    # Install with project scope
    claude plugin install salesforce-coe@grimoire --scope project
    ```

    **d. Report result to user:**
    - If already enabled: `✅ Salesforce COE plugin already installed and enabled`
    - If enabled from disabled: `✅ Salesforce COE plugin enabled`
    - If freshly installed: `✅ Salesforce COE plugin installed (project scope)`
    - If failed: Show the error and tell user they can install manually later with:
      ```
      claude plugin marketplace add https://github.com/ontic-in/grimoire
      claude plugin install salesforce-coe@grimoire --scope project
      ```
    - Do NOT block the rest of setup if plugin installation fails — treat it as non-fatal.

    **e. Introduce available commands (if plugin is installed and enabled):**

    After confirming the plugin is active, show the user what slash commands are now available from `salesforce-coe`:

    ```
    ### Salesforce COE Plugin — Available Commands

    The `salesforce-coe` plugin provides these slash commands:

    | Command | Purpose |
    |---------|---------|
    | `/salesforce-coe:sp:plan` | Create implementation plan for a user story by mapping requirements to feature guides |
    | `/salesforce-coe:sp:implement` | Execute Salesforce implementation from an approved plan |
    | `/salesforce-coe:sp:qa` | Quality assurance validation for an implemented user story |
    | `/salesforce-coe:sp:feedback` | Capture consultant feedback and update feature guides |
    | `/salesforce-coe:sp:create-user-stories` | Generate sequenced user stories from a finalized requirements worksheet |
    | `/salesforce-coe:sp:create-or-update-requirements-worksheet` | Generate or update a requirements worksheet from transcripts, SOWs, and client docs |

    **Automatic skill:** `learning-loop` — activates automatically during implementation when deviations from documented patterns are detected.

    > **Note:** These commands are provided by the `salesforce-coe` grimoire plugin, which includes the COE knowledge base (best practices, configuration patterns, implementation guidance) as grounding context for the agent.
    ```

12. **Auto-Commit**: Stage and commit all changes

    **Stage all modified files:**
    ```bash
    git add README.md CLAUDE.md .exo/workflows/primary_workflow.yaml user-stories.md user-story-template.md
    ```

    **Create commit:**
    ```bash
    git commit -m "[setup] Initialize project: [Client Name] - [Tier] tier

    - Client: [Client Name]
    - Project: [Project Name]
    - Tier: [Tier] ([amount], [duration])
    - User stories: [imported / placeholder]

    CI: ⏭️ Skipped (project initialization)"
    ```

    **Push to remote:**
    ```bash
    git push
    ```

    **Show confirmation:**
    ```
    ✅ Project initialized and committed!

    Commit: <short-hash>
    Pushed: Yes

    [Next step recommendation from Step 10]
    ```

## Error Handling

| Error | Recovery |
|-------|----------|
| README.md not found | Check if you're in the right repository. The starter pack template should have a README.md at the root. |
| CLAUDE.md not found | Check if the `.claude/` directory exists. This may not be a starter pack template. |
| Workflow YAML not found | Check `.exo/workflows/` for the workflow file. It may be named `no_steps_workflow.yaml` (pre-rename) or `primary_workflow.yaml`. |
| Tier file not found | Verify `tiers/service-cloud/` directory contains enable.md, elevate.md, and transform.md. |
| User story file path invalid | Ask user to verify the path. Offer to paste content directly instead. |
| Git commit fails | Check `git status` for issues. Ensure all files were saved correctly before staging. |
| `[CLIENT_INDUSTRY]` placeholder not found in YAML | The workflow file may have already been customized. Search for the current system_prompt text and update it directly. |
| Grimoire marketplace add fails | Check network connectivity. User can retry manually: `claude plugin marketplace add https://github.com/ontic-in/grimoire` |
| Plugin install fails | The grimoire marketplace may not be published yet. Try installing from a local path if available: `claude plugin install /path/to/salesforce-coe/dist/salesforce-coe`. Setup continues regardless. |

## Agent Next Steps

After executing the setup command:
- If user has transcripts but no worksheet → suggest `/salesforce-coe:sp:create-or-update-requirements-worksheet`
- If user has a worksheet but no stories → suggest `/salesforce-coe:sp:create-user-stories`
- If user has stories → suggest `/salesforce-coe:sp:plan US-001`
- If project is fully set up → remind user of the workflow: plan → implement → qa → feedback
