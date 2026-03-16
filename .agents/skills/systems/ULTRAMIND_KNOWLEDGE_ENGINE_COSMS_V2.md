# ULTRAMIND Knowledge Engine COSMS V2

Version: 2.0.0
Status: proposed_not_applied

## Purpose
Build a machine-friendly private knowledge layer that turns notes, skills, projects, memories, and patterns into connected operating knowledge for agents and humans.

## Design Direction
- Keep the center simple
- Make the edges intelligent
- Prefer clean objects over long prose
- Prefer card-first exploration over dense dashboards
- Prefer graph-ready storage over backend lock-in

## Core Model
The knowledge engine is a COSMS layer:
- private or sanitized
- domain-specific
- machine-friendly
- agent-upgradeable
- human-browsable

## Core Objects
### Node
A reusable knowledge card.
- `node_id`
- `node_type`
- `title`
- `summary`
- `body`
- `tags[]`
- `source_refs[]`
- `confidence`
- `status`
- `created_at`
- `updated_at`

### Edge
A typed relation between cards.
- `edge_id`
- `from_node`
- `to_node`
- `relation_type`
- `confidence`
- `created_by`

### Cluster
A dynamic grouping of related cards.
- `cluster_id`
- `label`
- `node_ids[]`
- `theme`
- `open_questions[]`

### SynthesisRun
A recorded pass that creates or updates associations.
- `run_id`
- `input_nodes[]`
- `new_edges[]`
- `detected_gaps[]`
- `suggested_queries[]`
- `status`

## Relation Types
Start small:
- `relates_to`
- `supports`
- `depends_on`
- `contradicts`
- `evolves_to`
- `example_of`
- `part_of`

## Machine-Friendly Schema Direction
Use Pydantic-style models first.
Serialize to JSON cleanly.
Stay compatible with later Neo4j mapping.

Mapping rule:
- `Node` -> graph node
- `Edge` -> graph relationship
- `Cluster` -> derived grouping, not primary storage
- `SynthesisRun` -> operational history

## Core Loops
### 1. Ingest
Take raw notes, docs, transcripts, or skill content and normalize them into nodes.

### 2. Associate
Create candidate links by semantic similarity, shared tags, and inferred relation type.

### 3. Synthesize
Generate summaries, clusters, open questions, and contradictions.

### 4. Query Gaps
When confidence is weak or clusters are thin, generate NotebookLM gap queries.

### 5. Upgrade
Convert new findings into patch packs, node updates, or new relation edges.

## Front-End Contract
The front end should feel simple and calm.
Default to a sortable card canvas with optional graph mode.

### Required Views
- Card list
- Cluster board
- Graph view
- Gap queue
- Recent synthesis log

### Card Behavior
Each card should support:
- open
- sort
- filter
- pin
- link
- merge
- split
- promote to project or skill atom

### Self-Association UX
The system should suggest links, not hide them.
Users should be able to:
- accept suggestion
- reject suggestion
- soften confidence
- request another synthesis pass

## Backend Direction
V1 can be file-backed.
V2 can map to Neo4j.
Do not block the design on final database choice.

Recommended backend path:
1. file-backed Pydantic objects
2. graph-ready serialization layer
3. Neo4j adapter when relationship density demands it

## Agent Role In This System
Agents should:
- ingest knowledge
- propose links
- detect contradictions
- identify gaps
- emit patch requests
- upgrade domain COSMS over time

Humans should:
- review high-impact links
- approve major merges
- decide canonical doctrine shifts

## NotebookLM Role
NotebookLM is a gap-finding and synthesis input tool.
It should not be treated as canonical memory.
Its outputs should be normalized into:
- node candidates
- relation candidates
- contradiction notes
- patch opportunities
- open questions

## Immediate Next Build
- define the first node schema
- define the first edge schema
- define a gap-query prompt pack
- build a minimal card-first interface contract
- connect the result to skill-family patch workflows
