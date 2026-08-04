---
id: conversion
title: Conversion
type: topic
status: drafted # full sourced draft; awaiting author voice pass per AGENTS.md constraint 6
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

In my professional work experiences, funnel analysis played an integral role. One part of the company's business is working with domain experts who create training data for AI models. An expert passes several steps before they can contribute: identity checks, quality screens, and training on the platform. Each step loses people. My role was the analytics function: measuring the pass rate at every step and segmenting to see which experts were getting stuck and where, so the team could fix the worst step and measure again. If your product has steps between signup and value, you have the same problem, and the same method works.

<!-- TODO(heqing): voice pass -->

## What conversion is

A conversion rate is the fraction of entities that pass from one funnel step to the next. That sounds like one number. It is really four choices, and the rate means nothing until all four are written down and held fixed.

| Choice | The question | What goes wrong when it floats |
|---|---|---|
| Entity | Do you count visits, unique visitors, users, accounts, or leads? | This is the classic definition fight. Kaushik argues for unique visitors over visits, since buying spans multiple sessions, and concedes the opposite convention exists. His larger point is that consistency matters more than the choice [KAUSHIK-2006]. |
| Numerator event | What exactly counts as converting? | Fix the business outcome first, then measure. Kaushik's rule is to never measure conversion before the goals of the site are named, and to show the revenue next to the percentage [KAUSHIK-2006]. |
| Denominator population | Who was actually eligible to convert? | Condition on the entities that reached the step. Including everyone else adds noise to the comparison [KOHAVI-2007]. |
| Window | How long after entering the denominator may an entity still convert? | Conversions arrive late. The experimentation literature calls these delayed or latent conversions [KOHAVI-2007]. With an unclosed window the rate is a moving target, not a number [BERNHARDSSON-2017]. |

The early canonical definition, from the web experimentation literature, is the percentage of visits that include a purchase [KOHAVI-2007]. Note that it silently fixes all four choices: visit, purchase, visits to the site, within the visit. Your funnel will need its own four answers. The modern book-length treatment of measuring these things trustworthily is [KOHAVI-2020].

- [TODO(heqing): interview — what entity/event/window should a team's first conversion metric use, and how does the choice differ for e-commerce checkout vs. B2B lead-to-contract vs. an internal tool's adoption funnel? Does quote-to-order behave like a web funnel?]
- [TODO(heqing): interview — the most common conversion-definition mistake you have seen before a team had an analyst.]

## Not activation, not retention

Conversion is a step ratio at a moment in the journey, and the journey has many such moments. The AARRR framing puts a conversion rate at every step from acquisition through revenue, and advises picking a handful of steps and measuring each one [MCCLURE-2007]. Two neighboring ideas get folded into "conversion" and should not be.

**Activation** is one specific conversion: the one into first realized value. The modern working definition is a key action, at a set frequency, by a set time after signup. Pinterest's was users still saving content weekly, four weeks after signup [WINTERS-2017]. A survey of over 500 products gives activation-rate benchmarks by product type and warns explicitly against conflating activation with conversions or transactions [RACHITSKY-2022].

**Retention** is what happens after the conversion: whether the converted entity keeps coming back. Conversion asks whether they passed the step. Retention asks whether they stayed. That side of the story lives on the [retention page](retention.md).

- [TODO(heqing): interview — where do you draw the conversion/activation boundary in practice? Is "activated" just one more named conversion step, or does it deserve separate treatment?]

## Why conversion is worth measuring

Three classical arguments, each with a real story behind it.

1. **A single friction point at a bottleneck step can carry enormous value.** The "$300 Million Button" is the canonical story: a large retailer's checkout demanded registration before purchase. Replacing the Register button with Continue, plus one sentence saying an account was optional, raised purchases 45 percent, worth $15 million the first month and $300 million the first year [SPOOL-2009].
2. **Expert opinion reliably mispredicts what converts.** The experimentation literature names this the HiPPO problem, for the highest paid person's opinion. Its examples include a checkout page that was "upgraded" and lost most of its revenue, and a coupon-code field whose removal raised conversion by 6.5 percent [KOHAVI-2007]. At early Amazon, a senior vice president forbade shopping-cart recommendations for fear of distracting buyers from checkout. The engineer ran a controlled test anyway, the feature won by a wide margin, and it shipped [LINDEN-2006].
3. **Conversion is where qualitative friction becomes quantifiable.** In the $300 Million Button story, usability sessions surfaced the frustration in customers' own words, and the database put numbers on it: 45 percent of customers had multiple registrations, the site handled 160,000 password-reset requests a day, and 75 percent of the people requesting one never completed their purchase [SPOOL-2009]. The listening located the problem. The counting sized it.

