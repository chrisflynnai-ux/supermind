# PATCH_skill_template_refactor_to_meta_template_system_v4_0_0

- Status: ready_for_claude
- Source: `.agents/skills/meta/SKILL_TEMPLATE_V3.md`
- Proposed replacement: `.agents/skills/meta/meta_template_system_v4_0_0.xml`
- Patch type: refactor
- Apply now: no

## Intent
Convert the template guidance into a V4 template-system role that issues canonical scaffold rules for later family migrations.

## Required Changes
- Normalize to `meta_template_system`
- Preserve reusable scaffold logic while removing redundant prose
- Make template outputs explicit for future folder-by-folder migration
- Attach template ownership to builder and architect roles

## Companion Inputs
- `.agents/skills/meta/META_PATCH_PACK_V4.md`
- `.agents/skills/meta/FOLDER_REFACTOR_WORKFLOW_V4.md`
- `.agents/skills/meta/patches/NOTEBOOKLM_META_PROMPT_FRAMEWORK_V4.md`
