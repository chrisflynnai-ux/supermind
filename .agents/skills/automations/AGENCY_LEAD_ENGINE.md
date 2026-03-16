# AGENCY LEAD ENGINE
## VSL Deconstruction Outreach System

**Mode:** QUICK 🚀  
**Goal:** Generate qualified high-ticket coaching leads with value-first outreach  
**Weapon:** VSL Deconstructor Skill + Manus Research

---

## THE STRATEGY

### Why This Works

1. **Genuine Value First** — You're not pitching, you're helping
2. **Demonstrates Expertise** — The breakdown IS the proof
3. **Personalised at Scale** — Each prospect gets custom analysis
4. **Low Resistance** — "I watched your VSL and noticed..." opens doors
5. **Qualifies Automatically** — Only serious coaches have VSLs worth analyzing

### The Offer

> "I broke down your VSL and found 3 specific spots where you're losing viewers. Here's the analysis — no strings attached. If you want help fixing them, let's talk."

---

## PIPELINE ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────┐
│                     LEAD ENGINE PIPELINE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  STAGE 1: SOURCE          STAGE 2: ENRICH         STAGE 3: ANALYZE  │
│  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐   │
│  │   Manus     │         │  Scrape     │         │    VSL      │   │
│  │  Research   │────────▶│  VSL URLs   │────────▶│Deconstructor│   │
│  │             │         │  + Socials  │         │    Skill    │   │
│  └─────────────┘         └─────────────┘         └─────────────┘   │
│        │                       │                       │            │
│        ▼                       ▼                       ▼            │
│  50 Leads Found          VSL + Contact           Weakness Report    │
│                                                                      │
│  STAGE 4: PERSONALIZE    STAGE 5: OUTREACH       STAGE 6: FOLLOW   │
│  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐   │
│  │  Generate   │         │   Send DM   │         │   Track +   │   │
│  │  Breakdown  │────────▶│  or Email   │────────▶│  Follow Up  │   │
│  │   Report    │         │             │         │             │   │
│  └─────────────┘         └─────────────┘         └─────────────┘   │
│        │                       │                       │            │
│        ▼                       ▼                       ▼            │
│  PDF/Loom Ready          Value Delivered         Meeting Booked    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## STAGE 1: LEAD SOURCING

### Option A: Manus Research (Automated)

**Manus Task Prompt:**
```
Find 50 high-ticket coaching leads with the following criteria:

MUST HAVE:
- Active VSL or webinar funnel (video sales letter on their site)
- Price point $2,000+ (high-ticket)
- Active social presence (Instagram 5K+, YouTube, or LinkedIn)
- English-speaking market

NICHES TO TARGET:
- Business/entrepreneurship coaching
- Sales coaching
- Marketing/agency coaching
- Real estate coaching
- Health/fitness coaching (high-ticket programs)
- Life/executive coaching
- Course creators with VSL funnels

FOR EACH LEAD, PROVIDE:
1. Name
2. Business name
3. Niche
4. Website URL
5. VSL URL (direct link to their video sales letter)
6. Instagram handle
7. Email (if public)
8. Estimated price point
9. Brief notes on their offer

OUTPUT FORMAT: CSV with headers
```

### Option B: Manual Sourcing (Faster Start)

**Where to Find VSL Coaches:**

| Source | Method | Volume |
|--------|--------|--------|
| **YouTube Ads** | Search "[niche] coaching" → watch ads → find VSLs | High |
| **Facebook Ad Library** | Search coaching keywords → find landing pages | High |
| **ClickFunnels Showcase** | Browse successful funnels | Medium |
| **Instagram** | Search #coachingbusiness #highticketcoach | High |
| **LinkedIn** | Search "coach" + filter by connections | Medium |
| **Podcast Guests** | Coaching podcasts → guest coaches | Qualified |
| **Course Platforms** | Kajabi, Teachable showcases | Medium |

