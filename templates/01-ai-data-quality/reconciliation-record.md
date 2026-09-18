# Reconciliation record

Control artifact for the pattern [The reconciliation protocol (M1-08)](../../docs/modules/01-ai-data-quality/reconciliation-protocol.md). MIT licensed. Copy this file into your own repository, fill one copy per disagreement, replace every `[TODO: …]` field, and delete the guidance blockquotes. The procedure follows the reconciliations paragraph of the federal internal-control standards [GAO-2025] and the working rules in a state auditor's bank-reconciliation guide [SAO-2020], and the two-times rule follows the bitemporal distinction between what was true and what was recorded [FOWLER-2021] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** sections 1 to 4 are filled in during the hour the two owners spend together, and an agent can draft sections 2 and 4 from the two queries with Prompt A. Section 5 is the decision and stays with the person who signs it. Section 6 is the machine-readable core, and section 7 is the prompt library. The smallest complete record is two numbers with their as-of times, one ladder that closes to zero, and one name with a date.
>
> **What this record settles:** which of two numbers already in the room stands, and why. Checking one number against something outside its query is the [plausibility-check control plan](plausibility-check-control-plan.md); naming the one computation every consumer reads is the [metric-computation control plan](metric-computation-control-plan.md). This record feeds both.

## 1. The two numbers

One row per fact. Fill both columns before anyone explains anything.

| | Side A | Side B |
|---|---|---|
| The number | `[TODO: e.g. 412,380]` | `[TODO: e.g. 396,150]` |
| What it claims to be | `[TODO: metric name and period, e.g. revenue, March]` | `[TODO: same words, as the other side says them]` |
| System or tool it came from | `[TODO: e.g. the warehouse's blessed revenue view]` | `[TODO: e.g. the billing system's monthly statement]` |
| Query, export or link | `[TODO: path or link]` | `[TODO: path or link]` |
| Who pulled it | `[TODO: name]` | `[TODO: name]` |
| Pulled at (as-of time, with timezone) | `[TODO: e.g. 2026-04-03 09:00 UTC]` | `[TODO: e.g. 2026-04-03 11:30 UTC]` |
| Is this the blessed computation? | `[TODO: yes / no / none exists for this metric]` | `[TODO: yes / no / none exists for this metric]` |
| Gap (A minus B) | `[TODO: e.g. 16,230]` | |

> A number is a value and a moment. Two pulls of the same query at different times are two numbers, and the difference between them belongs on the ladder as a line of its own, with its size.

## 2. The conditions behind each

One row per condition. Write what each side actually did, from its query or export, not what it was supposed to do. A row marked "different" is a candidate line on the ladder.

| Condition | Side A | Side B | Same? |
|---|---|---|---|
| Records excluded (test accounts, refunds, internal, cancelled, trials) | `[TODO]` | `[TODO]` | `[TODO: same / different]` |
| Calendar (calendar month, fiscal period, week start, timezone of the day boundary) | `[TODO]` | `[TODO]` | `[TODO]` |
| As-of time (when the data was pulled; whether late-arriving rows are in) | `[TODO]` | `[TODO]` | `[TODO]` |
| Grain (one row per what) | `[TODO]` | `[TODO]` | `[TODO]` |
| Unit and currency (cents or dollars; conversion rate and its date) | `[TODO]` | `[TODO]` | `[TODO]` |
| Definition of the thing counted (what "customer" or "order" means here) | `[TODO]` | `[TODO]` | `[TODO]` |
| Join path (tables joined, and the key on each side) | `[TODO]` | `[TODO]` | `[TODO]` |
| Anything else that differs | `[TODO]` | `[TODO]` | `[TODO]` |

> Fill this before anyone argues about which number is right. Every executive escalation the author has traced came down to a row in this table, and most to the first three.

## 3. The finest common grain

The finest grain both sides can be brought to, so the gap can be located rather than argued about.

| Item | Value |
|---|---|
| Common grain | `[TODO: e.g. by day and by customer; or by week and by plan if one side cannot go finer]` |
| How Side A was brought to it | `[TODO: query or export step]` |
| How Side B was brought to it | `[TODO: query or export step]` |

| Segment | Side A | Side B | Difference | Share of gap |
|---|---|---|---|---|
| `[TODO: e.g. week 1]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |
| `[TODO: e.g. week 2]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |
| … | | | | |
| Total | `[TODO]` | `[TODO]` | `[TODO: must equal the gap in section 1]` | 100% |

> Reading the table: a gap spread evenly across every segment usually means a definition or a unit; a gap in one period usually means a calendar; a gap in a handful of rows usually means a join or an exclusion. The audit rule for any interface between two systems is that control totals are agreed between source and target [GAO-2024]; this table is that rule one grain finer.

