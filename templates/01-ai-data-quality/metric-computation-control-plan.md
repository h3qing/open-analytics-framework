# Metric-computation control plan

Control artifact for the pattern [Single point of metric computation (M1-01)](../../docs/modules/01-ai-data-quality/single-point-of-metric-computation.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The registry compresses the rule the platform accounts converged on [CHANG-2021] [YU-2021] [LINKEDIN-UMP] (see [REFERENCES.md](../../REFERENCES.md)) down to a team with no platform; the drift-check mechanics are this framework's own method for that size. Everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** sections 1–2 are the machine-readable interface (give them to the agent as context, or name them from your business context file), section 4 is the prompt library, and section 3's reaction plan stays with the human owner in section 5.

## 1. Metric registry

One row per metric that leaves the room. The second column names the one blessed view or modeled table; nothing else may aggregate this metric.

| Metric | Computed in (the one place) | Consumers allowed to read it | Duplicates found | Retirement date |
|---|---|---|---|---|
| `[TODO: metric name]` | `[TODO: schema.view_name]` | `[TODO: each dashboard, report, export, and agent, one entry per surface]` | `[TODO: where each surviving copy lives]` | `[TODO: date per duplicate, or "drift-checked" if it cannot retire yet]` |
| `[TODO: metric name]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

> A duplicate is any formula for this metric outside the blessed object: dashboard SQL, a saved spreadsheet formula, a scheduled script, an agent prompt. Every duplicate is either retired by its date or listed in the drift check below. A duplicate with neither is a second source of truth, and finding one is a defect, not a footnote.

## 2. Machine-readable core

```json
{
  "spec": "metric-computation-registry/v1",
  "owner": "[TODO: name]",
  "warehouse": "[TODO: system]",
  "metrics": [
    {
      "id": "[TODO: metric id]",
      "blessed_object": "[TODO: schema.view_name]",
      "definition": "[TODO: one-sentence formula, including standing filters]",
      "consumers": ["[TODO: surface, one entry each]"],
      "duplicates": [
        {
          "location": "[TODO: where the copy lives]",
          "retirement_date": "[TODO: date, or null if drift-checked]",
          "drift_checked": false
        }
      ]
    }
  ],
  "invariant": "every consumer reads blessed_object; no consumer re-implements the aggregation",
  "sources": ["CHANG-2021", "YU-2021", "LINKEDIN-UMP"]
}
```

> This block restates section 1 in a form any agent can parse. Keep the two in step in the same edit; the JSON wins when the prose is ambiguous.

## 3. Drift check

For duplicates that cannot retire yet. The blessed view is the reference by construction: a divergence means the duplicate is corrected or retired early, and if the blessed view itself turns out to be wrong, it is fixed in the one place so every consumer heals together.

| Item | Value |
|---|---|
| Cadence | `[TODO: e.g. weekly; match how often the metric is quoted]` |
| Comparison window | `[TODO: e.g. the trailing 28 complete days]` |
| Tolerance | `[TODO: absolute or relative difference below which no action is taken; zero is a valid choice]` |
| On divergence | `[TODO: who is alerted, and by when the duplicate is corrected or retired]` |
| Check owner | `[TODO: name — normally the registry owner]` |

Vendor-neutral SQL sketch; adapt names and date functions to your warehouse.

```sql
-- Compare a surviving duplicate against the blessed view over the same window.
with blessed as (
  select period, metric_value
  from [TODO: schema.blessed_view]
  where period between [TODO: window_start] and [TODO: window_end]
),
duplicate as (
  select period, metric_value
  from ([TODO: the duplicate's formula, restated as a query]) d
  where period between [TODO: window_start] and [TODO: window_end]
)
select
  b.period,
  b.metric_value as blessed_value,
  d.metric_value as duplicate_value,
  d.metric_value - b.metric_value as drift
from blessed b
join duplicate d using (period)
where abs(d.metric_value - b.metric_value) > [TODO: tolerance];
```

> Rows returned are divergences; zero rows on every run is the success condition. When the duplicate retires, delete the check.

## 4. Agent prompt templates

### Prompt A — answer from the blessed computation only

```text
You are an analytics agent. The metric registry below names the one place each
metric is computed. Rules:
1. Answer questions about a registered metric by reading its blessed_object.
   State in your answer which object you read.
2. Never recompute a registered metric from source tables, even if you can.
   If the blessed object cannot answer the question (a missing dimension, a
   missing period), say so and stop rather than re-deriving the formula.
3. A question about an unregistered number is exploration: answer it, and say
   the number is not a registered metric.
4. Do not invent values for data you cannot access; return the query you
   would run and mark the result [BLOCKED] instead.

<metric-registry>
[paste section 2 JSON here]
</metric-registry>
```

### Prompt B — drift-check readout

```text
Run the drift check defined below for each duplicate still listed in the
registry. Report per duplicate: the comparison window, the largest divergence,
whether it exceeds the tolerance, and the retirement date. Flag any duplicate
with no retirement date and no drift check as a defect, not a footnote.
Show the comparison query you ran for each duplicate.

<control-plan>
[paste sections 1 and 3 here]
</control-plan>
```

## 5. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Review rule | Every edit to a blessed view is reviewed like code, because it changes every consumer's number at once. |
| Change binding | A definition change edits the blessed view and this registry in the same commit or pull request. |
| New-metric rule | A metric enters the registry before its second consumer exists. |
| Registry audit | `[TODO: cadence for re-running the duplicate inventory — new tools grow new formulas]` |
