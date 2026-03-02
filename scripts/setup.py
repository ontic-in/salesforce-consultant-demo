#!/usr/bin/env python3
"""
Project setup script for Service Cloud Starter Pack.

Reads JSON from stdin with fields: clientName, projectName, tier
Updates all template files with project-specific values.
"""

import sys
import json
import re
from datetime import date
from pathlib import Path

TIER_META = {
    "Enable": {"amount": "$20K", "duration": "6-8 weeks"},
    "Elevate": {"amount": "$35K", "duration": "10-12 weeks"},
    "Transform": {"amount": "$60K", "duration": "16-18 weeks"},
}

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():
    print("Reading input from stdin...")
    raw = sys.stdin.read()
    data = json.loads(raw)

    client_name = data["clientName"].strip()
    if not client_name:
        print("Error: clientName is required", file=sys.stderr)
        sys.exit(1)

    tier = data["tier"].strip()
    if tier not in TIER_META:
        print(f"Error: tier must be one of {list(TIER_META.keys())}", file=sys.stderr)
        sys.exit(1)

    project_name = (data.get("projectName") or "").strip()
    if not project_name:
        project_name = f"{client_name} Service Cloud Implementation"

    meta = TIER_META[tier]
    today = date.today().isoformat()

    print(f"Client: {client_name}")
    print(f"Project: {project_name}")
    print(f"Tier: {tier} ({meta['amount']}, {meta['duration']})")
    print()

    update_readme(client_name, project_name)
    update_claude_md(client_name, project_name, tier, meta, today)
    update_workflow_yaml(client_name, tier)
    update_user_story_template(client_name)

    print()
    print("Setup complete.")


def update_readme(client_name: str, project_name: str):
    print("Updating README.md...")
    path = PROJECT_ROOT / "README.md"
    text = path.read_text()

    text = text.replace(
        "# Starter Pack Agent Testing Template",
        f"# {client_name} - {project_name}",
    )


    path.write_text(text)
    print("  Done.")


def update_claude_md(client_name: str, project_name: str, tier: str, meta: dict, today: str):
    print("Updating CLAUDE.md...")
    path = PROJECT_ROOT / "CLAUDE.md"
    text = path.read_text()

    old_title = "# Claude Instructions for Service Cloud Starter Pack Optimization"
    new_title = f"# Claude Instructions for {project_name}"

    context_block = (
        f"\n> **Client:** {client_name}\n"
        f"> **Tier:** {tier} ({meta['amount']}, {meta['duration']})\n"
        f"> **Initialized:** {today}\n"
        f"> **Scope Reference:** `tiers/service-cloud/{tier.lower()}.md`\n"
    )

    text = text.replace(old_title, new_title + context_block, 1)

    path.write_text(text)
    print("  Done.")


def update_workflow_yaml(client_name: str, tier: str):
    print("Updating .exo/workflows/primary_workflow.yaml...")
    path = PROJECT_ROOT / ".exo" / "workflows" / "primary_workflow.yaml"
    text = path.read_text()

    text = text.replace("[CLIENT_INDUSTRY]", client_name)

    text = re.sub(
        r"^name:\s*Service Cloud - \w+ Tier",
        f"name: Service Cloud - {tier} Tier",
        text,
        flags=re.MULTILINE,
    )

    path.write_text(text)
    print("  Done.")


def update_user_story_template(client_name: str):
    print("Updating deliverables/user-stories/templates/user-story-template.md...")
    path = PROJECT_ROOT / "deliverables" / "user-stories" / "templates" / "user-story-template.md"
    text = path.read_text()

    text = text.replace("[Engagement Name]", client_name)

    path.write_text(text)
    print("  Done.")


if __name__ == "__main__":
    main()
