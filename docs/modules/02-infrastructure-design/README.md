# Module 2 — Analytics infrastructure design for rapid growth

> Scope: the analytics system itself — what to set up, in what order, and what has to stay true as the company grows. Covers stack composition by category, ingestion and modeling, change management, reliability, ownership, and the prerequisites for pointing an agent at your data. Does not cover: named products or vendor comparisons; whether a metric is defined right (Module 1A) or whether a number is accurate (Module 1B); agent deployment and validation (Module 3); governance policy and financial reporting (Module 4).

**Status:** build order set, no units written yet. Statuses live in [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md).

## Two halves

Infrastructure fails in two independent ways. It can be built wrong, and it can be run wrong. A company can buy a stack that answers nothing and a company can run a well-designed stack until it quietly stops being true. The causes and the fixes have nothing in common, so this module names them separately.

| | 2A — What you build | 2B — How you run it |
|---|---|---|
| The question | What should exist at my size, in what order, and what should I not build yet? | Does it keep returning the right answer as the company grows, and who owns it? |
| Fails as | Money spent on a stack that answers nothing, or a foundation you cannot retrofit because the history is already gone | A correct build that drifts, breaks without anyone noticing, or stops working the week one person leaves |
| DMAIC phase | Improve — designing the process that produces the number | Control — holding it as volume, headcount and sources grow |
| Knowledge layer | The [reference architectures](../../../reference-architectures/README.md): what a whole stack looks like at a stage | [`templates/02-infrastructure-design/`](../../../templates/02-infrastructure-design/) control plans |
| Guided layer | [TODO(heqing): a stack-selection skill, or none] | The verification skill in 2B, and the [skills](../../../skill/README.md) layer generally |

Read 2A first, and inside it start with what you cannot get back. Most of this module is reversible: a warehouse can be migrated, a tool can be cancelled, a model can be rewritten. History cannot be recovered once a source system has overwritten it, which is why the build order below leads with the units that expire rather than the units that matter most.

## Why this module exists

With the rapid improvement of AI capabilities, it may feel like AI can do everything, but the reality is that if you don't have the right setup or infrastructure for your AI, you can still do very minimal. Your complexity, cost, and efficacy will degrade dramatically. Setting up the right foundation and infrastructure is still vital for any business, for short-term analysis needs, mid-term growth needs, and long-term compliance needs. This module will help guide you on how to set up the best infrastructure for future growth, growing from a small company to a big company. It also gives you an expert opinion for when AI gives you a valid answer and you still don't know what to do.

## 2A — What you build

Ordered by what you lose if you skip it. Track 0 expires; everything after it you can still fix with money or time.

### Track 0 — What you cannot get back

| Unit | What it resolves | Type |
|---|---|---|
| Your first week, with no analyst and no warehouse | Which of the competing first moves actually goes first | guide |
| Which ten events to log before you can answer anything | How few events are enough to start, and which ones | guide |
| Snapshot every mutable table today | How to keep the history your source systems overwrite, and how much of it you lose per day | pattern |
| Land it raw, and never edit it | What the untouched layer holds, and what depends on it existing | pattern |
| Know where the personal data is before someone asks you to delete it | Which columns are personal, what never enters the warehouse, what has to be true when a request arrives | pattern |
| Find out what you can get out of your vendor's system, before you need it | What to do when the history you are losing sits in software you do not control | guide |

### Track 1 — What to buy, and in what order

| Unit | What it resolves | Type |
|---|---|---|
| Do you need a warehouse yet? | Which engine to analyze in, routed on how many systems you must join | pattern |
| What to buy first, and what can wait | The spend order, and what each step costs | pattern |
| How analytics pricing punishes growth | Which meter you are about to grow into | topic |
| Run it yourself, or pay someone | What a team with nobody on call can host | pattern |
| What a product analytics tool will not tell you | Whether the packaged tool is enough, given where your revenue is recorded | topic |
| Have you outgrown it, or did you buy too early? | The add signal and the cancel signal for each category | template |
| Leaving a tool without losing its history | What is exportable before you cancel, and what is aggregate-only and therefore gone | guide |

### Track 2 — Getting the data in

| Unit | What it resolves | Type |
|---|---|---|
| Pay for a connector, or write your own | Which sources justify a managed connector | pattern |
| Six sources you will probably connect, and what goes wrong with each | What to expect from billing, CRM, ad platforms, product events, web and support before you start | topic |
| Do you need change data capture, or is a nightly copy fine? | The choice only; replication mechanics are a separate unit | pattern |
| Data that changes after you load it | How far back to re-run, and what to do about deletes and late arrivals | pattern |
| When to write back into the CRM, and when a list will do | Whether activation is worth building yet | pattern |

### Track 3 — Making it usable

