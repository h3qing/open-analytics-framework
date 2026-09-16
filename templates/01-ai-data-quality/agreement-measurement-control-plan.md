# Agreement-measurement control plan

Control artifact for the pattern [Agreement measurement for analytics QA (M1-05)](../../docs/modules/01-ai-data-quality/agreement-measurement.md). MIT licensed — copy this file into your own repository, replace every `[TODO: …]` field, and delete the guidance blockquotes. The blinding rule follows the consensus guidance for multi-analyst studies [ACZEL-2021], the repeatability and reproducibility vocabulary follows the international standard for measurement precision [ISO-2023], and the kappa arithmetic is the two-judge form used in attribute agreement analysis [AUST-PONS-2022] (see [REFERENCES.md](../../REFERENCES.md)); everything organization-specific is a `[TODO]`.

> **How to use with an AI analytics agent:** the agent never sees section 2 while the study runs, because the answer sheets are reference answers. Section 3 is the arithmetic, section 4 says what each rate means, section 5 is the machine-readable core a scoring harness consumes, and section 6 is the prompt library. The smallest complete study is one second person, twenty questions, and one afternoon.
>
> **What this plan measures:** how repeatable your own reference answers are, before those answers are used to score anything. Building the twenty questions and comparing answers as values is the job of the [golden question set](golden-question-set.md); this plan sits on top of it.

## 1. Who judges

| Role | Who | Rule |
|---|---|---|
| Judge A, the owner of the golden set | `[TODO: name]` | The verified expected values in the golden set are A's answers. A does not re-answer for this study. |
| Judge B, the second person | `[TODO: name; someone who can answer from the data without A's help, and who does not report to A if that can be arranged]` | Answers all twenty from the question text alone. Sees neither the key nor A's queries. Does not discuss the questions with anyone until the sheet is submitted. |
| Scorer | `[TODO: name; may be A, but only after B's sheet is in]` | Compares values within tolerance, runs the assistant, fills section 2b. |
| Repeat by A (optional) | `[TODO: date, at least four weeks after the key was written]` | A answers the twenty again without opening the key. This measures repeatability, the same person twice; the main study measures reproducibility, two different people. |

> Blind means blind. A walk-through of "how we read these questions" before B starts turns two judges into one, and the study will then pass by construction. If B has a question about wording, B writes it on the sheet as a choice made, and does not ask.

## 2. The answer sheets

### 2a. The two people

One row per golden question. The question text is exactly what the assistant would be sent. "Conditions" is three bullets under the value: what was excluded, which calendar, and when the data was pulled. An assistant writes them from its own query; a person verifies them in seconds. "Tolerance" is the reporting difference a person decided the operation can live with for that metric, set before the study.

| # | Question, as sent to the assistant | Tolerance | A's value (the key) | A's conditions | B's value | B's conditions | Conditions match? | Agree? |
|---|---|---|---|---|---|---|---|
| 1 | `[TODO]` | `[TODO: e.g. 0.1 percent, or exact]` | `[TODO]` | `[TODO: excluded / calendar / as-of]` | `[TODO]` | `[TODO: excluded / calendar / as-of]` | `[TODO: yes / no]` | `[TODO: yes / no]` |
| 2 | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |
| … | | | | | | | | |
| 20 | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

> Check the conditions first. Two answers whose conditions differ are a disputed row whatever the values say, because a matching value under different conditions is a coincidence that will split later. Two answers whose conditions match agree when the values land within the tolerance. Write the reason for every disputed row in section 2b before anyone argues about who was right.

### 2b. The assistant, scored three ways

Filled by the scorer after both sheets are in. The assistant is sent the question text only, one question per conversation, three repetitions as the golden set requires.

