# User Story Template

Use this format when documenting user stories in `user-stories.md`.

---

```markdown
# relay logic - User Stories

## US-001: [Title]

**Status:** [ ] Not Started / [x] Approved / [ ] Implemented / [ ] Verified

### Business Requirement
[What the customer needs, with transcript references]

### Transcript References
- Line X: *"quote"*
- Line Y: *"quote"*

### Solution Design

**Custom Fields:**
| Field | Type | Values | Purpose | Transcript Reference |
|-------|------|--------|---------|---------------------|
| [API Name] | [Type] | [Values or -] | [Why needed] | Line X: *"quote"* |

**Other Configuration:**
- [Picklist values, page layouts, permission sets, etc.]

**Design Decisions:**
> **Decision:** [What was chosen]
> **Rationale:** [Why this option; can migrate to X later if needed]

### Feature Assumptions (What We're NOT Configuring)
| Feature | Rationale |
|---------|-----------|
| [Feature name] | Not discussed in transcript |
| [Feature name] | Explicitly confirmed not required - [quote or reference] |

### Implementation Checklist

**Deploy:**
- [ ] [Primary metadata to create/configure]
- [ ] [Additional primary metadata...]

**Secure & Make Usable (from dependency matrix):**
- [ ] [Permission Set / FLS updates]
- [ ] [Page Layout / FlexiPage placement]
- [ ] [Profile assignments (RT visibility, app visibility)]
- [ ] [Picklist value assignments per record type]

**Verify:**
- [ ] [SOQL verification query]
- [ ] [Functional test: create/update record as admin]
- [ ] [End-user test: verify as non-admin user]
- [ ] User verification with client
```

---

## Why Feature Assumptions Matter

These document the Salesforce capabilities we're consciously skipping. If the customer later asks "why don't we have X?", the assumption table provides the answer and audit trail.
