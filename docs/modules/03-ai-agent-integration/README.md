# Module 3 — AI agent integration into analytics workflows

> Scope: pointing an AI agent at your data and living with the consequences. Covers what the agent may reach, how it authenticates, what untrusted rows can make it do, what it records, whether its answers can be trusted, and how a company adopts it. Does not cover: building agents or the models underneath them; whether a metric is defined right (Module 1A) or a number accurate (Module 1B); the warehouse and models the agent reads from (Module 2); what you must be able to show an outsider afterwards (Module 4).

**Status:** build order set, no units written yet. Statuses live in [CONTENT_BACKLOG.md](../../../CONTENT_BACKLOG.md).

## Two halves

Agent integration fails in two ways that have nothing to do with each other. An agent can be accurate and still be a side door, and it can be perfectly locked down and confidently wrong. Golden questions do not stop a leak, and a careful login does not make an answer right. So this module names the two separately.

| | 3A — What it can reach | 3B — What it tells you |
|---|---|---|
| The question | Can it only see and do what this asker is already entitled to? | Can we trust the answer, and does the company act like it? |
| Fails as | A correct agent that becomes a side door: someone learns a customer list or a salary through the agent that they could never have queried directly | A fluent, confident, wrong number that nothing errored on, believed because it was well written |
| DMAIC phase | Control — an access boundary that holds no matter what is asked | Measure and Analyze — measurement-system analysis on an instrument that is not deterministic |
| Knowledge layer | [`templates/03-ai-agent-integration/`](../../../templates/03-ai-agent-integration/) control plans | The reference architecture, the deployed shape with its validation layer |
| Guided layer | The connector review, run before anything is plugged in | The verification skill: checking a number you cannot compute yourself |

Read 3A first. Both halves matter, but only one of them fails in a way you cannot take back.

## What decides the order

The units are ordered by whether you can still fix the damage later. A wrong number can be corrected. A leaked customer list cannot be un-leaked, and a question nobody logged has no answer three weeks later when someone asks how a number was produced. The units that protect you from permanent damage come first, and the units that make answers better come after.

Module 2 orders by what expires. Nothing here expires, because you can always turn the agent off. The risk here is different: granting a credential feels reversible, and it is, right up until a row leaves under it. That is why 3A's first track comes before everything else.

## Why this module exists

It seems easy to integrate an AI agent with your database. In practice, in an enterprise environment, there is much more to consider: security, compliance, reliability, factuality, the reusability of your knowledge, and the organization of your context. Many things can go wrong with the integration. This module helps you use AI securely, safely, and in a way you can trust, so that it adds value to your work.

<!-- TODO(heqing): two optional additions in your voice: a story of what you watched go wrong when an agent met production data, and why you settle access before trust when most writing does the reverse. -->

## 3A — What it can reach

3A asks four questions, in order: what identity does the agent carry, what can that identity reach, what can untrusted rows make it do, and what record survives of what it did.

### Track 0 — Before you connect anything

There are seven units in this track, and they are strongly recommended before your agent touches production data. Everything else can be added in the second month.

| Unit | What goes wrong without it | Type |
|---|---|---|
| What login should the AI use on your data? | One shared credential carries everyone's access, so the agent can reach whatever the most privileged person can | pattern |
| Decide which tables the AI can reach, before deciding who can ask | The agent is pointed at the whole warehouse, and a wrong join or a leak can come from anywhere in it | pattern |
| Which of your tables should an AI never see | Salary, customer contact details and another customer's rows sit in the same warehouse as product usage, reachable by the same query | pattern |
| Your support tickets can tell your AI what to do | Free-text your customers wrote is read as instructions, and the unit of sensitivity turns out to be the row, not the table | pattern |
| List every way your AI can send data out of the building | You harden what it can read and leave the path by which it hands data to somebody else | implementation guide |
| What to write down every time your AI answers a data question | A number is questioned three weeks later and there is no record of what was asked, by whom, or what ran | pattern |
| Checking a data connector before you plug it in | You install a connector whose tool descriptions you never read, and it is trusted from that moment on | skill |