The modern process argument goes one step further: conversion work as a standing tempo of testing rather than a one-off fix, run by a cross-functional team on a regular cadence [ELLIS-2017] [ELLIS-2024]. The tempering voice is worth hearing alongside it. Verna warns low-volume teams away from button-color micro-optimization and from chasing statistical significance their traffic cannot support; sometimes judgment has to decide [VERNA-2025].

- [TODO(heqing): interview — your strongest one-paragraph case for a founder who watches signups and revenue but has never looked at the rate between them.]
- [TODO(heqing): interview — where is your line between "run the test", "watch the trend", and "just decide"? Verna argues low-volume teams should sometimes trust judgment over significance [VERNA-2025]; Kohavi supplies the sample-size math [KOHAVI-2007].]

## Conversion, CAC, and the funnel math

Funnel step rates multiply. If 40 percent of visitors sign up, half of signups finish setup, and half of those purchase, then 10 percent of visitors purchase, because the overall rate is the product of the step rates. This arithmetic is what connects conversion to the money metrics. Customer acquisition cost is what you spend divided by how many customers come out of the funnel, so CAC moves inversely with conversion: double the funnel's overall rate and the same spend acquires customers at half the cost [SKOK-2013]. Downstream, the customer's lifetime value depends on retention, and the SaaS metrics literature frames the whole business question as whether LTV sufficiently exceeds CAC, with a ratio above three as the commonly cited guideline [SKOK-2013].

```mermaid
flowchart LR
    SP["Acquisition spend"] --> VIS["Visitors"]
    VIS -->|"funnel step rates multiply"| NC["New customers"]
    SP --> CAC["CAC = spend / new customers"]
    NC --> CAC
    NC --> RET["Retention"]
    RET --> LTV["LTV"]
    CAC --> RATIO["LTV vs. CAC"]
    LTV --> RATIO
```

Conversion hands the customer to retention, and the two multiply into everything after. The same chain is drawn from the other end on the [retention page](retention.md).

- [TODO(heqing): interview — is last-touch attribution good enough for a small team to start? When does attribution modeling stop being worth their attention?]

## Classical ways to see it

The standard visualizations, per the presentation guidance in [the pattern template](../pattern-template.md). All numbers in the figures below are round placeholders, not benchmarks.

**The funnel chart** — the century-old funnel metaphor applied to measured step rates. Steps in order, counts and pass rates at each:

```mermaid
flowchart TD
    V["Visit the site: 1,000 enter (placeholder)"] -->|"step rate 40%"| S["Start signup: 400"]
    S -->|"step rate 50%"| C["Complete setup: 200"]
    C -->|"step rate 50%"| P["First purchase: 100"]
```

**Step / drop-off analysis** — conversion measured per step, conditioned on the entities that actually reached that step [KOHAVI-2007]. The funnel chart shows where the counts shrink; the per-step view shows which rate is worst, which is a different question, because a step early in the funnel can lose more people at a better rate.

**Cohorted vs. blended conversion** — the aggregate (blended) rate lies in known ways. With a growing user base and slow conversion, new users flood the denominator before they have had time to convert, so the blended rate falls while every cohort is healthy [BERNHARDSSON-2017]. Mix shifts can do the reverse trick inside an experiment: a published case shows a treatment that looked 4 percent worse in aggregate while being better on almost every individual day, Simpson's paradox caused by changing the traffic split mid-experiment [KOHAVI-2010]. Cohorting by start date separates conversion likelihood from conversion speed [BERNHARDSSON-2017].

```mermaid
xychart-beta
    title "Placeholder sketch of the blended-rate illusion"
    x-axis "Week since launch" 1 --> 8
    y-axis "Conversion rate in percent" 0 --> 12
    line [10, 10, 10, 10, 10, 10, 10, 10]
    line [10, 9, 8, 7, 6, 6, 5, 5]
```

The flat line is each weekly cohort's eventual conversion rate, held at a placeholder 10 percent. The falling line is the blended rate measured each week while signups grow: the newest users have not had time to convert, and they dominate the denominator. Nothing got worse. The other side of the trade: fixed-window blended rates are cheap, computable in plain SQL, and legible to stakeholders, and modeling pays off only when the window or the timing itself matters [KENT-2021]. A blended number can still earn a place in executive reporting alongside the cohorted view [BEREZOVSKY-2024].

**The time-to-convert curve** — conversions arriving over time since cohort start, the survival-analysis view: entities that have not converted yet are censored, not failed, and the curve shows when a window can honestly be closed [BERNHARDSSON-2017] [KENT-2021]. A go-deeper pointer for most small teams, but the concept fits in one figure:

```mermaid
xychart-beta
    title "Placeholder sketch of one cohort's conversions over time"
    x-axis "Days since cohort start" 0 --> 60
    y-axis "Cumulative conversion in percent" 0 --> 12
    line [0, 4, 6, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10]
```