**Quick Manual Process:**
1. Open Facebook Ad Library
2. Search: "free training" + "coaching"
3. Click through to landing pages
4. If VSL exists → add to spreadsheet
5. Find their Instagram/email
6. Repeat

---

## STAGE 2: LEAD ENRICHMENT

### Data Points to Capture

```yaml
lead_record:
  # Identity
  name: "John Smith"
  business_name: "Scale Your Agency"
  
  # Contact
  email: "john@scaleagency.com"
  instagram: "@johnsmith_coach"
  linkedin: "linkedin.com/in/johnsmith"
  
  # VSL Data
  vsl_url: "https://scaleagency.com/free-training"
  vsl_length: "45 minutes"
  vsl_platform: "Vimeo"  # YouTube, Wistia, Vimeo, custom
  
  # Business Intel
  niche: "Agency coaching"
  price_point: "$5,000"
  offer_type: "Group coaching + community"
  funnel_type: "Webinar → Call → Close"
  
  # Engagement
  instagram_followers: 12500
  youtube_subscribers: 8200
  recent_post_engagement: "2-3%"
  
  # Notes
  pain_points_visible: "VSL is too long, weak hook, no proof stack"
  outreach_angle: "Hook optimization + testimonial placement"
```

### Enrichment Tools

| Tool | Purpose | Cost |
|------|---------|------|
| **Hunter.io** | Find email from domain | Freemium |
| **Apollo.io** | Email + company data | Freemium |
| **Phantombuster** | Scrape Instagram/LinkedIn | $59/mo |
| **Instantly.ai** | Email verification | Built-in |
| **Manual** | Visit site, check socials | Free |

---

## STAGE 3: VSL ANALYSIS

### VSL Deconstructor Skill Integration

**Input to Skill:**
```yaml
vsl_analysis_request:
  vsl_url: "https://example.com/training"
  prospect_name: "John Smith"
  prospect_niche: "Agency coaching"
  analysis_depth: "full"  # quick | full | comprehensive
  
  focus_areas:
    - hook_effectiveness
    - story_structure
    - proof_stack
    - objection_handling
    - cta_strength
    - pacing_retention
```

**Output from Skill:**
```yaml
vsl_analysis_report:
  prospect: "John Smith"
  vsl_url: "https://example.com/training"
  overall_score: 6.5/10
  
  strengths:
    - "Strong credentials establishment"
    - "Good case study at minute 12"
    - "Clear offer breakdown"
  
  critical_weaknesses:
    - weakness_1:
        issue: "Hook is generic"
        timestamp: "0:00-0:45"
        impact: "High drop-off in first 60 seconds"
        fix: "Lead with specific result + curiosity gap"
    
    - weakness_2:
        issue: "Proof stack too late"
        timestamp: "22:00"
        impact: "Skepticism builds before credibility"
        fix: "Move testimonials to minute 5-7"
    
    - weakness_3:
        issue: "CTA is weak"
        timestamp: "43:00"
        impact: "Low urgency, easy to procrastinate"
        fix: "Add scarcity + clear next step"
  
  quick_wins:
    - "Add pattern interrupt at minute 3"
    - "Insert 2 more proof points before price reveal"
    - "Stronger risk reversal language"
  
  estimated_conversion_lift: "15-25% with fixes"
```

---

## STAGE 4: PERSONALIZED OUTREACH ASSETS

### Option A: Quick Text Breakdown (DM/Email)

**Template:**
```
Subject: Watched your [NICHE] training — found 3 conversion killers

Hey [FIRST_NAME],

I watched your [VSL TITLE] training and noticed a few things 
that might be costing you sales.

Quick breakdown:

🔴 HOOK (0:00-0:45)
Your opening is solid but generic. Starting with 
"[THEIR ACTUAL HOOK]" doesn't create enough curiosity gap.
Leads are deciding to stay or leave in these 45 seconds.

🔴 PROOF TIMING (minute [X])
Your best testimonial is buried at minute [X]. 
By then, skepticism has already built. Moving proof 
earlier typically lifts completion rates 20%+.

🔴 CTA STRENGTH (minute [X])
"[THEIR ACTUAL CTA]" lacks urgency. No reason to 
act today vs. next week.

I put together a more detailed breakdown with specific 
fixes if you want it — no pitch, just the analysis.

Worth a look?

[YOUR NAME]
```

