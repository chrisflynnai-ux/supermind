---
skill_id: meta_skill_builder
name: Meta Skill Builder
version: 4.0.0
tier: meta
status: active
domain: meta
track: cross
model: sonnet
neurobox: 
triggers: [/buildskill]
source_xml: .agents\skills\meta\meta_skill_builder_v4_0_0.xml
mode: auto
refactored_at: 2026-03-16T08:27:51.423242+00:00
threadex_records: []
---

# Meta Skill Builder (v4.0.0)

> skill_brief Requested role, family, domain, target behavior, and track assignment. architecture_spec Approved role boundaries and decomposition design from meta_skill_architect. Includes relational links, wake conditions, and ownership assignments. patch_pack NotebookLM enhancement outputs: heuristics, failure modes, missing atoms, doctrine corrections. See META_PATCH_PACK_V4.md for format. clustered_atoms Skill Atoms grouped by target skill via NotebookLM Router (Layer 2 of Atomic Pipeline v2.1). Categories: heuristic, spec, failure, framework, pattern, checklist, workflow. template_bundle Canonical SkillML V1.4 template from .agents/skills/_template/master_skill_template_v1.xml. legacy_asset Current file to patch or replace. Preserved content is extracted, not copied forward blindly. relational_map Family relational operations map (e.g., meta_relational_operations_v4.yaml) defining upstream, downstream, wake conditions, and ownership. v4_skill_asset Canonical executable skill in SkillML V1.4 XML. Placed in .agents/skills/{domain}/{skill_id}_v{version}.xml. Must pass 19/19 validator checks. alias_update New or changed alias entries for orchestration/routing/aliases.yaml (legacy name to canonical skill_id). validation_report Results from skillml_validator, lint_skill, and alias_resolver runs. patch_applied_summary Appended to the source patch file: what changed, what was preserved, unresolved contradictions, and second-patch recommendation. 6.0 8.0 9.0 3 HALT + PATCH_PROPOSAL to meta_skill_architect

## L1: Contract

skill_brief Requested role, family, domain, target behavior, and track assignment. architecture_spec Approved role boundaries and decomposition design from meta_skill_architect. Includes relational links, wake conditions, and ownership assignments. patch_pack NotebookLM enhancement outputs: heuristics, failure modes, missing atoms, doctrine corrections. See META_PATCH_PACK_V4.md for format. clustered_atoms Skill Atoms grouped by target skill via NotebookLM Router (Layer 2 of Atomic Pipeline v2.1). Categories: heuristic, spec, failure, framework, pattern, checklist, workflow. template_bundle Canonical SkillML V1.4 template from .agents/skills/_template/master_skill_template_v1.xml. legacy_asset Current file to patch or replace. Preserved content is extracted, not copied forward blindly. relational_map Family relational operations map (e.g., meta_relational_operations_v4.yaml) defining upstream, downstream, wake conditions, and ownership. v4_skill_asset Canonical executable skill in SkillML V1.4 XML. Placed in .agents/skills/{domain}/{skill_id}_v{version}.xml. Must pass 19/19 validator checks. alias_update New or changed alias entries for orchestration/routing/aliases.yaml (legacy name to canonical skill_id). validation_report Results from skillml_validator, lint_skill, and alias_resolver runs. patch_applied_summary Appended to the source patch file: what changed, what was preserved, unresolved contradictions, and second-patch recommendation. 6.0 8.0 9.0 3 HALT + PATCH_PROPOSAL to meta_skill_architect

### Frameworks

**MMAGateContract:** 6.0 8.0 9.0

**CircuitBreaker:** 3 HALT + PATCH_PROPOSAL to meta_skill_architect

## L2: ExecutionProtocol

