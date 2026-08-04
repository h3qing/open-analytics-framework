---
id: conversion
title: Conversion
type: topic
status: stub # structure and interview questions only, per AGENTS.md constraint 6; sources researched and verified 2026-08-03, modern-sources round 2026-08-04
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

Scope: a rate between two funnel steps. Meaningless until four choices are fixed: the numerator event, the denominator population, the entity (visit, visitor, user, account, lead), and the window (how long after entering the denominator an entity may still convert). The classic definition fights — visits vs. unique visitors in the denominator [KAUSHIK-2006], delayed conversions and the window problem [KOHAVI-2007]. The window is not a detail: with an unclosed window, the rate is a moving target, not a number [BERNHARDSSON-2017]. The modern book-length treatment of trustworthy measurement is [KOHAVI-2020].

- [TODO(heqing): interview — what entity/event/window should a team's first conversion metric use, and how does the choice differ for e-commerce checkout vs. B2B lead-to-contract vs. an internal tool's adoption funnel? Does quote-to-order behave like a web funnel?]
- [TODO(heqing): interview — the most common conversion-definition mistake you have seen before a team had an analyst.]

## Not activation, not retention

Scope: the boundary section. Conversion is a step-ratio at a moment in the journey; activation is the specific conversion into first realized value; retention is whether the converted entity keeps coming back — see [retention](retention.md). The AARRR framing puts a conversion rate at every step of the journey [MCCLURE-2007]. The modern working definition of activation is a key action at a set frequency by a set time after signup — Pinterest's was weekly savers four weeks in [WINTERS-2017] — and the practitioner survey literature warns explicitly against conflating activation with conversion, with benchmarks by product type [RACHITSKY-2022].

- [TODO(heqing): interview — where do you draw the conversion/activation boundary in practice? Is "activated" just one more named conversion step, or does it deserve separate treatment?]

## Why conversion is worth measuring

Scope: three classical arguments, each with a real story behind it. A single friction point at a bottleneck step can carry enormous value — the "$300 Million Button," where replacing a forced-registration button with "Continue" raised purchases 45% [SPOOL-2009]. Expert opinion reliably mispredicts what converts — the HiPPO problem, with checkout "upgrades" that destroyed revenue [KOHAVI-2007] and an Amazon feature an SVP forbade that won its test decisively [LINDEN-2006]. And conversion is where qualitative friction becomes quantifiable. The modern process case is a standing testing tempo rather than one-off fixes [ELLIS-2017] [ELLIS-2024] — tempered by the practitioner warning against button-color micro-optimization and significance-chasing at low volume [VERNA-2025].

- [TODO(heqing): interview — your strongest one-paragraph case for a founder who watches signups and revenue but has never looked at the rate between them.]
- [TODO(heqing): interview — where is your line between "run the test", "watch the trend", and "just decide"? Verna argues low-volume teams should sometimes trust judgment over significance [VERNA-2025]; Kohavi supplies the sample-size math [KOHAVI-2007].]

## Conversion, CAC, and the funnel math

Scope: funnel-step rates multiply; CAC is spend divided by conversions, so CAC moves inversely with conversion; conversion hands off to retention, and the product of the two chains into LTV:CAC [SKOK-2013]. Bridge to the same section on the [retention page](retention.md).

- [TODO(heqing): interview — is last-touch attribution good enough for a small team to start? When does attribution modeling stop being worth their attention?]
- [TODO: figure — the funnel-rates → CAC → LTV:CAC chain, drawn simply.]

## Classical ways to see it

Scope: the standard visualizations, each with a figure per the presentation guidance in [the pattern template](../pattern-template.md):

- **The funnel chart** — the century-old funnel metaphor applied to measured step rates.
- **Step / drop-off analysis** — conversion measured per step, conditioned on the users who actually reached that step [KOHAVI-2007].
- **Cohorted vs. uncohorted conversion** — when to use which. An aggregate (blended) rate lies in known ways: with a growing user base and slow conversion, new users flood the denominator before they have had time to convert, so the blended rate falls while every cohort is healthy [BERNHARDSSON-2017]; mix shifts can make an aggregate look worse while every single day looks better — Simpson's paradox in a published experiment [KOHAVI-2010]. Cohorting by start date separates conversion likelihood from conversion speed [BERNHARDSSON-2017]. The other side: fixed-window uncohorted rates are cheap, SQL-only, and stakeholder-legible, and modeling pays off only when the window or timing itself matters [KENT-2021] — and a blended number still earns a place in executive reporting alongside the cohorted view [BEREZOVSKY-2024].
- **The time-to-convert curve** — conversions arriving over time since cohort start, the survival-analysis view: entities that have not converted *yet* are censored, not failed, and the curve shows when a window can honestly be closed. A go-deeper pointer for most small teams, but the concept fits in one figure [BERNHARDSSON-2017] [KENT-2021].
- **When the funnel is the wrong model** — the modern growth-loops critique argues funnels misdescribe products that grow through closed loops rather than one-way flow [BALFOUR-2018]; loops, long research phases, and sales-assisted journeys all strain the funnel picture.

