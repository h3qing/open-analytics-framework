# Prior art and landscape review

> Scope: the coverage matrix — one row per candidate pattern, recording what already exists publicly and what does not. This file is what makes the provenance system mean something. Status: **the full Phase 0 review is pending; rows land individually as units are synthesized.**

## Method

For each candidate pattern: search books, peer-reviewed papers, standards documents, well-known practitioner writing, and open-source project documentation, using generalized category terms only. Where prior art is found, it is cited precisely with its actual scope, not a strawman. Where nothing is found, the search terms are listed so the claim is checkable. Nothing is marked `Original` to look novel.

## Coverage matrix

| Pattern | Closest prior art | Citation key | What it covers | What it does not cover | Provisional tag |
|---|---|---|---|---|---|
| State-based retention measurement (M1-11) | Duolingo's growth model, documented by the practitioners who built it; per Mazal, itself adapted from state models at Zynga and MyFitnessPal | [GUSTAFSON-2023], [MAZAL-2023] | Seven MECE daily activity states; named transition rates (CURR, NURR, RURR, SURR, reactivation/resurrection); sensitivity simulation to select a focus metric; verifying the metric is movable and moves the topline | Application to organizations without analytics staff; low-volume weekly-window variant; reverse-funnel bottleneck framing and coarse-first instrumentation (original here); LLM-agent operationalization | Adapted |
| _remaining rows pending Phase 0_ | | | | | |

## Uncovered ground

_Pending Phase 0: where the review found genuinely uncovered territory._