| # | Two people agree? | Assistant's value | Matches A? | Matches B? | Reading |
|---|---|---|---|---|---|
| 1 | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO: settled, assistant right / settled, assistant wrong / disputed: what the question left open]` |
| … | | | | | |
| 20 | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

> A disputed row is not scored. It does not count for or against the assistant, whichever person it sided with. It goes to section 4 as a definitions item.

## 3. The agreement arithmetic

Spreadsheet-ready. One row per question, and everything below is a column or a cell.

1. **Agreement per row.** First `conditions_match`, by hand, from the two conditions columns. Then `agree = conditions_match AND ABS(A_value - B_value) <= tolerance` for an absolute tolerance, or `ABS(A_value - B_value) / ABS(A_value) <= tolerance` for a relative one. Exact rows agree only when equal. Refusal rows agree when both people declined.
2. **Human agreement rate.** `p = COUNTIF(agree, TRUE) / n`, with `n = 20`. This is the ceiling.
3. **The band.** `half_width = SQRT(p * (1 - p) / n)`, and in questions, `ROUND(n * half_width)`. At twenty questions and a rate of 0.75, the half-width is 0.097, which is about two questions either way. The band runs from `p - half_width` to `p + half_width`. This two-question band is the framework's own rule of thumb, chosen because it fits in one cell; a formal interval would be wider and would say less.
4. **Assistant against each person.** `a_A = COUNTIF(matches_A, TRUE) / n` and `a_B = COUNTIF(matches_B, TRUE) / n`. Percent agreement is the number for values: two people landing within a tenth of a percent of each other by chance is not a real risk, so no chance correction is applied.
5. **Assistant on the settled questions.** `settled = COUNTIF(agree, TRUE)` and `a_settled = COUNTIFS(agree, TRUE, matches_A, TRUE) / settled`. The misses inside this subset are the assistant's own errors, and they are the worklist.
6. **Kappa, for pass-or-fail verdicts only.** When A and B have each marked the assistant's answers pass or fail, build the four cells: `a` = both pass, `b` = A pass and B fail, `c` = A fail and B pass, `d` = both fail. Then `po = (a + d) / n`, `pe = ((a + b) / n) * ((a + c) / n) + ((c + d) / n) * ((b + d) / n)`, and `kappa = (po - pe) / (1 - pe)`. Worked: with `a = 11`, `b = 3`, `c = 2`, `d = 4`, `po = 0.75`, `pe = 0.70 × 0.65 + 0.30 × 0.35 = 0.56`, and `kappa = 0.19 / 0.44 = 0.43`. Report kappa beside `po`, never alone: when most answers pass, `pe` climbs and kappa collapses between judges who agree on nearly everything.
7. **Repeatability, if A re-answered.** The same arithmetic as steps 1 and 2 with A's second sheet against the key. A repeatability rate below the reproducibility rate means the questions have moved in the owner's own head, and the key needs its dated rows checked.

## 4. What a rate means

| Reading | What it means | What to do | Within |
|---|---|---|---|
| Values match, conditions differ | A coincidence, not an agreement; the two numbers will split later | Record the row as disputed and write the two conditions side by side | Before scoring |
| Any disputed rows | The question has two defensible readings, and the assistant will answer it confidently either way | One line per row in the [context file](../03-ai-agent-integration/context-file.md) naming the chosen reading, and a dated new row in the golden set; the old row is retired, never edited. The row is not scored until then. | `[TODO: e.g. one week]` |
| Human rate of 20 of 20 on the first run | The blind probably broke, or the questions cannot catch anything | Check that B saw nothing; add the traps the golden set asks for; rerun | Before scoring |
| Human rate below 12 of 20 | The questions, not the people, are the problem | Rewrite each question with the period, the filter and the definition stated in the text; rerun both sheets. The floor is the framework's own. | Before scoring |
| Assistant inside the band against either person | Its disagreement with the key is inside the key's own variation | No model work. The next hour goes into the disputed rows above. | Same day |
| Assistant below the band against both people | A real gap beyond what the definitions explain | Work the misses on the settled rows in the golden set's order: context, then model, then data | `[TODO: e.g. two working days]` |
| Misses on settled rows, at any assistant rate | The assistant's own errors | Each is a finding in the golden set's run log, classified in the same order | Same as above |
| The human rate moved between two runs | Maybe a change, maybe noise | Put the rate on a control chart with the [SPC control plan](spc-control-plan.md); react outside the limits, not inside | On the next run |

> The ceiling excuses nothing below it, and it rises. Every disputed row that becomes a written definition raises the human rate on the next run, and the assistant is held to the new rate.

## 5. Machine-readable core

```json
{
  "spec": "agreement-measurement/v1",
  "golden_set": "[TODO: path to the golden question set this study sits on]",
  "judges": {
    "a": { "name": "[TODO]", "role": "owner", "sheet": "the golden set's expected values" },
    "b": { "name": "[TODO]", "role": "second_person", "blind": true, "submitted_on": "[TODO: date]" },
    "scorer": "[TODO: name]"
  },
  "n": 20,
  "rows": [
    {
      "id": "[TODO: golden question id, e.g. q01]",
      "tolerance": "[TODO: e.g. relative 0.001, absolute 0, exact, or refusal]",
      "a_value": "[TODO]",
      "a_conditions": "[TODO: one line]",
      "b_value": "[TODO]",
      "b_conditions": "[TODO: one line]",
      "agree": "[TODO: true | false]",
      "assistant_value": "[TODO]",
      "matches_a": "[TODO: true | false]",
      "matches_b": "[TODO: true | false]",
      "reading": "[TODO: settled_right | settled_wrong | disputed]",
      "left_open": "[TODO: for a disputed row, what the question did not state; else null]"
    }
  ],
  "results": {
    "human_rate": "[TODO: agreements / n]",
    "band": { "half_width": "[TODO: sqrt(p(1-p)/n)]", "low": "[TODO]", "high": "[TODO]" },
    "assistant_vs_a": "[TODO]",
    "assistant_vs_b": "[TODO]",
    "assistant_on_settled": "[TODO: right on settled / settled]",
    "verdict_kappa": "[TODO: only if both judges marked pass/fail; else null]",
    "disputed_ids": ["[TODO]"],
    "settled_miss_ids": ["[TODO]"]
  },
  "routing": {
    "disputed": "context_file_line_and_dated_key_row",
    "inside_band": "no_model_work",
    "below_band": ["context", "model", "data"]
  },
  "floors": { "human_rate_min": 0.6, "first_run_all_agree_is_anti_signal": true },
  "sources": ["ACZEL-2021", "ISO-2023", "AUST-PONS-2022"]
}
```

> The JSON restates sections 1 to 4 in a form any agent can parse. Keep them in step in the same edit; the JSON wins when the prose is ambiguous. Section 2 stays out of anything the assistant reads while the study runs.

## 6. Agent prompt templates

### Prompt A — score the sheets

```text
You are scoring an agreement-measurement study. Using the rows provided:
1. For each row, decide whether A and B agree within the row's tolerance,
   and whether the assistant's value matches A and matches B. Show the
   comparison for any row that is close to the tolerance.
