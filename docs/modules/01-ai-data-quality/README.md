# Module 1 — AI data quality measurement and improvement

> Scope: the quality of the whole measurement system — both whether you are measuring the right thing and whether the number you get back is right. Covers metric definition, instrumentation, statistical control, validation, and the trust signals built on them. Does not cover: model selection, prompting, or benchmark performance; infrastructure design (Module 2); agent deployment mechanics (Module 3); metric change control as a governance process (Module 4).

**Status:** the opening module. Three patterns drafted, five topic pages drafted, everything awaiting a voice pass. What is coming lives in [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md).

## Two halves

A measurement system fails in two independent ways. It can measure the wrong characteristic, or it can measure the right characteristic wrongly. Both are quality defects, they have different causes and different fixes, and a team that only works on one keeps getting surprised by the other. This module names them separately.

| | 1A — Definition quality | 1B — Data integrity |
|---|---|---|
| The question | Are we measuring the right thing, defined once and defined well? | Does the pipeline return that number correctly, and stay in control? |
| Fails as | A precisely computed number that nobody can act on, or three teams reporting three different values for "active" | A correct definition returning a wrong value: bad join, late partition, silent schema change |
| DMAIC phase | Define — naming the critical-to-quality characteristic | Measure, Analyze, Improve, Control — measurement-system analysis and SPC |
| Knowledge layer | The [metrics library](../../metrics/README.md) | [`templates/01-ai-data-quality/`](../../../templates/01-ai-data-quality/) control plans |
| Guided layer | The [skills](../../../skill/README.md) that walk a team through defining a metric in their own context | [TODO(heqing): validation-harness skill, or none] |

Read 1A first. A definition defect propagates into every check 1B can run: statistical control on a metric that measures the wrong thing produces a well-behaved number nobody should steer by.

## Why this module exists

AI is getting incredibly powerful at working through your data, but everything needs a good foundation. If your raw numbers are wrong in the first place, AI would not have known, or you would not have trust in your final results.

Also, precisely because AI is powerful and people have more and more trust in it, any failure in the analysis becomes very hidden, because it is hard to trace. People like to take it at face value. In order to fix both problems, we have to have confidence in the raw data, and have as many checks as possible to ensure our data has passed every check. When business users or anybody uses the number, we have confidence that the number is accurate.

<!-- Open interview questions for the voice pass:
     1. The answer above is mostly the 1B case (hidden failures, trust in raw numbers).
        The 1A half is still open: name a time the definition itself was the defect —
        the number was computed correctly and still sent people the wrong way.
     2. Which half have you watched fail more often, and why are they one module rather than two?
     3. "ensure our data has passed every check" was transcribed from speech and may not be
        what you said; the original read "ensure our data has sent the check piece in". -->

## 1A — Definition quality

What to measure, and how to pin a definition down so it holds. The durable knowledge lives in the [metrics library](../../metrics/README.md), one page per classical metric; the patterns here are sourced ways of working on a metric, with their case studies attached.

### Most metrics fall into six categories

You do not need a metric catalogue. You need to know which of six questions your business cannot currently answer, because that is where the next thing breaks. Almost every metric worth the trouble answers one of them, and each one is a question the business already asks out loud.

| Category | The question it answers | Topic pages |
|---|---|---|
| Acquisition | Where did they come from, and what did it cost to get them? | [attribution](../../metrics/attribution.md) · CAC *(planned)* |
| Conversion | Do they reach value, where do they stall, and how long does it take? | [conversion rate](../../metrics/conversion-rate.md) · [time to convert](../../metrics/time-to-convert.md) |
| Engagement | Are they using it, and how much? | [active users](../../metrics/active-users.md) |
| Retention | Do they come back, and for how long? | [retention](../../metrics/retention.md) · value retention *(planned)* · LTV *(planned)* |
| Money | What does this earn, and what does it cost to serve? | revenue · cost and margin *(both planned; shared with [Module 4](../04-governance-and-financial-reporting/README.md))* |
| Cross-cutting | Applies to all five above | segmentation *(planned)* · benchmarks *(planned)* |

Coverage matters more than order. If you can answer four of these and have never asked the other two, one of those two is where you get surprised.

### Units, by category

