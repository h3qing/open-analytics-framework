# Skills

Guided conversations that apply this framework's knowledge to one company's situation: questions one or two at a time, guidance after each answer, a decision record at the end. Every skill follows [the skill template](../docs/skill-template.md). MIT licensed.

| Skill | Status |
|---|---|
| [attribution-design](attribution-design/SKILL.md) — pick the credit rule for your size, align it with team incentives | draft |
| `analytics-readiness` — the diagnostic run before deploying an AI analytics agent (working name, Open Decision #2) | planned, Phase 2 |
| Defining your definitions (SK-01) and the vanity-metric check (SK-02) | candidate rows in the backlog |

The `analytics-readiness` diagnostic outputs a readiness report with a prioritized remediation plan mapped to the four modules, including the narrowest wedge — the single metric that, if made trustworthy enough that nobody re-checks it, changes the most downstream. Its construction is Phase 2, deliberately before the module content: writing the forcing questions is how the content gets articulated.

## Seeded forcing questions

Accumulated as patterns land, ahead of Phase 2 construction:

- From [M1-11 state-based retention measurement](../docs/modules/01-ai-data-quality/state-based-retention-measurement.md): *Name, from data you already have, the single lifecycle transition where you lose the most users.* If nobody can answer without inventing a new query on the spot, the organization is goaled on aggregates it cannot act on, and the retention-state pattern is a prerequisite for pointing an AI analytics agent at engagement questions.
Guided skills built on a topic page are Module 1A work: they walk a team through defining a metric in their own context. The `analytics-readiness` diagnostic is the exception — it spans all four modules.

- From the [conversion topic page](../docs/metrics/conversion-rate.md): *Ask three teams what "active" and "converted" mean, and compare the answers.* If the definitions differ and none is written down, no metric downstream of them can be trusted. The checkable model is Facebook holding the whole company to one definition of active, inside and out, edge cases documented. This question may grow into its own guided skill on defining definitions; candidate row SK-01 in the backlog.
