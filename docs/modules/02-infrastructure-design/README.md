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

| Unit | What goes wrong without it | Type |
|---|---|---|
| Your first week, with no analyst and no warehouse | You spend the first month building something nobody asked for, and the history you needed expires while you do it | guide |
| Which ten events to log before you can answer anything | The product emits nothing, so no question about what users actually did has an answer | guide |
| Snapshot every mutable table today | Your source systems overwrite the past, and no amount of money buys back the days you did not copy | pattern |
| Land it raw, and never edit it | A number comes out wrong and you cannot tell whether the design or the run produced it | pattern |
| Know where the personal data is before someone asks you to delete it | A deletion request arrives and nobody can say which tables hold personal rows | pattern |
| Find out what you can get out of your vendor's system, before you need it | The history you are losing sits in software you do not control, and you learn the limits the day you need it | guide |

### Track 1 — What to buy, and in what order

| Unit | What goes wrong without it | Type |
|---|---|---|
| Do you need a warehouse yet? | You buy a warehouse a year early, or you run reporting on production until customers feel it | pattern |
| What to buy first, and what can wait | The money goes to storage before there is a question, and the one thing that cannot be added later gets skipped | pattern |
| How analytics pricing punishes growth | The bill jumps the quarter you grow, because nobody looked at which axis each tool meters | topic |
| Run it yourself, or pay someone | You self-host something that pages a person you do not employ | pattern |
| What a product analytics tool will not tell you | You buy the packaged tool and it still cannot see where your revenue is recorded | topic |
| Have you outgrown it, or did you buy too early? | Tools accumulate, nothing gets cancelled, and nobody can say which ones earn their keep | template |
| Leaving a tool without losing its history | You cancel a tool and find its history was aggregate-only, so it is simply gone | guide |

### Track 2 — Getting the data in

| Unit | What goes wrong without it | Type |
|---|---|---|
| Pay for a connector, or write your own | You maintain three hand-written connectors, or pay per row for one you could have written in a day | pattern |
| Six sources you will probably connect, and what goes wrong with each | Every source has a trap that costs a week, and you find them one at a time | topic |
| Do you need change data capture, or is a nightly copy fine? | You build streaming replication for a business that needed a nightly copy | pattern |
| Data that changes after you load it | Refunds and corrections land after the load, and last month's number quietly changes | pattern |
| When to write back into the CRM, and when a list will do | You build a sync nobody uses, or your salespeople work from a spreadsheet three days stale | pattern |

### Track 3 — Making it usable

| Unit | What goes wrong without it | Type |
|---|---|---|
| How many layers of SQL you actually need | One query becomes forty, each slightly different, and nobody knows which one is right | pattern |
| Name your tables so you can still find them in six months | Nobody can say what one row means, so every question starts with an investigation | template |
| One customer table when billing and the CRM disagree | Billing and the CRM describe the same company at different grains, so no join between them is trustworthy | guide |
| The spreadsheet in your pipeline, and when it is allowed to stay | A mapping only a person knows lives on a laptop, or it rots inside the pipeline | pattern |
| Pick one file for your metric definitions | Three tools compute revenue three ways and each one is defensible | pattern |
| Pick the reporting day once, and write it down | Two reports disagree about which month something landed in, and both are right | pattern |

### Track 4 — Money

| Unit | What goes wrong without it | Type |
|---|---|---|
| Money data gets a stricter standard than product data | A finance number is corrected by overwriting it, and the old value is gone | pattern |
| What breaks a revenue query: plans, proration, trials, discounts | The revenue number is off and nobody can say by how much, or why | topic |
| Refunds, chargebacks, currency, and three different revenue numbers | Your number and finance's number differ, and there is no agreed explanation for the gap | topic |
| What was this customer paying in March? | A pricing conversation needs last quarter's plan and nothing recorded it | guide |
| Do you actually need a ledger? | You build double-entry for a business that needed an append-only table, or the reverse | pattern |
| Count what a model call costs: tokens, retries, tool calls | Inference is your cost of goods sold and nothing measures it per customer | pattern |

