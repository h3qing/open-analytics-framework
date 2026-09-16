# Plausibility-check control plan

Control artifact for the pattern [Detecting plausible-but-wrong outputs (M1-03)](../../docs/modules/01-ai-data-quality/plausible-but-wrong.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The control-total check follows the definition in the federal audit manual [GAO-2024], and the practice of checking an output against a value known before the data arrived is the sample-ratio-mismatch guardrail generalized [FABIJAN-2019] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** section 1 and the JSON core in section 4 are the machine-readable interface, section 5 is the prompt library, and section 3 stays with the human owner. The smallest complete implementation is one row of the checks table: one number, one independent total, one tolerance, one name.

## 1. Numbers that leave the room

One row per number a board deck, an invoice, a customer, or an agent's answer carries. The second column names something the query did not produce; if the only candidate is the same warehouse view summed differently, the cell is not filled yet.

| Number | Checked against (independent of the query) | Tolerance | Who looks | Within |
|---|---|---|---|---|
| `[TODO: e.g. monthly revenue]` | `[TODO: e.g. the billing system's monthly statement, same period, same definition]` | `[TODO: e.g. 0.5 percent, or zero for money]` | `[TODO: name]` | `[TODO: e.g. before the number leaves the room; same working day on a hold]` |
| `[TODO: e.g. monthly active users]` | `[TODO: e.g. the application's own count, or distinct authenticated ids from the auth log]` | `[TODO]` | `[TODO]` | `[TODO]` |
| `[TODO: e.g. orders in the period]` | `[TODO: e.g. the payment processor's export, count of captured payments]` | `[TODO]` | `[TODO]` | `[TODO]` |

> A tolerance is an edit to this file with a date and a reason in section 4, never a value someone raises to make a failing check pass. Zero is a valid tolerance for anything with money in it.

## 2. The five checks

Spreadsheet-ready where possible; the SQL sketches are vendor-neutral and adapt to any warehouse. Run them in this order and stop at the first hold.

1. **Control total.** `output_total = SUM(output.metric_value)` over the period. `difference = output_total - control_total`, `relative = ABS(difference) / control_total`. Hold if `relative > tolerance`. The control total is a number typed in from the independent system, with its source and date recorded beside it, never a query against the same warehouse.
2. **Grain.** On the output table, `row_count = COUNT(*)` and `key_count = COUNT(DISTINCT grain_key)`. Expected difference zero. A positive difference is a fan-out from a join, and the number holds until the duplicated keys are explained.
3. **Invariants.** `SUM(parts) = topline` within rounding; `SUM(shares) = 1.00` within rounding; no value below zero where the definition forbids it. These use only the output and catch a broken partition; they cannot catch a doubled total, so they come after the control total and never instead of it.
4. **Bounds.** Two or three ratios the business cannot produce unless something is wrong, each with a bound from the definition or from the last `[TODO: e.g. three]` closed periods: `[TODO: e.g. revenue per order]`, `[TODO: e.g. sessions per active user]`, `[TODO: e.g. refunds as a share of sales]`. A value outside the bound holds the number.
5. **Second path.** For the money numbers only: a second query from a different source table, with a different join or no join, sharing no intermediate table with the first, written where possible by a different person. Compare over the same period at the same tolerance as the control total. A golden question with a hand-fixed answer for a closed period counts as a second path.

```sql
-- Grain check on the output that leaves the room.
select
  count(*) as row_count,
  count(distinct [TODO: grain_key]) as key_count,
  count(*) - count(distinct [TODO: grain_key]) as extra_rows
from [TODO: schema.output_table]
where period = [TODO: period];
```

```sql
-- Control-total check. The control total is a typed-in value from the
-- independent system, not a query against this warehouse.
select
  sum(metric_value) as output_total,
  [TODO: control_total] as control_total,
  sum(metric_value) - [TODO: control_total] as difference,
  abs(sum(metric_value) - [TODO: control_total]) / [TODO: control_total] as relative
from [TODO: schema.output_table]
where period = [TODO: period];
```

> Rows outside tolerance are holds; a clean run returns differences of zero. When a hold is explained and the cause fixed, rerun every check, not only the one that fired.

## 3. Reaction plan

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| When the checks run | Before the number leaves the room, and on every change to the query, the model, or the definition behind it |
| On a hold | `[TODO: who investigates]` within `[TODO: e.g. same working day]`; the number does not ship until the difference is explained |
| First checks on a hold | Did the period match; did the definition match; did a join add rows; did a filter go missing; did the independent system change what it counts |
| On a found cause | Fix the query, rerun all five checks, log the cause |
| On a difference that turns out to be real | The independent system and the warehouse disagree for a reason; record which one is right and why, and change the control total's source only with a dated reason |
| What never happens | A tolerance raised, or a check deleted, to make a run pass |
| Hold log | `[TODO: where holds and their found causes are recorded]` |

## 4. Machine-readable core

```json
{
  "spec": "plausibility-check-control-plan/v1",
  "owner": "[TODO: name]",
  "numbers": [
    {
      "id": "[TODO: e.g. monthly_revenue]",
      "output_table": "[TODO: schema.output_table]",
      "grain_key": "[TODO: e.g. order_id]",
      "control_total": {
        "source": "[TODO: e.g. billing system monthly statement]",
        "independent_of_warehouse": true,
        "value": "[TODO: typed in, with the date it was read]",
        "as_of": "[TODO: date]"
      },
      "tolerance": { "relative": "[TODO: e.g. 0.005]", "last_changed": { "date": "[TODO]", "reason": "[TODO]" } },
      "invariants": ["parts_sum_to_topline", "shares_sum_to_one", "no_negative_values"],
      "bounds": [
        { "ratio": "[TODO: e.g. revenue_per_order]", "low": "[TODO]", "high": "[TODO]", "from": "[TODO: e.g. last three closed periods]" }
      ],
      "second_path": {
        "required": "[TODO: true for money numbers]",
        "source_table": "[TODO: different from output_table's sources]",
        "shares_intermediate_tables": false,
        "author": "[TODO: name, ideally not the first query's author]"
      },
      "checked_by": "[TODO: name]",
      "within": "[TODO: e.g. same working day on a hold]"
    }
  ],
  "reaction": {
    "on_hold": "number does not ship until the difference is explained",
    "investigate_within": "[TODO]",
    "hold_log": "[TODO: location]"
  },
  "sources": ["GAO-2024", "FABIJAN-2019"]
}
```

> The JSON restates sections 1 to 3 in a form any agent can parse. Keep them in step in the same edit; the JSON wins when the prose is ambiguous.

## 5. Agent prompt templates

### Prompt A — check a number before it leaves the room

```text
You are an analytics agent running the plausibility-check control plan
below on the result provided. Rules:
1. Run the five checks in order: control total, grain, invariants, bounds,
   second path. Show the arithmetic for each so a person can repeat it in a
   spreadsheet.
2. Treat the control total as given. Do not recompute it from the warehouse
   and do not question it; if the output disagrees, the output is on hold.
3. Report each check as PASS or HOLD with the computed values. On any HOLD,
   stop, name the check that fired, and draft a two-sentence note to the
   owner listing the first checks from the reaction plan. Do not guess at
   the cause.
4. Do not widen a tolerance or skip a check. If a check cannot be run because
   an input is missing, report it as NOT RUN and say what is missing.
5. Attach one line to the number stating what it was tied to and how close
   it came, in the form: "Tied to [source] for [period]: [difference],
   [relative] against a tolerance of [tolerance]."

<plausibility-check-control-plan>
[paste section 4 JSON here]
</plausibility-check-control-plan>

<result>
[paste the output rows, the query that produced them, and the period]
</result>
```

### Prompt B — compute the second path

```text
Compute [TODO: the number] for [TODO: the period] a second way. Rules:
1. Start from [TODO: the second source table]. Do not read
   [TODO: the first query's output table or any intermediate table it used].
2. Prefer no join. If a join is unavoidable, state the grain on both sides
   and show that the join key is unique on the side you are joining to.
3. Show the query and the result. Do not look at the first path's figure
   until your own is computed; then report the difference and whether it is
   within the tolerance in the plan.
4. If the two paths disagree, do not pick one. Report both, the difference,
   and which check in the plan should run next.

<plausibility-check-control-plan>
[paste section 4 JSON here]
</plausibility-check-control-plan>
```

> Run Prompt A on every agent answer that carries a number someone will act on. An answer without the tie-out line is unfinished.

## 6. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where this plan lives | `[TODO: repository path]` |
| Review rule | Tolerances, control-total sources, and check deletions are edits to this file, reviewed like code, each with a date and a reason. |
| Change binding | When the query, the model, or the definition behind a number changes, the checks rerun before the new number leaves the room, and this file changes in the same commit if a source or a bound moved. |
| Standing check | If no check has held in `[TODO: e.g. a quarter]`, confirm the control totals are still being read from the independent system and not from the warehouse; a check that cannot fail and a check that never needs to look identical. |
