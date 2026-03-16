# Claude Upgrade Handoff V4

Use this folder as the patch handoff surface for the meta family.
Do not upgrade canonical `.claude/skills/meta` files by inference alone. Use the named patch artifacts and the proposed V4 replacements.

## Handoff Sequence
1. Open `PATCH_REGISTRY_V4.yaml`
2. Pick one `patch_id`
3. Read the referenced patch file in `patches/`
4. Compare the legacy source file to the proposed V4 file in `.agents/skills/meta`
5. Apply upgrades in canonical only after review and validation

## Current Ready Patches
- `PATCH_mma_refactor_to_meta_mma_v4_0_0`
- `PATCH_skill_builder_refactor_to_meta_skill_builder_v4_0_0`
- `PATCH_skill_architect_refactor_to_meta_skill_architect_v4_0_0`
- `PATCH_skill_template_refactor_to_meta_template_system_v4_0_0`
- `PATCH_skill_framework_alignment_to_meta_template_system_v4_0_0`
- `PATCH_meta_family_relational_ops_v4_0_0`

## Required Companion Artifacts
- `.agents/skills/meta/META_FAMILY_AUDIT_V4_2026-03-07.md`
- `.agents/skills/meta/META_PATCH_PACK_V4.md`
- `.agents/skills/meta/META_NOTEBOOKLM_QUERY_PACK_V4.md`
- `.agents/skills/meta/meta_relational_operations_v4.yaml`

## Status Rule
All patches in this folder are `planned_not_applied` until human review approves canonical merge.