- [TODO(heqing): interview — which visualization first: a conversion trend line, a funnel bar chart, or step-by-step drop-off? Which are decoration until a certain volume?]
- [TODO(heqing): interview — do Kent's triggers for graduating from a fixed window to time-to-convert curves match your experience? What volume or lag threshold made you switch, if ever?]
- [TODO(heqing): interview — when reporting upward, did you keep a blended conversion number next to the cohorted views, and how did you stop the blended one from misleading?]
- [TODO: figures — funnel with step rates, a drop-off bar chart, and a cohort time-to-convert curve, all with obviously-placeholder numbers.]

## Finding and fixing the bottleneck

Scope: how a team locates the binding constraint step and addresses it. The practitioner methodology on record: audit the funnel end-to-end, find the largest drop-off, and start there — often activation [QU-2023]. The loop parallels the coarse-first bottleneck hunt in the [state-based retention pattern](../modules/01-ai-data-quality/state-based-retention-measurement.md): rough-locate the loss, get a qualitative anecdote for why, attempt a fix, re-measure — and expect the constraint to move once fixed.

Honest note: no vendor-neutral practitioner treatment applies the theory of constraints to conversion funnels — the search was run and came up empty. This is original-content territory for this framework.

- [TODO(heqing): interview — as an industrial engineer, does Goldratt's five-focusing-steps logic transfer to a funnel? Where does the analogy break: funnels lose units permanently rather than queueing them, steps are not machines with capacity, the "bottleneck" is a rate rather than a throughput limit.]
- [TODO(heqing): interview — after you fixed the worst funnel step in a real deployment, where did the constraint move next, and how quickly did the team notice?]

## Patterns & case studies

No pattern page yet. The funnel-audit methodology [QU-2023] is a candidate seed for the first conversion pattern. Candidate case studies, all first-party accounts, verified 2026-08-03:

- **The $300 Million Button** — a drop-off located at one checkout step, qualitative research explaining why, a one-word fix, a measured $300M/year gain [SPOOL-2009]. The complete conversion loop in miniature, doable with zero analysts.
- **The Obama 2008 splash-page experiment** — intuition favored video and "Sign Up"; the test said otherwise, and each signup was valued downstream at ~$21 in donations [SIROKER-2010].
- **Experiments at Airbnb** — the measurement-discipline counterweight: the peeking problem, and a "neutral" redesign that was a >2% win hidden by a browser bug [OVERGOOR-2014].

## Sources & Stories

The stories above are the spine: Jared Spool's $300 Million Button [SPOOL-2009], Dan Siroker's first-party account of the Obama campaign's splash-page test [SIROKER-2010], and Jan Overgoor's account of experimentation at Airbnb [OVERGOOR-2014]. The classical definition and measurement treatment draws on Avinash Kaushik's conversion-rate writing [KAUSHIK-2006], the Microsoft experimentation team's KDD paper [KOHAVI-2007], Dave McClure's AARRR framing [MCCLURE-2007], Greg Linden's early-Amazon story [LINDEN-2006], and David Skok's SaaS metrics work for the CAC/LTV connection [SKOK-2013].

The modern, instrumentation-era layer: Erik Bernhardsson's cohort-conversion and survival-curve treatment from his Spotify and Better work [BERNHARDSSON-2017], the Kohavi lineage's published mix-shift pitfalls [KOHAVI-2010] and book-length successor [KOHAVI-2020], Casey Winters on activation [WINTERS-2017], the Rachitsky–Timen activation-rate survey [RACHITSKY-2022], the growth-loops critique of the funnel itself [BALFOUR-2018], and product-manager voices from the podcast circuit — Hila Qu on funnel auditing [QU-2023], Sean Ellis on the testing tempo [ELLIS-2024] alongside the book [ELLIS-2017], and Elena Verna on what not to optimize [VERNA-2025].

[TODO: synthesis pending — two research memos with per-section sources, reserve anecdotes, and known gaps are on file; author interview and voice pass to follow.]
