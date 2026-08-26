# Business context file

Control artifact for the pattern [The one file your AI should read before it answers anything (M3-06)](../../docs/modules/03-ai-agent-integration/context-file.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The section shape follows the hand-authored document a paired benchmark measured, about four kilobytes [RUMIANTSAU-2026] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** send sections 1–3 to the agent, in full, with every question. Section 4 is the prompt library, and section 5 stays with a human owner. Keep the filled-in file to one to three pages. If it outgrows that, split it by business domain; do not index it and do not retrieve fragments of it.
>
> **What never goes in this file:** named customers, contract values, salaries, or any personal detail, because the file travels to your model vendor with every question. Write "our largest account", never the name.

## 1. Definitions

The three to ten metrics your company actually quotes. If you cannot fill a cell, that is the ambiguity the agent is currently guessing at.

| Metric | Formula in one sentence | Grain | Filters that always apply | Source of truth |
|---|---|---|---|---|
| `[TODO: metric name]` | `[TODO: e.g. "sum of active subscription amounts in the billing system, excluding test mode"]` | `[TODO: e.g. "one row per subscription per day"]` | `[TODO: e.g. "test accounts and internal users excluded"]` | `[TODO: the one table or system]` |
| `[TODO: metric name]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

> If a definition already lives in a modeled layer or a definitions repository, the formula cell names that owner ("defined in `[TODO: model name]`") instead of restating the formula. A restated formula is a second copy that will drift.

Terms that mean something specific here:

| Term people say | What it means here | Not to be confused with |
|---|---|---|
| `[TODO: e.g. "customer"]` | `[TODO: e.g. "a paying account"]` | `[TODO: e.g. "a signup, a seat, a workspace"]` |
| `[TODO: term]` | `[TODO]` | `[TODO]` |

## 2. Business context

| Item | Value |
|---|---|
| Fiscal year starts | `[TODO: month]` |
| "Last quarter" today means | `[TODO: date range]` |
| Reporting timezone | `[TODO]` |
| Reporting currency | `[TODO]` |
| What counts as a customer | `[TODO: entity and paying status, stated against the nearby thing it is not]` |
| Canonical table per entity | `[TODO: entity → table, one line each]` |
| Tables the agent must never use | `[TODO: table and one-line reason, e.g. staging or deprecated]` |
| Known data quirks | `[TODO: one line each, e.g. a snapshot table that must not be summed over time, a text field storing yes/no as strings, placeholder identifiers]` |
| Questions the agent should refuse | `[TODO: classes of question, and what to say instead]` |

> Quirks are the things a new hire learns the hard way in their first month. If a quirk is really a missing filter, build the filter into the table and delete the quirk line; a documented filter is a filter the agent may skip.

## 3. Machine-readable core

```json
{
  "spec": "business-context-file/v1",
  "owner": "[TODO: name]",
  "last_changed": { "date": "[TODO]", "by": "[TODO]", "why": "[TODO: one line]" },
  "fiscal_calendar": {
    "year_starts": "[TODO: month]",
    "timezone": "[TODO]",
    "currency": "[TODO]"
  },
  "customer_definition": "[TODO: one sentence]",
  "metrics": [
    {
      "id": "[TODO]",
      "definition": "[TODO: one sentence]",
      "grain": "[TODO]",
      "standing_filters": ["[TODO]"],
      "source_of_truth": "[TODO: table or system]"
    }
  ],
  "canonical_tables": [
    { "entity": "[TODO]", "table": "[TODO]", "never_use": ["[TODO: lookalike tables]"] }
  ],
  "synonyms": [
    { "people_say": "[TODO]", "system_calls_it": "[TODO]" }
  ],
  "refuse": ["[TODO: question classes the agent declines]"]
}
```

> This block restates sections 1–2 in a form any agent can parse. Keep the two in step in the same edit; the JSON wins when the prose is ambiguous.

## 4. Agent prompt guidance

### Prompt A — answer a question with the file

```text
Read the business context file below before answering. Rules:
1. Use only the definitions, filters, and source-of-truth tables it names.
   State in your answer which metric definition, which standing filters, and
   which table you used.
2. Never use a table listed under never_use.
3. If the file and the schema disagree, or the file does not cover the
   question, say so and stop rather than guessing.
4. If the question falls in a refused class, decline and point to the file.
5. Do not invent values for data you cannot access; return the query you
   would run and mark the result [BLOCKED] instead.

<business-context-file>
[paste sections 1-3 here]
</business-context-file>

Question: [TODO: the question]
```

### Prompt B — staleness check

```text
Answer each question below using the business context file provided,
independently, showing the query for each. Do not look at the expected
answers; you are not given them.

<business-context-file>
[paste sections 1-3 here]
</business-context-file>

Questions:
[TODO: five questions whose answers the owner already knows]
```

> Run Prompt B after every change to the file or to a table it names. A wrong answer to a known question is the staleness alarm. Keep the questions and answers out of the file itself, or the check passes by construction.

## 5. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where the file lives | `[TODO: repository path — your own repository, plain text, never only inside a vendor's platform]` |
| Review rule | Every edit is reviewed like code, because an edit to this file changes every downstream answer the agent gives. |
| Change binding | The file changes in the same commit or pull request as the thing it describes. |
| Staleness check | Prompt B, after every change, against the five known answers. |

> This file is privileged configuration, not documentation. Anyone who can edit it changes every answer your AI gives, so it belongs somewhere with review on write.
