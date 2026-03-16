# OVERVIEW — Ultramind Intake “Synthesizers Track” (3–4 Stages)

Below is the cleanest way to describe the **intake + synthesis pipeline** you’ve been evolving, in a way that matches your **SSOT + Locked Objects + Draft/Master doctrine**.

---

## OPTION A (Recommended): 4-Stage Intake Track (Before the 3 Production Tracks)

### STAGE 0 — INTAKE NORMALIZER (Raw ? Structured)
**Goal:** Take the messy “research bundle” and normalize it into a consistent object model.

**Inputs (raw bundle):**
- Avatar notes, reviews, competitor swipes, transcripts, briefs, COB docs, proof PDFs/screenshots

**Outputs:**
- `INTAKE_INDEX.json` (what exists, where it lives, what’s missing)
- `SOURCE_MAP` (URLs/files grouped + tagged)
- `UNKNOWN_LIST` (explicit gaps to prevent hallucination)

**Orchestrator:** Intake MOD (lightweight)

---

### STAGE 1 — SSOT GENERATORS (Ground truth objects)
**Goal:** Convert intake into your canonical SSOTs.

**Outputs (Locked Objects):**
- `PROJECT_BRIEF_v2`
- `AVATAR_BUNDLE_v1` (or folded into PB if you prefer)
- `CHANGE_OF_BELIEFS_v1`
- `EVIDENCE_PACK_v1` (grounded references, not “claims”)
- `VOICE_GUIDE_v2` (if available)

**Rule:** Stage 1 creates SSOTs. Stage 2+ may *consume* but not mutate.

**Orchestrator:** Stage-A MOD + “SSOT Builder” skill(s)

---

### STAGE 2 — SYNTHESIS SPINES (Strategy objects)
**Goal:** Distill SSOTs into “what must remain true” throughout all assets.

**Outputs (Locked Objects):**
- `MESSAGE_SPINE_v2.1` (promise, mechanism, proof pillars, objections, CTA)
- Optional: `VISUAL_SPINE_v1` (layout pacing + vibe + hierarchy cues)
- Optional: `OFFER_LADDER_v1` (Core/Premium/VIP differentiation rules)

**Orchestrator:** Strategy MOD (Offer Architect primary)

---

### STAGE 3 — PRODUCTION HANDOFF PACK (Make it runnable)
**Goal:** Produce the exact “execution contract” downstream skills need.

**Outputs:**
- `PRODUCTION_BRIEF_v1` (one page: what to write, what not to write, proof refs, CTA rules)
- `TASK_GRAPH_v1` (who writes what, in what order, with what dependencies)
- `QUALITY_GATES_v1` (MMA scoring expectations + hard fails)

**Orchestrator:** Production MOD (routes to Sales Page / Email / VSL / etc.)

---

## OPTION B: 3-Stage Intake Track (Compressed)
1) **SSOT Build** (PB + EP + VG + Avatar/COB)
2) **Spines Build** (Message/Visual/Offer spines)
3) **Handoff Pack** (Production brief + task graph)

(Works fine if you want less “ceremony,” but Stage 0 is very useful once memory/tools are live.)

---

# Your 3-Track Workflow (After Intake)

Once Intake is done, your system becomes three coordinated tracks (each with an orchestrator):

## Track 1 — Drafts & Ideas (Exploration)
**Purpose:** Hooks, angles, story frames, rough layouts, variants  
**Agents:** Market Intel Synth, Offer Architect, Draft Copy agents  
**Output:** Draft variants + hook bank + angle bank (non-final)

## Track 2 — Production & Refine (Build)
**Purpose:** Produce full assets against locked spines  
**Agents:** Sales Page Copywriter, Email Genius, SCD, Image Planner  
**Output:** Full V1 assets (complete but not “perfect”)

## Track 3 — Polish & Perfect (Resonance + QA + Self-Healing)
**Purpose:** MMA scorecard, Human Persuasion Editor, proof discipline, voice lock  
**Agents:** MMA, HPE (“Velvet Hammer”), Neuro-Resonance Auditor, Patch system  
**Output:** Release candidate + correction log + proposed patches

---

# STATUS REVIEW — Where You Are Now (Based on Your Handoff)

## ? Strong Wins (Foundation is real now)
- **Skill Builder v1.2.0** is a legit “meta-factory” (SSOT + PD + MOD/MMA + FMs + Golden Runs).
- **Master Writing Partner v2.0** is production-grade and already conforms to your operating system patterns.
- SSOT templates (EP/MS/PB/VG) are already unified and embedded in L4 (huge unlock).

## ?? Current Gaps (Highest leverage next)
1) **PCG Blocks 3–4** unfinished  
   - You’re missing the “delivery/retention + conscience/constitution” knowledge blocks that make the product system “complete.”
2) **Post-launch loop** is not formalized  
   - You have creation + QA. You still need “metrics ? interpretation ? patch suggestion ? propagation.”
3) **Red Team / Market Skeptic** is still missing  
   - MMA checks quality; it doesn’t *attack the offer* like a hostile buyer.

---

# FEEDBACK — Memory + Python + Pydantic + Convex (Best-Practice Path)

You’re heading the right direction. The key is to treat memory as **state objects** (not chat history).

## 1) Make Convex the SSOT State Store (Not a dumping ground)
Store ONLY canonical objects and logs:
- `ProjectState` (current versions + pointers)
- `LockedObjects` (PB/MS/EP/VG + hashes)
- `DraftArtifacts` (versioned outputs)
- `MMAReports` (scored + verdict)
- `CorrectionLogs` (diff summaries)
- `PatchProposals` (skill_id, issue, patch text, confidence)

## 2) Use Pydantic as the “Schema Court”
Every tool call should validate input/output:
- Reject malformed SSOT objects early
- Force explicit `UNKNOWN` fields instead of silent guessing
- Enforce “Locked Object” immutability by schema + hash checks

## 3) Add 3 Python Tools Immediately (High ROI)
- **diff_locked_objects(a,b)** ? emits “what changed” cleanly  
- **token_accountant(context_map)** ? triggers garbage-collection / summarization routines  
- **patch_proposer(mma_reports, correction_logs)** ? drafts patch snippets for SKILL_UPGRADER

(These tools are what make self-healing *real* vs aspirational.)

## 4) Garbage Collection Protocol (Prevents token bankruptcy)
Each major step writes:
- `SESSION_STATE.md` (ultra short)
- `STATE_POINTERS.json` (Convex IDs + versions)
Then the orchestrator can “reload the world” without carrying long context.

## 5) Circuit Breaker (Prevents validation loop of death)
Hard rule:
- If the same issue fails 3 times ? freeze scope ? produce “Minimal Viable Ecosystem” ? human override required.

---

# What I’d Do Next (If I were running the system)

## Immediate (highest leverage)
1) Build a **Stage 0 Intake Normalizer** (tiny but critical)  
2) Build **Market Skeptic / Red Team** skill (attacks Message Spine before copy exists)  
3) Finish **PCG Blocks 3–4** (because delivery + conscience completes your product OS)

## Near-term
4) Add **Data Interpreter** skill (post-launch metrics ? strategy pivots)  
5) Formalize **Patch Ritual** as an actual tool-driven pipeline:
   MMA_REPORT + CORRECTION_LOG ? PATCH_PROPOSAL ? version bump ? registry update

---

# The One-Sentence Summary
You’ve crossed the line from “prompt library” to an actual operating system:
Now the next evolution is **state + schema + tool-driven recursion** so the system can learn without you manually rewriting skills every time.
