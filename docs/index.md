# Start here

> Scope: the front door. States the thesis, explains how the framework is organized, and gives the reading order. No pattern content lives here.

## The thesis

These systems do not fail at the model layer. They fail at deployment. Query generation is largely a solved problem — model ability is generalized, but it lacks opinion and industry experience. What breaks is everything around it: inconsistent metric definitions across teams, schemas that drift, outputs that look correct while resting on bad joins or incomplete data, and the resulting collapse of organizational trust that sends everyone back to manual validation. That is a process and systems problem, not a modeling problem, which is why industrial-engineering methodology is the right lens.

[TODO(heqing): expand in your own voice — what this means for the reader, and why the deployment layer is where your five years were spent.]

## Who this is for

[TODO(heqing): primary worked case (early-stage and AI-native companies) and how the patterns generalize down. Say it explicitly rather than pretending to be audience-neutral.]

## How the framework is organized

Four modules, fixed by the project specification, plus three layers that cut across them.

**The modules,** read in order: [data quality](modules/01-ai-data-quality/README.md), [infrastructure](modules/02-infrastructure-design/README.md), [agent integration](modules/03-ai-agent-integration/README.md), [governance and financial reporting](modules/04-governance-and-financial-reporting/README.md). Four is a commitment, not a working guess: new material finds its home inside a module rather than becoming a fifth one.

**Module 1 has two named halves,** because "data quality" is two questions that get confused with each other:

- **1A, definition quality** — are you measuring the right thing, defined once and defined well. DMAIC's Define phase.
- **1B, data integrity** — does the pipeline return that number correctly, and stay in control. Measure through Control.

A number can be wrong in either direction independently, and the fixes have nothing in common. See [the Module 1 charter](modules/01-ai-data-quality/README.md).

**Module 2 has two named halves** for the same reason, since infrastructure fails as a build or as an operation:

- **2A, what you build** — what should exist at your size, in what order, and what not to build yet. DMAIC's Improve phase.
- **2B, how you run it** — whether it keeps returning the right answer as the company grows, and who owns it. Control.

Inside 2A the order is what expires, not what matters most: history is the only thing on the list you cannot buy back later. See [the Module 2 charter](modules/02-infrastructure-design/README.md).

**Module 3 has two named halves,** because an agent can be accurate and still be a side door, and locked down and confidently wrong:

- **3A, what it can reach** — can it only see and do what this asker is already entitled to. Control.
- **3B, what it tells you** — can we trust the answer, and does the company act like it. Measure and Analyze.

Read 3A first. Both matter, but only one fails in a way you cannot take back. Where Module 2 orders by whether a decision can be reversed, this one orders by whether the consequence can: granting a credential is reversible right up until a row leaves under it. See [the Module 3 charter](modules/03-ai-agent-integration/README.md).

**Module 4 has two named halves,** and they fail in front of different outsiders:

- **4A, what you must be able to show** — can you produce the evidence without manufacturing it. Control.
- **4B, the money numbers themselves** — are the figures defined correctly for an AI business and reported consistently. Define and Measure.

4B is not Module 1A applied to money. These definitions carry a disclosure consequence: changing what counts as an active user is internal, and changing what counts as ARR between two board decks is a restatement. See [the Module 4 charter](modules/04-governance-and-financial-reporting/README.md).

**Where Module 3 stops and Module 4 starts.** Module 3 owns the run, Module 4 owns the record. If a defect shows up inside a running agent session and is fixed by changing the runtime, it is Module 3. If it only shows up when an outsider asks you to produce something that already left the building, it is Module 4. The version that decides most cases on sight: Module 3's rules are about the agent specifically, and Module 4's rules bind every identity, including the founder's.

**The layers:**

- **Knowledge** — the [metrics library](metrics/README.md): classical metric knowledge, one topic page per metric. This is Module 1A's reference layer, not a fifth module; the revenue, cost and margin pages will also serve Module 4.
- **Patterns** — `docs/modules/`: sourced ways of working on a metric, with case studies attached. Every pattern uses the same eight-section shape, [the pattern template](pattern-template.md), which maps onto DMAIC.
- **Artifacts** — something to adopt, not just read: copyable [`templates/`](../templates/README.md) and guided [`skill/`](../skill/README.md) interviews. Every module ships at least one.

Reference and guide are separate: the canonical statement of a pattern lives in `docs/modules/`; the longer walkthroughs live in [`implementation-guides/`](../implementation-guides/README.md) and [`reference-architectures/`](../reference-architectures/README.md).

Patterns cite the stories and research they draw from: see [the prior-art review](prior-art.md) and [REFERENCES.md](../REFERENCES.md).

## Available now

- [State-based retention measurement](modules/01-ai-data-quality/state-based-retention-measurement.md) — the first pattern, drawn from the Duolingo growth story. Drafted; awaiting the author's voice pass.

## Reading order

[TODO(heqing): recommended paths — e.g., "deploying an agent this quarter" vs. "no analytics function yet". Write after Module 1 content exists.]