### Option B: Loom Video Breakdown (Higher Touch)

**Loom Script Structure:**
```
[0:00-0:30] INTRO
"Hey [Name], I'm [You]. I watched your [training name] 
and wanted to share some quick observations that could 
help your conversions."

[0:30-2:00] WEAKNESS 1 — THE HOOK
- Screen share their VSL
- Point to specific moment
- Explain the problem
- Suggest the fix

[2:00-3:30] WEAKNESS 2 — PROOF TIMING
- Same structure

[3:30-5:00] WEAKNESS 3 — CTA
- Same structure

[5:00-5:30] CLOSE
"These are quick wins that typically lift conversions 
15-25%. If you want help implementing, happy to chat. 
Either way, hope this helps."
```

**Loom Benefits:**
- Higher response rate (feels personal)
- Shows your expertise visually
- Harder to ignore than text
- Builds trust through face time

### Option C: PDF Report (Premium Feel)

**1-Page PDF Structure:**
```
┌─────────────────────────────────────────────────────┐
│           VSL CONVERSION ANALYSIS                    │
│           [PROSPECT NAME] — [DATE]                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│  OVERALL SCORE: 6.5/10                              │
│  ████████░░░░░░ Potential: 8.5+                     │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  🔴 CRITICAL ISSUE #1: Weak Hook                    │
│  Timestamp: 0:00-0:45                               │
│  Impact: High viewer drop-off                       │
│  Fix: [Specific recommendation]                     │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  🔴 CRITICAL ISSUE #2: Late Proof Stack             │
│  Timestamp: 22:00                                   │
│  Impact: Skepticism before credibility              │
│  Fix: [Specific recommendation]                     │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  🔴 CRITICAL ISSUE #3: Weak CTA                     │
│  Timestamp: 43:00                                   │
│  Impact: Low urgency                                │
│  Fix: [Specific recommendation]                     │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  ESTIMATED LIFT: 15-25% conversion improvement      │
│                                                      │
│  Want help implementing? [CALENDAR LINK]            │
│                                                      │
│  Prepared by: [YOUR NAME] | [YOUR COMPANY]          │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## STAGE 5: OUTREACH EXECUTION

### Channel Selection

| Channel | Best For | Response Rate | Effort |
|---------|----------|---------------|--------|
| **Instagram DM** | Coaches with active IG | 15-25% | Low |
| **LinkedIn DM** | B2B coaches, consultants | 10-20% | Medium |
| **Email** | Anyone with public email | 5-15% | Low |
| **Loom + Email** | High-value targets | 20-35% | High |
| **Video Reply** | IG/LinkedIn posts | 25-40% | Medium |

### Outreach Sequence

**Day 1: Initial Value Drop**
```
[Platform: Instagram DM]

Hey [Name] — watched your [training name].

Quick observation: your hook at 0:00-0:45 is costing you 
viewers. "[Their actual opening line]" doesn't create 
enough curiosity to keep people watching.

I broke down 3 specific fixes that could lift your 
conversions. Want me to send it over?

No pitch — just the analysis.
```

**Day 3: Follow-up (if no response)**
```
Bumping this ^ 

The proof timing issue alone (moving testimonials earlier) 
typically lifts completion rates 15-20%.

Happy to share the breakdown if useful.
```

**Day 7: Final Touch**
```
Last one — 

I recorded a quick Loom walking through your VSL 
with timestamps. [LOOM LINK]

