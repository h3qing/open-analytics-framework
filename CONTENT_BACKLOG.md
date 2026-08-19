# Content backlog

One row per writeable unit; a unit is finishable in one 60–90 minute sitting. Statuses: `candidate` (pre prior-art review), `ready`, `in progress`, `drafted`, `published`. Rows at `candidate` are provisional until the Phase 0 prior-art review runs and the candidate list is cut by the author.

The Module column uses `1A` (definition quality) and `1B` (data integrity) for the two halves of Module 1 — see [the Module 1 charter](docs/modules/01-ai-data-quality/README.md). Metric topic pages (`MX-*`) and guided skills (`SK-*`) are 1A work, except where a topic serves Module 4; no row is homeless.

| ID | Module | Working title | Type | Target | Status | Key sources | Effort |
|---|---|---|---|---|---|---|---|
| MX-01 | 1A | Segmentation | topic | — | ready | Author's own thesis: segmentation is where the manufacturing lens stops working | 1 session |
| MX-02 | 1A | Benchmarks, and how to check a number before you steer by it | topic | — | ready | Five failed traces: Reichheld 5%, 5x-cheaper, 7-friends, Groove 71%, DAU/MAU 50% | 1 session |
| MX-03 | 1A | Retention | topic | — | in progress | Fader & Hardie sorting effect, NRR filings, author's two-axis split | 1 session |
| MX-04 | 1A | Time to convert | topic | — | drafted | Little's Law, flow metrics; merged, author answers folded in | — |
| SK-01 | 1A | Defining your definitions (guided skill) | skill | — | ready | Facebook single-definition story (Schultz lecture, S-1) | 1 session |
| SK-02 | 1A | Is this a vanity metric? (guided skill) | skill | — | candidate | Ries 2009 posts, data-theater critique, Twitter mDAU story | 1 session |
| SK-03 | 1A | Attribution design (guided skill) | skill | — | drafted | Attribution topic page (size guide, incentive checks) | 1 session |
| M1-01 | 1B | Single point of metric computation | pattern | v0.1.0 | candidate | [TODO: prior art] | 1 session |
| M1-02 | 1B | Statistical process control for data pipelines | pattern | v0.1.0 | candidate | [TODO: prior art] | 1 session |
| M1-03 | 1B | Detecting plausible-but-wrong outputs | pattern | v0.1.0 | candidate | [TODO: prior art] | 1 session |
| M1-04 | 1B | Golden question sets for AI analytics validation | pattern | v0.1.0 | candidate | [TODO: prior art] | 1 session |
| M1-05 | 1B | Agreement measurement for analytics QA | pattern | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| M1-06 | 1B | Data quality SLOs and error budgets | pattern | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| M1-07 | 1B | Schema drift detection and data contracts | pattern | v0.1.0 | candidate | [TODO: prior art] | 1 session |
| M1-08 | 1B | The reconciliation protocol | pattern | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| M1-09 | 1B | Measuring trust, not just accuracy | pattern | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| M1-10 | 1B | Data incident root cause analysis | pattern | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| M1-11 | 1A | State-based retention measurement | pattern | v0.2.0 | drafted | Duolingo growth model (Gustafson, Mazal) | 1 session |
| M2-01 | 2 | Minimum viable analytics stack | pattern | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| M2-02 | 2 | The semantic layer as trust infrastructure | pattern | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| M2-03 | 2 | Change management for analytics code | pattern | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| M2-04 | 2 | Stage-appropriate builds | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M2-05 | 2 | Self-serve boundaries | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M3-01 | 3 | The readiness gate | pattern | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| M3-02 | 3 | The validation harness | pattern | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| M3-03 | 3 | Escalation design | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M3-04 | 3 | Staged organizational rollout | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M3-05 | 3 | Agent output governance | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M4-01 | 4 | Metric definition change control | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M4-02 | 4 | Minimum viable data governance | pattern | v1.0.0 | candidate | [TODO: prior art] | 1 session |
| M4-03 | 4 | Revenue metrics under usage-based pricing | pattern | v1.0.0 | candidate | [TODO: prior art + source list] | 1 session |
| M4-04 | 4 | Cost and margin reporting for AI products | pattern | v1.0.0 | ready | Author's stated differentiator; inference cost per user, margin under usage-based pricing | 1 session |
| M3-06 | 3 | Handing a metric definition to an agent | pattern | v0.3.0 | ready | M1-11's machine-readable spec and prompts as the model; closes the library's AI gap | 1 session |
| M4-05 | 4 | The investor reporting pack | pattern | v1.0.0 | candidate | [TODO: prior art + source list] | 1 session |
| RA-01 | 2 | Analytics stack for an AI-native startup, pre-first-data-hire | reference architecture | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| RA-02 | 3 | AI analytics agent deployment with a validation layer | reference architecture | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| IG-01 | 1A | Standing up a metric definitions repository | implementation guide | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| IG-02 | 1B | Building your first golden question set | implementation guide | v0.3.0 | candidate | [TODO: prior art] | 1 session |
