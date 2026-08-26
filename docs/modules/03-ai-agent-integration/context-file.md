---
id: M3-06
title: The one file your AI should read before it answers anything
module: 3B
type: pattern
status: drafted # full sourced draft; awaiting author voice pass per AGENTS.md constraint 6
sources:
  - RUMIANTSAU-2026
  - GANZ-2026
  - LIAO-2026
  - LI-2023
  - KHUNE-2024
  - OPENAI-2026
  - AGENTSMD
template: ../../../templates/03-ai-agent-integration/context-file.md
summary: >
  Write one short plain-text context file, kept in your own repository,
  that every AI agent reads before answering anything about your data:
  your metrics with grain and standing filters, the calendar, the
  customer definition, the quirks, and the lookalike-table rules. Written before any tool decision,
  because the file moves answer quality more than the tool does.
keywords:
  - context file
  - business context
  - grounding
  - text-to-SQL
  - metric definitions
  - semantic document
  - agent context
  - portability
---

# The one file your AI should read before it answers anything

## Problem

Point an AI agent at your warehouse and it sees table names, column names, and nothing else. The schema does not say which of two similar revenue tables is the one you quote, or that a customer means a paying account rather than a signup. So the agent guesses, and the guess comes back as fluent SQL returning a number that reads like a right answer.

When the wrong numbers surface, the fix everyone reaches for is a better model, because a wrong answer looks like a capability problem. The measured evidence says the lever is elsewhere. In a paired benchmark, three frontier models were statistically indistinguishable from each other, and a small hand-written document of measures and conventions moved every one of them up by seventeen to twenty-three points.[^rumiantsau-2026] Where the answer depends on unwritten business knowledge, the best system on an enterprise benchmark reached 15.9 percent.[^liao-2026] What your company knows and has not written down is the thing no model upgrade supplies.

<!-- TODO(heqing): a class-level story from your own work of an agent guessing at an ambiguous table: what was ambiguous, what it answered, and who caught it. -->

## When this applies

- You are connecting an AI agent of any category to your company's data, or still deciding which one. Write the file first either way: it is the input to a fair tool evaluation, and it survives the choice.
- You have no analyst. The file costs one afternoon and no money, and it moves whole when you switch tools.

## The pattern

Write one plain-text context file, keep it in your own repository, and have every agent read it in full before answering anything about your data. It holds the metrics you actually quote, each with formula, grain, standing filters, and source of truth, plus the calendar, the customer definition, the quirks, and the lookalike-table rules. Keep it short enough to send with every question. Give it one named owner, and review every edit like code, because an edit here changes every downstream answer.

```mermaid
flowchart LR
    subgraph repo ["Your repository"]
        FILE[["The context file<br/>metrics: formula, grain, standing filters, source of truth<br/>business context: calendar, customer, quirks<br/>disambiguation: canonical tables, synonyms, refusals<br/>one owner, edits reviewed like code"]]
    end
    Q(["A question about<br/>your data"]) --> AGENT
    FILE -->|"read in full,<br/>every question"| AGENT
    AGENT(["Any agent<br/>this year's or next year's,<br/>general or purpose-built"]) --> ANS["An answer computed with<br/>your definitions"]
```

Swapping the agent moved answer quality within noise. Adding the file moved every agent by seventeen points or more.[^rumiantsau-2026]

## Position

Write the context file before you change tools or models, and before you buy anything, not after.

The common order is the reverse. A team connects a tool, gets wrong answers, and upgrades the model or shops for a better tool, because a wrong answer looks like a capability problem and an upgrade asks nothing of anyone. Writing the file is an afternoon of work, so it loses by default.

The evidence says the file is the fix. The paired benchmark found the models interchangeable and the document not.[^rumiantsau-2026] A transformation-tool vendor's own benchmark points the same way: its two frontier models performed almost identically, and the gains came from modeling and context work.[^ganz-2026] And the file is not only for the machine. On a benchmark that ships a sentence of written business knowledge with each question, people gained almost exactly as much from it as the strongest model did, 20.6 points against 20.0.[^li-2023] The file is onboarding material for anyone who answers questions about your data, and the agent is the newest hire who reads it.

Where the file lives is the position's second half. Keep it wherever your context already lives and your agent can already read: a git repository is the default, and the wiki or shared document workspace your team writes in works too, as long as you can export the file whole. What matters is that the working copy is plain text you control, with everything a tool derives from it treated as a rebuildable cache. One dated event shows the exposure: a platform vendor retired its hosted assistant objects and provided no automated migration for the conversations inside them.[^openai-2026] A plain-text file you can export moves anywhere in an afternoon.

## Implementation

The [template](../../../templates/03-ai-agent-integration/context-file.md) carries the section skeleton, the machine-readable core, and the agent prompts. The sequence below is one afternoon for one person.

