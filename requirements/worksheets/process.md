# Requirements Worksheet Process Guide

*For Consultants Using the Enable Tier Worksheet*

---

## Overview

This guide explains how to use the AI-accelerated requirements gathering system for Sales Cloud Starter Pack (Enable tier) discovery.

## The Two Phases

### Phase 1: Pre-Session AI Analysis

Before your collaborative session with the client:

1. **Gather Input Materials**
   - Fathom transcript from discovery/sales calls
   - Any documents the client has provided (org charts, process docs, etc.)
   - Brief context about the client's business

2. **Run the AI Analysis**
   ```
   Provide the agent with:
   - Transcript content
   - Client documents
   - Request: "Analyze this and pre-fill the Enable tier worksheet"
   ```

3. **Review AI Suggestions**
   - The agent will return the worksheet with suggestions marked as `📝 AI Suggestion`
   - Review for accuracy before the client session
   - Note any areas that need clarification

### Phase 2: Collaborative Client Session

Live session with the client (typically 60-90 minutes via screen share):

1. **Set Expectations** (5 min)
   - Explain the worksheet purpose
   - Show how suggestions are marked
   - Emphasize this is collaborative - nothing is final until they confirm

2. **Walk Through Sections** (60-75 min)
   - Go section by section
   - For AI suggestions: "Based on our earlier conversation, we think X - is this correct?"
   - Mark items as ✅ Confirmed or ❓ Needs Discussion
   - Capture items outside Enable scope in the Parking Lot

3. **Wrap Up** (10 min)
   - Review Next Steps section
   - Assign action items with owners and dates
   - Schedule follow-up if needed

---

## Section-by-Section Guide

### Section 1: About Your Business

**What we're capturing:** Basic company setup that affects the entire system.

**Key decisions:**
- Fiscal year (affects all reporting and forecasting)
- Multi-currency (must be enabled at org creation - irreversible)
- Time zones (affects automation and scheduling)

**Tips:**
- If unsure about fiscal year, default to calendar year
- Multi-currency is Enable tier scope, but Advanced Currency Management is not

---

### Section 2: Your Sales Team

**What we're capturing:** Users and hierarchy structure.

**Key decisions:**
- Number of full licenses needed
- Reporting hierarchy (who reports to whom)
- Whether managers see team data

**Tips:**
- Get actual names and emails - needed for user setup
- Confirm hierarchy matches how they want data visibility to work

---

### Section 3: Your Existing Customer Data

**What we're capturing:** Data migration scope and quality.

**Key decisions:**
- What data to import (accounts, contacts, opportunities)
- Data cleanliness - do we need a cleanup phase?
- Duplicate prevention rules

**Tips:**
- Ask for sample data files to assess quality
- Underpromise on data migration complexity

---

### Section 4: Lead Management

**What we're capturing:** Lead capture, assignment, and conversion process.

**Key decisions:**
- Web-to-Lead setup requirements
- Assignment rules (how leads get routed)
- Lead stages and conversion process

**Enable Tier Scope:**
- ✅ Web-to-Lead
- ✅ Lead assignment rules
- ✅ Lead queues
- ✅ Auto-response rules
- ✅ Lead conversion
- ❌ Lead scoring (Elevate tier)
- ❌ Lead nurturing automation (Elevate tier)

**Tips:**
- Get the actual website form fields they want
- Clarify round-robin vs. territory-based assignment

---

### Section 5 & 6: Account & Contact Management

**What we're capturing:** How they organize companies and people.

**Key decisions:**
- Account hierarchy needs
- Classification/categorization scheme
- Required fields for data quality

**Enable Tier Scope:**
- ✅ Account hierarchy (parent-child)
- ✅ Account/contact record types
- ✅ Custom fields
- ❌ Territory management (Elevate tier)
- ❌ Account teams (Elevate tier)

**Tips:**
- Keep categorization simple - recommend starting with 3-5 options max
- Required fields should be minimal to start

---

### Section 7: Opportunity Management

**What we're capturing:** Their sales process and deal tracking.

**Key decisions:**
- Sales stages and probabilities
- Required opportunity fields
- Contact roles requirements

**Enable Tier Scope:**
- ✅ Custom sales process (stages)
- ✅ Sales Path (guided selling)
- ✅ Contact roles on opportunities
- ❌ Opportunity teams (Elevate tier)
- ❌ Opportunity splits (Elevate tier)
- ❌ Quote management (Elevate tier)

