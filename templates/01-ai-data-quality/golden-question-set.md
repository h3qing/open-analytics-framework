# Golden question set

Control artifact for the pattern [Golden question sets for AI analytics validation (M1-04)](../../docs/modules/01-ai-data-quality/golden-question-sets.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The value-comparison conventions follow the execution-comparison feature one platform documents [DATABRICKS-2026], the accepted-alternative practice follows LinkedIn's internal assistant [CHEN-2024], and the repeat-run rule follows Uber's stated run-to-run variance [KHUNE-2024] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** the agent never reads this file. Section 3 is the machine-readable core a run harness consumes; the harness sends the agent one question at a time, from the question text only. Section 4 is the prompt library, section 5 is the run log, and section 6 stays with the human owner.
>
> **What never leaves this file:** the expected values. They are real numbers about your business, and they are also the answer key. A test the agent can read passes by construction.

## 1. The questions

One row per question. Start with five rows from the numbers that leave the room, then the traps, then at least one refusal. Every row the team has already been burned by goes in.

| # | Question | Expected value | Verified how | Tolerance | Trap it guards | Last run | Result |
|---|---|---|---|---|---|---|---|
| 1 | `[TODO: e.g. revenue recognized in the last closed quarter]` | `[TODO: the value, pinned to a closed period]` | `[TODO: e.g. the billing system's quarter-close report, checked by a named person]` | `[TODO: e.g. 0.1 percent, or exact]` | `[TODO: e.g. a lookalike table, or none]` | `[TODO: date]` | `[TODO: pass / fail / flaky]` |
| 2 | `[TODO: a trap question]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO: the trap]` | `[TODO]` | `[TODO]` |
| 3 | `[TODO: a question the data cannot answer]` | refuse | `[TODO: why the data cannot answer it, e.g. the table starts after the period asked about]` | must decline | confident answer about missing data | `[TODO]` | `[TODO]` |
| 4 | `[TODO: a question that once produced a wrong answer in production]` | `[TODO: the right answer]` | `[TODO]` | `[TODO]` | `[TODO: what went wrong the first time]` | `[TODO]` | `[TODO]` |

> Rules for a row. The period is closed, so the value never moves. A person looked the value up in a system they trust, and the row says which system and who. The tolerance is written down, and zero is a valid choice. A row whose value cannot be verified by hand is not a golden question yet; put the question in a holding list, not in this table.

Accepted alternatives, one row per second answer that turned out to be equally right:

| # | Alternative accepted answer | Why it is also right | Accepted on | By |
|---|---|---|---|---|
| `[TODO: question number]` | `[TODO]` | `[TODO: e.g. a different but defensible reading of the question]` | `[TODO: date]` | `[TODO: name]` |

> Register the alternative; never loosen the tolerance to admit it. The two look the same on a pass rate and are opposite in effect.

## 2. Composition check

| Kind of question | Rows | Minimum |
|---|---|---|
| Numbers that leave the room, pinned to a closed period | `[TODO: row numbers]` | 5 |
| Known traps | `[TODO: row numbers]` | 3 |
| Refusals | `[TODO: row numbers]` | 1 |
| Wrong answers already seen in production | `[TODO: row numbers]` | every one |

> Twenty rows a founder can verify beat a hundred nobody can. If the table is growing faster than the verification, stop adding rows.

## 3. Machine-readable core

```json
{
  "spec": "golden-question-set/v1",
  "owner": "[TODO: name]",
  "location": "[TODO: repository path; never inside the context file or any store the agent reads]",
  "repetitions": 3,
  "pass_rule": "a question passes when every repetition lands within tolerance; two of three is flaky, not passing",
  "questions": [
    {
      "id": "[TODO: e.g. q01]",
      "kind": "[TODO: leaves_the_room | trap | refusal | seen_in_production]",
      "question": "[TODO: the question text, exactly as it will be asked]",
      "expected": {
        "type": "[TODO: scalar | rows | refusal]",
        "value": "[TODO: the value, or the rows, or null for a refusal]",
        "period": "[TODO: the closed period the value is pinned to]",
        "verified_how": "[TODO: system and report]",
        "verified_on": "[TODO: date]",
        "verified_by": "[TODO: name]"
      },
      "comparison": {
        "tolerance": "[TODO: e.g. relative 0.001, absolute 0, or exact]",
        "rounding": "[TODO: e.g. 4 significant digits]",
        "order_matters": false
      },
      "trap": "[TODO: one line, or null]",
      "accepted_alternatives": [],
      "definition_version": "[TODO: the version of the metric definition this row belongs to]",
      "effective_from": "[TODO: date]",
      "retired_on": null
    }
  ],
  "on_failure_order": ["context", "model", "data", "answer_key"],
  "sources": ["DATABRICKS-2026", "CHEN-2024", "KHUNE-2024"]
}
```

> The JSON is what a harness runs. Keep it in step with section 1 in the same edit; the JSON wins when the prose is ambiguous. A change to an expected value is a new entry with a new `effective_from` and the old entry given a `retired_on`, never an edit in place; an answer key with no history cannot tell a fix from a cover-up.

## 4. Agent prompt templates

### Prompt A — one question, as the harness sends it

```text
Answer the question below about our data. Rules:
1. Show the query you ran and the value it returned.
2. State which metric definition, which standing filters, and which table
   you used.
3. If the data cannot answer the question, say so and stop. Do not
   estimate and do not substitute a nearby question.
4. Do not invent values for data you cannot access; return the query you
   would run and mark the result [BLOCKED] instead.

<business-context-file>
[paste the context file here only if the agent does not already carry it]
</business-context-file>

Question: [TODO: one question from section 3, the text only]
```

> One question per conversation, with no history, so a later question cannot borrow an earlier answer. Never include the expected value, the tolerance, or the trap.

### Prompt B — classify a failure, for the owner

```text
A golden question failed. Below are the question, its expected value with
how it was verified, and the agent's answer with its query. Decide which
is most likely, in this order: (1) the context the agent was given is
missing or wrong, (2) the model misread the question, (3) the data itself
changed, (4) the expected value is wrong or stale. Say which, point to the
evidence in the query, and propose the one-line fix. If the expected value
is wrong, propose a new row with today's date; do not edit the old one.

<question-row>
[paste the entry from section 3]
</question-row>

<agent-answer>
[paste the agent's answer and query]
</agent-answer>
```

## 5. Run log

One entry per run. Append, never overwrite.

| Run date | Trigger | What changed | Passed | Failed | Flaky | Findings, by kind | Signed off by |
|---|---|---|---|---|---|---|---|
| `[TODO: date]` | `[TODO: change / schedule / dispute]` | `[TODO: e.g. model version, prompt, context file commit, a table]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO: e.g. context 2, model 0, data 0, key 1]` | `[TODO: name]` |

```json
{
  "run_id": "[TODO]",
  "run_at": "[TODO: timestamp]",
  "trigger": "[TODO: change | schedule | dispute]",
  "changed": "[TODO: what changed since the last run, one line]",
  "agent": "[TODO: tool and model version]",
  "repetitions": 3,
  "results": [
    {
      "id": "[TODO: question id]",
      "runs": ["[TODO: pass | fail]", "[TODO: pass | fail]", "[TODO: pass | fail]"],
      "verdict": "[TODO: pass | fail | flaky]",
      "finding": "[TODO: context | model | data | answer_key, or null]",
      "fix": "[TODO: one line, or null]"
    }
  ],
  "summary": {
    "passed": "[TODO: count]",
    "failed": "[TODO: count]",
    "flaky": "[TODO: count]",
    "flake_rate": "[TODO: flaky divided by questions]"
  },
  "signed_off_by": "[TODO: name]"
}
```

> The flake rate is a number in its own right. A rising flake rate with nothing changed usually means a hosted model updated under you.

## 6. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where the set lives | `[TODO: repository path, outside anything the agent reads]` |
| Run after | Any change to the agent, the model version, the prompt, the context file, or a table a question reads |
| Run on a schedule | `[TODO: e.g. weekly, five questions, to catch a hosted model updating under you]` |
| Repetitions | 3. Two of three is flaky, not a pass. |
| On a failure | The owner classifies it within `[TODO: e.g. two working days]` using Prompt B, in the order context, model, data, key |
| On a disputed production answer | It becomes a row within `[TODO: e.g. one week]`, with the right answer recorded |
| On a definition change | Expect failures. The failing rows are the change's blast radius. New rows carry new effective dates and old rows are retired, never edited. |
| Review rule | Every edit to this file is reviewed like code, because an edit here changes what counts as right. |