Where the curve flattens is where the window can close. Before that point, any rate you quote is still moving.

**When the funnel is the wrong model** — the modern growth-loops critique argues that funnels describe one-way flow, while fast-growing products often grow through closed loops whose output feeds back in as input [BALFOUR-2018]. Loops, long research phases, and sales-assisted journeys all strain the funnel picture.

- [TODO(heqing): interview — which visualization first: a conversion trend line, a funnel bar chart, or step-by-step drop-off? Which are decoration until a certain volume?]
- [TODO(heqing): interview — do Kent's triggers for graduating from a fixed window to time-to-convert curves match your experience? What volume or lag threshold made you switch, if ever?]
- [TODO(heqing): interview — when reporting upward, did you keep a blended conversion number next to the cohorted views, and how did you stop the blended one from misleading?]

## Finding and fixing the bottleneck

The practitioner methodology on record is an audit: instrument the funnel end to end, measure the drop-off at every step, find the largest one, and start there, which in product-led funnels is often the activation step [QU-2023]. The loop parallels the coarse-first bottleneck hunt in the [state-based retention pattern](../modules/01-ai-data-quality/state-based-retention-measurement.md): rough-locate the loss, get a qualitative anecdote for why it happens, attempt a fix, and re-measure. The opening story on this page is the same loop run on an expert-onboarding funnel.

Honest note: no vendor-neutral practitioner treatment applies the theory of constraints to conversion funnels — the search was run and came up empty. This is original-content territory for this framework.

- [TODO(heqing): interview — as an industrial engineer, does Goldratt's five-focusing-steps logic transfer to a funnel? Where does the analogy break: funnels lose units permanently rather than queueing them, steps are not machines with capacity, the "bottleneck" is a rate rather than a throughput limit.]
- [TODO(heqing): interview — after you fixed the worst funnel step in a real deployment, where did the constraint move next, and how quickly did the team notice?]

## Patterns & case studies

No pattern page yet. The funnel-audit methodology [QU-2023] is a candidate seed for the first conversion pattern. One finding from the research is worth recording: public conversion work is narrated almost entirely as single experiments, and no multi-year program account equivalent to the Duolingo retention story surfaced. Candidate case studies, all first-party accounts, verified 2026-08-03:

- **The $300 Million Button** — a drop-off located at one checkout step, qualitative research explaining why, a one-word fix, a measured $300M/year gain [SPOOL-2009]. The complete conversion loop in miniature, doable with zero analysts.
- **The Obama 2008 splash-page experiment** — a multivariate test of four buttons and six media panels over roughly 310,000 visitors. Intuition favored video and a "Sign Up" button; the winner was "Learn More" with a family photo, lifting signups from 8.26 to 11.6 percent. Each signup was valued downstream at about $21 in donations, which is the bridge from a conversion rate to LTV thinking [SIROKER-2010].
- **Experiments at Airbnb** — the measurement-discipline counterweight: a test that looked significant at day seven and converged to neutral, answered by pre-committing sample size, and a "neutral" search redesign that was a greater than 2 percent booking win hidden by a browser bug, found only by segmenting [OVERGOOR-2014].

## Sources & Stories

The stories above are the spine: Jared Spool's $300 Million Button [SPOOL-2009], Dan Siroker's first-party account of the Obama campaign's splash-page test [SIROKER-2010], and Jan Overgoor's account of experimentation at Airbnb [OVERGOOR-2014]. The classical definition and measurement treatment draws on Avinash Kaushik's conversion-rate writing [KAUSHIK-2006], the Microsoft experimentation team's KDD paper [KOHAVI-2007], Dave McClure's AARRR framing [MCCLURE-2007], Greg Linden's early-Amazon story [LINDEN-2006], and David Skok's SaaS metrics work for the CAC/LTV connection [SKOK-2013].

The modern, instrumentation-era layer: Erik Bernhardsson's cohort-conversion and survival-curve treatment from his Spotify and Better work [BERNHARDSSON-2017], the Kohavi lineage's published mix-shift pitfalls [KOHAVI-2010] and book-length successor [KOHAVI-2020], Casey Winters on activation [WINTERS-2017], the Rachitsky–Timen activation-rate survey [RACHITSKY-2022], the growth-loops critique of the funnel itself [BALFOUR-2018], and product-manager voices from the podcast circuit — Hila Qu on funnel auditing [QU-2023], Sean Ellis on the testing tempo [ELLIS-2024] alongside the book [ELLIS-2017], and Elena Verna on what not to optimize [VERNA-2025].

The opening story is from the author's own practice, on an expert-onboarding funnel, and the theory-of-constraints treatment in the bottleneck section is reserved as the author's original contribution. Placeholder figures on this page use deliberately round invented numbers and are not benchmarks.