| Unit | What it resolves | Type |
|---|---|---|
| How many layers of SQL you actually need | How many layers, and whether a star schema or one wide table is the right default at this size | pattern |
| Name your tables so you can still find them in six months | The naming rule, and how to declare what one row means | template |
| One customer table when billing and the CRM disagree | Multiple billing customers per domain, duplicate CRM companies, no mapping between them | guide |
| The spreadsheet in your pipeline, and when it is allowed to stay | What to do with a mapping no rule can derive | pattern |
| Pick one file for your metric definitions | Where a definition physically lives, and what reads it | pattern |
| Pick the reporting day once, and write it down | Which day a thing counts in, whose time zone, and when a month closes | pattern |

### Track 4 — Money

| Unit | What it resolves | Type |
|---|---|---|
| Money data gets a stricter standard than product data | Two standards: product data must never be lossy, financial data is never deleted even when wrong | pattern |
| What breaks a revenue query: plans, proration, trials, discounts | How each one miscounts, and what to do about it | topic |
| Refunds, chargebacks, currency, and three different revenue numbers | Which of invoiced, collected and recognized you are reporting, and why it will not match finance exactly | topic |
| What was this customer paying in March? | How to model subscription state over time | guide |
| Do you actually need a ledger? | When double-entry earns its cost, and the smaller thing that usually does instead | pattern |
| Count what a model call costs: tokens, retries, tool calls | One event schema for a model call | pattern |

## 2B — How you run it

Nothing here expires, and nothing here is worth doing before 2A exists. These are the units that keep a built system true.

### Track 5 — Operating it

| Unit | What it resolves | Type |
|---|---|---|
| Fifteen minutes a week to tie revenue to the bank | The cadence, the tolerance, and what goes in the break log | pattern |
| Get your SQL out of the BI tool and into git | What moves first, and what to do with the dashboards left behind | guide |
| Code review when you are the only person who writes SQL | What substitutes for a second reader | pattern |
| What runs when you open a pull request | What to check automatically, and how long a solo maintainer will tolerate it taking | guide |
| The smallest thing that can run your pipeline every night | Whether you need an orchestrator yet | pattern |
| How fresh does this number actually need to be? | The freshness target, set by what someone can do differently in the next hour | pattern |
| It said success. The numbers are still wrong. | Which cheap checks catch a run that completed while dropping rows | pattern |
| Four alerts and a Friday morning look | What to alert on, what to check by hand, what to ignore | guide |
| Undo a bad run after the table is already overwritten | What rollback means when there is nothing to roll back to | pattern |
| Tell people the number was wrong, and decide how far to send it | Who to tell, scaled by how far the number already travelled | template |
| What to write down so someone else could run this next month | What the person taking over needs, written for the one receiving it | template |

### Track 6 — People

| Unit | What it resolves | Type |
|---|---|---|
| Who owns the numbers before you hire an analyst | One name per metric, and the tie-break when two people want it | guide |
| One list for every data question anyone asks | How to turn requests into evidence, and when the queue is long enough to hire | pattern |
| Which questions anyone can answer, and which need a person | Where the self-serve boundary sits, including once anyone can ask in English | pattern |
| Send the number, do not build the dashboard | Where a metric should appear | pattern |
| How to tell it is time to hire someone for data | The signal, built from your own request log | topic |
| Analyst, analytics engineer, or data engineer: which to hire first | The role, and whether the answer at your size is a contractor two days a month instead | template |
| The first 90 days: what they should ship, and what they should refuse | What the first hire builds, and what they decline | guide |
| Interviewing a data person when you cannot read SQL | The loop, and the anti-signals | guide |

### Track 7 — Letting an agent touch it

Module 2 owns the prerequisites. Deployment and validation are [Module 3](../03-ai-agent-integration/README.md).

| Unit | What it resolves | Type |
|---|---|---|
| What has to be true before you let an agent answer questions from your data | The prerequisite list | guide |
| Give the agent ten tables, not your warehouse | What a curated schema contains, and which filters get baked into the views | pattern |
| Who can read what in the warehouse | Roles, timeouts and masking, for a person or an agent alike | pattern |
| How to tell whether a number is wrong before you bet money on it | Which checks to run, and when to stop | skill |

`Land it raw, and never edit it` sits on the seam. It is a 2A decision whose entire value is paid out in 2B: without an untouched copy of what arrived, you cannot tell whether a wrong number came from the design or from the run, and the two halves stop being distinguishable.

## Reference architectures

| Architecture | Covers | Status |
|---|---|---|
| [Analytics stack for an AI-native startup, pre-first-data-hire](../../../reference-architectures/analytics-stack-ai-native-startup.md) | The company that owns its own database and expects to hire | stub |
| The stack for a company with no engineers | Export, a hosted query surface, a scheduled spreadsheet, one named owner | not started |

## Patterns

_None written yet._ Units enter [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md) as they are scheduled, in the order above, rather than all at once.

## Control-plan template

Every module ships at least one. Home: [`templates/02-infrastructure-design/`](../../../templates/02-infrastructure-design/), empty until the tracking plan lands.
