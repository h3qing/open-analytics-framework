# Decisions

One entry per judgment call: decision, alternatives, why.

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

## 2026-08-03 — Metrics library added as the knowledge layer

**Decision:** Classical metric knowledge gets its own layer: `docs/metrics/`, one topic page per metric (retention first; active users, revenue, cost, margins, usage to follow). A topic page teaches the metric — definition, why it matters, connections to adjacent metrics, classical visualizations — and patterns become sourced ways of working on a topic, with their case studies attached (the Duolingo state-model pattern is one way to work on retention). Skills are confirmed as the eventual guided layer: developing each metric in a user's specific business context. The four-module set is no longer treated as fixed; modules can expand as the structure evolves. Topic pages carry the same Sources & Stories requirement, and the CI check now covers `docs/metrics/`.

**Alternatives:** Keep patterns as the only content unit; fold metric knowledge into module charters; wait for Phase 0 to merge first.

**Why:** A reader searching for help arrives thinking "retention," not "state-based measurement pattern M1-11." Leading with the metric matches how the audience actually asks the question, and gives every future pattern and skill a stable home to hang off. This partially supersedes the 2026-07-30 skills deferral: the destination is now committed; the build order still waits on Phase 0.
