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

## Frontmatter: which module, and for Module 1, which half

Every pattern's `module:` field names its home. Module 1 patterns use `1A` or `1B`, never bare `1`: `1A` for definition quality (what to measure), `1B` for data integrity (whether the number is right). See [the Module 1 charter](modules/01-ai-data-quality/README.md).

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

## Presentation

The sections fix the shape; this fixes the fidelity. The audience is teams without analysts on staff, and the bar is the source material: the original stories these patterns draw from use charts and diagrams to carry their argument, and a pattern that flattens them into prose has lost fidelity, not gained rigor.

- **Draw the structure.** If the pattern has a state model, a flow, a loop, or a before/after, show it as a Mermaid diagram — GitHub renders these natively, nothing to install. The state diagram in [state-based retention measurement](modules/01-ai-data-quality/state-based-retention-measurement.md) is the reference example.
- **Draw data as a real chart.** Mermaid cannot express series of different lengths, scatter marks, or stacked areas, and forcing a shape it can draw distorts the argument. When the picture is the argument, commit an SVG under a `figures/` directory next to the page and reference it with normal image syntax; GitHub renders it. The two cohort charts on [conversion rate](metrics/conversion-rate.md) are the reference example.
- **One dataset behind related figures.** If two charts make a point together, compute both from the same numbers, so the second really is what the first produces rather than a drawn assertion. Say so in the caption.
- **Use real published numbers when they exist; otherwise mock plausible ones and say so in the caption.** Where a source publishes the data, plot the source's own figures and credit them. Where it does not, invent numbers that look like a real business rather than round decoys, and label them illustrative in the caption. Do not put the word placeholder in a chart title: a title that announces the chart is unfinished makes the whole page read as a draft.
- **Let the picture replace the prose.** A figure that earns its place shortens the section it sits in. If the explanation survives intact beside the chart, one of them is not working.
- **Skimmable first.** A reader should get the shape of the pattern from the headings, one diagram, and the canonical statement in section 3, before committing to the full text.
- **Break up density.** A third consecutive paragraph of prose is a signal to reach for a table, a diagram, or a worked example instead.
- **Draft notes are invisible.** Open questions and editorial markers live in HTML comments, never as list items a reader can see. A published page that shows its own outline reads as unfinished, whatever its contents.
