# AI GEO SUPER-SKILL SUITE
## Agent Orchestration Implementation Plan

**Version:** 1.0.0  
**Status:** Implementation Blueprint  
**Architecture:** Human-in-the-Loop Agentic Workflow

---

# EXECUTIVE SUMMARY

## The Vision
Transform the 7-module AI GEO Suite from static documentation into a **live orchestration system** where AI agents execute the work and humans approve at strategic checkpoints.

## The Principle
```
AGENT DOES THE WORK → HUMAN APPROVES THE OUTPUT → NEXT STAGE TRIGGERS
```

## The Stack
- **Orchestrator:** n8n (self-hosted) or Make.com
- **AI Brain:** Claude API / Abacus AI
- **Data Collection:** Firecrawl, Ahrefs API, GSC API
- **Storage:** Airtable / Supabase
- **Delivery:** Google Docs, Notion, or Custom Dashboard

---

# QUICK OVERVIEW: THE 7-STAGE PIPELINE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI GEO ORCHESTRATION PIPELINE                            │
│                    Human Checkpoints at Each Gate                           │
└─────────────────────────────────────────────────────────────────────────────┘

 CLIENT                                                              RESULTS
 INPUT                                                               OUTPUT
   │                                                                    ▲
   ▼                                                                    │
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐   │
│ M7   │───▶│ M1   │───▶│ M2   │───▶│ M3   │───▶│ M4   │───▶│ M5   │───┤
│AUDIT │    │STRAT │    │RESRCH│    │WRITE │    │VIDEO │    │ASSET │   │
└──┬───┘    └──┬───┘    └──┬───┘    └──┬───┘    └──┬───┘    └──┬───┘   │
   │           │           │           │           │           │       │
   ▼           ▼           ▼           ▼           ▼           ▼       │
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐   │
│GATE 1│    │GATE 2│    │GATE 3│    │GATE 4│    │GATE 5│    │GATE 6│   │
│HUMAN │    │HUMAN │    │HUMAN │    │HUMAN │    │HUMAN │    │HUMAN │   │
│CHECK │    │CHECK │    │CHECK │    │CHECK │    │CHECK │    │CHECK │   │
└──────┘    └──────┘    └──────┘    └──────┘    └──────┘    └──────┘   │
                                                                       │
                              ┌──────┐    ┌──────┐                     │
                              │ M6   │───▶│GATE 7│─────────────────────┘
                              │ORCH  │    │HUMAN │
                              │SITE  │    │CHECK │
                              └──────┘    └──────┘
```

---

# THE 7 GATES: HUMAN CHECKPOINT SYSTEM

## Gate Philosophy
- **Agent:** Does 80% of the work (research, drafting, analysis)
- **Human:** Makes 20% of decisions (approval, direction, refinement)
- **Result:** 10x faster than manual, 100% quality controlled

---

## GATE 1: AUDIT APPROVAL
**Module 7 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Crawl client site (Firecrawl)
  - Pull competitor data (Ahrefs API)
  - Extract SERP top 10 (DataForSEO)
  - Analyze header structures
  - Generate gap matrix
  - Calculate revenue opportunity
  - Draft executive summary
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "15-30 minutes"
  
  review_items:
    - question: "Are the right competitors identified?"
      action: "Approve or swap competitors"
      
    - question: "Is the revenue estimate realistic?"
      action: "Adjust assumptions if needed"
      
    - question: "Are the top 3 priorities correct?"
      action: "Reorder or replace priorities"
      
  approval_options:
    - "✅ APPROVE → Trigger Module 1"
    - "🔄 REVISE → Send back to Agent with notes"
    - "❌ REJECT → Manual intervention required"
```

### Deliverable at Gate:
- Site Authority Scorecard (PDF)
- BOFU Gap Analysis (YAML)
- Executive Summary (2 pages)
- **GO/NO-GO decision for client engagement**

---

