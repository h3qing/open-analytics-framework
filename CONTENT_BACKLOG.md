# Content backlog

One row per writeable unit; a unit is finishable in one 60–90 minute sitting. Statuses: `candidate` (pre prior-art review), `ready`, `in progress`, `drafted`, `published`. Rows at `candidate` are provisional until the Phase 0 prior-art review runs and the candidate list is cut by the author.

The Module column uses `1A` (definition quality) and `1B` (data integrity) for the two halves of Module 1, `2A` (what you build) and `2B` (how you run it), `3A` (what it can reach) and `3B` (what it tells you), and `4A` (what you must be able to show) and `4B` (the money numbers) — see the [Module 1](docs/modules/01-ai-data-quality/README.md), [Module 2](docs/modules/02-infrastructure-design/README.md), [Module 3](docs/modules/03-ai-agent-integration/README.md) and [Module 4](docs/modules/04-governance-and-financial-reporting/README.md) charters. Metric topic pages (`MX-*`) and guided skills (`SK-*`) are 1A work, except where a topic serves Module 4; no row is homeless.

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
| M2-01 | 2A | Do you need a warehouse yet? | pattern | v0.3.0 | candidate | Redset query telemetry from 400 production clusters; Tigani on warehouse sizes | 1 session |
| M2-02 | 2A | Pick one file for your metric definitions | pattern | v0.3.0 | candidate | Semantic-layer research round; contested by M1-01 and IG-01, see DECISIONS | 1 session |
| M2-03 | 2B | Code review when you are the only person who writes SQL | pattern | v0.3.0 | candidate | Analytics-engineering practice; DORA delivery metrics as the transfer question | 1 session |
| M2-04 | 2A | Have you outgrown it, or did you buy too early? | template | v1.0.0 | candidate | Assembled last, from every other unit's add signal and cancel signal | 1 session |
| M2-05 | 2B | Which questions anyone can answer, and which need a person | pattern | v1.0.0 | candidate | Self-serve research round; absorbs what changes once anyone can ask in English | 1 session |
| M2-06 | 2A | Snapshot every mutable table today | pattern | v0.3.0 | ready | The one unit with a deadline: history a source system overwrites cannot be recovered | 2 sessions |
| M2-07 | 2A | Do you need change data capture, or is a nightly copy fine? | pattern | v0.3.0 | candidate | The unit whose sourcing already resolves; Kimball on CDC and late-arriving data | 1 session |
| M2-08 | 2A | Tracking plan | template | v0.3.0 | candidate | Module 2's first control plan; the templates directory is empty today | 1 session |
| M2-09 | 2B | How to tell whether a number is wrong before you bet money on it | skill | v0.3.0 | candidate | Text-to-SQL accuracy evidence; the checks a person without SQL can actually run | 1 session |
| M3-01 | 3 | The readiness gate | pattern | v0.3.0 | candidate | Written after both halves exist; it checks 3A Track 0 and the context file at once | 1 session |
| M3-02 | 3B | How to tell whether the agent's answer counts as right | pattern | v0.3.0 | candidate | Splits from the runtime reconciliation unit; see the evaluation settlement in DECISIONS | 1 session |
| M3-03 | 3B | Teaching your data agent to say "I don't know" | pattern | v1.0.0 | candidate | [TODO: author interview — no input behind this row yet] | 1 session |
| M3-04 | 3B | Who should get your AI data assistant first, and it is not the executives | pattern | v1.0.0 | candidate | [TODO: author interview — no input behind this row yet] | 1 session |
| M3-05 | 3B | How far an AI-generated number is allowed to travel | pattern | v1.0.0 | candidate | [TODO: author interview — no input behind this row yet] | 1 session |
| M3-06 | 3B | The one file your AI should read before it answers anything | pattern | v0.3.0 | drafted | A 4 KB context file moved three frontier models by the same large margin; the tool was not the variable | 1 session |
| M3-07 | 3A | What login should the AI use on your data? | pattern | v0.3.0 | ready | Merges four proposals; OAuth holds but fails on over-privileged humans, on scheduled work, and on stdio transport | 1 session |
| M3-08 | 3A | Decide which tables the AI can reach, before deciding who can ask | pattern | v0.3.0 | ready | Table-granular selection fails when sensitivity lives in a free-text column | 1 session |
| M3-09 | 3A | Your support tickets can tell your AI what to do | pattern | v0.3.0 | candidate | The unit of sensitivity is the row, and it was written by someone you do not employ | 1 session |
| M3-10 | 3A | What to write down every time your AI answers a data question | pattern | v0.3.0 | candidate | You cannot go back and record an answer you did not log | 1 session |
| RA-02 | 3 | AI analytics agent deployment with a validation layer | reference architecture | v0.3.0 | candidate | Assembled last, from what the units actually said | 1 session |
| M4-01 | 4A | Before you edit the metric doc, make the agent re-derive last quarter's revenue | pattern | v1.0.0 | candidate | Author's own position; the hole is the edit that legitimately moves the number | 1 session |
| M4-02 | 4A | The five governance artifacts a ten-person company actually needs | pattern | v1.0.0 | candidate | Build the evidence once: diligence, audit and security questionnaire want the same things | 1 session |
| M4-03 | 4B | What you can honestly call ARR when customers pay for what they use | pattern | v1.0.0 | candidate | Invoiced, collected and recognized are three numbers for the same month | 1 session |
| M4-04 | 4B | What goes in cost of goods sold when your product is a model call | pattern | v1.0.0 | ready | Author's stated differentiator; feeds on Module 2's model-call metering | 1 session |
| M4-05 | 4B | The investor pack: every number, its definition, and what backs it | template | v1.0.0 | candidate | Diligence asks for history that cannot be manufactured later | 1 session |
| M4-06 | 4A | A prompt is not a permission | pattern | v1.0.0 | ready | Author's position, sharpened: name the artifact that stops the agent if the model output were attacker-controlled | 1 session |
| M4-07 | 4A | The eight other things you can't change later | reference architecture | v1.0.0 | candidate | Beyond billing: consent, access logs, deletion receipts, the eval that gated a ship | 1 session |
| M4-08 | 4A | Show me the query, or don't send me the number | pattern | v1.0.0 | ready | The executable query is the artifact, not the reasoning trace | 1 session |
| M4-09 | 4A | Do you actually need SOC 2 yet? | pattern | v1.0.0 | candidate | Routes on written evidence that a named deal is blocked on it | 1 session |
| RA-01 | 2A | Analytics stack for an AI-native startup, pre-first-data-hire | reference architecture | v0.2.0 | candidate | [TODO: prior art] | 1 session |
| IG-01 | 1A | Standing up a metric definitions repository | implementation guide | v0.3.0 | candidate | [TODO: prior art] | 1 session |
| IG-02 | 1B | Building your first golden question set | implementation guide | v0.3.0 | candidate | [TODO: prior art] | 1 session |
