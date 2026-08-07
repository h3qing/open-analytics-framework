---
id: retention
title: Retention
type: topic
status: stub # structure and interview questions only, per AGENTS.md constraint 6
summary: >
  What retention is, why it is the other side of churn, why it is worth
  measuring at all, how it drives LTV and interacts with CAC, and the
  classical ways to visualize it. Patterns and case studies for working
  on retention hang off this page.
keywords:
  - retention
  - churn
  - LTV
  - CAC
  - cohort analysis
  - retention curve
---

# Retention

[TODO(heqing): one-paragraph opening in your voice — what question retention answers about a business, for a reader who has never had an analyst.]

## What retention is

Scope: the definition a founder can actually use. A retention number is meaningless until three choices are fixed: the entity (user, account, workspace), the activity event (what counts as "came back"), and the window (day, week, month).

- [TODO(heqing): interview — what default entity/event/window conventions should this page recommend, and how should a B2C daily product vs. a B2B weekly product choose differently?]
- [TODO(heqing): interview — the most common definition mistake you have seen a team make before they had an analyst.]

## The other side of churn

Scope: retention and churn are complements — for a fixed cohort and window, they sum to one. The interesting content is when each framing earns its place.

- [TODO(heqing): interview — when do you reach for the churn framing (finance, LTV math, contract renewals?) and when for the retention framing (product work, engagement loops?), and why.]

## Why retention is worth measuring

Scope: the case for a small team spending attention here at all — the compounding effect of a retained base, retention as the signal that the product is working, and the cost asymmetry against acquisition.

- [TODO(heqing): interview — the strongest version of this argument you would make to a founder who only watches signups.]
- [TODO: verify sources for the classical claims before citing them — no unsourced assertions.]

## Retention, LTV, and CAC

Scope: retention is the input that makes LTV finite or not — the retention curve determines expected customer lifetime, LTV bounds what CAC an organization can afford, and the ratio's health depends entirely on the retention assumptions under it.

- [TODO(heqing): interview — how deep into the math should this go for the no-analyst audience? One worked example, or formulas with a diagram?]
- [TODO: figure — the retention curve → lifetime → LTV chain, drawn simply.]

## Classical ways to see it

Scope: the standard visualizations, each with a figure per the presentation guidance in [the pattern template](../pattern-template.md), and what each one is for:

- **The retention curve** — percent of a cohort still active over time since start; the flattening curve vs. the curve that decays to zero, and what each shape means.
- **The cohort table / heatmap** — cohorts as rows, age as columns; where to look on it and the patterns worth recognizing.
- **The state model** — the user base as explicit activity states with transition rates; covered in depth by the [state-based retention measurement](../modules/01-ai-data-quality/state-based-retention-measurement.md) pattern.

- [TODO(heqing): interview — which visualization should a team build first, and which are decoration until a certain size?]
- [TODO: figures — retention curve shapes and a small cohort heatmap example with obviously-placeholder numbers.]

## Patterns & case studies

- [State-based retention measurement](../modules/01-ai-data-quality/state-based-retention-measurement.md) — decompose the aggregate into user states and goal a team on the highest-leverage transition rate. Case study: the Duolingo growth model.

## Sources & Stories

[TODO: pending source synthesis — the Duolingo story is already in REFERENCES.md; classical retention/LTV/CAC treatments need to be found and verified before they are cited.]