## GATE 2: STRATEGY APPROVAL
**Module 1 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Ingest audit findings
  - Generate Platform Strategy (6D Model)
  - Map Topic Clusters (Hub-Spoke)
  - Define Avatar Profiles
  - Create 90-day Content Calendar skeleton
  - Draft positioning statement
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "20-30 minutes"
  
  review_items:
    - question: "Does the positioning align with client brand?"
      action: "Approve or adjust angle"
      
    - question: "Are the topic clusters comprehensive?"
      action: "Add missing clusters or trim scope"
      
    - question: "Is the avatar accurate?"
      action: "Refine demographics/psychographics"
      
  approval_options:
    - "✅ APPROVE → Trigger Module 2"
    - "🔄 REVISE → Adjust strategy direction"
```

### Deliverable at Gate:
- Platform Strategy Document
- Topic Cluster Map (visual)
- Avatar Profile Cards
- **Strategic direction locked**

---

## GATE 3: KEYWORD APPROVAL
**Module 2 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Pull keyword data (Ahrefs/Semrush API)
  - Filter by BOFU intent signals
  - Score by MMA (Money, Movement, Authority)
  - Group into clusters
  - Identify "Quick Win" opportunities
  - Generate keyword-to-content mapping
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "15-20 minutes"
  
  review_items:
    - question: "Are high-value keywords correctly prioritized?"
      action: "Reorder priority list"
      
    - question: "Any keywords to exclude (brand risk, off-topic)?"
      action: "Remove from list"
      
    - question: "Is the content-type mapping correct?"
      action: "WSA vs Comparison vs Video assignment"
      
  approval_options:
    - "✅ APPROVE → Trigger Module 3 batch"
    - "🔄 REVISE → Adjust keyword selection"
```

### Deliverable at Gate:
- BOFU Keyword Master List (50-100 keywords)
- Priority Matrix (Top 20 for immediate action)
- Content Type Assignments
- **Keyword targets locked**

---

## GATE 4: CONTENT APPROVAL
**Module 3 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Generate content brief from keyword
  - Research top 10 competitors (header analysis)
  - Draft Whole Solution Article (3,000-4,500 words)
  - Insert entity mentions
  - Add FAQ section (5 questions)
  - Create meta title/description
  - Suggest internal links (Module 6 structure)
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "30-45 minutes per article"
  
  review_items:
    - question: "Is the angle differentiated from competitors?"
      action: "Approve unique hook or request revision"
      
    - question: "Is the information accurate?"
      action: "Fact-check claims and stats"
      
    - question: "Does it match brand voice?"
      action: "Tone adjustments"
      
    - question: "Are CTAs appropriate?"
      action: "Adjust conversion points"
      
  approval_options:
    - "✅ APPROVE → Queue for publishing"
    - "🔄 REVISE → Specific section edits"
    - "📝 EDIT → Human takes over for polish"
```

### Deliverable at Gate:
- Publication-ready article (Google Doc/Notion)
- Meta data package
- Internal link recommendations
- **Content approved for Module 6 deployment**

---

## GATE 5: VIDEO APPROVAL
**Module 4 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Convert WSA to video script format
  - Apply Hook-Story-Offer structure
  - Generate B-roll suggestions
  - Create thumbnail concepts (3 options)
  - Draft YouTube metadata (title, description, tags)
  - Suggest timestamps/chapters
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "15-20 minutes per script"
  
  review_items:
    - question: "Is the hook compelling (first 8 seconds)?"
      action: "Strengthen or rewrite hook"
      
    - question: "Is the pacing right for video?"
      action: "Trim or expand sections"
      
    - question: "Are CTAs natural (not salesy)?"
      action: "Adjust CTA placement/language"
      
  approval_options:
    - "✅ APPROVE → Send to video production"
    - "🔄 REVISE → Script adjustments"
```

### Deliverable at Gate:
- Video script (teleprompter-ready)
- Thumbnail concepts
- YouTube metadata package
- **Script approved for recording**

---

## GATE 6: ASSET APPROVAL
**Module 5 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Identify lead magnet opportunity from content
  - Generate lead magnet outline
  - Draft lead magnet content (checklist/template/guide)
  - Create landing page copy
  - Draft email sequence (3-5 emails)
  - Design automation workflow
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "20-30 minutes per asset"
  
  review_items:
    - question: "Is the lead magnet valuable enough to trade email?"
      action: "Enhance value or pivot format"
      
    - question: "Is the landing page copy compelling?"
      action: "Headline/CTA adjustments"
      
    - question: "Is the email sequence on-brand?"
      action: "Tone and offer adjustments"
      
  approval_options:
    - "✅ APPROVE → Build in marketing automation"
    - "🔄 REVISE → Content adjustments"
