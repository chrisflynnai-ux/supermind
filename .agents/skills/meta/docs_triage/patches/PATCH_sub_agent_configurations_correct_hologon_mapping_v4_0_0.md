# PATCH_sub_agent_configurations_correct_hologon_mapping_v4_0_0

## File Summary Report
- Target: `C:/Users/cfar7/OneDrive/Desktop/ULTRAMIND/SUPERMIND ACCESS DOCS/SUB_AGENT_CONFIGURATIONS_v2_0_0.yaml`
- Current strength: rich sub-agent inventory, good operational prompts, useful skill role mapping
- Current issue: Neuro-Box/Hologon mapping is partially inverted in the 7S explanations
- Keep level: repairable strategic config source
- Apply now: no

## Repair Intent
Correct the side-to-neurochemical and 7S label mappings so later agent prompts do not inherit false doctrine.

## Required Changes
- preserve `SAFE -> BODY -> Dopamine`
- preserve `SPECIAL -> HEART -> GABA`
- preserve `SMART -> MIND -> Acetylcholine`
- preserve `SIGNIFICANCE -> SPIRIT -> Serotonin`
- correct `SUPERIOR -> PSYCH -> Adrenaline`
- correct `SUPPORTED -> CONSCIENCE -> Oxytocin`
- keep `SOUL` center and `STEAL`/`SALVATION` framing separate from the six outer sides
- patch any older P1/P2/P3 framing where it conflicts with the current 4-track model

---

## Patch Applied Summary
- Applied: 2026-03-07
- Applied by: Claude (agent)
- Status: ready_for_claude → **applied**

### Hologon Mapping Corrections (Critical)
1. **SUPPORTED/SUPERIOR swap fixed** — was `SUPPORTED (PSYCHE/Adrenaline)` + `SUPERIOR (CONSCIENCE/Oxytocin)`, corrected to:
   - `SUPPORTED (CONSCIENCE/Oxytocin): "Can I act now?"`
   - `SUPERIOR (PSYCH/Adrenaline): "Do I belong here?"`
2. **PSYCHE → PSYCH normalized** in 2 locations (Strategic Copy Director Neuro-Box reference, global phase/track dimensions label)

### 4-Track Alignment Corrections
3. **Global config renamed** from `phases` (P1/P2/P3) to `tracks` (T1/T2/T3/T4)
4. **Added T1_research** track definition (discovery, no MMA gate)
5. **Renamed P1_draft → T2_draft**, P2_production → T3_production, P3_polish → T4_polish
6. **Fixed T2 draft MMA threshold** from 7.0 to 6.0 (canonical: T2>=6.0)
7. **Updated all `phase:` references** in agent definitions: P1→T2, P2→T3, P3→T4 (20+ occurrences)
8. **Updated ZPWO system prompt** from "3-phase workflow" to "4-track workflow" with T1-T4 definitions
9. **Updated OrchestrationResult schema** from `Literal['P1','P2','P3']` to `Literal['T1','T2','T3','T4']`
10. **Updated phase_commands** section to `track_commands` with `/research` added

### Skill Reference Updates
11. **ZPWO skill_ref** updated from `zpwo_v1.0.0.xml` to `zpwo_v4_0_0.xml`
12. **MMA skill_ref** updated from `mma_master_monitor_agent_v1.0.0.xml` to `meta_mma_v4_0_0.xml`
13. **MMA agent skill lists** (3 occurrences) updated from legacy to canonical V4 ID

### What Was Preserved
- Complete named-agent inventory (all pod definitions, system prompts, skill references)
- 7D scoring system with weights and thresholds
- 7S/7F chain coverage checks and asset-type requirements
- MMA routing rules and circuit breaker settings
- All LangGraph workflow definitions
- CopilotKit/AG-UI integration hooks
- Pydantic AI schemas
- Context management rules
- Style layer priority tiers (P1-P4 are priority labels, not workflow phases)
- Version history entries (historical, kept as-is)
- Purchase Driver Sequence (already canonical)
- SAFE/BODY/Dopamine, SPECIAL/HEART/GABA, SMART/MIND/Acetylcholine, SIGNIFICANCE/SPIRIT/Serotonin (all confirmed correct, no changes needed)

### Unresolved
- None. All required changes from patch file applied.

### Second Patch Needed
- No for Hologon mapping — all 6 sides + center now canonical.
- **Optional**: Individual agent skill_refs still reference legacy v2.0.0/v2.1.0 filenames (e.g., `advertorial_copy_master_v2.0.0.xml`). These should be updated as those skills are migrated to V1.4 canonical IDs in later batches.
