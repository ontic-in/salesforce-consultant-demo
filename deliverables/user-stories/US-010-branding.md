# US-010: Branding

**Status:** [ ] Not Started

## Business Requirement

Apply Relay Logic's brand identity to the Salesforce org — company logo, Lightning theme colors, and basic UI customization so the system feels like their own tool, not a generic platform.

## Worksheet References
- Section 14, Branding: *"❓ Needs Discussion — not discussed in discovery"*
- Section 14, Logo: *"❓ Needs Discussion"*
- Section 14, Brand Colors: *"❓ Needs Discussion"*

## Solution Design

### Lightning Theme

| Setting | Value | Notes |
|---|---|---|
| Brand Color (Primary) | ❓ Needs client brand guide | Header bar, active tabs |
| Logo | ❓ Needs logo file from client | Header logo (max 125x50px recommended) |
| Loading Page Logo | ❓ Same as header logo | Shown during page loads |
| Background Color | ❓ Default white or client preference | Page background |

> **Design Decision:** Lightning Theme (not Lightning App) for branding
> **Rationale:** Lightning Theme applies org-wide brand colors and logo without creating a separate app. Simpler and appropriate for Enable tier. A custom Lightning App is a separate story if needed.

**Org Analysis Findings:**

| Item | Current State | Gap | Action |
|---|---|---|---|
| Lightning Theme | SDO default theme | Need Relay Logic branding | Update |
| Company logo | SDO logo | Need Relay Logic logo | Update |
| Brand colors | SDO defaults | Need Relay Logic colors | Update |

## Feature Assumptions (What We're NOT Configuring)

| Feature | Rationale |
|---|---|
| Custom Lightning App | Not needed for basic branding; theme is sufficient |
| Custom login page | Not discussed; standard Salesforce login |
| Custom email headers/footers | Handled in US-006 email templates |
| Custom favicon | Not supported in standard Lightning |

## Implementation Checklist

### Phase 1: Gather Brand Assets (Client Action Required)

- [ ] Request from client: logo file (PNG/JPG, max 125x50px for header)
- [ ] Request from client: primary brand color (hex code)
- [ ] Request from client: secondary brand color (optional)

### Phase 2: Apply Branding

- [ ] Create/update Lightning Theme in Setup → Themes and Branding:
  - Upload logo
  - Set brand color
  - Set page background color (if specified)
- [ ] Set as active theme for the org

### Secure & Make Usable

- [ ] Verify logo appears in header for all users
- [ ] Verify brand colors applied to navigation bar, active tabs
- [ ] Verify theme appears correctly on mobile app
- [ ] User verification with client

---

❓ **Open Questions:**
1. **Logo file** — Do you have a logo file ready? (PNG/JPG, recommended 125x50px)
2. **Brand colors** — What are Relay Logic's primary brand colors? (hex codes)
3. **Priority** — Is branding a Day 1 requirement or can it wait until after core functionality is live?
