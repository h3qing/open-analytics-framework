# Pattern template

Every pattern document uses this shape. Eight sections, several of which are one or two sentences. Stub every content file against it; do not add, remove, or reorder sections.

## The eight sections

1. **Problem** — what goes wrong without this.
2. **When this applies** — and explicitly, when it does not.
3. **The pattern** — the canonical statement, a few sentences.
4. **Position** — the common practice this rejects, and why. Required. Must contain at least one sentence of the form "do X, not Y." A pattern with no position is a description, not a pattern.
5. **Implementation** — steps, linked to the artifact in `templates/` and any relevant implementation guide.
6. **How you know it is working** — the observable signal or metric.
7. **Failure modes** — how this gets implemented badly.
8. **Sources & Stories** — where this comes from. List the key sources and stories using natural references (e.g. "the Duolingo growth model as described by the practitioners who built it", "practices described by Benn Stancil", "similar patterns at early Uber"). The pattern itself is the primary artifact; these are for traceability if the reader wants to go deeper. All citation keys must resolve in [REFERENCES.md](../REFERENCES.md).

## DMAIC mapping

The Six Sigma thread is structural, not claimed. Each template section is a DMAIC stage:

| DMAIC stage | Template section |
|---|---|
| Define | Problem, When this applies |
| Measure | How you know it is working |
| Analyze | Failure modes |
| Improve | Implementation |
| Control | The artifact in `templates/` |

Every module ships at least one **control plan** template in `templates/`. That is the artifact that makes the methodology real rather than decorative.