```

### Deliverable at Gate:
- Lead magnet (PDF/template)
- Landing page copy
- Email sequence drafts
- **Asset approved for deployment**

---

## GATE 7: SITE DEPLOYMENT APPROVAL
**Module 6 Output → Human Review**

### What Agent Does:
```yaml
agent_tasks:
  - Map internal linking structure
  - Generate schema markup (JSON-LD)
  - Create sitemap updates
  - Identify orphan pages to link
  - Draft redirect rules (if needed)
  - Generate robots.txt recommendations
```

### What Human Reviews:
```yaml
human_checkpoint:
  duration: "30-45 minutes"
  
  review_items:
    - question: "Is the hub-spoke structure logical?"
      action: "Approve or adjust linking plan"
      
    - question: "Is schema markup valid?"
      action: "Run through validator"
      
    - question: "Any technical risks?"
      action: "Review redirects, robots.txt changes"
      
  approval_options:
    - "✅ APPROVE → Deploy to production"
    - "🔄 REVISE → Adjust technical plan"
    - "🛑 HOLD → Requires dev review"
```

### Deliverable at Gate:
- Internal linking map
- Schema markup files
- Technical implementation checklist
- **Site changes approved for deployment**

---

# EXAMPLE WORKFLOW: END-TO-END

## Scenario: New Client "TechFlow CRM"

### Day 1: Intake & Audit
```
09:00 - Client provides: Domain, 3 competitors, goals
09:05 - AGENT (M7): Initiates audit workflow
        ├── Firecrawl: Crawls techflow.com
        ├── Ahrefs API: Pulls competitor data
        ├── DataForSEO: Extracts SERP top 10 for "CRM software"
        └── Claude: Analyzes gaps, drafts executive summary
10:30 - AGENT: Audit complete, notifies human
10:45 - HUMAN (Gate 1): Reviews audit
        ├── Confirms competitors are correct ✅
        ├── Adjusts revenue estimate (too aggressive) 🔄
        └── Approves top 3 priorities ✅
11:00 - HUMAN: Clicks "APPROVE" → Triggers Module 1
```

### Day 1-2: Strategy
```
11:05 - AGENT (M1): Generates strategy
        ├── Platform Strategy: "CRM for Growing Sales Teams"
        ├── Topic Clusters: 5 hubs identified
        ├── Avatar: "Sales Manager Sarah"
        └── 90-day calendar skeleton
14:00 - AGENT: Strategy complete, notifies human
15:00 - HUMAN (Gate 2): Reviews strategy
        ├── Adjusts positioning angle slightly 🔄
        ├── Adds 1 missing cluster ✅
        └── Approves avatar ✅
15:30 - HUMAN: Clicks "APPROVE" → Triggers Module 2
```

### Day 2-3: Research
```
15:35 - AGENT (M2): Runs keyword research
        ├── Pulls 500 keywords from Ahrefs
        ├── Filters to 127 BOFU keywords
        ├── Scores by MMA framework
        └── Maps to content types
09:00 - AGENT: Research complete, notifies human
09:30 - HUMAN (Gate 3): Reviews keywords
        ├── Removes 3 brand-risk keywords ❌
        ├── Promotes 2 keywords to priority ✅
        └── Confirms content-type mapping ✅
10:00 - HUMAN: Clicks "APPROVE" → Triggers Module 3 (batch of 5)
```

### Day 3-7: Content Creation (Batch)
```
10:05 - AGENT (M3): Generates 5 WSA drafts in parallel
        ├── Article 1: "TechFlow vs Salesforce"
        ├── Article 2: "Best CRM for Sales Teams"
        ├── Article 3: "CRM Implementation Guide"
        ├── Article 4: "TechFlow vs HubSpot"
        └── Article 5: "CRM ROI Calculator Guide"
        
[Each article: ~2-3 hours to generate]