Hope it helps either way. 🤙
```

### Volume Targets

| Metric | Daily | Weekly | Monthly |
|--------|-------|--------|---------|
| Leads sourced | 10 | 50 | 200 |
| VSLs analyzed | 5 | 25 | 100 |
| Outreach sent | 10 | 50 | 200 |
| Responses | 2-3 | 10-15 | 40-60 |
| Calls booked | 1 | 5-7 | 20-28 |
| Closed deals | - | 1-2 | 4-8 |

---

## STAGE 6: TRACKING & FOLLOW-UP

### Simple Tracking Sheet

```
| Lead | Niche | VSL Analyzed | Outreach Date | Channel | Response | Call Booked | Status |
|------|-------|--------------|---------------|---------|----------|-------------|--------|
| John Smith | Agency | ✅ | 2026-01-15 | IG DM | ✅ Interested | ✅ 1/20 | Qualified |
| Jane Doe | Fitness | ✅ | 2026-01-15 | Email | Pending | - | Outreach |
| Bob Wilson | Sales | ✅ | 2026-01-14 | LinkedIn | ❌ No response | - | Follow-up |
```

### Status Pipeline

```
SOURCED → ANALYZED → OUTREACH → RESPONDED → CALL BOOKED → QUALIFIED → CLOSED
   │          │          │          │            │            │          │
   50        25         25         8            5            3          1
```

---

## LEAN SKILL: VSL LEAD ANALYZER

### Skill Definition (Add to Your Stack)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<skill id="vsl_lead_analyzer" version="1.0.0">
  <metadata>
    <n>VSL Lead Analyzer</n>
    <description>Analyze prospect VSLs and generate personalized outreach</description>
    <category>sales</category>
    <load_cost>medium</load_cost>
  </metadata>
  
  <dependencies>
    <npm>puppeteer</npm>
    <npm>openai</npm>
    <pip>whisper</pip>
  </dependencies>
  
  <capabilities>
    <capability id="extract_vsl">
      <trigger>get VSL transcript from URL</trigger>
      <accepts>url</accepts>
      <returns>transcript + timestamps</returns>
    </capability>
    <capability id="analyze_vsl">
      <trigger>analyze VSL for weaknesses</trigger>
      <accepts>transcript, context</accepts>
      <returns>weakness report</returns>
    </capability>
    <capability id="generate_outreach">
      <trigger>create personalized outreach</trigger>
      <accepts>analysis, prospect_info, channel</accepts>
      <returns>outreach message</returns>
    </capability>
    <capability id="generate_report">
      <trigger>create PDF breakdown report</trigger>
      <accepts>analysis, prospect_info</accepts>
      <returns>PDF file</returns>
    </capability>
  </capabilities>
  
  <scripts>
    <script lang="javascript" capability="extract_vsl">
      <![CDATA[
const puppeteer = require('puppeteer');

async function extractVSL(url) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto(url, { waitUntil: 'networkidle2' });
  
  // Find video element
  const videoSrc = await page.evaluate(() => {
    const video = document.querySelector('video');
    const iframe = document.querySelector('iframe[src*="youtube"], iframe[src*="vimeo"], iframe[src*="wistia"]');
    
    if (video) return video.src;
    if (iframe) return iframe.src;
    return null;
  });
  
  await browser.close();
  
  // Return video source for transcription
  return { videoSrc, pageUrl: url };
}

module.exports = { extractVSL };
      ]]>
    </script>
    
    <script lang="python" capability="analyze_vsl">
      <![CDATA[
from openai import OpenAI
import json

def analyze_vsl(transcript: str, prospect_context: dict) -> dict:
    client = OpenAI()
    
    analysis_prompt = f"""
    Analyze this VSL transcript for a {prospect_context.get('niche', 'coaching')} business.
    
    TRANSCRIPT:
    {transcript}
    
    Provide analysis in this exact JSON format:
    {{
        "overall_score": 7.5,
        "strengths": ["strength 1", "strength 2"],
        "critical_weaknesses": [
            {{
                "issue": "description",
                "timestamp": "estimated time",
                "impact": "high/medium/low",
                "fix": "specific recommendation"
            }}
        ],
        "quick_wins": ["win 1", "win 2", "win 3"],
        "estimated_lift": "15-25%"
    }}
    
    Focus on:
    1. Hook effectiveness (first 60 seconds)
    2. Proof/testimonial timing
    3. Story structure
    4. Objection handling
    5. CTA strength and urgency
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": analysis_prompt}],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)
      ]]>
    </script>
    
    <script lang="python" capability="generate_outreach">
      <![CDATA[
def generate_outreach(analysis: dict, prospect: dict, channel: str) -> str:
    
    weakness = analysis['critical_weaknesses'][0]
    
    templates = {
        "instagram_dm": f"""Hey {prospect['first_name']} — watched your {prospect.get('vsl_title', 'training')}.

Quick observation: {weakness['issue']}

This is likely costing you viewers/sales. I broke down 3 specific fixes.

Want me to send the full analysis? No pitch — just the breakdown.""",
        
        "email": f"""Subject: Watched your {prospect.get('niche', '')} training — found 3 conversion killers

Hey {prospect['first_name']},

I watched your {prospect.get('vsl_title', 'training')} and noticed a few things that might be costing you sales.

🔴 Issue #1: {weakness['issue']}
Impact: {weakness['impact']}
Fix: {weakness['fix']}

I have 2 more specific fixes if you want the full breakdown.

Worth a look?

{prospect.get('sender_name', '')}""",
        
        "linkedin": f"""Hi {prospect['first_name']},

I came across your {prospect.get('niche', '')} training and noticed something that could be hurting conversions.

{weakness['issue']} — this typically causes {weakness['impact']} impact.

I put together a quick breakdown with fixes. Happy to share if useful.

No pitch — just observations from someone who's analyzed 100+ VSLs."""
    }
    
    return templates.get(channel, templates['email'])
      ]]>
    </script>
  </scripts>
</skill>
```

