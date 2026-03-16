# META NOTEBOOKLM QUERY PACK V4

Purpose: enhancement queries for `.agents/skills/meta` before or during V4 refactor work.

---

## Query 1: Modern Claude Skill Patterns

Analyze the provided meta-family sources and identify the best modern Anthropic or Claude-aligned patterns for:
- skill discovery and activation
- progressive disclosure without context bloat
- split between reference docs and executable skills
- reviewer and builder role separation

Return:
- 5 high-value patterns
- 5 anti-patterns
- 3 recommended upgrades for the meta family

## Query 2: Discovery and Frontmatter Hygiene

Review these files as a discovery system, not just as content:
- Which files are easiest to route correctly?
- Which files have weak activation, naming, or role clarity?
- What naming and trigger conventions should become canonical for V4?

Return:
- canonical naming rules
- activation metadata rules
- missing discovery fields to standardize

## Query 3: Prompt-to-Skill Decomposition

Compare the current meta files and identify where broad documents should be split into narrow executable roles.

Return:
- which files should stay reference-only
- which files should become executable V4 skills
- a decomposition map with role names and responsibilities

## Query 4: Orchestration and Review Loop Improvements

Analyze the current orchestrator, validator, builder, and architect logic.

Return:
- stronger review loop patterns
- better ownership rules between router, auditor, architect, builder, and quality gate
- recommended fix-loop and patch-loop improvements for family migrations

## Query 5: Pipeline Contradictions

Compare all meta-family manufacturing references against the atomic pipeline doctrine:
- Skill Atoms
- NotebookLM Router
- Claude Synthesizer

Find any conflicting or stale references, especially older Prism-based language.

Return:
- contradiction list
- severity per contradiction
- exact doctrine to retire
- exact doctrine to keep

## Query 6: Relational Operations Patterns

Using the meta family as a system, identify the strongest way to define relational operations between skills.

Return:
- required relational fields
- common wake conditions
- review ownership patterns
- patch ownership patterns
- example contracts for orchestrator, auditor, architect, builder, and template roles

---

## Required Output Format

For each query, normalize the result into:
- new heuristics
- new failure modes
- missing atoms
- outdated doctrine
- recommended structural upgrades