Day 5 - AGENT: All 5 drafts complete
Day 5-6 - HUMAN (Gate 4): Reviews each article
        ├── Article 1: Approved ✅
        ├── Article 2: Minor revisions 🔄 → Re-run
        ├── Article 3: Approved ✅
        ├── Article 4: Approved ✅
        └── Article 5: Needs fact-check 📝 → Human edit
Day 6 - HUMAN: Clicks "APPROVE ALL" → Triggers Module 4 & 5 in parallel
```

### Day 7-10: Video & Assets (Parallel)
```
MODULE 4 TRACK:
Day 7 - AGENT: Converts Article 1, 2, 3 to video scripts
Day 8 - HUMAN (Gate 5): Reviews scripts
        ├── Script 1: Approved ✅
        ├── Script 2: Hook needs work 🔄
        └── Script 3: Approved ✅
Day 9 - Scripts sent to video production

MODULE 5 TRACK:
Day 7 - AGENT: Creates lead magnet from Article 5 (Calculator)
        ├── Generates PDF guide
        ├── Drafts landing page
        └── Writes 5-email sequence
Day 8 - HUMAN (Gate 6): Reviews assets
        ├── Lead magnet: Add more value 🔄
        ├── Landing page: Approved ✅
        └── Email sequence: Tone adjustment 🔄
Day 9 - Assets finalized
```

### Day 10-12: Site Orchestration
```
Day 10 - AGENT (M6): Generates site structure
        ├── Internal linking map for 5 new articles
        ├── Schema markup (FAQ, Article, Organization)
        ├── Sitemap updates
        └── Orphan page link recommendations
Day 11 - HUMAN (Gate 7): Reviews technical plan
        ├── Linking structure: Approved ✅
        ├── Schema: Validated ✅
        └── Technical risks: None identified ✅
Day 12 - Deploy to production
```

### Day 12: LAUNCH
```
✅ 5 Articles Published
✅ 3 Video Scripts in Production
✅ 1 Lead Magnet Live
✅ Email Sequence Active
✅ Site Structure Updated
✅ Schema Deployed

TOTAL HUMAN TIME: ~8-10 hours
TOTAL ELAPSED: 12 days
WITHOUT AGENTS: 60-80 hours, 4-6 weeks
```

---

# IMPLEMENTATION ARCHITECTURE

## Tech Stack Options

### Option A: n8n + Claude (Self-Hosted)
```
┌─────────────────────────────────────────────────────────────┐
│                      n8n WORKFLOWS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │Firecrawl│    │ Ahrefs  │    │ Claude  │    │Airtable │  │
│  │  MCP    │    │   API   │    │   API   │    │   DB    │  │
│  └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘  │
│       │              │              │              │        │
│       └──────────────┴──────────────┴──────────────┘        │
│                          │                                  │
│                          ▼                                  │
│                   ┌─────────────┐                           │
│                   │   SLACK/    │                           │
│                   │   EMAIL     │◀── Human Notifications    │
│                   │  APPROVAL   │                           │
│                   └─────────────┘                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Option B: Make.com + Abacus AI (Cloud)
```
┌─────────────────────────────────────────────────────────────┐
│                    MAKE.COM SCENARIOS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Scenario 1: Audit Pipeline (M7)                           │
│  Scenario 2: Strategy Pipeline (M1)                        │
│  Scenario 3: Research Pipeline (M2)                        │
│  Scenario 4: Content Pipeline (M3)                         │
│  Scenario 5: Video Pipeline (M4)                           │
│  Scenario 6: Asset Pipeline (M5)                           │
│  Scenario 7: Deploy Pipeline (M6)                          │
│                                                             │
│  Each scenario:                                            │
│  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐        │
│  │Trigger │──▶│Abacus  │──▶│ Store  │──▶│ Notify │        │
│  │(Manual)│   │  AI    │   │(Notion)│   │(Slack) │        │
│  └────────┘   └────────┘   └────────┘   └────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Option C: Claude Code Desktop (Manual Orchestration)
```
┌─────────────────────────────────────────────────────────────┐
│              CLAUDE CODE DESKTOP WORKFLOW                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Human runs each module manually in Claude Code:            │
│                                                             │
│  1. Load Module 7 skill → Run audit → Export to /outputs   │
│  2. Review output → Approve                                 │
│  3. Load Module 1 skill → Run strategy → Export            │
│  4. Review output → Approve                                 │
│  ... etc                                                    │
│                                                             │
│  Pros: No setup, full control                              │
│  Cons: Manual triggering, no automation                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# QUICK START: MINIMUM VIABLE ORCHESTRATION

