# Diagnostic skill

Home of `analytics-readiness` (working name — Open Decision #2): a structured diagnostic run on an organization's analytics function *before* that organization deploys an AI analytics agent. Output: a readiness report with a prioritized remediation plan mapped to the four modules, including the narrowest wedge — the single metric that, if made trustworthy enough that nobody re-checks it, changes the most downstream.

**Status:** not built yet. Construction is Phase 2, deliberately before the module content: writing the forcing questions is how the content gets articulated.

Planned shape: `SKILL.md` (frontmatter + body), `references/` for per-module detail, `assets/` for the report template. Five stages — frame, forcing questions, privacy gate before any outward search, score and route, output. MIT licensed. Installation docs land here when the skill does.

## Seeded forcing questions

Accumulated as patterns land, ahead of Phase 2 construction:

- From [M1-11 state-based retention measurement](../docs/modules/01-ai-data-quality/state-based-retention-measurement.md): *Name, from data you already have, the single lifecycle transition where you lose the most users.* If nobody can answer without inventing a new query on the spot, the organization is goaled on aggregates it cannot act on, and the retention-state pattern is a prerequisite for pointing an AI analytics agent at engagement questions.
- From the [conversion topic page](../docs/metrics/conversion.md): *Ask three teams what "active" and "converted" mean, and compare the answers.* If the definitions differ and none is written down, no metric downstream of them can be trusted. The checkable model is Facebook holding the whole company to one definition of active, inside and out, edge cases documented. This question may grow into its own guided skill on defining definitions; candidate row SK-01 in the backlog.