2. Compute the human agreement rate, the band as sqrt(p(1-p)/n) with n the
   number of rows, the assistant's rate against A, against B, and on the
   settled rows only. If pass/fail verdicts from both judges are present,
   compute observed agreement and kappa exactly as in the plan and report
   both together.
3. List every disputed row with what each person's conditions say about
   what was excluded, which calendar, and when the data was pulled. Do not decide which reading is right.
4. State whether the assistant is inside the band against either person,
   and list the settled rows it missed. Do not propose model changes.

<agreement-measurement-plan>
[paste section 5 JSON here, with the rows filled in]
</agreement-measurement-plan>
```

### Prompt B — turn a disputed row into a definition, for the owner

```text
A golden question has two defensible readings. Below are the question, the
two people's values, and the choice each of them made. Draft, for the owner
to decide:
1. One line for the business context file that states the reading chosen,
   with the period boundary, filter, or definition spelled out so that the
   question can no longer be read the other way.
2. The new golden-set row that follows from that reading, with today's
   date as effective_from. Do not edit the old row; mark it retired.
3. One sentence on what the other reading would be right for, in case
   someone needs that number under a different name.
Do not pick the reading yourself. Present both and stop.

<disputed-row>
[paste the row from section 5, including a_conditions and b_conditions]
</disputed-row>
```

## 7. Ownership and review

| Item | Value |
|---|---|
| Owner (one named person) | `[TODO: name]` |
| Where this plan lives | `[TODO: repository path, outside anything the assistant reads]` |
| Run before | The first time the assistant is scored against the golden set |
| Run again after | Any change to the golden set's expected values, and at least `[TODO: e.g. quarterly]` |
| Second person | Rotates if possible; the same pair for a year drifts toward the same readings |
| On a disputed row | A context-file line and a dated key row within `[TODO: e.g. one week]`; not scored until then |
| On a first run of 20 of 20 | Check the blind before celebrating |
| Review rule | Every edit to this file is reviewed like code, because an edit here changes what counts as agreement. |