## Phase 1: Manual with Templates (Week 1)
```yaml
setup:
  - Create Airtable base with 7 tables (one per module)
  - Load module skills into Claude Code Desktop
  - Create Slack channel for approvals
  
workflow:
  - Human triggers each module manually
  - Outputs saved to Airtable
  - Slack notification for review
  - Human approves in Airtable → Next module triggered manually
```

## Phase 2: Semi-Automated (Week 2-3)
```yaml
setup:
  - Create n8n workflows for Modules 7, 2, 3 (highest volume)
  - Integrate Firecrawl + Ahrefs API
  - Add Claude API for analysis/generation
  
workflow:
  - Audit: Automated collection, manual trigger for analysis
  - Research: Automated keyword pull, manual approval
  - Content: Automated brief generation, manual draft approval
```

## Phase 3: Full Orchestration (Month 2)
```yaml
setup:
  - All 7 modules automated
  - Approval dashboard (Notion/custom)
  - Slack notifications with approve/reject buttons
  - Automatic handoff between modules on approval
  
workflow:
  - Client intake triggers full pipeline
  - Human only intervenes at gates
  - System tracks progress and SLAs
```

---

# APPROVAL DASHBOARD CONCEPT

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI GEO ORCHESTRATION DASHBOARD                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CLIENT: TechFlow CRM                                    Status: IN PROGRESS│
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  PIPELINE PROGRESS:                                                         │
│  ┌────────┬────────┬────────┬────────┬────────┬────────┬────────┐          │
│  │   M7   │   M1   │   M2   │   M3   │   M4   │   M5   │   M6   │          │
│  │   ✅   │   ✅   │   ✅   │   🔄   │   ⏳   │   ⏳   │   ⏳   │          │
│  │ DONE   │ DONE   │ DONE   │REVIEW  │WAITING │WAITING │WAITING │          │
│  └────────┴────────┴────────┴────────┴────────┴────────┴────────┘          │
│                                                                             │
│  ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│  GATE 4 AWAITING APPROVAL:                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Article: "TechFlow vs Salesforce: Complete 2026 Comparison"         │   │
│  │                                                                     │   │
│  │ Word Count: 3,847    │ Readability: 8th Grade    │ SEO Score: 94   │   │
│  │                                                                     │   │
│  │ [📄 VIEW DRAFT]  [✅ APPROVE]  [🔄 REQUEST REVISION]  [❌ REJECT]  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  REVISION NOTES (optional):                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ "Strengthen the ROI section with specific numbers"                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│  COMPLETED THIS WEEK:                                                       │
│  • M7 Audit: Approved Jan 20 (Revenue gap: $45k-$120k/mo identified)       │
│  • M1 Strategy: Approved Jan 21 (5 topic clusters defined)                 │
│  • M2 Research: Approved Jan 22 (73 BOFU keywords prioritized)             │
│                                                                             │
│  UPCOMING:                                                                  │
│  • M3: 4 more articles in generation queue                                 │
│  • M4: Scripts pending M3 approval                                         │
│  • M5: Lead magnet pending M3 content                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# NEXT STEPS

## Immediate (This Week)
1. **Choose stack:** n8n vs Make.com vs Manual
2. **Set up Airtable base** with module tables
3. **Test Module 7** workflow end-to-end manually

## Short-Term (Next 2 Weeks)
4. **Automate Module 7** (highest client impact)
5. **Automate Module 2** (highest time savings)
6. **Create approval Slack bot** or Notion dashboard

## Medium-Term (Month 2)
7. **Connect all 7 modules** into single orchestration
8. **Build client intake form** that triggers pipeline
9. **Add SLA tracking** (time per stage)

---

**The goal: Human does strategy, Agent does labor.**

*8,144 lines of skill documentation → Automated execution engine*
