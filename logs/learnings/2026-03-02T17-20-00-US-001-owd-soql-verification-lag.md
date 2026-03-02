# Learning: OWD SOQL verification shows stale values after deploy

## Metadata
- **Timestamp**: 2026-03-02T17-20-00
- **User Story**: US-001
- **Source**: US-001
- **Feedback Type**: Missing documentation
- **Status**: pending

## Target Guide

- **Feature Guide**: `features/user-management/org-wide-defaults/guide.md`
- **Section**: Troubleshooting
- **Action**: Add row to table

## Proposed Change

### Context
During US-001 implementation, after successfully deploying Account OWD from ReadWrite to Read, the SOQL verification query (`SELECT DefaultAccountAccess FROM Organization`) still returned `Edit` (the old value) for approximately 30 seconds. This led to initial confusion about whether the deploy had actually succeeded. A second query 30 seconds later confirmed the new value `Read`. The deploy report confirmed success the entire time — the lag was in SOQL propagation, not in the deploy itself.

### Content to Add
| SOQL shows old OWD value after successful deploy | Sharing recalculation is still running — Organization sObject reflects the new value only after recalculation completes (~30 seconds) | Wait 30 seconds after deploy, then re-query. Do not re-deploy — the change was applied; it just takes time to propagate to SOQL. Check `sf project deploy report` to confirm deploy succeeded. |
