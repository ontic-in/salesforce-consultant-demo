# Service Cloud - Enable Tier Scope

## Overview

| Attribute | Value |
|-----------|-------|
| **Price** | $20,000 |
| **Timeline** | 6-8 weeks |
| **Target** | Greenfield Service Cloud implementations, small-mid support teams |
| **Users** | Up to 10 users |

---

## In Scope

### Case Management & Tracking
- Case object configuration
- Case status values (New, Working, Waiting, Escalated, Resolved, Closed)
- Case priorities (Low, Medium, High, Critical)
- Case types/record types
- Case fields customization
- Case page layouts
- Case list views
- Case related lists

### Case Capture
- Web-to-Case forms (basic)
- Email-to-Case routing
- Auto-response rules (email confirmation)
- Case creation from email
- Email threading on cases

### Case Assignment & Routing
- Case Assignment Rules (criteria-based)
- Case Queues
- Assign to users or queues based on criteria
- Default case owner
- Manual queue claiming by agents

### Case Escalation
- Escalation Rules (time-based)
- Case age escalation
- Priority-based escalation
- Manager notification on escalation

### Contact & Account Management
- Contact fields customization
- Account fields customization
- Account Hierarchy (parent-child)
- Contact-to-Case relationships (standard lookup)
- Contacts to multiple accounts (optional)

### Email Integration
- Email-to-Case
- Outlook Integration and Sync (standard - access Salesforce from Outlook, log emails)
- Gmail Integration and Sync (standard - Chrome extension, access Salesforce from Gmail)
- Send email from case feed
- Email templates (up to 10)
- Email-to-Case address setup

### Activity Management
- Tasks and Events on cases
- Case comments
- Activity History on cases
- Email logging
- Call logging

### Automation (Basic)
- Flow Builder (record-triggered flows, up to 3)
- Email alerts and notifications
- Field updates (automatic)
- Task creation (automatic)
- Status updates based on conditions

### Reports & Dashboards
- Standard Reports (OOTB - includes case volume, case aging, open cases, resolution times, queue status, agent productivity)
- 1 Custom Dashboard with 5 custom reports
- Dashboard shows top 5 client-selected metrics

### Mobile
- Salesforce Mobile App access
- View/edit cases on mobile
- Log activities on mobile
- Case comments on mobile

### User Management
- Up to 10 full users
- Role Hierarchy (up to 3 levels)
- Basic Profiles
- Permission Sets (limited)
- Public Groups

### Security & Access
- Organization-Wide Defaults (OWD) configuration
- Sharing Rules (role-based and criteria-based)
- Field-Level Security (FLS)
- Basic data security model

### Branding
- Company logo
- Lightning Theme colors
- Basic UI customization

### Data Management
- Data Import (Accounts, Contacts, Cases)
- Data migration from existing system
- Duplicate Management (basic rules)

### Training
- Train the Trainer (4 hours)
- End user training materials

---

## Out of Scope

### Advanced Case Routing (Elevate+)
- Round-robin assignment (requires custom Flow or AppExchange app)
- Territory-based assignment (requires Enterprise Territory Management or custom code)
- Skills-based routing
- Capacity-based routing
- Load balancing

### Service Console (Elevate+)
- Service Console app configuration
- Console layouts
- Split view configuration
- Softphone integration
- Console utilities

### Knowledge Management (Elevate+)
- Knowledge articles
- Knowledge base setup
- Article types
- Article categories
- Publishing workflow
- Article search

### Omni-Channel (Elevate+)
- Omni-Channel routing
- Skills-based routing
- Capacity-based routing
- Real-time routing
- Agent status management

### Entitlements & Milestones (Elevate+)
- Entitlement Management
- Service Contracts
- Milestones
- SLA tracking (advanced)
- Entitlement processes
- Violation workflows

### Live Agent / Chat (Elevate+)
- Live Agent setup
- Chat deployments
- Chat routing
- Chat transcripts
- Pre-chat forms
- Chat buttons

### Email Add-Ons (Requires Separate License)
- Einstein Activity Capture (automatic email/calendar sync)
- Salesforce Inbox (enhanced email integration features)

### Advanced Features (Transform)
- Case Swarming
- Multiple Service Processes
- Advanced Entitlement Processes
- Approval Workflows
- Field Service Lightning
- Customer Community/Portal
- Advanced SLA management
- CTI Integration

### Advanced Automation (Elevate/Transform)
- Complex Flow Builder (>5 flows)
- Multi-step Approval Processes
- Scheduled automation (complex)
- Platform Events
- Apex triggers/classes

### Advanced Analytics (Transform)
- Einstein Analytics
- AI-powered case classification
- Predictive case routing
- Custom dashboards (unlimited)
- Scheduled reports

---

## Boundaries & Notes

### Common Gray Areas

| Request | Decision | Notes |
|---------|----------|-------|
| "We need knowledge articles" | Out of scope | Elevate tier feature |
| "Can we track service contracts?" | Limited | Basic entitlement tracking only, full contracts in Elevate |
| "We need Live Agent chat" | Out of scope | Elevate tier feature (1 deployment) |
| "Multiple case processes" | Limited | 1-2 simple case processes supported |
| "Service Console" | Out of scope | Elevate tier feature |
| "Skills-based routing" | Out of scope | Transform tier feature |
| "Case swarming" | Out of scope | Transform tier feature |

### Upgrade Triggers

Recommend Elevate tier discussion when client mentions:
- Knowledge base/articles
- Service Console requirements
- Omni-Channel routing
- Live Agent or chat
- Entitlements with milestones
- Advanced SLA tracking
- Quick Text and macros

Recommend Transform tier discussion when client mentions:
- Multiple service processes
- Skills-based routing
- Case swarming
- Service Contracts with complex SLAs
- Approval workflows
- Customer satisfaction surveys
- Advanced automation (>5 flows)

### Implementation Notes

- Einstein Activity Capture is the recommended email/calendar sync approach
- Limit workflow rules to essential automations (recommend <5)
- Dashboard limit of 3 forces prioritization - work with client to identify top KPIs
- Data import includes cleanup consultation but not extensive data transformation
- Email-to-Case is simpler than On-Demand Email-to-Case (recommend standard)
- Case assignment rules limited to basic territory/queue routing
- Escalation rules should focus on time-based and priority-based triggers

### User Limits & Constraints

- Up to 10 full Service Cloud users
- 3 custom dashboards maximum
- 5 standard reports included
- Up to 5 workflow rules
- Up to 3 basic Process Builder flows
- Up to 10 email templates
- Basic case assignment rules (not Omni-Channel)

---

## What Success Looks Like

After Enable tier implementation, client should have:
- Cases automatically created from web forms and email
- Cases automatically assigned to appropriate agents/queues
- Basic escalation rules triggering for aging cases
- Email integration working for Gmail/Outlook
- 3 dashboards showing key support metrics
- Mobile access for agents in the field
- Clean migrated data from previous system
- Trained team ready to use the system
