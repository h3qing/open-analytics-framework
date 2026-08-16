# Metrics library

One page per classical metric. Each page teaches the metric itself — what it is, why it is worth measuring, how it connects to the others, and the classical ways to see it — and then points to the patterns and case studies that show how real teams worked on it. The audience is the same as everywhere in this framework: organizations without dedicated analysts.

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
| [Value retention](value-retention.md) | drafted; author answers folded in, voice pass pending |

Retention was too big for one page. [Retention](retention.md) covers the entity: users, accounts and workspaces, and whether they come back. [Value retention](value-retention.md) covers the money: whether contract value renews and expands. Lifetime value, where the two meet and where acquisition cost enters, is the third page and is still to be written.

Planned next: LTV, then segmentation, then benchmarks and how to check a number before you steer by it, then cost and margin. Revenue and usage after those.
