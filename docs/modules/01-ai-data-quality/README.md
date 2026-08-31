# Module 1 — AI data quality measurement and improvement

> Scope: the quality of the whole measurement system — both whether you are measuring the right thing and whether the number you get back is right. Covers metric definition, instrumentation, statistical control, validation, and the trust signals built on them. Does not cover: model selection, prompting, or benchmark performance; infrastructure design (Module 2); agent deployment mechanics (Module 3); metric change control as a governance process (Module 4).

**Status:** charter plus first drafted pattern. This is the opening module. Patterns land here after prior-art review and interview or source-synthesis sessions; the working list lives in [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md).

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

[TODO(heqing): the failure this module prevents, in one paragraph, in your voice. Say which half you have watched fail more often, and why the two are one module rather than two. Interview question to be generated in session.]

## 1A — Definition quality

What to measure, and how to pin a definition down so it holds. The durable knowledge lives in the [metrics library](../../metrics/README.md), one page per classical metric; the patterns here are sourced ways of working on a metric, with their case studies attached.

| ID | Pattern | Status | Key sources |
|---|---|---|---|
| M1-11 | [State-based retention measurement](state-based-retention-measurement.md) | drafted — awaiting author voice pass | Duolingo growth model (Gustafson, Mazal) |

Topic pages currently drafted: [attribution](../../metrics/attribution.md), [conversion rate](../../metrics/conversion-rate.md), [time to convert](../../metrics/time-to-convert.md), [active users](../../metrics/active-users.md), [retention](../../metrics/retention.md). Planned topics and guided skills are backlog rows `MX-*` and `SK-*`.

## 1B — Data integrity

Whether the number the pipeline returns is the number the definition asks for. Rows without a link are `candidate` until the Phase 0 prior-art review cuts the list; the backlog is the source of truth.

| ID | Working title | Target |
|---|---|---|
| M1-01 | [Single point of metric computation](single-point-of-metric-computation.md) | v0.1.0 |
| M1-02 | [Statistical process control for data pipelines](statistical-process-control-for-pipelines.md) | v0.1.0 |
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
