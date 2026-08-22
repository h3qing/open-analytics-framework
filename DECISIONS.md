# Decisions

One entry per judgment call: decision, alternatives, why.

## 2026-08-20 — Module 3 splits into 3A and 3B, ordered by whether the consequence can be reversed

**Decision:** two calls, made from a twelve-area research sweep with every source re-fetched and checked. (a) Module 3 names two halves, in this order: **3A, what it can reach** — authentication, permission parity, selective exposure, untrusted text, and the session record; and **3B, what it tells you** — grounding, context, evaluation, monitoring, and adoption. 3A comes first because it is the half that fails irreversibly. (b) The module is ordered by **whether the consequence can be reversed**, not whether the decision can. Module 2 orders by expiry, and expiry does not transfer here: nothing in Module 3 expires and the agent can be switched off. Granting a credential is perfectly reversible right up until a row leaves under it, and a question that was never logged has no answer three weeks later. 3A opens with a Track 0 of seven units that are the only set genuinely mandatory before an agent touches production data.

**Alternatives:** leaving the module undivided, which stops being defensible at fifty units; and splitting on "is the answer right" versus "what may the answer do", which fails the independence test because the rule for how many checks a number needs is keyed to how much the agent is trusted, so improving validation directly changes the handling rule. Access has no such coupling: no amount of grounding changes who is entitled to see the salary table.

**Why:** the same failure-mode test that produced 1A/1B and 2A/2B produces this one, and applying one test three times keeps the framework's structure explainable in a sentence. The ordering rule is this module's own contribution: irreversibility carries over from Module 2 but attaches to the consequence rather than to a deadline. The author's positions were tested rather than assumed; each survived with a stated qualifier, recorded per unit in the research memo rather than here.

## 2026-08-19 — Module 2 splits into 2A and 2B; ordered by what expires; `topic` retired outside the metrics library

**Decision:** three calls, made while laying out Module 2 against the structure Module 1 had just been given. (a) Module 2 names two halves on the same failure-mode test used for Module 1. **2A, what you build:** what should exist at this size and in what order, DMAIC's Improve. **2B, how you run it:** whether it keeps returning the right answer as the company grows, Control. (b) Inside 2A the build order is sorted by what expires rather than by importance, because a research sweep over the module's sub-areas produced five different instructions for the reader's first week and no way to choose between them; sorting by irreversibility does choose, since history a source system has already overwritten is the only thing on the list that money cannot recover later. Track 0 collects those units and everything after it is reversible. (c) `topic` is retired as a routable type outside `docs/metrics/`. Six proposed units arrived typed `topic` without being classical metrics, and `docs/metrics/` is the metrics library. A non-metric unit now has to earn a Position and ship as a pattern; anything that cannot becomes a section of a neighbouring pattern or a control plan under `templates/`.

**Alternatives:** for (a), leave Module 2 undivided, which is defensible at eleven units and stops being defensible at fifty; for (b), order by importance, by stage, or by the reader's own stated urgency, all of which reopen the five-way tie; for (c), widen `docs/metrics/` to hold infrastructure topics, which costs the library its meaning, or add a fourth content directory, which costs a CI content-dir entry and splits the reader's path.

**Why:** the two halves fail independently and their fixes share nothing, which is the same test that justified 1A and 1B, so applying it twice keeps one rule rather than two. Ordering by expiry is the only ordering the material itself supports, and it is the module's one genuinely original claim. Retiring `topic` is the cheapest of the three: it decides all six homeless units, costs nothing in CI, and is self-enforcing for Modules 3 and 4.

## 2026-08-19 — Module 1 splits into two named halves; four modules re-fixed