Each category holds three kinds of unit: the **topic** page that teaches the metric, the **patterns** that are specific ways of working on it, and the **skills** that walk you through defining it for your own business.

#### Acquisition

| Unit | What it resolves | Type | Status |
|---|---|---|---|
| [Attribution](../../metrics/attribution.md) | Who gets credit for an outcome, and which model to pick at your size | topic | drafted |
| [Check attribution by turning it off](checking-attribution-by-turning-it-off.md) | How to test an attribution belief when you cannot run a clean holdout | pattern | drafted |
| [Attribution design](../../../skill/attribution-design/SKILL.md) | Picking the credit rule, and aligning it with team incentives | skill | draft |
| The budget distortion loop | What happens when the harvesting channel takes credit from the creating one | pattern | candidate |

#### Conversion

| Unit | What it resolves | Type | Status |
|---|---|---|---|
| [Conversion rate](../../metrics/conversion-rate.md) | The four definition choices, and how much funnel to instrument | topic | drafted |
| [Time to convert](../../metrics/time-to-convert.md) | Speed as its own metric, and the pipeline as a queue | topic | drafted |
| Count the weight of a step, not the number of steps | Why lengthening a checkout can raise conversion | pattern | candidate |
| Separate whether they convert from how fast they convert | The two questions a blended average hides | pattern | candidate |

#### Engagement

| Unit | What it resolves | Type | Status |
|---|---|---|---|
| [Active users](../../metrics/active-users.md) | The four definition choices, the windows and ratios, and the vanity test | topic | drafted |
| [Redefining a metric in the open](redefining-a-metric-in-the-open.md) | How to change a definition, or repair a broken one, without losing trust | pattern | drafted |
| Is this a vanity metric? | Whether a number anyone can move is worth reporting | skill | candidate |

#### Retention

| Unit | What it resolves | Type | Status |
|---|---|---|---|
| [Retention](../../metrics/retention.md) | Entity retention: the window, the cohort curve, why curves flatten | topic | drafted |
| [State-based retention measurement](state-based-retention-measurement.md) | Decomposing an aggregate into states, and goaling one transition rate | pattern | drafted |
| The sorting effect | Retention rates that improve for years while nobody becomes more loyal | pattern | candidate |
| The curve that could not exist | A rising cohort curve diagnosed as two plans sharing one chart | pattern | candidate |

#### Money

Shared with [Module 4](../04-governance-and-financial-reporting/README.md), which owns the reporting and governance half. Module 1A owns the definitions.

| Unit | What it resolves | Type | Status |
|---|---|---|---|
| Revenue under usage-based pricing | What counts as revenue when the meter never stops | topic | candidate |
| Cost and margin for AI products | Inference cost per user, and margin when usage is the price | topic | candidate |

#### Cross-cutting

| Unit | What it resolves | Type | Status |
|---|---|---|---|
| Segmentation | Where the manufacturing lens stops working | topic | ready |
| Benchmarks, and how to check a number before you steer by it | What to do when a famous figure will not trace | topic | ready |
| Defining your definitions | Getting to one written definition per metric, with a name on it | skill | ready |

## 1B — Data integrity

Whether the number the pipeline returns is the number the definition asks for. All rows below are `candidate` until the Phase 0 prior-art review cuts the list; the backlog is the source of truth.

| ID | Working title | Target |
|---|---|---|
| M1-01 | Single point of metric computation | v0.1.0 |
| M1-02 | Statistical process control for data pipelines | v0.1.0 |
| M1-03 | Detecting plausible-but-wrong outputs | v0.1.0 |
| M1-04 | Golden question sets for AI analytics validation | v0.1.0 |
| M1-07 | Schema drift detection and data contracts | v0.1.0 |
| M1-05 | Agreement measurement for analytics QA | v0.2.0 |
| M1-06 | Data quality SLOs and error budgets | v0.2.0 |
| M1-08 | The reconciliation protocol | v0.2.0 |
| M1-09 | Measuring trust, not just accuracy | v0.2.0 |
| M1-10 | Data incident root cause analysis | v0.2.0 |

M1-01 sits on the seam: it is the pattern that makes one definition physically enforceable, which is why a definition defect and an integrity defect can be told apart at all.

## Control-plan template

Every module ships at least one. Home: [`templates/01-ai-data-quality/`](../../../templates/01-ai-data-quality/).
