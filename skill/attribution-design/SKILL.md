---
name: attribution-design
description: >
  Design your company's first attribution setup: pick the credit rule
  that fits your size, align it with how teams are paid and scored, and
  leave with a one-page decision record. Run as a guided conversation,
  one or two questions at a time.
topic: ../../docs/metrics/attribution.md
status: draft # first concrete skill; shape per docs/skill-template.md; awaiting author review
---

# Attribution design

This skill walks a founder or team lead through designing attribution they can trust, using the knowledge on the [attribution topic page](../../docs/metrics/attribution.md). It asks questions one or two at a time and gives guidance after each answer. Class-level answers are enough throughout: no internal numbers, customer names, or system details are needed, and nothing here searches the web.

## Stage 1: Frame

Ask, one at a time:

- **Q1.** What outcome are you trying to attribute? A purchase, a signup, a closed deal, something else? Name one.
- **Q2.** Roughly what band is your marketing spend (under $100K a year, $100K to a few million, more) and your revenue (under $50M, over)? Bands only.
- **Q3.** Which teams touch the path to that outcome today? (Marketing, SDR or sales, partnerships, product, just you?)

Guidance: if the user cannot name one outcome, stop and route them to the [conversion page](../../docs/metrics/conversion.md) first. Attribution splits credit for an outcome; an undefined outcome has nothing to split.

## Stage 2: Route by size

Apply the size guide from the topic page:

- **Under roughly $100K of spend:** recommend no attribution software. Last-touch, one channel test at a time, "where did you hear about us?" as a sanity check. Skip to Stage 3's go-to-market questions only if more than one team touches the outcome; otherwise go to Stage 5 and write the record.
- **Under roughly $50M of revenue:** last-touch plus a proven-channels list plus judgment. Continue through Stage 3 fully.
- **Above roughly $10M of spend:** the user has outgrown rule-based debates; recommend media-mix modeling and controlled experiments, and continue to Stage 3's incentive questions, which apply at every size.

## Stage 3: Interview

Marketing thread, one at a time:

- **Q4.** What rule assigns credit today, even informally? (If the answer is "whatever the tool shows," the rule is last-click and nobody chose it.)
- **Q5.** What is the window: how long after a touch does a conversion still count? Has anyone written it down?
- **Q6.** What decision does the attribution number actually feed? Budget moves, a dashboard nobody acts on, or someone's target?

Go-to-market thread, one at a time:

- **Q7.** Who is paid or scored on this number? Which teams have it in their quota or OKRs?
- **Q8.** Can a team that is scored on the number change how it is defined or recorded? (If yes, flag it: the ledger cannot be kept by the teams being scored.)
- **Q9.** What behavior does the current rule pay for, and what behavior does the company actually want more of? Are they the same thing?
- **Q10.** The smell test: for each team, roughly what is the conversion rate from their inputs to their outputs, and does anyone downstream complain about input quality? A rate far below expectations upstream of a complaint usually means someone is exaggerating a number without caring about downstream impact.

Pushback rules: do not accept "we track everything" (ask which single decision the number changed last quarter), and do not accept "our attribution is accurate" (ask who verified it by turning something off).

## Stage 4: Recommend

Build the recommendation from the answers, each part traced to the topic page:

- Rule choice by size (the size guide table).
- If question 8 flagged self-scoring: recommend a neutral ledger, a win-touch review run by someone not scored on the number.
- If question 9 found a mismatch: name it plainly as the thing to fix before any tooling; a credit rule that pays for the wrong behavior gets the wrong behavior.
- Always: schedule a turn-it-off verification. Slow season, or one segment, watch whether the outcome changes. Set the goal and the measurement before the test, and do not change them after.

## Stage 5: Output, the attribution decision record

Fill this with the user and hand it over:

```markdown
# Attribution decision record — [TODO: company or product name]

- Outcome attributed: [TODO]
- Credit rule chosen: [TODO: rule and why, one sentence]
- Window: [TODO: how long a touch counts, written down here on purpose]
- Who is paid or scored on this number: [TODO: teams]
- Who keeps the ledger: [TODO: someone not scored on the number]
- Behavior this rule pays for: [TODO: and confirmation it matches what the company wants more of]
- Turn-off verification: [TODO: what gets turned off, when, in which segment, and what number is watched]
- Revisit when: [TODO: the complexity trigger — new segment, new territory, new team incentive — not a calendar date]
```
