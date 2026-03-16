# ATOMIC KNOWLEDGE SYNTHESIS — QUICK REFERENCE
## v2.0 | Replaces Prism-based Pipeline

---

## THE ARCHITECTURE

```
SKILL ATOMS (Layer 1) → NOTEBOOKLM ROUTER (Layer 2) → CLAUDE SYNTHESIZER (Layer 3)
     ↓                         ↓                              ↓
  Extract                   Query                         Compile
  1-3 page units         Cross-link                    Double-II bundle
  API naming             Cluster                       Production skill
```

---

## WHY v2.0?

| v1.0 (Wrong) | v2.0 (Correct) |
|--------------|----------------|
| Prism (LaTeX tool) | NotebookLM Router |
| Mega-prompts | Atomic extraction |
| Tool tax | Modular queries |
| One-shot | Reusable atoms |

---

## SKILL ATOM NAMING

```
[category].[descriptive_name].[version]

Categories:
• heuristic  — Rules of thumb
• spec       — Technical patterns
• failure    — What breaks & fixes
• framework  — Architectures
• pattern    — Code snippets
• checklist  — Validation criteria
• workflow   — Process sequences
```

**Examples:**
```
heuristic.10_to_1_rule.v1
spec.playwright_wrapper.v1
failure.context_rot_prevention.v1
```

---

## SKILL ATOM TEMPLATE

```markdown
# ATOM: [category].[name].[version]
# Source Ref: [Citation]

## 1. CORE LOGIC (Intent)
- **Constraint:** [One-sentence rule]
- **Rationale:** [Why]

## 2. TECHNICAL PATTERN (Mechanism)
- **Language/SDK:** [e.g., Python]
- **Code Snippet:** [Code block]

## 3. FAILURE MODES (Learned Constraints)
- **Warning:** [What breaks]
- **Fix:** [How to prevent]

## 4. USAGE TRIGGER
- **Trigger:** [When to use]
- **Anti-Trigger:** [When NOT]

## 5. CROSS-REFERENCES
- **Related Atoms:** [List]
- **Parent Skill:** [Module]
```

---

## 5-STEP WORKFLOW

```
1. EXTRACT → Generate atoms from sources (NotebookLM)
2. UPLOAD  → Add atoms as sources to fresh notebook
3. QUERY   → Route, cross-link, cluster atoms
4. COMPILE → Feed clusters to Claude Synthesizer
5. DEPLOY  → Validate and add to manifest
```

---

## NOTEBOOKLM ROUTER QUERIES

**Route:**
```
"Find all atoms related to [topic]"
```

**Cross-Link:**
```
"Compare [atom A] against [atom B]"
```

**Cluster:**
```
"Group atoms needed for Module [N]"
```

**Contradict:**
```
"Where do sources disagree about [topic]?"
```

---

## CLAUDE SYNTHESIZER OUTPUT

**Double-II Bundle:**
```
/module_name/
├── SKILL.md           # Information layer
├── implementation.py  # Code layer
├── flowgram.mmd       # Visual bridge
└── zero_point.json    # Index (<100 tokens)
```

---

## ATOM FOLDER STRUCTURE

```
/library/atoms/
├── heuristics/    # Rules of thumb
├── specs/         # Technical patterns
├── failures/      # Learned constraints
├── frameworks/    # Architectures
├── patterns/      # Code snippets
├── checklists/    # Validation
└── workflows/     # Processes
```

---

## QUICK COMMANDS

| Command | Action |
|---------|--------|
| `Extract: [topic]` | Generate atoms from sources |
| `Route: [query]` | Find related atoms |
| `Cluster: Module [N]` | Group atoms for skill |
| `Compile: [atoms]` | Generate Double-II bundle |
| `Validate: [skill]` | Constitution check |

---

## ECONOMICS

| Layer | Tool | Cost |
|-------|------|------|
| 1 | NotebookLM | Free |
| 2 | NotebookLM | Free |
| 3 | Claude | Sub |

**Time:** 4-7 hours per module

---

## CRITICAL RULES

1. **Atoms < 3 pages** (prevent tool tax)
2. **API naming** (consistent retrieval)
3. **Cross-reference** (atoms link to atoms)
4. **NotebookLM = Router** (not synthesizer)
5. **Claude = Compiler** (heavy synthesis)

---

*Atomic Knowledge Synthesis v2.0*  
*"Lego bricks, not monoliths"*