## 4. The difference ladder

One line per cause. Start at Side A, apply one condition, write the amount it explains, carry the running total, and arrive at Side B. Sign convention: an amount is negative when applying the condition moves the running total down.

| Step | Cause (from the section 2 row) | Condition on A | Condition on B | Amount | Running total |
|---|---|---|---|---|---|
| Start | Side A as pulled | | | | `[TODO: Side A value]` |
| 1 | `[TODO: e.g. refunds]` | `[TODO: e.g. gross]` | `[TODO: e.g. net of refunds]` | `[TODO: e.g. −5,940]` | `[TODO]` |
| 2 | `[TODO: e.g. calendar]` | `[TODO: e.g. fiscal period]` | `[TODO: e.g. calendar month]` | `[TODO]` | `[TODO]` |
| 3 | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |
| End | Side B as pulled | | | | `[TODO: Side B value]` |
| | **Remainder** (last running total minus Side B) | | | | `[TODO: must be 0]` |

Spreadsheet-ready: `running_total[n] = running_total[n-1] + amount[n]`, and `remainder = running_total[last] - side_b`. The sum of the amounts equals `side_b - side_a`.

> The ladder ends at zero or the number is on hold. A remainder that is not zero goes into section 5 as "unexplained", with its size, an owner and a date, and nobody signs the reference decision until it closes. "Timing" is a valid cause only with an amount beside it.

## 5. Reference decision

Filled before the meeting ends, by the one person who signs it.

| Item | Value |
|---|---|
| Which number stands | `[TODO: Side A / Side B / neither; on hold]` |
| Why | `[TODO: e.g. the definition says net of refunds on the calendar month; Side A's view had the defects, and is corrected to match]` |
| Which ladder lines were defects, and which were definitional choices | `[TODO: e.g. lines 1 and 2 definitional, now written down; line 3 a defect in the join; line 4 timing]` |
| Decided by | `[TODO: name]` |
| Date | `[TODO: date]` |
| Blessed computation | `[TODO: existed and stands / existed and is corrected in change X / did not exist; Side [A/B] is now named as it, per the metric-computation control plan]` |
| Definitions line (dated, verbatim, appended and never edited in place) | `[TODO: e.g. 2026-04-03: revenue is net of refunds, on the calendar month, as of the billing statement date]` |
| Context-file line (dated, verbatim) | `[TODO: the same fact in the words the assistant reads]` |
| Losing copy | `[TODO: retired on [date] / kept with a drift check against the reference]` |
| Numbers already sent out carrying the losing figure | `[TODO: which deck, which date, who received it; or none]` |
| Disclosure question | `[TODO: yes / no. Whether a corrected number that already left the company is a restatement belongs to Module 4]` |
| Unexplained remainder, if any | `[TODO: amount, owner, due date; else none]` |
| Same pair, same cause before? | `[TODO: no / yes, record dated [date]. If yes, this goes to root cause analysis]` |

> Averaging the two numbers, or taking the one that fits the story, is never a valid entry in the first row. The senior person may choose; the choice is made after section 2 is full and section 4 closes, and is written here so it does not have to be made again.

## 6. Machine-readable core

```json
{
  "spec": "reconciliation-record/v1",
  "metric": "[TODO: e.g. revenue]",
  "period": "[TODO: e.g. 2026-03]",
  "sides": {
    "a": { "value": "[TODO]", "source": "[TODO]", "query": "[TODO: path]", "pulled_by": "[TODO]", "as_of": "[TODO: ISO 8601 with timezone]", "blessed": "[TODO: true | false | null]" },
    "b": { "value": "[TODO]", "source": "[TODO]", "query": "[TODO: path]", "pulled_by": "[TODO]", "as_of": "[TODO: ISO 8601 with timezone]", "blessed": "[TODO: true | false | null]" }
  },
  "gap": "[TODO: a.value - b.value]",
  "conditions": [
    { "name": "excluded", "a": "[TODO]", "b": "[TODO]", "same": "[TODO: true | false]" },
    { "name": "calendar", "a": "[TODO]", "b": "[TODO]", "same": "[TODO]" },
    { "name": "as_of", "a": "[TODO]", "b": "[TODO]", "same": "[TODO]" },
    { "name": "grain", "a": "[TODO]", "b": "[TODO]", "same": "[TODO]" },
    { "name": "unit_currency", "a": "[TODO]", "b": "[TODO]", "same": "[TODO]" },
    { "name": "definition", "a": "[TODO]", "b": "[TODO]", "same": "[TODO]" },
    { "name": "join_path", "a": "[TODO]", "b": "[TODO]", "same": "[TODO]" }
  ],
  "common_grain": "[TODO: e.g. day x customer]",
  "ladder": [
    { "step": 1, "cause": "[TODO]", "condition_a": "[TODO]", "condition_b": "[TODO]", "amount": "[TODO: signed number]", "kind": "[TODO: defect | definitional | timing]" }
  ],
  "remainder": "[TODO: must be 0 to sign]",
  "decision": {
    "reference": "[TODO: a | b | hold]",
    "why": "[TODO]",
    "decided_by": "[TODO]",
    "date": "[TODO]",
    "blessed_computation": "[TODO: stands | corrected | named_now]",
    "definitions_line": "[TODO: dated, verbatim]",
    "context_file_line": "[TODO: dated, verbatim]",
    "losing_copy": "[TODO: retired_on date | drift_checked]",
    "already_sent": "[TODO: list or none]",
    "disclosure_question": "[TODO: true | false]",
    "recurrence": "[TODO: false | record id of the earlier one]"
  },
  "sources": ["GAO-2025", "SAO-2020", "FOWLER-2021", "GAO-2024"]
}
```

