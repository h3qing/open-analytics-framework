# Schema contract control plan

Control artifact for the pattern [Schema drift detection and data contracts (M1-07)](../../docs/modules/01-ai-data-quality/schema-drift-and-data-contracts.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The field-level shape follows the published contract standard's split between logical and physical type [BITOL-ODCS], and the check vocabulary follows the large-scale verification literature [SCHELTER-2018] [BRECK-2019] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** sections 1 and 2 plus the JSON core in section 4 are the machine-readable interface, section 5 is the prompt library, and section 3 stays with the human owner. The smallest complete implementation is one row of the field table: one field, one allowed-values check, run on every load.

## 1. Contracted fields

One row per field your metrics actually read. Get the list by opening the one computation behind each metric that leaves the room and writing down every field it selects, filters on, joins on or groups by. Fields not on this list are not under contract, and that is deliberate.

| Field | Lands in | Read by | Physical type | Unit / timezone, in words | Owner of the change |
|---|---|---|---|---|---|
| `[TODO: column]` | `[TODO: schema.table]` | `[TODO: metric name]` | `[TODO: e.g. integer]` | `[TODO: e.g. amounts in minor units (cents), USD]` | `[TODO: person or team who can change it upstream]` |
| `[TODO: column]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO: e.g. timestamps in UTC, not local]` | `[TODO]` |
| `[TODO: column]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO: n/a]` | `[TODO]` |

> Write the unit and the timezone in words even when they feel obvious. A field that silently changes from days to hours, or from cents to dollars, is undetectable if nobody recorded which it was.

## 2. The checks

Two groups. Structural checks are cheap and mostly redundant with the query failing. Semantic checks are the ones that earn the plan.

### 2a. Structural

| Check | Applies to | Fails when |
|---|---|---|
| Field present | every contracted field | the column is missing from the landed table |
| Type readable | every contracted field | the value cannot be cast to the declared physical type |
| Arrived this load | every contracted field | the load completed with zero rows carrying the field |

> If your transformation tool can declare column names and types on a model and fail the build on a mismatch, let it own this whole group and spend your attention on 2b.

### 2b. Semantic

| Check | Applies to | Parameter | Fails when |
|---|---|---|---|
| Allowed values | categorical fields | `[TODO: the full set your CASE / mapping handles]` | a value outside the set appears |
| Allowed range | numeric fields | `[TODO: min, max]` | a value falls outside |
| Completeness | every contracted field | `[TODO: tolerated null share, e.g. 0.02]` | the share of nulls exceeds it |
| Placeholder values | every contracted field | `[TODO: sentinels to reject, e.g. -1, 0, '', 'Unknown', 'N/A']` | a sentinel appears where a real value is expected |
| Consistency rule | pairs of fields | `[TODO: e.g. if status = 'refunded' then amount <= 0]` | the rule is violated |
| Closed-period stability | the metric's own output | `[TODO: how many prior periods are frozen]` | a closed period's value changes between runs |

Vendor-neutral SQL sketches. Adapt names, date functions and the load marker to your warehouse.

```sql
-- Allowed values: a new category nobody mapped
SELECT DISTINCT status
FROM   [TODO: schema.table]
WHERE  loaded_at >= [TODO: start of this load]
  AND  status NOT IN ([TODO: 'active', 'trialing', 'cancelled']);

-- Completeness: the field started arriving empty
SELECT COUNT(*)                                      AS rows_loaded,
       AVG(CASE WHEN [TODO: column] IS NULL THEN 1.0 ELSE 0.0 END) AS null_share
FROM   [TODO: schema.table]
WHERE  loaded_at >= [TODO: start of this load];

-- Placeholders: passes NOT NULL, means nothing
SELECT COUNT(*) AS placeholder_rows
FROM   [TODO: schema.table]
WHERE  loaded_at >= [TODO: start of this load]
  AND  CAST([TODO: column] AS VARCHAR) IN ('-1', '0', '', 'Unknown', 'N/A');

-- Closed-period stability: a backfill rewrote history
SELECT p.period,
       p.value        AS value_when_first_closed,
       c.value        AS value_now,
       c.value - p.value AS drift
FROM   [TODO: your frozen snapshot table] p
JOIN   [TODO: your metric view]           c ON c.period = p.period
WHERE  p.period < [TODO: the current open period]
  AND  c.value <> p.value;
```

> The last check needs a frozen snapshot to compare against, so write one row per closed period the first time the period closes and never update it. Without that row you cannot tell a backfill from a memory.

## 3. Reaction plan

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where the checks run | `[TODO: job or tool, and at what point in the load]` |
| Cadence | Every load, plus `[TODO: cadence]` for the closed-period check |
| On a structural failure | `[TODO: who]` within `[TODO: e.g. same working day]`; the query is already broken, so fix the input or update the contract |
| On a semantic failure | `[TODO: who]` within `[TODO: e.g. same working day]`. Decide first whether the data is wrong or the contract is stale |
| Quarantine or flag | `[TODO: does a failed load stop downstream models, or land with a warning? Pick one and write it down]` |
| What counts as a legitimate change | A deliberate, explainable upstream change, written down with a date. A new value nobody can explain is not one |
| On a legitimate change | Edit the contract in the same reviewed commit that explains it, and record the date in section 4 |
| On a defect | Fix the input, re-run the load, log it |
| Violation log | `[TODO: where violations and their found causes are recorded]` |

> Deciding this after the first alert fires is how alerts become things people mute.

## 4. Machine-readable core

```json
{
  "spec": "schema-contract-control-plan/v1",
  "owner": "[TODO: name]",
  "warehouse": "[TODO: system]",
  "fields": [
    {
      "id": "[TODO: schema.table.column]",
      "read_by": ["[TODO: metric name, one entry per metric]"],
      "logical_type": "[TODO: string | integer | decimal | timestamp | boolean]",
      "physical_type": "[TODO: the warehouse type as landed]",
      "unit": "[TODO: e.g. minor_units_usd | days | seconds | none]",
      "timezone": "[TODO: e.g. UTC | none]",
      "upstream_owner": "[TODO: person or team]",
      "structural": {
        "required": true,
        "nullable": "[TODO: true | false]"
      },
      "semantic": {
        "allowed_values": ["[TODO: full set, or null if not categorical]"],
        "min": "[TODO: or null]",
        "max": "[TODO: or null]",
        "max_null_share": "[TODO: e.g. 0.02]",
        "reject_placeholders": ["-1", "0", "", "Unknown", "N/A"]
      },
      "last_changed": { "date": "[TODO]", "reason": "[TODO: the explained upstream change]" }
    }
  ],
  "consistency_rules": [
    { "id": "[TODO: short name]", "expression": "[TODO: e.g. status = 'refunded' implies amount <= 0]" }
  ],
  "closed_period_stability": {
    "frozen_periods": "[TODO: how many prior periods are frozen]",
    "snapshot_table": "[TODO: where the frozen values live]"
  },
  "reaction": {
    "on_failure": "[TODO: quarantine | flag]",
    "investigate_within": "[TODO: e.g. same working day]",
    "investigator": "[TODO: name or rotation]",
    "violation_log": "[TODO: location]"
  },
  "sources": ["BITOL-ODCS", "SCHELTER-2018", "BRECK-2019"]
}
```

> The JSON restates sections 1 to 3 in a form any agent can parse. Keep them in step in the same edit; the JSON wins when the prose is ambiguous.

## 5. Agent prompt templates

### Prompt A — run the contract against a landed batch

```text
You are an analytics agent running the schema contract below against one
batch of landed data.
1. For every field in the contract, check the structural conditions
   (present, castable to physical_type, non-empty this load) and report
   pass or fail with the row counts behind each result.
2. Then run the semantic checks: allowed_values, min/max, null share
   against max_null_share, reject_placeholders, and every consistency rule.
3. For each failure, state the field, the rule, the observed value or
   share, and how many rows are affected. Show the SQL you ran.
4. Say nothing about causes. Do not edit the contract, and do not widen a
   constraint to make a check pass.
5. End with a single line: PASS, or FAIL followed by the field ids.

<schema-contract>
[paste section 4 JSON here]
</schema-contract>

<batch>
[paste the table name and the load window, or the rows themselves]
</batch>
```

### Prompt B — triage one violation

```text
A contract check failed. Using the contract and the evidence below, help a
human decide whether the data is wrong or the contract is stale.
1. Restate the rule that failed and what was observed.
2. List what would have to be true for this to be a legitimate upstream
   change rather than a defect, and what evidence would settle it. A new
   category appearing in a status field is the common legitimate case.
3. Draft two options: a data fix, and a contract edit with the exact JSON
   change it would require.
4. Recommend one, and say plainly how confident you are. A human owner
   commits either change.

<schema-contract>
[paste section 4 JSON here]
</schema-contract>

<violation>
[paste the failing check output and any known upstream changes]
</violation>
```

### Prompt C — propose a contract for a new metric

```text
Given the SQL for one metric below, produce the contract rows it implies.
1. List every field the query selects, filters on, joins on or groups by.
   Ignore fields the query does not touch.
2. For each field, propose logical_type, physical_type, and whether it is
   required. Where the unit or timezone is not derivable from the SQL, write
   [TODO: ask the owner] rather than guessing.
3. Where a CASE expression or an IN list enumerates categories, propose
   allowed_values as exactly that set, and flag any ELSE or default branch
   as a place where an unmapped value would be swallowed silently.
4. Output a section 4 JSON block. Leave every value you could not derive as
   a [TODO].

<metric-sql>
[paste the one computation behind the metric]
</metric-sql>
```

## 6. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where this plan lives | `[TODO: repository path, version controlled beside the query it protects]` |
| Review rule | Contract changes are edits to this file, reviewed like code, each with a date and the explained upstream change behind it |
| Scope review | `[TODO: e.g. quarterly]`, re-derive the field list from the current metric computations and drop fields no metric reads any more |
| Standing check | If no check has failed in `[TODO: e.g. a quarter]`, verify the checks still run and still cover the fields the metrics read. A silent contract and a dead contract look identical |
