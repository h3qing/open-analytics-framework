# SLO register for the numbers that leave the room

Control artifact for the pattern [Data quality SLOs and error budgets (M1-06)](../../docs/modules/01-ai-data-quality/data-quality-slos.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The objective-and-budget vocabulary follows the site-reliability books [BEYER-2016] [BEYER-2018], and the comparison of what the pipeline does against what the reader needs follows the process-capability chapter of the standard quality-control textbook and Wheeler's working form [MONTGOMERY-2019] [WHEELER-2019] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** section 1 is the register, section 2 is the arithmetic, section 3 says what happens when a budget is spent, section 4 is the machine-readable core, section 5 is the prompt library, and section 6 stays with the human owner. The smallest complete implementation is one row: the one number your most senior reader looks at, that reader's name, the time they look, and the number of bad mornings a quarter they told you they would live with.
>
> **What this register does not hold:** the control limits. Those describe what the pipeline does and live in the [SPC control plan](spc-control-plan.md). This register holds what the reader needs. The two are compared in section 2 and never merged.

## 1. The register

One row per number and per dimension. Most numbers need a `fresh` row first and a `right` row second; add a `complete` row only where a source can drop out without anything failing. The requirement column is written in the reader's words, by the reader, and the owner translates it into an indicator afterwards.

| # | Number | Reader, and when they read it | Dimension | Requirement, in the reader's words | Window | Bad periods allowed | Indicator (what is measured to call a period bad) |
|---|---|---|---|---|---|---|---|
| 1 | `[TODO: the number]` | `[TODO: name]`, `[TODO: e.g. every weekday at 09:00]` | fresh | Landed by `[TODO: time]` with data through `[TODO: e.g. yesterday]` | Rolling quarter, about `[TODO: 65]` readings | `[TODO: e.g. 3]` | Landing time of the load that feeds it, read at `[TODO: time]` |
| 2 | same | same | complete | Every expected source present for the period, and the count inside the limits | Same | `[TODO]` | Share of expected sources landed, and the row count from the [SPC control plan](spc-control-plan.md) |
| 3 | same | same | right | Reconciles to `[TODO: the independent total, e.g. the billing statement]` within `[TODO: tolerance]` | Same | `[TODO]` | The reconciliation check from the [plausibility-check control plan](plausibility-check-control-plan.md) |
| 4 | `[TODO: the next number]` | `[TODO]` | `[TODO: fresh, complete, right]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

> Three questions get a row filled with the reader in ten minutes. When do you look at this number? What do you do differently if it is late, short, or wrong that day? How many such days a quarter could you live with? Write the third answer down as a count. The percentage in section 2 is derived from it and is never the thing the reader agreed to.
>
> A requirement copied from what the pipeline usually does is not a requirement. If the reader cannot say what a bad day costs them, the number may not need a row yet.

## 2. The arithmetic

Spreadsheet-ready. One row of the register, one column of daily indicator readings, and everything below follows.

1. **The budget.** `budget = bad_periods_allowed`, straight from the register. The share the site-reliability books would print is `slo_share = 1 - budget / periods_in_window`; three bad mornings in 65 is 95.4 percent. Keep the count as the number people talk about, because 3 is what the reader said and 95.4 is what a spreadsheet said.
2. **Period status.** For each period, `bad = indicator outside the requirement`, for example `landing_time > deadline`, `sources_landed < sources_expected`, or `ABS(number - independent_total) > tolerance`. A period is bad or not; there is no partial credit.
3. **Budget spent and remaining.** Over a rolling window of an integral number of weeks, so every window holds the same number of weekends [BEYER-2018]: `spent = COUNTIF(status, "bad")` and `remaining = budget - spent`.
4. **Pace.** `pace = spent / weeks_elapsed`. When `pace * 13 > budget`, the budget will not last the quarter, and the reader hears that now rather than in week thirteen. This is the framework's plain form of what the reliability books call a burn rate [BEYER-2018].
5. **Capability.** Take the chart on the indicator from the [SPC control plan](spc-control-plan.md): its `mean` and its `avg_moving_range`, and `sigma = avg_moving_range / 1.128`. For a requirement the indicator must stay below, such as a deadline, `margin = (requirement - mean) / (3 * sigma)`; for one it must stay above, such as a share of sources, `margin = (mean - requirement) / (3 * sigma)`. This is the one-sided capability index of the quality field, Cpk, written for a single limit [WHEELER-2019]. Read it in the reader's units first: the gap between the natural process limit nearest the requirement and the requirement itself, in minutes or in rows.
6. **What the margin says.** Above about 1.5, the pipeline meets the requirement with room to spare and a bad period is a special cause worth investigating. Between 1 and 1.5, it meets the requirement only while it stays predictable and centred, and Wheeler's advice is to want the cushion [WHEELER-2019]. Below 1, the requirement sits inside the pipeline's own limits, routine variation spends the budget, and no alert will change that. The rough share of bad periods to expect is `1 - NORM.S.DIST((requirement - mean) / sigma, TRUE)` for an upper requirement, assuming day-to-day variation is roughly bell-shaped; multiply by the periods in the window for a count.

Worked, illustrative, for the freshness row: deadline 09:00, budget 3 of 65 mornings. A load that lands at 06:40 on average with an average moving range of 22 minutes has natural limits of 05:41 and 07:39, a margin of 2.4, and 81 minutes between its upper limit and the deadline; a late morning there is news. A load that lands at 08:50 on average with the same moving range has limits of 07:51 and 09:49, a margin of 0.2, and lands late on about three mornings in ten, so the budget of three is gone in the second week while the chart shows nothing, because nothing changed.

## 3. What happens when a budget is spent

| Reading | What it means | What to do | Within |
|---|---|---|---|
| A bad period, and the chart on the indicator shows a point outside its limits that day | A special cause: something changed | The SPC reaction plan runs; the reader hears before they read the number, with the cause once found | Same day |
| A bad period, and the chart is quiet | Routine variation crossed the requirement | Nothing to fix today; check the margin in section 2 | Same day |
| Budget spent, and the chart is quiet | A capability problem: the requirement sits inside the pipeline's limits | Change the process (the schedule, the source, the scope of the table) or renegotiate the requirement with the reader. Do not move the limits. | `[TODO: e.g. two weeks]` |
| Budget spent, and the chart signalled on the bad days | Repeated special causes | Each bad day has a found cause in the signal log; the pattern across them goes to root cause work | `[TODO: e.g. one week]` |
| Pace says the budget will not last the quarter | The reader is going to be surprised in week ten | Tell the reader now, with the count, and agree what changes first | Same week |
| Budget untouched for two consecutive quarters | Either the requirement is too loose or nobody reads the number | Ask the reader whether they would notice a bad day; tighten the row or retire it | At the quarterly review |
| A `right` row goes bad | The number is wrong, whatever the dashboard says | The number does not leave the room until it reconciles; the [plausibility checks](plausibility-check-control-plan.md) say how | Before the reader's next reading |

> The budget is the reader's, not the owner's. Spending it is not a failure and hoarding it is not a success. It is the agreed number of days a quarter the reader has said they will absorb, and the register exists so that nobody has to renegotiate that on a bad morning.

## 4. Machine-readable core

```json
{
  "spec": "slo-register/v1",
  "owner": "[TODO: name]",
  "window": { "kind": "rolling_quarter", "weeks": 13, "periods": "[TODO: e.g. 65 weekday readings]" },
  "rows": [
    {
      "id": "[TODO: e.g. weekly_revenue_fresh]",
      "number": "[TODO: the number, as the reader names it]",
      "reader": { "name": "[TODO]", "reads_at": "[TODO: e.g. weekdays 09:00]" },
      "dimension": "[TODO: fresh | complete | right]",
      "requirement": {
        "text": "[TODO: in the reader's words]",
        "kind": "[TODO: upper_limit | lower_limit | tolerance]",
        "value": "[TODO: e.g. 09:00, or 1.0 as a share, or 0.005 as a relative tolerance]"
      },
      "budget": { "bad_periods_allowed": "[TODO: e.g. 3]", "slo_share": "[TODO: derived, 1 - budget / periods]" },
      "indicator": {
        "signal_id": "[TODO: the matching signal id in the SPC control plan, or null]",
        "source": "[TODO: where the daily reading comes from]"
      },
      "capability": {
        "mean": "[TODO: from the chart]",
        "avg_moving_range": "[TODO: from the chart]",
        "sigma": "[TODO: avg_moving_range / 1.128]",
        "margin": "[TODO: (requirement - mean) / (3 * sigma), sign per section 2]",
        "expected_bad_periods": "[TODO: rough count from section 2, step 6]"
      },
      "status": {
        "as_of": "[TODO: date]",
        "spent": "[TODO]",
        "remaining": "[TODO]",
        "pace_per_week": "[TODO]",
        "reading": "[TODO: in_budget | special_cause | capability_problem | untouched]"
      },
      "agreed": { "with": "[TODO: the reader's name]", "on": "[TODO: date]" }
    }
  ],
  "policy": {
    "capability_problem": "change_process_or_renegotiate_requirement; never move the limits",
    "special_cause": "spc_reaction_plan",
    "untouched_two_quarters": "ask_reader_then_tighten_or_retire",
    "right_row_bad": "number_does_not_leave_the_room"
  },
  "sources": ["BEYER-2016", "BEYER-2018", "MONTGOMERY-2019", "WHEELER-2019"]
}
```

> The JSON restates sections 1 to 3 in a form any agent can parse. Keep them in step in the same edit; the JSON wins when the prose is ambiguous. The control limits are read from the SPC control plan and copied here for the capability arithmetic; they are edited there, never here.

## 5. Agent prompt templates

### Prompt A — fill a row with the reader

```text
You are helping the owner of a data quality register interview the person
who reads one number. Ask these questions one at a time and wait for each
answer:
1. When do you look at this number, and what do you decide from it?
2. If it were late one morning, what would you do differently? If it
   were short (a source missing)? If it were wrong?
3. How many such days in a quarter could you live with before you stopped
   trusting it or had to redo something?
Then draft one register row per dimension the reader cares about, with the
requirement written in the reader's own words and the budget as a count of
bad periods. Do not propose a percentage, and do not describe what the
pipeline currently does. The owner reviews the row with the reader and
commits it.

<slo-register>
[paste section 4 JSON here, with existing rows]
</slo-register>
```

### Prompt B — the quarterly reading

```text
You are an analytics agent reading an SLO register against the daily
indicator series and the chart baselines provided. For each row:
1. Mark each period bad or not against the requirement, and compute spent,
   remaining, and pace exactly as in section 2. Show the arithmetic.
2. Using the chart's mean and average moving range, compute sigma, the
   margin, and the rough expected bad periods.
3. Classify the row: in budget; special cause (bad periods coincide with
   chart signals); capability problem (budget spent or pacing to be spent
   with a quiet chart); or untouched for two quarters.
4. Draft a three-sentence note to the reader named on the row: the count
   spent against the count agreed, what the chart says about why, and
   what the owner proposes. Do not change any requirement, budget, or
   limit; propose the change and stop.

<slo-register>
[paste section 4 JSON here]
</slo-register>

<indicator-series>
[paste dates and daily readings per row, plus the chart baseline from the
SPC control plan]
</indicator-series>
```

## 6. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where this register lives | `[TODO: repository path]` |
| Reviewed with each reader | `[TODO: e.g. quarterly, in the reader's calendar]` |
| A change to a requirement or a budget | An edit to this file with a date and the reader's name, reviewed like code |
| The control limits | Never edited here. They belong to the [SPC control plan](spc-control-plan.md) and change only after a confirmed process change. |
| Standing check | If a row's budget has not been touched in two quarters, the review asks the reader whether they would notice a bad day. |
