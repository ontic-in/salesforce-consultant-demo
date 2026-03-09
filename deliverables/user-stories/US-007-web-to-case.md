# US-007: Web-to-Case

**Status:** [ ] Not Started

## Business Requirement

Relay Logic is planning to add a web form on their help center for case submission. The form should capture key information (Name, Email, Company, Product, Subject, Description) with reCAPTCHA spam protection. Submitted cases should route through the same assignment rules as email-created cases.

## Worksheet References
- Section 5, Web-to-Case: *"Yes — planned. Marcus: 'We're planning to add a web form on our help center'"*
- Section 5, Web Form Fields: *"Name, Email, Company, Product (dropdown), Subject, Description — 5-7 fields max for good UX"*
- Section 5, reCAPTCHA: *"Yes — recommended for public-facing forms to prevent spam"*

## Solution Design

### Web-to-Case Form Fields

| Field | Salesforce Field | Type | Required | Notes |
|---|---|---|---|---|
| Name | Contact Name (auto-match) | Text | Yes | Maps to Contact lookup |
| Email | SuppliedEmail / Contact Email | Email | Yes | Used for Contact matching and replies |
| Company | SuppliedCompany / Account Name | Text | Yes | Used for Account matching |
| Product | Product__c | Dropdown | Yes | Core Platform, Integrations, Analytics Module |
| Subject | Subject | Text | Yes | Case subject line |
| Description | Description | Textarea | Yes | Case details |

> **Design Decision:** 6 fields — lean form for good conversion
> **Rationale:** B2B SaaS best practice is 5-7 fields max. Product dropdown enables auto-routing. Contact matching by email creates/links Contact records.

### Web-to-Case Settings

| Setting | Value |
|---|---|
| Enable Web-to-Case | Yes |
| Default Case Origin | Web |
| Case Owner | Default assignment rule (US-004) |
| reCAPTCHA | Enabled |
| Response Template | Case_Auto_Response (from US-006) |
| Daily Limit | 5,000 (Salesforce default) |

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Web-to-Case | Not configured for RL | Enable and generate form | Create |
| reCAPTCHA | Not configured | Enable in Web-to-Case settings | Create |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Custom Visualforce/LWC form | Standard Web-to-Case HTML sufficient for Enable tier |
| File upload on web form | Not discussed; standard form doesn't support attachments |
| Customer Portal case submission | Out of scope — Transform tier feature |
| Multi-language forms | Not discussed; English-only |
| Custom form styling | Client embeds generated HTML; styling is their responsibility |

## Implementation Checklist

### Phase 1: Enable Web-to-Case

- [ ] Enable Web-to-Case in Setup → Web-to-Case Settings
- [ ] Enable reCAPTCHA spam protection
- [ ] Set default case origin to "Web"

### Phase 2: Generate Form

- [ ] Generate Web-to-Case HTML form from Setup → Web-to-Case:
  - Include fields: Name, Email, Company, Product__c, Subject, Description
  - Include hidden Case Origin = Web
- [ ] Add reCAPTCHA script to generated HTML
- [ ] Set return URL (❓ confirm with client — help center thank-you page)
- [ ] Provide generated HTML to client for embedding on help center

### Phase 3: Configure Routing

- [ ] Verify Web-to-Case cases use active assignment rules (US-004)
- [ ] Verify auto-response email fires for Web origin cases (US-006 auto-response rule)

### Secure & Make Usable

- [ ] Test: Submit form → case created with Origin=Web, correct Product, routed to correct queue
- [ ] Test: Auto-response email received by submitter
- [ ] Test: reCAPTCHA blocks bot submissions
- [ ] Provide client with HTML embed code and instructions
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Help center URL** — Where will the form be embedded? What's the thank-you page URL?
