# Decisions

One entry per judgment call: decision, alternatives, why.

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
