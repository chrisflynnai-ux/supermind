# Systems Knowledge Engine Audit V4

## Target
- Source: `.agents/skills/systems/ULTRAMIND_KNOWLEDGE_ENGINE.md`
- Date: 2026-03-07
- Status: reviewed_for_patch

## Verdict
- Classification: `patch_and_simplify`
- Keep: vision, knowledge-first autonomy direction, graph-centric model, intent over brittle automation
- Reduce: tool comparison prose, long speculative code examples, duplicated autonomy claims, broad implementation roadmap
- Add: machine-friendly COSMS contract, Neo4j-ready schema shape, clean sortable card UX contract, explicit self-association loop, gap-query workflow

## Main Findings
1. The source mixes manifesto, product comparison, architecture, code sketching, and roadmap in one file.
2. The core durable value is the knowledge engine concept, not the Heptabase/Tana/N8N comparison layer.
3. The next version should be easier for agents and humans to operate: cleaner schema, fewer examples, explicit objects, explicit loops.
4. The visual layer should target a simple Flowith-like card and graph interface rather than a heavy custom UI description.
5. The memory direction should be `Pydantic models -> graph-friendly serialization -> Neo4j later` instead of forcing backend certainty too early.

## Proposed Target Shape
- `ULTRAMIND_KNOWLEDGE_ENGINE_COSMS_V2.md`
- concise architecture brief
- machine-friendly object model
- self-association and synthesis loop
- card-first UI contract
- gap-query prompts feeding later upgrades