**Tips:**
- Get them to walk through a real recent deal
- Probabilities should add up logically (early stages lower)
- Sales Path guidance is highly valuable - spend time here

---

### Section 8: Activities & Tasks

**What we're capturing:** Activity tracking and email/calendar integration.

**Key decisions:**
- Which activities to track
- Email/calendar sync preferences
- Automatic task creation rules

**Enable Tier Scope:**
- ✅ Activity tracking
- ✅ Tasks and events
- ✅ Email integration (Gmail/Outlook)
- ✅ Calendar sync

**Tips:**
- Einstein Activity Capture is the recommended approach for email/calendar sync
- Clarify if they want emails auto-logged or manual

---

### Section 9: Basic Automation

**What we're capturing:** Workflow rules and automation needs.

**Key decisions:**
- Notification triggers
- Field update rules
- Automatic task creation

**Enable Tier Scope:**
- ✅ Workflow rules (limited)
- ✅ Process Builder basics
- ✅ Email alerts
- ❌ Complex approval workflows (Elevate tier)
- ❌ Advanced Flow automation (Elevate tier)

**Tips:**
- Keep automation simple in Enable tier
- Document complex requests in Parking Lot for Elevate

---

### Section 10: Reports & Dashboards

**What we're capturing:** Reporting and visibility needs.

**Key decisions:**
- Key metrics for leadership vs. reps
- Dashboard layout preferences
- Report frequency/distribution

**Enable Tier Scope:**
- ✅ Standard reports
- ✅ Custom reports (limited)
- ✅ Dashboards (up to 3 recommended)
- ❌ Advanced analytics (Elevate tier)
- ❌ Einstein Analytics (Transform tier)

**Tips:**
- Start with 1 leadership dashboard and 1 rep dashboard
- Can always add more reports post-launch

---

## Handling Common Situations

### Client Asks for Something Outside Enable Scope

1. Acknowledge the request
2. Explain it's part of Elevate/Transform tier
3. Document in Parking Lot
4. Ask if they want to discuss upgrading

Example: "That's a great feature - opportunity splits for team selling. That's actually part of our Elevate tier. Let me note that in our Parking Lot, and we can discuss whether that's something you'd want to add to this project."

### Client Can't Decide

1. Offer a recommendation based on best practices
2. Note it can be changed post-launch
3. Document the uncertainty

Example: "Most companies in your industry use 5-7 sales stages. I'd recommend starting with these [show example], and we can refine them in the first month based on how it feels."

### AI Suggestion is Wrong

1. Simply correct it - no need to explain the AI
2. Mark as ✅ with the correct answer
3. This helps improve future suggestions

---

## Post-Session

1. **Clean up the worksheet** - Remove AI suggestion markers, keep only confirmed answers
2. **Send to client** - For their records and final sign-off
3. **Feed to implementation agent** - The worksheet maps to questionnaire.csv which feeds our implementation system
4. **Track in ClickUp** - Update ticket status and attach final worksheet

---

## Mapping to Implementation

The worksheet sections map to the implementation system as follows:

| Worksheet Section | questionnaire.csv Category | Implementation Impact |
|-------------------|---------------------------|----------------------|
| Section 1: About Your Business | System Setup - Company Information | Org settings, fiscal year, currency |
| Section 2: Your Sales Team | User Management, Roles & Hierarchy | User creation, role hierarchy |
| Section 3: Existing Data | Data Management | Data import planning |
| Section 4: Lead Management | Lead Management | Web-to-Lead, assignment rules |
| Section 5: Accounts | Account Management | Record types, page layouts |
| Section 6: Contacts | Contact Management | Fields, page layouts |
| Section 7: Opportunities | Opportunity Management | Sales process, stages, paths |
| Section 8: Activities | Activity Management | Activity settings, email integration |
| Section 9: Automation | Workflow Automation | Workflow rules, processes |
| Section 10: Reports | Reporting & Analytics | Dashboards, reports |

---

## Tips for Success

1. **Screen share is essential** - Client needs to see the worksheet as you fill it
2. **Use their language** - Avoid Salesforce jargon
3. **Validate AI suggestions explicitly** - "We think X based on our call - is that right?"
4. **Capture the why** - Notes column is for context that helps implementation
5. **Time box sections** - Don't spend too long on any one section
6. **Parking Lot is your friend** - Keeps session focused on Enable scope
