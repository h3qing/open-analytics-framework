---
id: conversion
title: Conversion
type: topic
status: stub # structure and interview questions only, per AGENTS.md constraint 6; sources researched and verified 2026-08-03
summary: >
  What conversion is, where it ends and activation and retention begin,
  why a rate between two funnel steps is worth a small team's attention,
  how conversion drives CAC and chains into LTV, and the classical ways
  to visualize a funnel. Patterns and case studies for working on
  conversion hang off this page.
keywords:
  - conversion
  - funnel
  - drop-off
  - CAC
  - A/B testing
  - activation
---

# Conversion

[TODO(heqing): one-paragraph opening in your voice — what question conversion answers about a business, for a reader who has never had an analyst.]

## What conversion is

Scope: a rate between two funnel steps. Meaningless until four choices are fixed: the numerator event, the denominator population, the entity (visit, visitor, user, account, lead), and the window (how long after entering the denominator an entity may still convert). The classic definition fights — visits vs. unique visitors in the denominator [KAUSHIK-2006], delayed conversions and the window problem [KOHAVI-2007].

- [TODO(heqing): interview — what entity/event/window should a team's first conversion metric use, and how does the choice differ for e-commerce checkout vs. B2B lead-to-contract vs. an internal tool's adoption funnel? Does quote-to-order behave like a web funnel?]
- [TODO(heqing): interview — the most common conversion-definition mistake you have seen before a team had an analyst.]

## Not activation, not retention

Scope: the boundary section. Conversion is a step-ratio at a moment in the journey; activation is the specific conversion into first realized value; retention is whether the converted entity keeps coming back — see [retention](retention.md). The AARRR framing puts a conversion rate at every step of the journey [MCCLURE-2007].

- [TODO(heqing): interview — where do you draw the conversion/activation boundary in practice? Is "activated" just one more named conversion step, or does it deserve separate treatment?]

## Why conversion is worth measuring

Scope: three classical arguments, each with a real story behind it. A single friction point at a bottleneck step can carry enormous value — the "$300 Million Button," where replacing a forced-registration button with "Continue" raised purchases 45% [SPOOL-2009]. Expert opinion reliably mispredicts what converts — the HiPPO problem, with checkout "upgrades" that destroyed revenue [KOHAVI-2007] and an Amazon feature an SVP forbade that won its test decisively [LINDEN-2006]. And conversion is where qualitative friction becomes quantifiable.

- [TODO(heqing): interview — your strongest one-paragraph case for a founder who watches signups and revenue but has never looked at the rate between them.]

## Conversion, CAC, and the funnel math

Scope: funnel-step rates multiply; CAC is spend divided by conversions, so CAC moves inversely with conversion; conversion hands off to retention, and the product of the two chains into LTV:CAC [SKOK-2013]. Bridge to the same section on the [retention page](retention.md).

- [TODO(heqing): interview — is last-touch attribution good enough for a small team to start? When does attribution modeling stop being worth their attention?]
- [TODO: figure — the funnel-rates → CAC → LTV:CAC chain, drawn simply.]

## Classical ways to see it

Scope: the standard visualizations, each with a figure per the presentation guidance in [the pattern template](../pattern-template.md):

- **The funnel chart** — the century-old funnel metaphor applied to measured step rates.
- **Step / drop-off analysis** — conversion measured per step, conditioned on the users who actually reached that step [KOHAVI-2007].
- **Cohorted conversion and conversion windows** — conversion by start cohort, and the curve of conversions arriving over time. Honest note: unlike retention's cohort heatmap, no single classical source owns this chart; the page teaches the idea plainly.

- [TODO(heqing): interview — which visualization first: a conversion trend line, a funnel bar chart, or step-by-step drop-off? Which are decoration until a certain volume? And when is the funnel the wrong model — loops, long research phases, sales-assisted journeys?]
- [TODO(heqing): interview — what rule of thumb do you give a low-traffic team asking "is this +2% real?" — and when should they refuse to A/B test at all and just watch the trend?]
- [TODO: figures — funnel with step rates, and a drop-off bar chart with obviously-placeholder numbers.]

## Patterns & case studies

No pattern page yet. Candidate case studies, all first-party accounts, verified 2026-08-03:

- **The $300 Million Button** — a drop-off located at one checkout step, qualitative research explaining why, a one-word fix, a measured $300M/year gain [SPOOL-2009]. The complete conversion loop in miniature, doable with zero analysts.
- **The Obama 2008 splash-page experiment** — intuition favored video and "Sign Up"; the test said otherwise, and each signup was valued downstream at ~$21 in donations [SIROKER-2010].
- **Experiments at Airbnb** — the measurement-discipline counterweight: the peeking problem, and a "neutral" redesign that was a >2% win hidden by a browser bug [OVERGOOR-2014].

## Sources & Stories

The stories above are the spine: Jared Spool's $300 Million Button [SPOOL-2009], Dan Siroker's first-party account of the Obama campaign's splash-page test [SIROKER-2010], and Jan Overgoor's account of experimentation at Airbnb [OVERGOOR-2014]. The classical definition and measurement treatment draws on Avinash Kaushik's conversion-rate writing [KAUSHIK-2006], the Microsoft experimentation team's KDD paper [KOHAVI-2007], Dave McClure's AARRR framing [MCCLURE-2007], Greg Linden's early-Amazon story [LINDEN-2006], and David Skok's SaaS metrics work for the CAC/LTV connection [SKOK-2013].

[TODO: synthesis pending — full research memo with per-section sources, reserve anecdotes, and known gaps is on file; author interview and voice pass to follow.]