### Track 1 — Identity, and where parity breaks

Permission parity is the rule that a person must not learn through the agent anything they could not have queried directly. It is a ceiling rather than a floor, and it breaks in more places than it holds.

| Unit | What goes wrong without it | Type |
|---|---|---|
| Why the AI can see things you can't, and the other way round | Nobody can explain why the agent answered a question the asker could not have run themselves | pattern |
| Running scheduled reports without handing over everyone's access | A nightly refresh borrows a person's credential, and their leaving breaks the pipeline or their access outlives them | pattern |
| One answer, two systems, two sets of permissions | The agent blends a warehouse table with a document store that has different rules, and the stricter one silently loses | pattern |
| The agent in a shared channel answers one person in front of nine | The permission model was designed for one asker and the answer is delivered to a room | pattern |
| What to switch off when someone leaves | Offboarding covers people and misses the credentials they created | implementation guide |

### Track 2 — What that identity may reach

| Unit | What goes wrong without it | Type |
|---|---|---|
| Masking, or just leaving the column out | You mask a column, the agent can still join around it, and the masking bought nothing | pattern |
| Your assistant will surface things nobody meant to hide | Data that was technically readable but practically buried becomes trivially discoverable by asking in English | pattern |
| What happens to a row after the AI reads it | The row leaves the warehouse boundary and no rule follows it | pattern |
| Anyone who can edit that file can change every answer your AI gives | The context file becomes the highest-privilege object in the company and is protected like a README | pattern |
| When you let it write, and what has to be true first | Read-only is abandoned for one convenient case and the money tables are in reach | pattern |
| Who decides what each role may see when nobody owns governance | Nobody has ever decided, so the answer is whatever the first grant happened to be | pattern |

### Track 3 — What the untrusted rows can make it do

| Unit | What goes wrong without it | Type |
|---|---|---|
| Stop trying to catch the attack, take away the way out | You buy a filter for a problem that filtering has never solved, instead of removing the exit | pattern |
| Read-only is not the same as safe | Read-only removes the write, leaves the exfiltration, and gets treated as the whole answer | pattern |

### Track 4 — The record, and the ceiling

| Unit | What goes wrong without it | Type |
|---|---|---|
| Making your warehouse show who actually asked, not just the bot | Every query is attributed to one service account, so no incident can be traced to a person | pattern |
| Your AI's logs now hold your customer data too | The log built for accountability becomes the least protected copy of the sensitive data | pattern |
| Someone says the AI showed them data they shouldn't see | The report arrives and nobody knows how to establish whether it is true | implementation guide |
| Put a hard ceiling on every query your agent runs | An iterative agent explores, re-queries and retries, and the bill arrives at the end of the month | pattern |
| A one-afternoon access check for your AI analyst | Nobody has ever verified that the boundary you designed is the boundary that exists | implementation guide |
| The one-page sheet of what your AI can see | No single place records what it reaches, under which credential, expiring when | template |

## 3B — What it tells you

This half moves from grounding, to checking whether the grounding worked, to what the company is allowed to do with the answer.

### Track 5 — Getting the answers right

One result matters more than everything else in this half. In a paired evaluation, three frontier models from two vendors were statistically indistinguishable from each other, and a small written context file moved every one of them by the same large margin. The tool is replaceable, and the file is the asset.

| Unit | What goes wrong without it | Type |
|---|---|---|
| The one file your AI should read before it answers anything | The agent guesses at ambiguous tables, and the fix everyone reaches for is a better model rather than a written definition | pattern |
| Write your company's context file in an afternoon | You agree the file matters and never sit down to write it | template |
| What to write first so an AI agent gets your numbers right | The effort goes into describing every column, which is the highest-cost lowest-return work available | pattern |
| The pairs you feed it are the pairs you can no longer test it with | Your examples and your answer key are the same set, so the test passes by construction | pattern |
| Your agent will inherit your SQL's bugs | An undocumented filter in the transformation is reproduced faithfully, and unlike a person the agent cannot notice | pattern |
| A text file or a semantic layer: when do you need the heavier thing? | You buy the heavier thing before the file, or refuse it long after the file stopped holding | pattern |
| Keep your business context in files you own, not inside your AI tool | The context accumulates inside one vendor and leaving becomes a rewrite | pattern |
| When the definition changes, what changes the file? | The definition moves in one place and the agent keeps answering from the other | pattern |
| A one-hour audit: can an AI agent read your data repository? | You cannot tell whether your own repository is legible to an agent until it answers wrongly | implementation guide |

