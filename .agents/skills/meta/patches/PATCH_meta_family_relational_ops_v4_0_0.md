# PATCH_meta_family_relational_ops_v4_0_0

- Status: ready_for_claude
- Source: `.agents/skills/meta/META_FAMILY_AUDIT_V4_2026-03-07.md`
- Proposed replacement: `.agents/skills/meta/meta_relational_operations_v4.yaml`
- Patch type: linkage
- Apply now: no

## Intent
Formalize the relational operating model for the meta family so orchestration, auditing, building, and patching are explicit instead of implied.

## Required Changes
- Define upstream/downstream contracts for all six meta roles
- Define wake conditions and review ownership
- Define patch ownership and escalation direction
- Keep linkage data machine-readable for future routing or manifest integration

## Companion Inputs
- `.agents/skills/meta/meta_relational_operations_v4.yaml`
- `.agents/skills/meta/META_PATCH_PACK_V4.md`
- `.agents/skills/meta/patches/NOTEBOOKLM_META_PROMPT_FRAMEWORK_V4.md`
