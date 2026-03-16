# Claude Doc Triage Handoff V4

Use this folder to decide which docs to trust, patch, or treat as historical.

## Read Order
1. `DOC_TRIAGE_REGISTRY_V4_2026-03-07.md`
2. `CURRENT_TRACK_CANONICAL_DOCS_V4.md`
3. `REPAIR_QUEUE_V4.yaml`
4. the named patch file for the target doc
5. `DISCARD_QUEUE_V4.yaml` if there is confusion about older summaries

## Current Rule
- Trust Tier 1 docs first.
- Patch strong Tier 2 docs before using them as current canon.
- Treat Tier 3 docs as historical unless a patch says otherwise.

## Present Track
Wave 1:
- refactor skills
- stabilize harness
- align routing and validators
- run NotebookLM patch workflow
- support Interscale services

Wave 2:
- COSMS hardening
- Neo4j/vector adapters
- collective hubs