Use the Atomic Knowledge Synthesis Pipeline v2.1 as the canonical manufacturing process: Skill Atoms to NotebookLM Router to Claude Synthesizer to SkillML V1.4 XML. Do not preserve legacy naming when a canonical V4 ID exists. Update aliases.yaml for backward compatibility. Every executable skill must contain all 5 required sections (Meta, Contract, ExecutionProtocol, SelfCheck, PatchLog), all 4 layer tags (CONTRACT, RULES, REASONING, IMPL), and explicit relational contracts. If legacy content conflicts with canonical doctrine, update toward doctrine. Do not copy stale patterns forward. Doctrine stays in markdown reference docs. Only routable, executable, testable behavior goes into XML skills (H2: Doctrine Out, Contracts In). Every built skill must declare patch_owner and review_owner per the family relational operations map. Benchmark all new builds against meta_zpwo (first V1.4-compliant skill, 19/19). progressive_disclosure meta_skill_architect (role boundaries and decomposition) meta_skill_auditor (audit findings and patch roadmap) meta_template_system (canonical scaffolds and discovery rules) meta_mma (quality gate and re-audit) manifest and routing updates (aliases.yaml, SKILLS_MANIFEST.yaml) meta_skill_builder (self — owns its own patches) meta_mma Ingest Brief and Context Load architecture_spec from meta_skill_architect.
          Load patch_pack and clustered_atoms if available.
          Load relational_map for upstream/downstream/ownership.
          Load legacy_asset if this is a patch (not a new build). All required inputs present. Architecture spec approved. Map Atoms to Sections Apply the Atomic Pipeline v2.1 atom-to-section mapping:
          - framework atoms to Meta (Description, PrimaryOutcome)
          - spec atoms to Contract (Inputs, Outputs)
          - heuristic atoms to ExecutionProtocol Rules
          - workflow atoms to ReasoningFramework Steps
          - pattern atoms to Implementation
          - checklist atoms to SelfCheck Check elements
          - failure atoms to SelfCheck FailureModes
          If no atoms available, extract equivalent content from legacy asset or architecture spec. Every V1.4 section has source material identified. Build V4 Asset Generate SkillML V1.4 XML using master_skill_template_v1.xml as scaffold.
          Populate all 5 required sections.
          Add all 4 layer tags (CONTRACT, RULES, REASONING, IMPL).
          Add minimum 3 SelfCheck elements + MMAGate + FailureModes.
          Add PatchLog entry with atom sources listed.
          Write to .agents/skills/{domain}/{skill_id}_v{version}.xml. File is well-formed XML with all required elements. Validate Run post-synthesis quality gates:
          - python tools/skillml_validator.py (must pass 19/19)
          - python tools/lint_skill.py (migration score target 80%+)
          - python tools/alias_resolver.py (routing resolution check)
          Fix any failures. Circuit breaker: max 3 fix attempts before escalating to meta_skill_architect. 19/19 validator checks pass. Lint score at or above 80%. Emit Handoff Artifacts Generate:
          - alias_update: new entries for aliases.yaml (if new skill or renamed)
          - validation_report: validator + linter output
          - patch_applied_summary: appended to source patch file
          Hand off to meta_mma for quality gate review.
          Run python tools/manifest_builder.py to update inventory. Patch file updated. Manifest reflects new or changed skill. Use when creating a skill from scratch:
          1. Receive brief + architecture spec from meta_skill_architect
          2. Cluster atoms via NotebookLM Router (Pipeline Layer 2)
          3. Compile atoms into XML via Claude Synthesizer (Pipeline Layer 3)
          4. Validate 19/19 + lint score
          5. Emit handoff artifacts Use when upgrading an existing skill:
          1. Receive audit findings from meta_skill_auditor
          2. Load legacy asset and patch_pack
          3. Extract preservable content from legacy
          4. Rebuild in V1.4 structure (do not patch legacy XML in place)
          5. Validate and emit Use when migrating a domain family:
          1. Receive family audit and relational map
          2. Process skills in dependency order (upstream first)
          3. Build each skill individually
          4. Update aliases.yaml and manifest after each
          5. Re-audit family after batch complete Validate V1.4 structure (19 checks). Must pass before handoff. Extended linting and migration readiness scoring. Target: 80%+. Verify routing resolution for new or changed skill_ids. Regenerate SKILLS_MANIFEST.yaml after skill creation or change. BUILDER FLOW (Single Skill)
1. Read brief + architecture spec + patch pack
2. Map atoms to V1.4 sections (framework->Meta, spec->Contract, etc.)
3. Build XML using master template scaffold
4. Run: python tools/skillml_validator.py (19/19 required)
5. Run: python tools/lint_skill.py (80%+ required)
6. Emit alias_update + validation_report + patch_applied_summary
7. Hand off to meta_mma for review gate

