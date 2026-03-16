# META Patch Manifest V4

This folder tracks proposed upgrades for the `.agents/skills/meta` family.
These patches are planning and handoff artifacts only. They are not applied to canonical `.claude/skills/` files.

## Operating Rule
- Build and refine in `.agents/skills/meta`
- Save named patch artifacts in `patches/`
- Validate replacement V4 files where tooling allows
- Hand off named patch artifacts to Claude or human review for canonical merge later

## Patch Naming Standard
- Format: `PATCH_{target}_{change}_{version}.md`
- Example: `PATCH_skill_builder_refactor_to_meta_skill_builder_v4_0_0.md`

## Current Patch Set
- `PATCH_mma_refactor_to_meta_mma_v4_0_0.md`
- `PATCH_skill_builder_refactor_to_meta_skill_builder_v4_0_0.md`
- `PATCH_skill_architect_refactor_to_meta_skill_architect_v4_0_0.md`
- `PATCH_skill_template_refactor_to_meta_template_system_v4_0_0.md`
- `PATCH_skill_framework_alignment_to_meta_template_system_v4_0_0.md`
- `PATCH_meta_family_relational_ops_v4_0_0.md`

## Supporting Files
- `PATCH_REGISTRY_V4.yaml`
- `CLAUDE_UPGRADE_HANDOFF_V4.md`
- `NOTEBOOKLM_META_PROMPT_FRAMEWORK_V4.md`