**Decision:** "Data quality" was carrying two unrelated meanings, and the confusion had a visible cost: the metrics library had no module home, its backlog rows sat at module `—`, and a retention-measurement pattern (M1-11) was filed in the module otherwise full of schema-drift and reconciliation work. Module 1 now names both halves explicitly. **1A, definition quality:** are we measuring the right thing, defined once and defined well — DMAIC's Define phase, with the metrics library as its knowledge layer and M1-11, `MX-*` and `SK-*` as its units. **1B, data integrity:** does the pipeline return that number correctly and stay in control — Measure through Control, holding M1-01 to M1-10. The four-module set is re-fixed as a commitment matching the project specification; `docs/metrics/` stays where it is as a cross-cutting layer whose home is 1A and whose revenue, cost and margin pages will also serve Module 4. Every backlog row now carries a module.

**Alternatives:** make the metrics library a fifth module (cleanest conceptually, contradicts the four-module commitment and `GOVERNANCE.md`); leave it as a layer belonging to no module (honest but leaves the map with a hole where the most finished work is); move the files under `docs/modules/01-.../metrics/` (mirrors the map in the directory tree, churns every cross-link, and pins future revenue and cost pages inside the wrong module).

**Why:** the two failure modes are genuinely independent — a precisely computed wrong metric and a correctly defined bad join are both quality defects with nothing in common in their fixes — and Six Sigma already separates them, which is the methodology the framework claims. Naming a division inside a module costs nothing externally, since the four modules and their titles are unchanged. This supersedes the "four-module set is no longer treated as fixed" clause of the 2026-08-03 entry; the rest of that entry stands.

## 2026-07-31 — First content unit as source-synthesis, ahead of Phase 0 (M1-11)

**Decision:** Four calls made while synthesizing the Duolingo growth model into pattern M1-11. (a) The unit was written as a full sourced draft — an author-approved exception to hard constraints 6–7 for source-synthesis units, where every claim cites public sources rather than author experience; the author's own input (retention as a reverse acquisition funnel; coarse-first bottleneck instrumentation) was captured via interview and is marked original in the doc. Status is `drafted`, never `published`, until the author's voice pass. (b) Placement: Module 1, as a measurement-architecture pattern (decomposing an untrustworthy aggregate into auditable states), with ID M1-11 targeting v0.2.0. (c) Pattern docs may carry YAML frontmatter for agent consumption — metadata above the template, not a ninth section; prompt templates and JSON specs live in the `templates/` artifact so the eight-section shape stays intact. (d) Its prior-art row was recorded individually ahead of the full Phase 0 sweep, which is what licenses the `Adapted` tag.

**Alternatives:** structure-plus-interview stub (strict constraint reading); placement in Module 2 ("rapid growth") or a cross-cutting doc; embedding prompts in the pattern body; waiting for Phase 0.

**Why:** the sources are the answers for a synthesis unit, so the interview rule's purpose (no fabricated experience) is preserved; Module 1 is the measurement module and the pattern is about making a topline measurable and actionable; the template's fixed shape is load-bearing for CI and readers; a per-unit prior-art row keeps provenance honest without blocking on the full review.

## 2026-07-30 — Module 1 opens the framework

**Decision:** Module 1 (AI data quality measurement and improvement) is the opening module.

**Alternatives:** Module 3 (AI agent integration) — faster to write, more generalizable, and closest to the deployment-layer thesis.

**Why:** Matches the committed module order so the repo reads in sequence, and pairs most directly with the Six Sigma / SPC thread that distinguishes the framework. Module 3's speed advantage matters less than a coherent opening.

## 2026-07-30 — Scaffold judgment calls (local skeleton, pre-publication)

**Decision:** Three small calls made while scaffolding locally. (a) Single `LICENSE` file containing the explanation of the dual-license split plus both full texts (CC BY 4.0 fetched from Creative Commons, MIT from SPDX), rather than a `LICENSES/` directory — matches the plan's stated structure. (b) The CI provenance check accepts `[TODO: …]` placeholders in a Provenance section, failing only on a missing section or a citation key absent from `REFERENCES.md` — otherwise every honest stub would fail CI, punishing exactly the discipline the plan asks for. (c) `CONTENT_BACKLOG.md` is populated from the uncut strawman candidate list with every row at status `candidate` and provenance `[TODO]`, so the backlog structure exists without pretending Phase 0 has run. Contributor Covenant 3.0 used, as the current version.

