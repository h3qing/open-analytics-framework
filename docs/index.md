# Start here

> Scope: the front door. States the thesis, explains how the framework is organized, and gives the reading order. No pattern content lives here.

## The thesis

These systems do not fail at the model layer. They fail at deployment. Query generation is largely a solved problem — model ability is generalized, but it lacks opinion and industry experience. What breaks is everything around it: inconsistent metric definitions across teams, schemas that drift, outputs that look correct while resting on bad joins or incomplete data, and the resulting collapse of organizational trust that sends everyone back to manual validation. That is a process and systems problem, not a modeling problem, which is why industrial-engineering methodology is the right lens.

[TODO(heqing): expand in your own voice — what this means for the reader, and why the deployment layer is where your five years were spent.]

## Who this is for

[TODO(heqing): primary worked case (early-stage and AI-native companies) and how the patterns generalize down. Say it explicitly rather than pretending to be audience-neutral.]

## How the framework is organized

- Four modules, read in order: [data quality](modules/01-ai-data-quality/README.md), [infrastructure](modules/02-infrastructure-design/README.md), [agent integration](modules/03-ai-agent-integration/README.md), [governance and financial reporting](modules/04-governance-and-financial-reporting/README.md).
- The [metrics library](metrics/README.md): classical metric knowledge, one topic page per metric, with patterns and case studies hanging off each topic.
- Every pattern uses the same eight-section shape: [the pattern template](pattern-template.md), which maps onto DMAIC.
- Reference and guide are separate: the canonical statement of a pattern lives in `docs/modules/`; the longer walkthroughs live in [`implementation-guides/`](../implementation-guides/README.md) and [`reference-architectures/`](../reference-architectures/README.md).
- Something to adopt, not just read: every module ships copyable artifacts in [`templates/`](../templates/README.md).
- Patterns cite the stories and research they draw from: see [the prior-art review](prior-art.md) and [REFERENCES.md](../REFERENCES.md).

## Available now

- [State-based retention measurement](modules/01-ai-data-quality/state-based-retention-measurement.md) — the first pattern, drawn from the Duolingo growth story. Drafted; awaiting the author's voice pass.

## Reading order

[TODO(heqing): recommended paths — e.g., "deploying an agent this quarter" vs. "no analytics function yet". Write after Module 1 content exists.]