> The JSON restates sections 1 to 5 in a form any agent can parse. Keep them in step in the same edit; the JSON wins when the prose is ambiguous.

## 7. Agent prompt templates

### Prompt A — draft the conditions and the ladder from two queries

```text
Two numbers for the same metric disagree. Below are the two values, the
time each was pulled, and the query or export behind each. Rules:
1. For each side, read its query and fill the conditions table: records
   excluded, calendar, as-of time, grain, unit and currency, definition
   of the thing counted, join path. Write what the query does, not what
   it was meant to do. Mark each row same or different.
2. Propose the finest grain both sides can reach, and if the data is
   available, compute the difference by segment at that grain.
3. Build the difference ladder from Side A to Side B: one line per
   condition marked different, with the signed amount it explains and
   the running total. Show the arithmetic so a person can repeat it in a
   spreadsheet.
4. Report the remainder. If it is not zero, say so, name it as
   unexplained, and list what you would check next. Do not spread the
   remainder across the lines to make it close.
5. Do not say which number is right. Do not average them. Stop after
   the ladder.

<reconciliation-record>
[paste section 6 JSON with sides filled in]
</reconciliation-record>

<queries>
[paste the two queries or export definitions]
</queries>
```

### Prompt B — draft the dated lines, for the person who signs

```text
A disagreement between two numbers has been reconciled and the reference
has been decided. Below is the record. Draft, for the owner to approve:
1. One dated line for the metric definition stating the settled
   condition, with the period boundary, exclusion, unit or definition
   spelled out so the question cannot be read the other way again.
2. The same fact as one dated line for the business context file, in
   the words an assistant needs before answering this question.
3. If the losing side was a copy of the metric, one sentence naming it
   as retired on a date or as kept with a drift check against the
   reference.
Append the lines; never edit an existing line in place. Do not change the
decision. If the record's remainder is not zero, refuse and say why.

<reconciliation-record>
[paste section 6 JSON, filled in through the decision]
</reconciliation-record>
```

### Prompt C — before answering a question that has split the room before

```text
Before answering the question below, check the reconciliation records
and the dated lines in the context file for this metric. If a settled
condition applies, use it and cite the dated line in your answer. If the
question could be read two ways and no dated line settles it, say which
reading you used, and list the conditions (excluded, calendar, as-of,
grain, unit, definition) under your number so it can be reconciled
against another.

<question>
[paste the question]
</question>
```

> Run Prompt A the moment two numbers disagree, before the meeting if possible. Run Prompt C on every question that has appeared in a reconciliation record.

## 8. Ownership and review

| Item | Value |
|---|---|
| Owner of this record | `[TODO: the person who signed section 5]` |
| Where records live | `[TODO: repository path; one file per disagreement, dated]` |
| Time allowed | One hour with both owners present for sections 1 to 5; `[TODO: e.g. two working days]` for an unexplained remainder to close |
| Standing reconciliation | For the `[TODO: three to five]` money numbers, run sections 1 to 4 monthly against the independent total, whether or not anyone has noticed a gap |
| Review rule | The reference decision and the dated lines are reviewed like code. A dated line is appended, never edited. |
| Recurrence rule | The same pair of numbers disagreeing twice for the same cause is a finding, and the case goes to root cause analysis rather than to a second record. |
| Standing check | If no record has been filed in `[TODO: e.g. a quarter]`, confirm that disagreements are still reaching this file and not being settled by the senior person in the room. |
