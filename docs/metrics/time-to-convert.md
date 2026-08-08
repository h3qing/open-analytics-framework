---
id: time-to-convert
title: Time to convert
type: topic
status: stub # structure and interview questions only, per AGENTS.md constraint 6; deep research round running 2026-08-08
summary: >
  How fast an entity moves through the pipeline, from the top of the
  funnel to the end. The sibling of conversion rate: the rate says how
  many get through, this says how long it takes, and the two together
  decide what a window means and how much throughput a pipeline has.
keywords:
  - time to convert
  - cycle time
  - lead time
  - sales cycle
  - time to value
  - velocity
  - Little's Law
  - survival analysis
---

# Time to convert

[TODO(heqing): one-paragraph opening in your voice — what question time to convert answers, for a reader who has never had an analyst. Your framing to draw from: it is how fast a user, good, or entity moves through the pipeline, from top of funnel to end of funnel.]

## Why speed is its own metric

Scope: [conversion rate](conversion-rate.md) counts how many entities get through. This page measures how long they take. The two are not interchangeable: a pipeline can convert the same fraction of entities twice as fast, which changes cash timing, forecast accuracy, and how quickly a fix shows up in the numbers. Speed is also what makes the rate's window an honest choice rather than an arbitrary one.

- [TODO: research round running — verified sources for the vocabulary and its origins.]

## The pipeline as a queue

Scope: the industrial-engineering view. A funnel with stages, arrivals, and work in progress is a queueing system, and time to convert is its cycle time. Little's Law relates throughput, work in progress, and cycle time; Lean distinguishes cycle time, lead time, and takt time.

- [TODO: research round running — Little's Law provenance, cycle vs. lead time definitions, and whether anyone has published this mapping for business funnels or whether it is original ground here.]
- [TODO(heqing): interview — as an industrial engineer, does the queue model hold for a customer funnel? Where does it break: entities that leave permanently rather than waiting, stages without fixed capacity, arrivals you cannot schedule?]

## Measuring it honestly

Scope: the average time to convert is usually the wrong statistic. Entities that have not converted yet are excluded from the mean, which biases it downward, and the distribution is skewed enough that the median and the 85th percentile say different things. Percentiles and survival curves are the honest forms, and the [conversion rate page](conversion-rate.md) covers where the curve flattens and a window can close.

- [TODO: research round running — accessible practitioner treatments of censoring, percentiles over averages, and forecasting from cycle-time distributions.]

## What it looks like in practice

Scope: the business vocabulary for the same idea, and where each is used: sales cycle length, time to first value, lead response time, stage-to-stage aging.

- [TODO: research round running.]
- [TODO(heqing): interview — in your own practice, which stage's duration was worth watching, and what did watching it change?]

## When speed is the wrong goal

Scope: reducing cycle time can lower the quality of what comes out the other end. The honest treatment names the trade rather than assuming faster is better.

- [TODO(heqing): interview — have you seen rushing a pipeline produce a worse cohort at the end of it?]

## Patterns & case studies

No pattern page yet. Candidates come from the research round.

## Sources & Stories

[TODO: pending research — a deep round is running on the industrial-engineering spine (Little's Law, cycle and lead time), flow metrics from software delivery, the business vocabulary, and the statistics of measuring duration honestly. Every source will be fetched and verified before it is cited here.]
