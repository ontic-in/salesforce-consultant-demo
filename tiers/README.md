# Tiers & Scope Documentation

This directory documents what features are **in scope** vs **out of scope** for each cloud and tier combination.

## Structure

```
tiers/
├── README.md                 (this file)
├── sales-cloud/
│   ├── enable.md            ($15K tier, 6-8 weeks)
│   ├── elevate.md           ($45K tier, 10-12 weeks)
│   └── transform.md         ($75K tier, 16-18 weeks)
├── service-cloud/
│   ├── enable.md            ($20K tier, 6-8 weeks)
│   ├── elevate.md           ($35K tier, 10-12 weeks) [MOST POPULAR]
│   └── transform.md         ($60K tier, 16-18 weeks)
└── [future-cloud]/
    └── ...
```

## File Format

Each scope file follows a consistent structure:

```markdown
# [Cloud] - [Tier] Scope

## Overview
- Price point
- Timeline
- Target customer

## In Scope
### Category 1
- Feature A
- Feature B

### Category 2
- Feature C

## Out of Scope
- Feature X (available in [higher tier])
- Feature Y (available in [higher tier])

## Boundaries & Notes
- Important clarifications
- Common gray areas
```

## Usage

The requirements worksheet agent (`requirements/worksheets/agent.md`) references these scope files to:
1. Know what to include in recommendations
2. Route out-of-scope requests to the Parking Lot
3. Suggest tier upgrades when appropriate

## Adding a New Cloud/Tier

1. Create directory: `tiers/[cloud-name]/`
2. Add scope files: `enable.md`, `elevate.md`, `transform.md`
3. Follow the standard format above
4. Update the worksheet template if needed (`requirements/worksheets/`)
