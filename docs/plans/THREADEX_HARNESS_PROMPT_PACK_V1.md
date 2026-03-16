# Threadex & Harness NotebookLM Prompt Pack V1

Date: 2026-03-11
Use this to run NotebookLM sessions for Threadex memory and harness design enhancement.

---

## Notebook 1: Threadex Memory Architecture

### Source Loading Order

Load into NotebookLM in this order:

1. **`docs/plans/2026-03-11-threadex-memory-architecture-design.md`** — The Threadex design being validated
2. **`.agents/skills/automations/automations_master_architect_v4_0_0.xml`** — MAA v4.0.0 (memory seams, contracts, doctrine)
3. **os-eco/Mulch reference** — BM25 + JSONL append-only expertise management (https://github.com/jayminwest/mulch)
4. **M5 Implementation Appendix** — Voice agent memory patterns (from `CURRENT ACTIVE BUILDS/MAA 5 and 6 Modules/`)
5. **M6 architecture docs** — Conversation state + learning optimization (from same folder)

Optional additions for deeper coverage:
- Cognee documentation (if available)
- MemO documentation (if available)
- DuckDB+vss examples
- ZPWO v4.0 skill

### Run Sequence

Run the 6 query clusters from `NOTEBOOKLM_THREADEX_MEMORY_QUERY_PACK_V1.md` in this order:

| Pass | Clusters | Focus | Why This Order |
|------|----------|-------|----------------|
| 1 | A + C | Storage model + Organization | Foundation architecture — validates the bones |
| 2 | B + E | SIMS lifecycle + Production memory | Lifecycle flows — validates how data moves |
| 3 | D + F | Search layer + Cross-harness | Integration points — validates interfaces |

**After each pass:** Copy NotebookLM outputs to a .docx file for import into Claude Code.
Name: `Notebook LM Query Threadex [Pass Number].docx`

---

## Notebook 2: Harness Systems Design

### Source Loading Order

Load into NotebookLM in this order:

1. **`docs/plans/2026-03-11-threadex-memory-architecture-design.md`** — Memory layer the harness must integrate with
2. **`.agents/skills/automations/automations_master_architect_v4_0_0.xml`** — MAA v4.0.0 (ACP seam, contracts, routing)
3. **ZPWO v4.0 skill** — Orchestration doctrine (`.agents/skills/meta/` or `.claude/skills/meta/`)
4. **AGENTS.md v4.0** — Current agent routing table
5. **M7 CONDUCTOR spec** — Voice agent orchestration (from `CURRENT ACTIVE BUILDS/`)

Optional additions:
- OpenClaw / NanoClaw documentation
- os-eco/Overstory + Sapling docs
- Google A2A protocol reference
- CrewAI / AutoGen architecture docs
- Super Knowledge compendiums

### Run Sequence

Run the 5 query clusters from `NOTEBOOKLM_HARNESS_SYSTEMS_QUERY_PACK_V1.md` in this order:

| Pass | Clusters | Focus | Why This Order |
|------|----------|-------|----------------|
| 1 | A + C | Dual-harness architecture + Lean teams | Core architecture decisions first |
| 2 | B + D | ACP protocol + Cognitive bandwidth | Communication and context management |
| 3 | E | Multi-model routing | Integration and routing last (depends on A-D) |

**After each pass:** Copy NotebookLM outputs to a .docx file for import into Claude Code.
Name: `Notebook LM Query Harness [Pass Number].docx`

---

## Post-Run Integration Protocol

After running all notebooks through NotebookLM:

### Step 1: Import Results
```text
Load all .docx files into Claude Code session.
Request: "Triage these NotebookLM findings into Bucket 1 (Patch Now),
Bucket 2 (Future Seams), Bucket 3 (Doctrine Conflicts)"
```

### Step 2: Apply Threadex Patches
```text
Apply Bucket 1 findings from Threadex queries to the design doc.
Update: docs/plans/2026-03-11-threadex-memory-architecture-design.md
Create: PATCH_REGISTRY entry for the enhancement pass
```

### Step 3: Create Harness Design Brief
```text
Using Bucket 1 findings from Harness queries, create:
docs/plans/2026-03-XX-harness-architecture-design.md
(The harness design doc — new deliverable from this research)
```

### Step 4: Update MAA v4.0.0 Seams (if needed)
```text
If NotebookLM reveals new memory seams or ACP contracts
that MAA should declare, apply as patch to:
.agents/skills/automations/automations_master_architect_v4_0_0.xml
```

---

## Query Pack Locations

| Pack | Location | Clusters |
|------|----------|----------|
| Threadex Memory | `docs/plans/NOTEBOOKLM_THREADEX_MEMORY_QUERY_PACK_V1.md` | A-F (6 clusters) |
| Harness Systems | `docs/plans/NOTEBOOKLM_HARNESS_SYSTEMS_QUERY_PACK_V1.md` | A-E (5 clusters) |
| This Prompt Pack | `docs/plans/THREADEX_HARNESS_PROMPT_PACK_V1.md` | — |

---

## Expected Outcomes

After completing both notebook runs + integration:

- [ ] Threadex design doc patched with NotebookLM findings
- [ ] Harness architecture design doc created
- [ ] SIMS lifecycle validated or enhanced
- [ ] ACP message envelope schema drafted
- [ ] Lean team canonical compositions defined
- [ ] Context budget allocation strategy defined
- [ ] Multi-model routing table v1 sketched
- [ ] Cross-harness memory compatibility confirmed
- [ ] All Bucket 3 doctrine conflicts resolved
- [ ] Patch registry updated
