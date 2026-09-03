# Metrics library

One page per classical metric. Each page teaches the metric itself — what it is, why it is worth measuring, how it connects to the others, and the classical ways to see it — and then points to the patterns and case studies that show how real teams worked on it. The audience is the same as everywhere in this framework: organizations without dedicated analysts.

## Where this sits

This library is the knowledge layer of **Module 1A, definition quality** — the half of [Module 1](../modules/01-ai-data-quality/README.md) that asks whether you are measuring the right thing, as against 1B, which asks whether the pipeline returns that number correctly. It is a layer, not a fifth module: the framework stays at four. Topic pages on revenue, cost and margin will also serve [Module 4](../modules/04-governance-and-financial-reporting/README.md), which is why the library lives at `docs/metrics/` rather than inside one module's directory.

The relationship between the layers:

- **Topic pages** (here) carry the durable knowledge: definitions, connections, visualizations.
- **Patterns** (`docs/modules/`) are specific, sourced ways of working on a metric — the [state-based retention measurement](../modules/01-ai-data-quality/state-based-retention-measurement.md) pattern is one way to work on retention, with Duolingo as its case study.
- **Skills** (`skill/`) will be the guided path: an agent-assisted way to develop each metric in your own business context, built on the topic page's definitions.

Topic pages carry a Sources & Stories section like every other content file; citation keys resolve in [REFERENCES.md](../../REFERENCES.md).

## Topics

| Topic | Status |
|---|---|
| [Attribution](attribution.md) | drafted; author answers and voice pass done, guided skill shipped |
| [Conversion rate](conversion-rate.md) | drafted; author answers and voice pass done |
| [Time to convert](time-to-convert.md) | drafted; author answers folded in, voice pass pending |
| [Active users](active-users.md) | drafted; author opening written, interview questions open |
| [Retention](retention.md) | drafted; entity retention only, author answers folded in, voice pass pending |
| [Benchmarks](benchmarks.md) | drafted; every trace re-verified, interview pending |

Retention was too big for one page. [Retention](retention.md) now covers the entity: users, accounts and workspaces, and whether they come back. Value retention, where the thing retained is contract value, and lifetime value, where retention meets acquisition cost, are separate pages still to be written.

Planned next: value retention and LTV, then segmentation, then cost and margin. Revenue and usage after those.
