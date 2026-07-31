# Retention-state control plan

Control artifact for the pattern [State-based retention measurement (M1-11)](../../docs/modules/01-ai-data-quality/state-based-retention-measurement.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. State-model defaults follow Duolingo's published growth model [GUSTAFSON-2023] [MAZAL-2023] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** sections 1–2 are the machine-readable interface (give them to the agent as context), section 5 is the prompt library, and section 6 is the output contract. A human owner keeps section 4.

## 1. Definitions

| Field | Value |
|---|---|
| Entity | `[TODO: user / account / workspace]` |
| Canonical activity event | `[TODO: the one event that counts as "active" — one definition, versioned]` |
| Cadence | `[TODO: daily / weekly — use weekly if daily rates are noise at your volume]` |
| Source of truth table | `[TODO: table or view name]` |
| Definition owner | `[TODO: name]` |

## 2. State model (machine-readable)

```json
{
  "spec": "retention-state-model/v1",
  "entity": "[TODO]",
  "activity_event": "[TODO]",
  "cadence": "[TODO: daily | weekly]",
  "states": [
    { "id": "new", "definition": "first-ever period of activity", "in_dau": true },
    { "id": "current", "definition": "active today; also active in prior 6 days", "in_dau": true },
    { "id": "reactivated", "definition": "active today; last active 7-29 days ago", "in_dau": true },
    { "id": "resurrected", "definition": "active today; last active 30+ days ago", "in_dau": true },
    { "id": "at_risk_wau", "definition": "not active today; active in prior 6 days", "in_dau": false },
    { "id": "at_risk_mau", "definition": "not active in prior 7 days; active in prior 30", "in_dau": false },
    { "id": "dormant", "definition": "not active in 30+ days", "in_dau": false }
  ],
  "aggregates": {
    "dau": ["new", "current", "reactivated", "resurrected"],
    "wau": "dau + at_risk_wau",
    "mau": "wau + at_risk_mau"
  },
  "rates": [
    { "id": "curr", "name": "current-user retention rate", "definition": "share of entities in state current in period t that are active again in period t+1" },
    { "id": "nurr", "name": "new-user retention rate", "definition": "share of entities in state new in period t that are active again within the following window" },
    { "id": "rurr", "name": "reactivated-user retention rate", "definition": "share of entities in state reactivated in period t that are active again within the following window" },
    { "id": "surr", "name": "resurrected-user retention rate", "definition": "share of entities in state resurrected in period t that are active again within the following window" },
    { "id": "reactivation_rate", "name": "reactivation rate", "definition": "share of at_risk_wau / at_risk_mau entities that return to activity" },
    { "id": "resurrection_rate", "name": "resurrection rate", "definition": "share of dormant entities that return to activity" }
  ],
  "invariant": "states are mutually exclusive and collectively exhaustive; state counts must sum exactly to the aggregates every period",
  "sources": ["GUSTAFSON-2023", "MAZAL-2023"]
}
```

> Rate definitions are operational paraphrases — the source articles name the rates without publishing exact formulas. Fix one convention here and keep it stable; changing a window silently is a metric-definition incident.

## 3. Classification query skeleton

Vendor-neutral SQL sketch; adapt names and date functions to your warehouse.

```sql
-- One row per entity per period, assigning exactly one state.
with activity as (
  select
    entity_id,                          -- [TODO: your entity key]
    max(event_date) filter (where event_date <  current_date) as last_active_before_today,
    min(event_date)                     as first_active_ever,
    bool_or(event_date = current_date)  as active_today
  from [TODO: canonical_activity_events]
  group by entity_id
)
select
  entity_id,
  case
    when active_today and first_active_ever = current_date                       then 'new'
    when active_today and last_active_before_today >= current_date - 6           then 'current'
    when active_today and last_active_before_today >= current_date - 29         then 'reactivated'
    when active_today                                                            then 'resurrected'
    when last_active_before_today >= current_date - 6                            then 'at_risk_wau'
    when last_active_before_today >= current_date - 29                           then 'at_risk_mau'
    else 'dormant'
  end as state
from activity;
```

Transition rates come from joining today's snapshot to yesterday's on `entity_id` and counting state pairs.

## 4. Control plan

| Item | Value |
|---|---|
| Focus rate (from sensitivity analysis) | `[TODO: e.g. curr — chosen by simulation, not intuition]` |
| Current baseline | `[TODO: measured value and date]` |
| Goal | `[TODO: target and horizon]` |
| Owner | `[TODO: name]` |
| Review cadence | `[TODO: weekly recommended]` |
| Expected range | `[TODO: normal week-to-week variation, from history — react outside it, not inside it]` |
| Reaction plan | `[TODO: who does what when the rate leaves the expected range]` |
| MECE audit | `[TODO: automated check that state counts sum to aggregates; alert owner on residual]` |
| Channel guardrail | `[TODO: cap on notification/email volume per entity — reactivation channels degrade permanently if burned]` |

### Sensitivity-analysis worksheet

1. Export the last `[TODO: N]` periods of state counts and transition rates.
2. In a spreadsheet or notebook, project the aggregates forward `[TODO: horizon]` using current rates as constants.
3. For each rate in turn: increase it by one small fixed increment (Duolingo used 2% [GUSTAFSON-2023]), hold the others constant, re-project, and record the aggregate delta.
4. Rank rates by delta. The top-ranked rate that experiments can plausibly move is the focus-rate candidate.
5. Before committing: verify by A/B test that the rate is movable, and that moving it moves the aggregate [GUSTAFSON-2023].

## 5. Agent prompt templates

### Prompt A — classify and compute

```text
You are an analytics agent. Using the retention-state model spec below and the
data source named in it, produce for the period [TODO: date range]:
1. State counts per period, plus the DAU/WAU/MAU aggregates as defined sums.
2. The MECE audit: confirm state counts sum exactly to the aggregates; report
   any residual as a defect, not a footnote.
3. All transition rates in the spec, with numerator and denominator shown.
Do not invent values for data you cannot access; return the query you would
run and mark the result [BLOCKED] instead.

<state-model-spec>
[paste section 2 JSON here]
</state-model-spec>
```

### Prompt B — sensitivity ranking

```text
Using the state counts and transition rates provided below, simulate the
aggregate [TODO: dau | wau | mau] forward [TODO: horizon]. Then, for each
transition rate in turn, increase that rate by [TODO: increment, e.g. 2%],
hold all others constant, re-simulate, and record the delta in the final
aggregate. Output a table ranking rates by delta, and state which top-ranked
rates are plausibly movable by product experiment and which are not, with
one sentence of reasoning each. Show your projection method so a human can
reproduce it in a spreadsheet.

<data>
[paste state counts and rates]
</data>
```

### Prompt C — weekly control-plan readout

```text
You are producing the weekly retention readout defined by the control plan
below. Report: the focus rate this week vs. baseline and expected range;
whether the MECE audit passed; the three largest state-transition changes
vs. last week; and whether the reaction plan triggers. Use the JSON schema
in section 6 of the control plan. Flag any number you computed from fewer
than [TODO: minimum sample] entities as low-confidence rather than omitting
it silently.

<control-plan>
[paste section 4 here]
</control-plan>
```

## 6. Readout schema (agent output contract)

Structure only — values shown are intentionally `[TODO]` placeholders, never examples to imitate.

```json
{
  "period": "[TODO: ISO week or date range]",
  "mece_audit": { "passed": null, "residual_entities": "[TODO: computed]" },
  "focus_rate": {
    "id": "[TODO: e.g. curr]",
    "value": "[TODO: computed]",
    "baseline": "[TODO: from control plan]",
    "within_expected_range": null,
    "low_confidence": null
  },
  "notable_transitions": [
    { "from": "[TODO]", "to": "[TODO]", "change_vs_prior_period": "[TODO: computed]" }
  ],
  "reaction_plan_triggered": null,
  "narrative": "[TODO: three sentences max, written for the owner, no jargon]"
}
```
