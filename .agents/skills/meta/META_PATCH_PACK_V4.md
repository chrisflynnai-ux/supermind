# META PATCH PACK V4
## Source normalization for `.agents/skills/meta`

This patch pack captures synthesis decisions for the meta family after reviewing current meta assets and the atomic pipeline source of truth.

---

## New Heuristics

### H1. Benchmark One, Patch Many
- Treat one strong V4 asset as the benchmark for a family.
- Patch the rest toward that benchmark instead of re-arguing standards per file.
- For meta, `meta_zpwo` is the benchmark.

### H2. Doctrine Out, Contracts In
- Keep doctrine/reference material in markdown.
- Move only routable, executable, testable behavior into XML skills.
- If a file mixes system philosophy with runtime behavior, split it.

### H3. Relational Links Must Be Contractual
- Upstream inputs, downstream consumers, wake conditions, review ownership, and patch ownership belong in explicit contract sections.
- Do not rely on prose-only references between sister skills.

### H4. Large Skills Need Retrieval Surfaces
- Large files are acceptable only when they expose a clean contract, clear layer boundaries, and modular references.
- Large files without decomposition guidance are rebuild candidates.

### H5. Discovery Is A First-Class Quality Gate
- Canonical ID, role description, activation triggers, and routing cues should be audited before content depth.
- A powerful skill that cannot be found or routed is a broken skill.

---

## New Failure Modes

### FM1. Pipeline Drift
- Symptom: builder docs describe a different synthesis pipeline than the current canonical process.
- Risk: the team upgrades skills using stale manufacturing instructions.
- Fix: canonical role skills must reference only the atomic v2 pipeline.

### FM2. Role Bleed
- Symptom: builder, architect, auditor, and template responsibilities blur into one file.
- Risk: poor routing, duplicate maintenance, and contradictory behavior.
- Fix: separate meta roles into narrow executable skills plus reference-grade docs.

### FM3. Discovery Collapse
- Symptom: naming conventions, triggers, and discovery metadata differ across assets.
- Risk: manifest and routing ambiguity.
- Fix: centralize discovery rules in `meta_template_system` and audit them in `meta_skill_auditor`.

### FM4. Monolith Without Atoms
- Symptom: a file is large but offers no atom, module, or dependency map.
- Risk: NotebookLM enhancement loops cannot patch it surgically.
- Fix: require a decomposition map and atom candidates before major rewrites.

### FM5. Implicit Patch Ownership
- Symptom: a failure is identified but no role owns the fix.
- Risk: findings accumulate without execution.
- Fix: every meta skill must declare patch ownership and review ownership.

---

## Missing Atoms

- `framework.relational_skill_operations.v1`
- `checklist.skill_discovery_contract.v1`
- `failure.pipeline_drift_detection.v1`
- `workflow.folder_refactor_loop.v1`
- `checklist.meta_family_audit_gate.v1`
- `framework.prompt_to_skill_decomposition.v1`

---

## Outdated Doctrine To Retire From Canonical Flow

- Prism as the mandatory synthesis stage
- dotted legacy `skill.meta.*` and `skill.validation.*` IDs
- mixed template assumptions between old XML templates and V1.4 SkillML
- prose-only dependency language without explicit contract mapping

---

## Recommended Structural Upgrades

1. Add `meta_skill_auditor_v4_0_0.xml`.
2. Add `meta_skill_architect_v4_0_0.xml`.
3. Add `meta_skill_builder_v4_0_0.xml`.
4. Add `meta_template_system_v4_0_0.xml`.
5. Add `meta_mma_v4_0_0.xml`.
6. Add a meta-family relational operations map for wake conditions and ownership.
7. Use the same audit -> patch pack -> relational map -> refactor pattern in every later folder.