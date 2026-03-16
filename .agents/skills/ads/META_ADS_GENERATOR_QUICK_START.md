# Meta Ads Generator v1.0.0 — Quick Start Guide

**Status:** ✅ Production-Ready
**Location:** `.claude/skills/meta/meta_ads_generator_v1.0.0.xml`
**Date:** 2026-01-19

---

## WHAT IS THIS?

The **Meta Ads Generator** (aka "The Andromeda Architect") is your production skill for building high-performing Facebook/Instagram ad campaigns using the creative-as-targeting philosophy.

**Core Paradigm:** Creative IS targeting. Andromeda (Meta's AI) matches users to creatives based on content, not demographics.

---

## WHEN TO USE

Trigger this skill when:
- Building Meta (Facebook/Instagram) ad campaigns
- Need campaign architecture (Prospecting/Retargeting/Retention)
- Creative testing frameworks (3:2:2, 5x5)
- Troubleshooting Meta ad performance
- Scaling Meta ads profitably

---

## CORE FRAMEWORKS INCLUDED

### 1. M3 Swim Lanes (Always Use)
- **Prospecting** (60-70% budget): Broad targeting, creative self-selects
- **Retargeting** (20-30% budget): Site visitors, video viewers, engagers
- **Retention** (5-10% budget): Past customers, win-back/upsell

### 2. Testing Frameworks
- **3:2:2** (Low variance): 3 creatives × 2 texts × 2 headlines - for new campaigns or limited resources
- **5x5** (High variance): 5 creatives × 5 texts × 5 headlines - for scaling ($20k+/month)

### 3. Creative Formats
- **Lazy Static Headlines**: Authentic images + text overlays (highest ROI per hour)
- **Founder-Led VSL**: 60-90sec video (Hook → Promise → Proof → Pivot → CTA)
- **Hero vs Villain Story**: Narrative hook structure
- **Scam Hook Formula**: Contrarian hooks calling out industry lies

### 4. Production Systems
- **Creative Flywheel**: Rule of 1:10k - ship 1 new creative per $10k monthly spend
- **Visual Hook Architecture**: 80% of time on first 3 seconds
- **Nano Banana AI Static Machine**: AI-accelerated scaling of winners

---

## KEY METRICS

### Primary
- **ncROAS** (New Customer ROAS): Incremental revenue only - use for scale decisions
- **Hook Rate** (3-sec): % who stop scrolling (target >30%)
- **Hold Rate** (15-sec+): % who stay engaged (target >50%)
- **CPA**: Cost per acquisition (front-end profitability)
- **MER**: Marketing Efficiency Ratio (total rev / total ad spend)

### Creative Fatigue Signals
- Hook Rate drops 30%+ from baseline
- Frequency >3.5
- CPA increases 40%+ from baseline

---

## 12 CANONICAL FRAMEWORKS

1. **3:2:2 Flexible Ad System** - Low-variance testing for stable campaigns
2. **M3 Swim Lane Architecture** - Campaign structure (Prospecting/Retargeting/Retention)
3. **5x5 Testing Matrix** - High-variance testing for scaling accounts
4. **Founder-Led VSL Framework** - Short video for authority + trust
5. **Hero vs. Villain Story** - Narrative hook structure
6. **Lazy Static Headlines** - Ugly/authentic statics with text overlays
7. **Scam Hook Formula** - Contrarian hooks calling out false beliefs
8. **3-Step Viral Hook** - Pattern for first 3 seconds (Visual + Text + Audio)
9. **Nano Banana AI Static Machine** - AI-accelerated static creation
10. **Post ID Harvesting** - Preserve social proof when duplicating winners
11. **Lead Gen Lag-Time Optimization** - Optimize for backend conversion, not just lead capture
12. **Visual Hook Audit** - Diagnostic framework for low Hook Rate creatives

---

## 7 ANTI-PATTERNS (AVOID THESE)

1. **Variable Testing**: Testing color swaps instead of distinct concepts
2. **Frequent Pausing**: Pausing ads daily (resets learning phase)
3. **Front-End Obsession**: Ignoring backend LTV and ncROAS
4. **Avatar Sprawl**: Creating separate campaigns for minor demographic differences
5. **Retargeting Crutch**: Only profitable through retargeting, prospecting bleeds money
6. **Creative Starvation**: Running same creatives 30+ days without fresh concepts
7. **Over-Segmentation**: Dozens of narrow ad sets fighting Andromeda

---

## 15 FAILURE MODES WITH RECOVERY

Each failure mode includes:
- **Symptoms**: How to detect
- **Root Cause**: Why it happens
- **Diagnosis Steps**: How to confirm
- **Recovery**: Step-by-step fix
- **Prevention**: How to avoid

### Critical Ones to Know:
1. **Creative Fatigue**: Hook Rate drops 30%+, frequency >3.5 → Ship replacement concept within 24h
2. **Attribution Hallucination**: Platform ROAS looks great but MER flat → Use ncROAS for decisions
3. **Learning Limited Loop**: <50 conversions/week → Consolidate campaigns or increase budget
4. **Hook-Body Mismatch**: High Hook Rate but low conversion → Hook attracts wrong audience
5. **Pixel Malnutrition**: No conversions tracked despite sales → Fix pixel + Conversion API

---

## PYTHON VALIDATION TOOLS

### 1. `validate_campaign_structure`
- Validates M3 swim lane separation
- Checks audience exclusions (Prospecting excludes Retargeting/Retention)
- **Use:** Before launching campaigns

### 2. `validate_creative_concept_diversity`
- Detects variation testing vs concept testing
- Ensures concepts are distinct, not duplicates
- **Use:** Before launching creative tests

### 3. `calculate_ncROAS`
- Calculates new customer ROAS (incremental revenue)
- Compares to blended ROAS to identify attribution inflation
- **Use:** Weekly reporting, scale decisions

### 4. `detect_creative_fatigue`
- Analyzes Hook Rate decline, frequency, CPA increase
- Flags fatigued creatives
- **Use:** Weekly creative performance review

---

## 3 GOLDEN RUNS (TEST SCENARIOS)

### GR1: Ecom Beauty DTC
- $47 anti-aging serum, $15k/month budget, 3.0x ncROAS target
- M3 swim lanes + 3:2:2 testing + Founder VSL + Lazy Static
- Expected outputs: Campaign blueprint, creative matrix, fatigue detection protocol

### GR2: Lead Gen Local Service
- HVAC company, $5k/month budget, <$50 cost per qualified lead
- M3 lanes + Lazy Static + Scam Hook + Lead Gen Lag-Time Optimization
- Expected outputs: Geographic targeting, backend conversion optimization

### GR3: Webinar/Info Product
- $1,997 course, $25k/month budget, <$30 cost per registration
- 5x5 testing + Founder VSL + Hero vs Villain
- Expected outputs: 5x5 matrix, webinar-to-sale tracking, scaling protocol

---

## WORKFLOW RECIPES (MULTI-SKILL)

### Recipe 1: Cold Traffic to Sale
**When:** Cold Meta traffic for complex offers requiring education
**Skills:** meta_ads_generator → advertorial_copy_master → sales_page_copywriter_lite
**Optional:** market_intelligence_synthesizer (for ICP research upfront)

### Recipe 2: Webinar Funnel Launch
**When:** High-ticket offers ($997+) using webinar sales model
**Skills:** meta_ads_generator → vsl_script_writer_long_form → sales_page_copywriter_lite
**Optional:** email_campaign_copy_genius (webinar reminder sequence)

### Recipe 3: Lead Gen Service Business
**When:** Local service or B2B lead gen requiring qualification
**Skills:** meta_ads_generator → quick_info_product_builder_lite → email_campaign_copy_genius
**Optional:** sales_page_deconstructor (analyze competitor pages)

---

## REQUIRED SSOT INPUTS

### Required:
- `PROJECT_BRIEF`: Campaign goal, budget, target ncROAS, traffic type, funnel stage
- `OFFER_PACKAGE`: Product, price, value proposition, target avatar
- `MESSAGE_SPINE`: Promise, mechanism, proof pillars, objections

### Optional (Recommended):
- `ACCOUNT_CONTEXT`: Pixel history, existing campaigns, MER baseline, creative archive
- `CREATIVE_ARCHIVE`: Past winners, creative fatigue timeline, hook/body performance
- `EVIDENCE_PACK`: Claims grounding, testimonials, results data
- `VOICE_GUIDE`: Brand tone, taboos, personality

---

## QUALITY GATES (MMA)

### Critical (≥9.0):
- **tracking_integrity**: Pixel verified, Conversion API configured, test purchase complete
- **ethical_compliance_safety**: Meta policy compliant, no prohibited content, claims disclaimed

### High (≥8.0):
- **strategy_fit**: M3 architecture, creative strategy matches awareness level
- **creative_resonance**: Hook Rate >30%, concept diversity validated
- **budget_logic**: Learning phase minimums met (50 conv/week), safe scaling increments

---

## TEMPLATES INCLUDED

### 1. Campaign Blueprint Template
- Complete campaign structure with M3 swim lanes
- Budget allocation, creative production schedule
- Quality gates checklist, contingency plans

### 2. Creative QA Checklist
- Visual hook validation (first 3 seconds)
- Hook quality, body/story, CTA, compliance
- Technical specs (mobile-first, captions, file size)
- Concept diversity verification

### 3. Launch Day QA Checklist
- Pre-launch verification (pixel, conversions, exclusions)
- 24-hour monitoring (delivery, tracking, compliance)
- 7-day progress check (learning phase, Hook Rate, CPA)
- Ongoing monitoring schedule

---

## QUICKSTART WORKFLOW

### Step 1: Load Skill
```bash
# Trigger Meta Ads Generator skill
/meta-ads
```

### Step 2: Provide SSOT Inputs
- PROJECT_BRIEF with campaign goal, budget, target metrics
- OFFER_PACKAGE with product details
- MESSAGE_SPINE with promise, mechanism, proof

### Step 3: Choose Framework
- **New campaign or limited resources?** → Use 3:2:2 framework
- **Scaling $20k+/month?** → Use 5x5 framework
- **Local service or B2B?** → Use Lead Gen Lag-Time Optimization

### Step 4: Build Campaign Blueprint
- Skill generates M3 swim lane structure
- Creative testing matrix (3:2:2 or 5x5)
- Creative production schedule (Rule of 1:10k)
- Launch day QA checklist

### Step 5: Validate
- Run `validate_campaign_structure` (M3 lanes + exclusions)
- Run `validate_creative_concept_diversity` (concepts not variations)
- Use Creative QA Checklist before uploading

### Step 6: Launch & Monitor
- Complete Launch Day QA Checklist
- Monitor Hook Rate daily (target >30%)
- Run `detect_creative_fatigue` weekly
- Calculate `ncROAS` weekly for scale decisions

---

## WHEN IN DOUBT

1. **Consolidate** campaigns (fewer is better - more data per campaign)
2. **Test concepts** not variations (different stories, not color swaps)
3. **Let learning phase complete** (50 conversions minimum before judging)
4. **Ship creative weekly** (Rule of 1:10k - 1 new creative per $10k/month spend)

---

## SISTER SKILLS

- **strategic_copy_director_v2.0.0** (upstream: MESSAGE_SPINE creation)
- **market_intelligence_synthesizer_v2.1** (upstream: ICP research)
- **advertorial_copy_master_v2.1** (downstream: cold traffic pre-sell)
- **sales_page_copywriter_lite_v2.1** (downstream: conversion pages)
- **vsl_script_writer_long_form_v2.0** (downstream: video sales letters)
- **email_campaign_copy_genius_v2.0** (downstream: nurture sequences)

---

## PROGRESSIVE DISCLOSURE

- **L1 (≤600 tokens)**: Quick reference - paradigm, default skeleton, creative stack, primary metrics
- **L2 (≤4000 tokens)**: Core mechanisms (5), canonical frameworks (12), decision heuristics (25-50)
- **L3 (≤3000 tokens)**: Anti-patterns (7), failure modes (15), advanced systems, tooling
- **L4 (≤2000 tokens)**: Templates (campaign blueprint, creative QA, launch day QA, naming conventions)

**Default Load:** L1 always, L2 when executing, L3 when complexity high, L4 when generating deliverables

---

## NEXT STEPS

1. **Test Run:** Use Golden Run GR1 (Ecom Beauty DTC) to validate skill behavior
2. **Integrate:** Add to ZPWO routing for Meta ads requests
3. **Enhance:** Collect real campaign data, add to CREATIVE_ARCHIVE for pattern learning
4. **Scale:** Use with Recipe workflows for full funnel builds

---

**Version:** 1.0.0
**Tier:** Production
**Status:** Active
**Model:** Sonnet 4.5

*This skill is the critical growth engine for the ULTRAMIND Ads system.*