BUILDER FLOW (Batch Migration)
1. Load family audit + relational map
2. Sort by dependency (upstream first)
3. Build each skill per single-skill flow
4. Update aliases.yaml after each
5. Run manifest_builder after batch
6. Request family re-audit from meta_skill_auditor

### Frameworks

**ReasoningFramework:** Ingest Brief and Context Load architecture_spec from meta_skill_architect.
          Load patch_pack and clustered_atoms if available.
          Load relational_map for upstream/downstream/ownership.
          Load legacy_asset if this is a patch (not a new build). All required inputs present. Architecture spec approved. Map Atoms to Sections Apply the Atomic Pipeline v2.1 atom-to-section mapping:
          - framework atoms to Meta (Description, PrimaryOutcome)
          - spec atoms to Contract (Inputs, Outputs)
          - heuristic atoms to ExecutionProtocol Rules
          - workflow atoms to ReasoningFramework Steps
          - pattern atoms to Implementation
          - checklist atoms to SelfCheck Check elements
          - failure atoms to SelfCheck FailureModes
          If no atoms available, extract equivalent content from legacy asset or architecture spec. Every V1.4 section has source material identified. Build V4 Asset Generate SkillML V1.4 XML using master_skill_template_v1.xml as scaffold.
          Populate all 5 required sections.
          Add all 4 layer tags (CONTRACT, RULES, REASONING, IMPL).
          Add minimum 3 SelfCheck elements + MMAGate + FailureModes.
          Add PatchLog entry with atom sources listed.
          Write to .agents/skills/{domain}/{skill_id}_v{version}.xml. File is well-formed XML with all required elements. Validate Run post-synthesis quality gates:
          - python tools/skillml_validator.py (must pass 19/19)
          - python tools/lint_skill.py (migration score target 80%+)
          - python tools/alias_resolver.py (routing resolution check)
          Fix any failures. Circuit breaker: max 3 fix attempts before escalating to meta_skill_architect. 19/19 validator checks pass. Lint score at or above 80%. Emit Handoff Artifacts Generate:
          - alias_update: new entries for aliases.yaml (if new skill or renamed)
          - validation_report: validator + linter output
          - patch_applied_summary: appended to source patch file
          Hand off to meta_mma for quality gate review.
          Run python tools/manifest_builder.py to update inventory. Patch file updated. Manifest reflects new or changed skill.

## L3: (missing)

> _This layer was not present in the source XML. Add content during review._

## L4: (missing)

> _This layer was not present in the source XML. Add content during review._

## Contract

### Required Inputs

- **skill_brief** (markdown) — Requested role, family, domain, target behavior, and track assignment.
- **architecture_spec** (yaml) — Approved role boundaries and decomposition design from meta_skill_architect. Includes relational links, wake conditions, and ownership assignments.

### Optional Inputs

- **patch_pack** (markdown) — NotebookLM enhancement outputs: heuristics, failure modes, missing atoms, doctrine corrections. See META_PATCH_PACK_V4.md for format.
- **clustered_atoms** (markdown) — Skill Atoms grouped by target skill via NotebookLM Router (Layer 2 of Atomic Pipeline v2.1). Categories: heuristic, spec, failure, framework, pattern, checklist, workflow.
- **template_bundle** (xml) — Canonical SkillML V1.4 template from .agents/skills/_template/master_skill_template_v1.xml.
- **legacy_asset** (xml) — Current file to patch or replace. Preserved content is extracted, not copied forward blindly.
- **relational_map** (yaml) — Family relational operations map (e.g., meta_relational_operations_v4.yaml) defining upstream, downstream, wake conditions, and ownership.

### Primary Outputs

- **v4_skill_asset** (xml) — Canonical executable skill in SkillML V1.4 XML. Placed in .agents/skills/{domain}/{skill_id}_v{version}.xml. Must pass 19/19 validator checks.

### Quality Gates

- **T2:** 6.0
- **T3:** 8.0
- **T4:** 9.0

### Circuit Breakers

- **max_fix_loops:** 3
- **on_exhausted:** HALT + PATCH_PROPOSAL to meta_skill_architect

## Dependencies

### Upstream

(none extracted)

### Downstream

(none extracted)

## Guardrails

(none extracted)

## Graph Edges

(no edges extracted)
