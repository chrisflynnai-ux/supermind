# FOLDER REFACTOR WORKFLOW V4

Use this exact loop for every skill family after `.agents/skills/meta`.

## Sequence

1. Inventory the folder.
2. Identify the strongest current benchmark asset.
3. Audit every asset against:
   - naming and canonical IDs
   - discovery metadata and triggers
   - SkillML V1.4 compliance
   - contradictions and overlap
   - relational contracts with sister skills
4. Produce one verdict per asset:
   - keep as benchmark
   - patch
   - decompose
   - rebuild
   - archive
5. Synthesize the best components across the family.
6. Run the family NotebookLM enhancement query pack.
7. Normalize the results into a family patch pack.
8. Define relational operations between family roles.
9. Refactor canonical V4 role files.
10. Validate and re-audit.

## Required Artifacts Per Family

- `FAMILY_AUDIT_V4_YYYY-MM-DD.md`
- `FAMILY_PATCH_PACK_V4.md`
- `family_relational_operations_v4.yaml`
- `FAMILY_NOTEBOOKLM_QUERY_PACK_V4.md`
- canonical V4 role files

## Exit Criteria

- one benchmark asset is explicit
- canonical role set is explicit
- relational operations are contractual
- stale doctrine is retired from executable assets
- the family can act as a template for the next migration pass