### Track 6 — Knowing whether it is right

Two mechanisms live here and they are easy to confuse. One constrains the input on every answer, at runtime. The other scores outputs against known values, on a schedule. They have different owners and different failure modes.

| Unit | What goes wrong without it | Type |
|---|---|---|
| How to tell whether the agent's answer counts as right | Nobody has defined correct, so every evaluation argument is about the rubric | pattern |
| Making the agent reconcile against numbers you already trust | The agent computes a forecast from nothing and it is checked against nothing | pattern |
| The agent gave two different answers to the same question | Run-to-run variation is read as a bug or ignored as noise, with no rule to tell them apart | pattern |
| When to run your checks, and what they cost | Checks run on a schedule nobody chose, at a cost nobody counted | pattern |
| Check every morning that the agent can still reach your data | A token expired, a table was renamed, and the agent answered anyway from what was left | pattern |
| When a source is down, the agent has to say so | Silent partial answers are worse than an outage, because nobody knows to distrust them | pattern |
| Your agent is answering from a copy of your data that is three months old | The retrieval index is stale and the answers are confidently historical | pattern |
| The model changed under you and nothing broke | The provider shipped a new version and nothing in your checks noticed | pattern |
| Nobody is on call: what happens when the check fails | The check fires into a channel nobody reads, which is the same as no check | implementation guide |

### Track 7 — What the company does with the answer

| Unit | What goes wrong without it | Type |
|---|---|---|
| Should you buy an analytics AI, or point a general one at your data? | You compare products on a dimension that the evidence says barely matters | pattern |
| Try before you buy: a two-hour test on your own data | The evaluation is run on the vendor's demo dataset | implementation guide |
| Can your tool be instructed at all? | You buy a tool whose behaviour you cannot constrain, and find out afterwards | pattern |
| Who should get your AI data assistant first, and it is not the executives | The rollout starts with the people least able to catch a wrong answer and most able to act on one | pattern |
| Teaching your data agent to say "I don't know" | The agent answers everything, so its confidence carries no information | pattern |
| The questions an agent gets wrong no matter how good your context is | You keep improving context against a class of question that context cannot fix | pattern |
| How far an AI-generated number is allowed to travel | A number reaches a board deck or a customer with nothing marking where it came from | pattern |
| The day your AI analyst is wrong in front of everyone | One public wrong answer ends adoption, and nothing was prepared for it | pattern |
| Three numbers that tell you it is safe to give more people access | Access widens because nobody objected, rather than because anything was measured | implementation guide |
| When someone says the AI gave them a wrong number | Reports arrive and nothing turns them into a fix | pattern |
| Explaining a number the AI got wrong three weeks ago | You have the log and still cannot reconstruct the answer | implementation guide |
| What the agent costs you, on one line a week | The cost is invisible until it is annual | template |

The context file sits on the seam. It belongs to 3B by ownership, since its whole purpose is making answers right, but its cost is paid in the first week alongside 3A's Track 0, and it is also the highest-privilege object in the company: anyone who can edit it changes every answer the agent gives. It is the one unit that has to be read from both halves.

## The entrance and the exit

`M3-01`, the readiness gate, is the ceremony that checks both halves at once and refuses deployment until 3A's Track 0 exists and the context file is written. It is the module's front door and should be written after both halves are drafted, not before.

`RA-02`, the deployed shape with its validation layer, is assembled last, from whatever the units actually said.

## Control-plan template

Every module ships at least one. Home: [`templates/03-ai-agent-integration/`](../../../templates/03-ai-agent-integration/), empty until the access sheet lands.
