---
description: Initialize project with client name, tier, and existing materials
---

## Input

The form values are provided as JSON:

```text
$ARGUMENTS
```

## Task

Run `scripts/setup.py` with the form values and ensure it completes successfully. If it fails, help the user resolve the issue and re-run.

### Steps

1. **Run the setup script** — pipe the form JSON via stdin:

   ```bash
   echo '<the JSON from $ARGUMENTS>' | python3 scripts/setup.py
   ```

2. **Check the result:**

   - **Exit code 0** — the script succeeded. Its stdout logs show what was configured, which files were updated, and whether the grimoire plugin was installed. Proceed to step 3.

   - **Non-zero exit code** — the script failed. Show the error output to the user and help them fix the issue (e.g. missing file, wrong directory, Python not installed). Once resolved, re-run the script.

3. **Commit and push** the changes:

   ```bash
   git add README.md CLAUDE.md .exo/workflows/primary_workflow.yaml deliverables/user-stories/templates/user-story-template.md
   ```

   ```bash
   git commit -m "[setup] Initialize project: [client] - [tier] tier

   - Client: [client]
   - Project: [project]
   - Tier: [tier] ([amount], [duration])

   CI: skip (project initialization)"
   ```

   ```bash
   git push
   ```

4. **Tell the user** the next step in the process checklist is to upload discovery call transcripts and client documents.
