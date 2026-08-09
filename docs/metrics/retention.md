---
id: retention
title: Retention
type: topic
status: stub # author's opening and first answers in place 2026-08-08; research round running, draft next
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

You spent all the time and energy getting the user finally to be a part of your monthly paying group. Now what? Retention is the science of getting your user to keep engaging with your product, to keep getting value from it, and to become a long-running revenue-generating unit for your business.

Retention can be measured and tailored to your own business, but the whole point of it is the same everywhere: keep your customer happy, so they come back to you and keep adding value.

## What retention is

Scope: the definition a founder can actually use. A retention number is meaningless until three choices are fixed: the entity (user, account, workspace), the activity event (what counts as "came back"), and the window (day, week, month).

Retention could be almost anything. It could be your typical user activities. It could be your B2B accounts coming back to you year over year. It could be a dollar amount, the enterprise contracts you keep signing. What matters is the fundamental value your company is trying to create over the long term, because that is the thing you are trying to retain.

The most common definition mistake is copying someone else's. A famous retention model, Duolingo's for instance, may have nothing to do with your business, and a definition being well known does not make it yours. Look at your retention definition and ask whether it actually contributes to your north star. If it does not, it is the wrong definition, however respectable its pedigree.

## Two kinds of retention, and the hybrid

Scope: the split this page is built on, and the reason the same word causes arguments between teams.

Retention divides into two kinds. The first is retention of the entity: users, accounts, activity, whether they come back. The second is retention of the amount: contract value, whether the dollars renew and expand. Then there is the hybrid world, where revenue and churn combine into lifetime value.

- [TODO: research round in progress — verified sources for gross and net revenue retention, logo versus dollar churn, and where the two kinds of retention disagree.]

## The other side of churn

Scope: retention and churn are complements. For a fixed cohort and window, they sum to one. The interesting content is when each framing earns its place.

- [TODO(heqing): interview — with the two-kinds split above in place, does the churn framing belong mostly to the dollar side (finance, LTV, renewals) and the retention framing to the entity side (product, engagement loops)? Or do both sides need both words?]

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