---

## QUICK START: DO THIS TODAY

### Hour 1: Source 10 Leads
1. Open Facebook Ad Library
2. Search: "free training coaching"
3. Find 10 coaches with VSLs
4. Add to spreadsheet: Name, Website, VSL URL, Instagram

### Hour 2: Analyze 5 VSLs
1. Watch each VSL (1.5x speed)
2. Note: Hook, proof timing, CTA
3. Identify 2-3 weaknesses each
4. Write quick analysis

### Hour 3: Send 5 Outreach Messages
1. Craft personalized DM for each
2. Send via Instagram or email
3. Log in tracking sheet

### Repeat Daily
- 10 leads sourced
- 5 analyzed
- 5 outreach sent
- Expected: 1-2 responses/day → 1-2 calls/week → 1-2 clients/month

---

## REVENUE MATH

| Metric | Conservative | Moderate | Aggressive |
|--------|--------------|----------|------------|
| Monthly outreach | 100 | 200 | 400 |
| Response rate | 10% | 15% | 20% |
| Responses | 10 | 30 | 80 |
| Call rate | 50% | 50% | 50% |
| Calls | 5 | 15 | 40 |
| Close rate | 20% | 25% | 30% |
| Clients | 1 | 4 | 12 |
| Avg deal | $2,000 | $3,000 | $5,000 |
| **Monthly revenue** | **$2,000** | **$12,000** | **$60,000** |

---

## UPGRADE PATH

### Level 1: Manual (Now)
- You source, analyze, outreach manually
- Use VSL Deconstructor skill for analysis
- Track in spreadsheet

### Level 2: Semi-Automated (Week 2-4)
- Manus sources leads automatically
- You analyze and personalize
- Outreach templates speed up sending

### Level 3: Full Pipeline (Month 2+)
- Manus sources → Auto-enrichment
- VSL Skill analyzes → Auto-generates report
- You review and send personalized Looms
- Victoria AI handles follow-up sequences

---

*Agency Lead Engine — VSL Deconstruction Outreach System*  
*Value First. Expertise Demonstrated. Deals Closed.*
