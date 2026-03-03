# Relay Logic - Service Cloud User Stories

**Client:** Relay Logic
**Cloud:** Service Cloud
**Tier:** Enable ($20,000)
**Date:** 2026-03-03
**Source Worksheet:** requirements/worksheets/output/relay-logic-service-cloud-enable-worksheet-v2.md

---

## Story Index

| # | Story | File | Status |
|---|-------|------|--------|
| US-001 | Team Setup — Users, Roles, Profiles & OWD | `deliverables/user-stories/US-001-team-setup.md` | Not Started |
| US-002 | Account & Contact Data Model | `deliverables/user-stories/US-002-account-contact-data-model.md` | Not Started |
| US-003 | Case Object Configuration | `deliverables/user-stories/US-003-case-object-configuration.md` | Not Started |
| US-004 | Automation Flows (3 Flows) | `deliverables/user-stories/US-004-automation-flows.md` | Not Started |

---

## Implementation Sequence

### Dependency Map
```
US-001: Team Setup (Users, Roles, Profiles, OWD)
  └── US-004: Automation Flows (needs users for Senior Queue members)

US-002: Account & Contact Data Model (Customer Tier, Account Start Date)
  └── US-003: Case Object Configuration (Customer_Tier__c formula references Account.Customer_Tier__c)
        └── US-004: Automation Flows (flows reference Product_Line__c, Customer_Tier__c, case statuses)

US-002: Account & Contact Data Model
  └── US-004: Automation Flows (Flow 2 references Account_Start_Date__c)
```

### Implementation Order

| Order | Story | Dependencies | Can Start After |
|-------|-------|-------------|-----------------|
| 1 | US-001: Team Setup | None | Immediately |
| 1 | US-002: Account & Contact Data Model | None | Immediately (parallel with US-001) |
| 2 | US-003: Case Object Configuration | US-002 | US-002 complete |
| 3 | US-004: Automation Flows | US-001, US-002, US-003 | All others complete |

### Parallel Execution Opportunities
- US-001 and US-002 can run in parallel (no shared dependencies)
- US-003 must wait for US-002 (Customer_Tier__c formula references Account field)
- US-004 is the final story (depends on all three: users for queue, fields for flow logic)

---

## Parking Lot (From Requirements Worksheet)

*Items captured during discovery but outside selected story scope:*

| Item | Notes | Suggested Tier |
|------|-------|----------------|
| Customer Portal | Lisa: "We want a customer portal eventually." | Transform ($60K) |
| Stripe Billing Integration | Lisa: "It'd be great if we could see subscription info right in Salesforce." | Elevate ($35K) or Transform ($60K) |
| Skills-Based Routing | Requires Omni-Channel (Elevate+ feature) | Elevate ($35K) |
| Knowledge Base / Help Center | Knowledge Management is Elevate+ feature | Elevate ($35K) |
| Auto-Close Stale Cases | All 3 Enable tier flow slots committed | Post-launch or Elevate ($35K) |
| Post-Resolution Follow-Up Automation | All 3 flow slots committed | Post-launch or Elevate ($35K) |
| Queue Setup (Core Platform, Integrations) | Section 6 — not selected for this phase. Senior Support Queue created in US-004. | Future story |
| Assignment Rules (product-based routing) | Section 6 — not selected for this phase | Future story |
| Escalation Rules | Section 4 subsection — not selected for this phase | Future story |
| Email-to-Case | Section 5 — not selected for this phase | Future story |
| Web-to-Case | Section 5 — not confirmed in scope | Future story |
| Email Integration & Templates | Section 8 — not selected for this phase | Future story |
| Reports & Dashboards | Section 11 — not selected for this phase | Future story |
| Security — Sharing Rules & FLS | Section 13 — not selected for this phase | Future story |
| Branding | Section 14 — all details pending | Future story |
| Data Import/Migration | Section 3 — mostly unknown, current system is Gmail | Future story |

---

## Story Generation Notes

**Generated:** 2026-03-03
**Source:** requirements/worksheets/output/relay-logic-service-cloud-enable-worksheet-v2.md (Version 2)
**Stories:** 4 user stories (out of 12 proposed; 8 deferred)
**Reviewed by:** Consultant
**Sequencing:** Approved