## 2B — How you run it

Nothing here expires, and nothing here is worth doing before 2A exists. These are the units that keep a built system true.

### Track 5 — Operating it

| Unit | What goes wrong without it | Type |
|---|---|---|
| Fifteen minutes a week to tie revenue to the bank | Month end takes a day and a half because eleven discrepancies arrive at once, under deadline | pattern |
| Get your SQL out of the BI tool and into git | A number moves between two board decks and nothing explains why | guide |
| Code review when you are the only person who writes SQL | Nobody has ever read the query behind the number the board sees | pattern |
| What runs when you open a pull request | A broken model ships because the only check was remembering to look | guide |
| The smallest thing that can run your pipeline every night | The nightly refresh depends on a laptop being awake | pattern |
| How fresh does this number actually need to be? | You pay for hourly refreshes to serve a decision someone makes once a month | pattern |
| It said success. The numbers are still wrong. | The job completes, the dashboard loads, and rows were silently dropped | pattern |
| Four alerts and a Friday morning look | Either nothing is monitored, or so much is that everyone mutes the alerts | guide |
| Undo a bad run after the table is already overwritten | A bad run overwrites the table and there is nothing left to roll back to | pattern |
| Tell people the number was wrong, and decide how far to send it | A wrong number reaches a decision and nobody knows who has to be told | template |
| What to write down so someone else could run this next month | The person who built the reports leaves and takes the only working knowledge with them | template |

### Track 6 — People

| Unit | What goes wrong without it | Type |
|---|---|---|
| Who owns the numbers before you hire an analyst | Every metric belongs to everyone, so no metric belongs to anyone | guide |
| One list for every data question anyone asks | Requests arrive in chat, get answered once, and leave no record of what people actually need | pattern |
| Which questions anyone can answer, and which need a person | You become the bottleneck for questions anyone could have answered themselves | pattern |
| Send the number, do not build the dashboard | The dashboard exists, it is correct, and nobody opens it | pattern |
| How to tell it is time to hire someone for data | You hire a year late, or a year early into a job that is not yet a job | topic |
| Analyst, analytics engineer, or data engineer: which to hire first | You hire the wrong one of the three and lose a year finding out | template |
| The first 90 days: what they should ship, and what they should refuse | The first hire spends a year building a stack nobody asked for, or becomes a report desk | guide |
| Interviewing a data person when you cannot read SQL | You cannot evaluate the one skill you are hiring for | guide |

### Track 7 — Letting an agent touch it

Module 2 owns the prerequisites. Deployment and validation are [Module 3](../03-ai-agent-integration/README.md).

| Unit | What goes wrong without it | Type |
|---|---|---|
| What has to be true before you let an agent answer questions from your data | You point an agent at production and discover the prerequisites afterwards | guide |
| Give the agent ten tables, not your warehouse | The agent can reach everything, so a wrong join or a leak can come from anywhere | pattern |
| Who can read what in the warehouse | Access is granted once, never reviewed, and nobody can say who can see the salary table | pattern |
| How to tell whether a number is wrong before you bet money on it | You get a confident answer you cannot check, and act on it anyway | skill |

`Land it raw, and never edit it` sits on the seam. It is a 2A decision whose entire value is paid out in 2B: without an untouched copy of what arrived, you cannot tell whether a wrong number came from the design or from the run, and the two halves stop being distinguishable.

## Reference architectures

| Architecture | Covers | Status |
|---|---|---|
| [Analytics stack for an AI-native startup, pre-first-data-hire](../../../reference-architectures/analytics-stack-ai-native-startup.md) | The company that owns its own database and expects to hire | stub |
| The stack for a company with no engineers | Export, a hosted query surface, a scheduled spreadsheet, one named owner | not started |

## Patterns

_None written yet._ Units enter [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md) as they are scheduled, in the order above, rather than all at once.
