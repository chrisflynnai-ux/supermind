# SUPERMIND Custom Commands

These are Claude Code slash command shortcuts for the SUPERMIND workflow.

## Team Commands

| Command | Action |
|---------|--------|
| `/run-research` | Dispatch T1 Research Team |
| `/run-draft` | Dispatch T2 Draft Team |
| `/run-production` | Dispatch T3 Production Team |
| `/run-polish` | Dispatch T4 Perfecting Team |

## Quality Commands

| Command | Action |
|---------|--------|
| `/score-copy` | Run MMA M1 Quick Score |
| `/deep-audit` | Run MMA M2 Deep Audit |
| `/resonance-check` | Run NRA Neuro-Resonance Audit |

## Workflow Commands

| Command | Action |
|---------|--------|
| `/conductor` | Run conductor for next task |
| `/kanban` | Show kanban board status |
| `/gc` | Run garbage collection |
| `/state` | Show session state |

## Usage

These commands are implemented in the .claude/commands/ directory.
Each command file contains the prompt template that gets executed.
