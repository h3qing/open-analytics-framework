# SPC control plan for a data pipeline

Control artifact for the pattern [Statistical process control for data pipelines (M1-02)](../../docs/modules/01-ai-data-quality/statistical-process-control-for-pipelines.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The limit arithmetic follows Wheeler's XmR formulation [WHEELER-2010] [WHEELER-2012], cross-checked against the published tutorial constants [MOHAMMED-2008] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** sections 1–2 and the JSON core in section 4 are the machine-readable interface, section 5 is the prompt library, and section 3 stays with the human owner. The smallest complete implementation is one row of the signals table: one XmR chart, in a spreadsheet, on the daily row count of your most important table.

## 1. Signals

One row per charted signal. Start with the first row only; add the next signal after the first chart has run for a few weeks.

| Signal | Chart | Where the limits come from | Recompute rule |
|---|---|---|---|
| Daily rows loaded into `[TODO: most important table]` | XmR on the daily count | Last `[TODO: 20+]` days of history, arithmetic in section 2 | Only after a confirmed process change, from days after the change |
| Hours since `[TODO: table]` last updated, read at `[TODO: time]` | XmR on the daily reading | Same | Same |
| Share of nulls in `[TODO: critical column]`, daily | XmR on the daily percentage | Same | Same |

> Weekday and weekend are usually different processes. If the chart signals every weekend, split the row into two charts, or chart today's value minus the same weekday last week and put the limits on that difference. Do not widen anything by hand.

## 2. The limit arithmetic

Spreadsheet-ready. One column of dates, one column of values, and everything below follows.

1. **Baseline.** Take the last `n` daily values, ideally 20–25, provisionally as few as 6–10 [MOHAMMED-2008] [WHEELER-2012]. Exclude days you already know were broken, and say so in the core below.
2. **Mean.** `mean = AVERAGE(values)`.
3. **Moving ranges.** For each day after the first, `mR_t = ABS(value_t - value_t-1)`. This measures day-to-day variation only, which is the point: a shift in the data inflates a global standard deviation and hides itself, but barely touches the moving ranges [WHEELER-2010].
4. **Average moving range.** `mRbar = AVERAGE(mR_2 … mR_n)`.
5. **Natural process limits.** `upper = mean + 2.66 * mRbar` and `lower = mean - 2.66 * mRbar`. For counts and percentages, floor the lower limit at zero. The 2.66 is 3 divided by 1.128, the constant that converts an average moving range into an estimate of one standard deviation of routine variation [MOHAMMED-2008].
6. **Range limit (optional second panel).** `range_upper = 3.27 * mRbar` (printed as 3.267 or 3.268 across sources; the difference never matters at spreadsheet scale). A single day's swing above this line is a signal even when both endpoints sit inside the natural process limits.

Detection rules, in order of use:

- A point outside either natural process limit.
- A run of eight consecutive points on the same side of the mean line [MOHAMMED-2008].
- (If the range panel is kept) a moving range above `range_upper`.

## 3. Reaction plan

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where the chart lives | `[TODO: spreadsheet or dashboard location]` |
| Looked at | `[TODO: e.g. every morning after the load completes]` |
| On a point outside the limits | `[TODO: who investigates]` within `[TODO: e.g. same working day]` |
| First checks | `[TODO: e.g. did the load run; did an upstream export change; did a backfill land]` |
| What counts as a confirmed process change | A deliberate, explainable change to the pipeline or its sources, written down with a date. A shrug is not a confirmed change. |
| On a confirmed change | Recompute limits from days after the change [WHEELER-2012]; record date and reason in section 4 |
| On a defect | Fix it, log it, keep the limits |
| Inside the limits | No reaction. Reacting to routine variation adds variation [DEMING-FUNNEL]. |
| Signal log | `[TODO: where out-of-limits investigations and their found causes are recorded]` |

## 4. Machine-readable core

```json
{
  "spec": "spc-control-plan/v1",
  "owner": "[TODO: name]",
  "signals": [
    {
      "id": "[TODO: e.g. daily_rows_main_table]",
      "source_table": "[TODO]",
      "metric": "[TODO: row_count | freshness_hours | null_share]",
      "cadence": "daily",
      "split": "[TODO: none | weekday_weekend | same_weekday_delta]",
      "baseline": {
        "window": "[TODO: date range used]",
        "n": "[TODO: number of days]",
        "excluded_days": ["[TODO: known-broken days left out, with one-line reasons]"],
        "mean": "[TODO: computed]",
        "avg_moving_range": "[TODO: computed]"
      },
      "limits": {
        "lower": "[TODO: mean - 2.66 * avg_moving_range, floored at 0]",
        "upper": "[TODO: mean + 2.66 * avg_moving_range]",
        "range_upper": "[TODO: 3.27 * avg_moving_range]"
      },
      "detection_rules": ["point_outside_limits", "run_of_eight_same_side"],
      "recompute_policy": "only_after_confirmed_process_change",
      "last_recomputed": { "date": "[TODO]", "reason": "[TODO: the confirmed change]" }
    }
  ],
  "reaction": {
    "investigate_within": "[TODO: e.g. same working day]",
    "investigator": "[TODO: name or rotation]",
    "signal_log": "[TODO: location]"
  },
  "sources": ["WHEELER-2010", "WHEELER-2012", "MOHAMMED-2008"]
}
```

> The JSON restates sections 1–3 in a form any agent can parse. Keep them in step in the same edit; the JSON wins when the prose is ambiguous.

## 5. Agent prompt templates

### Prompt A — compute limits and check today

```text
You are an analytics agent running the SPC control plan below. Using the
daily series provided:
1. Compute the mean, the moving ranges, the average moving range, and the
   natural process limits exactly as in the plan (2.66 and 3.27 constants).
   Show the arithmetic so a human can reproduce it in a spreadsheet.
2. State whether today's value is inside or outside the limits, and whether
   the last eight points sit on one side of the mean.
3. If a detection rule fires, say which rule, and draft a two-sentence
   notification to the owner naming the signal and the first checks from
   the reaction plan. Do not speculate about causes.
4. Do not recompute or adjust limits. Flag them as stale only if
   last_recomputed predates a change listed in the series notes.

<spc-control-plan>
[paste section 4 JSON here]
</spc-control-plan>

<series>
[paste dates and values, plus notes on any known process changes]
</series>
```

### Prompt B — propose a recompute after a confirmed change

```text
A process change has been confirmed: [TODO: one sentence, with date].
Using the series provided, compute fresh limits from the days after the
change only, following the arithmetic in the plan. Report old limits, new
limits, and how many post-change days the new limits rest on; if fewer
than 10, label the new limits provisional. Output an updated section 4
JSON block with last_recomputed filled in. A human owner commits the edit.

<spc-control-plan>
[paste section 4 JSON here]
</spc-control-plan>

<series>
[paste dates and values]
</series>
```

## 6. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where this plan lives | `[TODO: repository path]` |
| Review rule | Limit changes are edits to this file, reviewed like code, each with a date and a confirmed process change behind it. |
| Standing check | If the chart has not signaled in `[TODO: e.g. a quarter]`, verify the data feeding it is still arriving; a silent chart and a dead chart look identical. |
