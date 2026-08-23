# Module 4 — Data governance and financial reporting specific to AI companies

> Scope: what has to be true whether or not anyone ever asks, and what you must be able to produce when they do. Covers the standing access rules, the records that cannot be edited, governing the context your agents read, explaining a number months later, the compliance regimes a small company actually faces, and the money numbers themselves. Does not cover: building the warehouse (Module 2); what happens inside a running agent session (Module 3); whether a number is accurate (Module 1B).

**Status:** build order set, no units written yet. Statuses live in [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md).

## Where this module starts, and Module 3 stops

The two modules overlap on governance, so the line between them is stated here once.

**Module 3 owns the run, and Module 4 owns the record.** A unit belongs to Module 3 if its defect shows up inside a running agent session and is repaired by changing the runtime: a credential, a tool, a retrieval step, a check before the answer is shown. It belongs here if the defect only shows up when somebody outside the team asks you to produce or defend something that already left the building, and repair means a standing rule plus an artifact you had to keep in advance.

When a rule binds the agent, ask what generates the rule. If the generator is "the agent must not exceed its caller, and must not be talked into something", it is Module 3. If it is "this record must be producible unaltered to an outsider", it is Module 4, and Module 2 or Module 3 implements it. The cruder version decides most cases on sight: Module 3's rules are about the agent specifically, and Module 4's rules bind every identity, including the founder's.

## Two halves

Both halves fail in front of an outsider, but not the same outsider and not for the same reason. One half fails on evidence, the other fails on definition, and neither fix helps the other. A perfect audit trail does not tell you what belongs in ARR, and a defensible revenue definition does not survive a request to show how last March's figure was produced.

| | 4A — What you must be able to show | 4B — The money numbers themselves |
|---|---|---|
| The question | If someone outside asks how a number was produced, what happened to a record, or who could see what, can you produce the evidence without manufacturing it? | Are the figures you report defined correctly for an AI business, and reported consistently across periods? |
| Fails as | The number is right and you cannot defend it. The definition that produced last March's figure is unrecoverable, a retention clock expired on the history diligence just asked for, an invoice was edited in place and the old value is gone | ARR that quietly mixes subscription, usage, credits, pilots and implementation fees. A margin that omits inference cost. A definition that changed between two board decks and rewrote a trend with nothing disclosed |
| DMAIC phase | Control — the evidence that the process was held, kept as long as someone can still ask | Define and Measure, applied to the money characteristics |
| Knowledge layer | [`templates/04-governance-and-financial-reporting/`](../../../templates/04-governance-and-financial-reporting/) control plans | The investor pack and the definitions sheets |
| Guided layer | [TODO(heqing): a reproduction drill, or none] | [TODO(heqing): a revenue-definition skill, or none] |

4B is not Module 1A applied to money. The difference is that these definitions carry a disclosure consequence: changing what counts as an active user is an internal problem, and changing what counts as ARR between two board decks is a restatement.

## Why this module exists

[TODO(heqing): interview-driven, written in session. Say in your own voice why a company with no compliance function should read any of this, and what you have watched go wrong when the record was not kept. The research supplies the rules; it cannot supply the reason you think this belongs in an analytics framework at all.]

## 4A — What you must be able to show

### Track 0 — Who and what can reach the data

This track states the standing rule that Module 3 implements: humans and agents form one access-control population, with one privilege ceiling and two lifecycles, because you cannot put multi-factor authentication on a service account.

| Unit | What goes wrong without it | Type |
|---|---|---|
| Give every bot its own login | Automated things borrow a person's credential, so nothing can be attributed and nothing can be revoked cleanly | pattern |
| A prompt is not a permission | The boundary is written in instructions the model can be talked out of, and recorded as though it were a control | pattern |
| The agent should not see more than the person asking, and sometimes less | Parity is treated as the whole rule, when an agent reading customer-written text needs less access than the human, not equal | pattern |
| One list of everything that can read your data | Nobody can answer the question, so no review is possible | implementation guide |
| When someone leaves, what else leaves with them | Offboarding covers the person and misses everything they created | pattern |
| What to tell a customer who asks how your AI reaches their data | The question arrives during a deal and the answer is improvised | template |

### Track 1 — Records you cannot change later

| Unit | What goes wrong without it | Type |
|---|---|---|
| Which of your tables should never be edited | Money rows are corrected in place and the original is gone | pattern |
| How to fix a wrong invoice without editing it | A correction destroys the evidence of what was originally charged | pattern |
| Stop your AI agent from writing to anything that becomes an invoice | A read-only flag in a tool is mistaken for a revoked write grant | implementation guide |
| The eight other things you can't change later | Immutability is applied to billing alone, and consent records, access logs, deletion receipts and the evaluation that gated a ship are all editable | reference architecture |
| How long to keep it, and the switch that stops deletion | A retention job runs during a dispute because nobody built a pause | implementation guide |
| Freeze every number before you send it to an investor | The figures in the deck cannot be reproduced later because the underlying tables moved | pattern |

### Track 2 — Governing the context

Code has been version-controlled and reviewed for decades. The context you hand an agent has the same blast radius and almost none of the same discipline.

