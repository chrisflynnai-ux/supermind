# META FAMILY AUDIT V4
## Date: 2026-03-07

Purpose: classify the current `.agents/skills/meta` assets, define the canonical V4 role set, and provide the migration gate for later domain folders.

---

## Canonical Targets

The meta family should converge on these executable roles:

- `meta_zpwo`
- `meta_mma`
- `meta_skill_builder`
- `meta_skill_architect`
- `meta_skill_auditor`
- `meta_template_system`

Reference-grade doctrine may remain in markdown, but executable orchestration must live in V1.4-compliant XML skills.

---

## Audit Table

| Asset | Current Role | Findings | Verdict | Canonical Outcome |
|------|------|------|------|------|
| `zpwo_v4_0_0.xml` | Orchestrator | Strongest current V4 benchmark. Has canonical `skill_id`, layer tags, SelfCheck, PatchLog, routing references, and explicit circuit breaker doctrine. | `keep as benchmark` | Keep as reference orchestrator and relational contract source. |
| `mma_master_monitor_agent_v1_0_0.xml` | Quality gate | Strong logic and golden runs, but legacy naming, no V1.4 shape, and relational contracts are implicit or buried. | `patch` | Replace with canonical `meta_mma` V4 skill. |
| `skill_builder_v1.2.0.xml` | Skill construction engine | Valuable build logic, token budgets, dependency concepts, Python-tool scaffolding. Uses legacy `skill.meta.*` naming, mixed schema conventions, and older XML structure. | `patch` | Replace with canonical `meta_skill_builder` V4 skill. |
| `SKILL_ARCHITECT_v2_ENHANCED.md` | Architecture doctrine | Best source for role separation, constitutional alignment, activation logic, and layered design. Not executable and overlaps with builder/template docs. | `decompose` | Convert execution-critical parts into `meta_skill_architect`; keep remainder as reference doctrine. |
| `ULTRAMIND_SKILL_FRAMEWORK_V3.md` | Unified framework | Useful system map, but contains stale Prism-stage synthesis language and mixed old/new standards. | `decompose` | Keep only as historical/reference framework; move canonical rules into V4 role assets. |
| `SKILL_TEMPLATE_V3.md` | Human-readable template | Good drafting aid for contracts and quality sections, but not the canonical SkillML V1.4 template and still partially placeholder-driven. | `patch` | Replace with executable `meta_template_system` V4 skill plus a future aligned template set. |
| `SKILL_TEMPLATE_V2.xml` | Legacy XML template | Useful placeholder source, but naming and structure predate V1.4. | `archive` | Keep only for historical migration reference. |
| `xml_skill_template_v2_1.xml` | Legacy XML template | Same issue as `SKILL_TEMPLATE_V2.xml`; useful only for migration archaeology. | `archive` | Keep only for historical migration reference. |
| `zpwo_v3_MICRO.xml` | Legacy orchestrator | Superseded by `zpwo_v4_0_0.xml`. | `archive` | Preserve for comparison only. |
| `Claude_Skill_Creator_Skill.md` | External skill-writing reference | Useful discovery/frontmatter guidance and eval loop ideas, but not aligned to current meta-family XML standard. | `decompose` | Extract discovery/frontmatter heuristics into patch pack; do not use as canonical format. |
| `SKILL_UPGRADE_PLANS_v1.0.md` | Upgrade roadmap pattern | Good example of patch-roadmap thinking and decomposition into knowledge blocks. | `keep as benchmark` | Reuse as a reporting pattern, not as a canonical schema. |

---

## Cross-Asset Findings

### Strengths

- The folder already contains the core roles needed for the whole system: orchestration, validation, building, architecture, and templating.
- The current `meta_zpwo` is a defensible V1.4 benchmark.
- The builder and architect materials already encode relational concepts such as dependencies, downstream consumers, triggers, and quality gates.

### Contradictions

- The atomic synthesis pipeline says the canonical flow is `Skill Atoms -> NotebookLM Router -> Claude Synthesizer`.
- `ULTRAMIND_SKILL_FRAMEWORK_V3.md` and the builder docs still reference `Prism` in the manufacturing flow.
- Several legacy meta files still use dotted legacy IDs such as `skill.meta.skill_builder.v1_2_0` rather than canonical `{domain}_{function}` IDs.
- Discovery and activation conventions are split across XML tags, markdown frontmatter thinking, and old ULTRAMIND template language.

### Structural Gaps

- No canonical `meta_skill_auditor` exists.
- No canonical `meta_template_system` exists.
- No single relational operations contract explicitly ties all meta skills together.
- Current builder and architect assets are too broad and mix doctrine with executable behavior.

---

## Required Meta-Family Decisions

1. `meta_zpwo` remains the benchmark and router.
2. `meta_mma` becomes the canonical quality and patch trigger skill.
3. `meta_skill_builder` handles skill creation and patch execution.
4. `meta_skill_architect` handles decomposition, role design, and integration logic.
5. `meta_skill_auditor` becomes the front door for folder audits and migration gating.
6. `meta_template_system` owns canonical templates, discovery metadata rules, and starter scaffolds.

---

## Exit Criteria For Meta Family

- Canonical V4 files exist for auditor, builder, architect, and template system.
- Relational operations between all six meta roles are explicit.
- Prism-era synthesis ambiguity is removed from canonical behavior.
- Future folder migrations can follow the same sequence without redefining the method.