1. **List the numbers you actually quote.** For each of the three to ten metrics that already leave the room, write a one-sentence formula, the grain ("one row per subscription per day"), the standing filters, and the one authoritative table.
2. **Write the business-context block.** Say when the fiscal year starts, what counts as a customer against the nearby thing it is not, and the timezone and currency every number is reported in.
3. **Write the disambiguation rules.** Name the canonical table for each entity and the lookalikes the agent must never use. List the words your company uses that the systems do not, and the questions the agent should refuse.
4. **Add the quirks.** Write down what a person learns the hard way in the first month, such as a snapshot table that must not be summed over time. Where a needed filter can be built into the table itself, do that instead, because a documented filter is a filter the agent may skip.
5. **Send it whole.** Do not index it and do not retrieve pieces of it. Keep it under a few pages; the measured document was about four kilobytes.[^rumiantsau-2026] AGENTS.md, a plain-markdown file at the repository root, gives it a location many agents already look for;[^agentsmd] carrying business context there is this framework's extension of the format.
6. **Name one owner and bind changes.** The file changes in the same commit as the thing it describes, and every edit gets a review. Keep five questions whose answers you already know, and re-run them after any change.

<!-- TODO(heqing): what did you write first in your own context file, and how long did the first version that visibly helped take? -->

## How you know it is working

- Answers state which metric definition they used and which table they read, and both match the file.
- The five held-back questions keep returning the answers you already know, including after edits.
- Swapping the model or the agent barely moves your hit rate, which means the lever is the file.
- **Anti-signal:** the file exists but answers contradict it. The agent is not reading it, and the file is decoration.

## Failure modes

- **Connecting first, writing later.** The first week is spent on confident wrong numbers, and in the framework's judgment that trust does not come back with later accuracy gains. <!-- TODO(heqing): have you watched a team lose trust in an assistant's numbers in its first week, and did the trust return once accuracy improved? -->
- **The file becomes an index.** The file grows, someone connects the wiki, and retrieval replaces reading. A large engineering team saw accuracy decline as similarity search covered more tables, and replaced it with small curated collections per domain.[^khune-2024] When the file outgrows a few pages, split it by domain. Do not index it.
- **Restating a formula a system already owns.** The definition then lives in two places and they drift. The file names the owner of a definition, and restates a formula only when nothing else holds it.
- **The file becomes a wiki page.** Once anyone can edit it, an edit silently changes every answer. This is privileged configuration, not documentation, so it belongs somewhere with review on write.
- **Customer names in the payload.** The file travels to the model vendor with every question. Keep named customers, contract values, and personal details out, and write "our largest account" instead of the name.
- **Reading the gain as a guarantee.** Roughly a third of questions still failed with the document present.[^rumiantsau-2026] The file is necessary and not sufficient, so an answer that matters still gets its own check.
- **Written once.** A definition changes and the file does not, so the agent answers from the old one with unchanged confidence. Bind edits to the commit that changes the thing described, and let the five held-back questions be the alarm.

## Sources & Stories

The paired benchmark is by Michael Rumiantsau and Ivan Fokeev, verified at abstract level; an earlier pass places the authors at a semantic-layer company, so the source is treated as commercially interested, though its measured artifact is a plain markdown file rather than an engine [^rumiantsau-2026]. The corroborating benchmark is by two employees of the vendor whose semantic layer it scores, with the conflict disclosed and only eleven questions, so its numbers are used for direction [^ganz-2026]. The enterprise ceiling is the EntSQL benchmark, cited at abstract level [^liao-2026], and the matched human and model gains are Table 2 of the BIRD paper [^li-2023]. The retrieval story is a first-party account from a large ride-hailing company; the savings figures that circulate with it do not appear in the company's own post [^khune-2024]. The platform retirement is the vendor's own migration guide, fetched on the shutdown date it names [^openai-2026]. The instruction-file format's page self-reports its adoption counts [^agentsmd].

The position's ordering follows the research behind this module; the review rule, the named owner, the held-back questions, and the same-commit binding are the framework's own. The prior-art row is pending in [prior-art.md](../../prior-art.md).

<!-- Footnote targets; full entries with links and caveats live in REFERENCES.md -->

[^agentsmd]: [[AGENTSMD]](../../../REFERENCES.md)
[^ganz-2026]: [[GANZ-2026]](../../../REFERENCES.md)
[^khune-2024]: [[KHUNE-2024]](../../../REFERENCES.md)
[^li-2023]: [[LI-2023]](../../../REFERENCES.md)
[^liao-2026]: [[LIAO-2026]](../../../REFERENCES.md)
[^openai-2026]: [[OPENAI-2026]](../../../REFERENCES.md)
[^rumiantsau-2026]: [[RUMIANTSAU-2026]](../../../REFERENCES.md)