| Unit | What goes wrong without it | Type |
|---|---|---|
| Put the business context you give your agents in git, with one owner | A definition changes, every downstream answer changes, and nothing records who or when | pattern |
| What to actually check when someone edits the definition of active user | Review is adopted without anyone knowing what a reviewer of prose is looking for | pattern |
| Before you edit the metric doc, make the agent re-derive last quarter's revenue | A wording change made for readability silently moves numbers nobody was watching | pattern |
| The number moved. Is that a fix or a break? | The check reports a difference with no verdict attached, which is the majority of real edits | pattern |
| Which edits actually need a check, and which are just paperwork | Every typo triggers a ceremony, so within a month the ceremony is skipped | pattern |
| Prove the wording change did what you think before you merge it | The gate exists and nobody can say what passing means | pattern |
| Set up the before-and-after check in one afternoon | The idea is agreed and never built | implementation guide |
| Keeping one definition true in three places at once | The warehouse, the context file and the dashboard drift apart and each is defensible | pattern |

### Track 3 — Explaining a number later

| Unit | What goes wrong without it | Type |
|---|---|---|
| Show me the query, or don't send me the number | A reported figure has narration behind it instead of something anyone can re-run | pattern |
| The number the agent made up on the way | The figure came from a retrieved document or arithmetic in the model's head, and there is no query to keep | pattern |
| One table that makes every number explainable | The pieces are logged in four places and no incident can be reconstructed from them | implementation guide |
| Reproducing last year's number | The query survives but the data moved, so re-running it produces a different answer | pattern |
| What your AI tool actually logs, and how to find out in twenty minutes | You discover the tool's provenance limits during the incident | implementation guide |
| Explaining last quarter's number six months later | The definition in force at the time was never recorded | pattern |
| Six questions to ask before you buy an AI analytics tool, and what a "no" tells you | Provenance is discovered to be impossible after the contract is signed | template |

### Track 4 — When the outside asks

| Unit | What goes wrong without it | Type |
|---|---|---|
| Do you actually need SOC 2 yet? | Months and real money go into an audit nobody required in writing | pattern |
| The six security things worth doing at ten people, audit or no audit | The work that reduces risk is skipped in favour of the work that produces evidence | pattern |
| What SOC 2 does not cover | The report is mistaken for security, or for privacy, and the gap is discovered later | pattern |
| Put your AI agents in the access review | The criteria name service accounts and nobody thought that included the agent | pattern |
| How to read a SOC 2 report someone sent you | You accept a vendor's report without checking scope, period or exceptions | implementation guide |
| Does HIPAA actually apply to you? A test you can finish today | Scope is guessed, in either direction, and both errors are expensive | pattern |
| Keep the regulated data out of your analytics stack | Controls get built for data that never needed to be there | pattern |
| You signed a BAA. What do you actually have to do on Monday? | The obligation is signed and nothing changes operationally | implementation guide |
| When one customer brings a rulebook the rest of the business doesn't have | One deal's regime is applied to the whole company, or to nothing | pattern |
| Does any rulebook say anything about letting an agent read this? | You assume there is an answer, and mostly there is silence | pattern |
| The other rulebooks, and the one field that triggers each | A regime applies because of a single column nobody noticed | template |
| The one-page security overview that answers most questionnaires | Every questionnaire is answered from scratch by a founder | template |

## 4B — The money numbers themselves

### Track 5 — Defining revenue when customers pay for what they use

| Unit | What goes wrong without it | Type |
|---|---|---|
| What you can honestly call ARR when customers pay for what they use | A number built for subscriptions is applied to consumption and nobody states what is inside it | pattern |
| Invoiced, collected, recognized: three different numbers for the same month | Three defensible numbers exist and the deck picks whichever is highest | implementation guide |
| Prepaid credits, and the money customers never spend | Credits are counted as revenue when sold, when drawn, or twice | pattern |
| A platform fee plus usage, counted once | Hybrid pricing is double counted or the variable half is dropped | pattern |
| When the price per token falls, your revenue chart lies | Volume and price move together and the chart separates neither | pattern |
| The one-page revenue definitions sheet | Every number is defensible and none is written down | template |

### Track 6 — Cost and margin when the cost of goods sold is a model call

| Unit | What goes wrong without it | Type |
|---|---|---|
| What goes in cost of goods sold when your product is a model call | Inference sits in operating expense and the gross margin is fiction | pattern |
| Cost per customer when one call serves three features | Shared, cached and failed calls are allocated by guess | pattern |
| Cost per user, per request, or per outcome: picking the denominator | The denominator is chosen for availability and informs no decision | pattern |
| The handful of accounts eating your margin | Consumption concentrates, a few accounts are underwater, and the average hides it | pattern |
| Why your margin moved when you didn't change anything | A provider price change is read as an efficiency gain, or the reverse | pattern |
| The one-page cost and margin report for your board | The board asks and the answer takes a week | template |

### Track 7 — What you hand to an outsider

| Unit | What goes wrong without it | Type |
|---|---|---|
| What a diligence request asks for that you cannot make later | The history was never captured and no amount of work recreates it | pattern |
| Your definition changed between two board decks | A trend is rewritten and nothing marks the change | pattern |
| The five governance artifacts a ten-person company actually needs | Governance is either absent or imported wholesale from an enterprise template | pattern |
| Build the evidence once: diligence, the audit and the security questionnaire want the same things | The same facts are assembled three times, from scratch, under three deadlines | implementation guide |
| What changes the day you sign your first enterprise customer | The obligations arrive with the contract and nothing was ready | pattern |
| The investor pack: every number, its definition, and what backs it | Each pack is rebuilt by hand and no two are consistent | template |