**Alternatives:** separate license files; strict CI from day one; empty backlog table.

**Why:** all three keep the repo honest about its actual state while matching the plan's structure exactly.

## 2026-07-30 — Analytics-skills expansion deferred until after Phase 0

**Decision:** The proposed expansion — a library of analytics skills with sourced definitions and explicit opinions, beyond the single diagnostic skill — is not entering the fixed specification yet. The spec stays at four deliverable types plus the `analytics-readiness` skill.

**Alternatives:** Amend the spec now (skills as a fifth deliverable type, `skill/` → `skills/`); or fold skills under the existing "something to adopt" principle without a spec change.

**Why:** The prior-art review will show where skills add the most over prose patterns. Amending the fixed spec before that evidence exists inverts the project's own method. Revisit when Phase 0 reports.

## 2026-08-11 — What the first five topic pages taught, written into the rules

**Decision:** Five working rules enter `AGENTS.md`, `docs/pattern-template.md` and `docs/skill-template.md`, each earned by a specific failure this session. (a) Pages are written for a reader who wants to act, never as literature reviews: sourcing status and accounts of what could not be found move to Sources & Stories. (b) Pages organize around decisions rather than concepts; the test reader ranked the page with a size guide first and the concept-shaped page last. (c) Every recommendation carries a version for a team of ten, because the framework kept advising neutral ledgers, holdout tests and controlled experiments to an audience it says has no analyst. (d) Charts that Mermaid cannot draw honestly become committed SVGs under a `figures/` directory, computed from one shared dataset when two figures argue together. (e) Draft notes live in HTML comments, never as visible list items.

**Alternatives:** leave these as per-page editorial judgment; keep forcing charts into Mermaid; keep visible TODOs as an honesty signal.

**Why:** each was found the expensive way. The literature-review register survived four review passes because no rule forbade it. Visible TODO bullets made a finished page read as a published outline. And the cohort-versus-blended argument only became obvious when it was drawn with lines of different lengths, which Mermaid cannot express at all.

## 2026-08-11 — Unverified benchmarks are named, not repeated

**Decision:** When a widely repeated figure cannot be traced to a primary source, the page says no citable number survived checking and gives the reader a way to build their own baseline instead. It does not repeat the number with a caveat attached.

**Alternatives:** cite the popular version with a hedge; stay silent about the number entirely.

**Why:** five famous figures failed tracing during this work, including one whose upper bound appears to have been introduced downstream of the source it is credited to. Repeating a number with a caveat still launders it, since the caveat travels less far than the figure. Saying plainly that it did not survive verification is both more useful and the thing this framework is unusually placed to say.

## 2026-08-03 — Metrics library added as the knowledge layer

**Decision:** Classical metric knowledge gets its own layer: `docs/metrics/`, one topic page per metric (retention first; active users, revenue, cost, margins, usage to follow). A topic page teaches the metric — definition, why it matters, connections to adjacent metrics, classical visualizations — and patterns become sourced ways of working on a topic, with their case studies attached (the Duolingo state-model pattern is one way to work on retention). Skills are confirmed as the eventual guided layer: developing each metric in a user's specific business context. The four-module set is no longer treated as fixed; modules can expand as the structure evolves. *(Superseded 2026-08-19: four modules are fixed again, and the library is a layer inside Module 1A.)* Topic pages carry the same Sources & Stories requirement, and the CI check now covers `docs/metrics/`.

**Alternatives:** Keep patterns as the only content unit; fold metric knowledge into module charters; wait for Phase 0 to merge first.

**Why:** A reader searching for help arrives thinking "retention," not "state-based measurement pattern M1-11." Leading with the metric matches how the audience actually asks the question, and gives every future pattern and skill a stable home to hang off. This partially supersedes the 2026-07-30 skills deferral: the destination is now committed; the build order still waits on Phase 0.
