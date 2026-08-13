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

Run this as a conversation: an AI agent, or a colleague with this file open, asks you the questions below one or two at a time and gives you the guidance after each answer. You can also run it alone, writing your answers down as you go, and it still works. Where the text says "ask" or "recommend" it is speaking to whoever runs the interview, the guidance comes from this framework's [attribution topic page](../../docs/metrics/attribution.md), and the answers are yours.

This skill walks a founder or team lead through designing attribution they can trust, using the knowledge on the [attribution topic page](../../docs/metrics/attribution.md). It asks questions one or two at a time and gives guidance after each answer. Class-level answers are enough throughout: no internal numbers, customer names, or system details are needed, and nothing here searches the web.

## Stage 1: Frame

Ask, one at a time:

- **Q1.** What outcome are you trying to attribute? A purchase, a signup, a closed deal, something else? Name one.
- **Q2.** Roughly what do you spend on marketing in a year: under $100K, $100K to $10M, or above $10M? A band is enough.
- **Q3.** Which teams touch the path to that outcome today? Marketing, an SDR (sales development rep, the person doing outbound calls and emails to book meetings), partnerships, product, just you?
- **Q4.** For a customer who signed up last week, can you tell where they came from?

Guidance on Q1: if the user cannot name one outcome, stop and route them to the [conversion page](../../docs/metrics/conversion-rate.md) first. Attribution splits credit for an outcome; an undefined outcome has nothing to split.

Guidance on Q4: if the answer is no, stop here, because every recommendation below assumes the source of a customer is recorded somewhere. The first job is not a credit rule. Put one tracking parameter on every link you control so the source arrives with the visit, add "how did you hear about us?" to the signup form, and come back to this skill in a month with a month of answers. A credit rule applied to data that never recorded the source only formalizes a guess.

## Stage 2: Route by size

One variable routes this: marketing spend per year. Take the first row that matches and stop. The bands are ordered and they cover every size. Revenue is a sanity check on the answer rather than the router: a company spending $200K a year against $80M of revenue is still in the middle band, and the revenue figure only tells you the spend is likely to grow.

| Yearly marketing spend | What to do |
|---|---|
| Under roughly $100K | No attribution software. Use last-touch (all credit to the last thing the customer touched before converting), run one channel test at a time, and treat "how did you hear about us?" as a sanity check rather than a decision driver. If only one team touches the outcome, skip Stage 3's go-to-market questions and go straight to Stage 5. |
| $100K to roughly $10M | Last-touch, plus a written list of the channels proven to drive results, plus judgment built on real customer knowledge. Attribution software and multi-touch models rarely pay for themselves in this band. Continue through Stage 3 fully. |
| Above roughly $10M | No per-touch credit rule at all. Marketing mix modeling (MMM: fitting outcome totals against channel spend over time, tracking no individual user) plus scheduled holdouts. Continue to Stage 3's incentive questions, which apply at every size. |

## Stage 3: Interview

Marketing thread, one at a time:

- **Q5.** What rule assigns credit today, even informally, and how long after a touch does a conversion still count? Has either been written down? (If the first answer is "whatever the tool shows," the rule is last-click, the tool default where the last ad or link clicked takes everything, and nobody chose it. If the second is a shrug, the window is whatever the tool defaults to, which is also a choice, just not yours.)
- **Q6.** What decision does the attribution number actually feed? Budget moves, a dashboard nobody acts on, or someone's target?

Go-to-market thread, one at a time:

- **Q7.** Who is paid or scored on this number? Which teams carry it in a quota (the revenue number a salesperson has to hit to be paid in full) or in their OKRs (objectives and key results, the goal-scoring system most companies run on)?
- **Q8.** Can a team that is scored on the number change how it is defined or recorded? (If yes, flag it: the ledger cannot be kept by the teams being scored.)
- **Q9.** What behavior does the current rule pay for, and what behavior does the company actually want more of? Are they the same thing?
- **Q10.** Ask each team, separately, whether what they get from the team upstream is good enough to work with. Write down who says no.

Guidance on Q10: the names on that list are the diagnosis. Every team has inputs and outputs, and the handoff between them tells the story. When the team downstream says the leads, the meetings, or the accounts are not good enough to work with, someone upstream is hitting a number without caring what happens after the handoff, which is a credit rule paying for volume in a company that needs quality.

Pushback rules: do not accept "we track everything" (ask which single decision the number changed last quarter), and do not accept "our attribution is accurate" (ask who verified it by turning something off).

## Stage 4: Recommend

Build the recommendation from the answers, each part traced to the topic page:

- Rule choice by size, from the Stage 2 table. For the top band, state the rule plainly so the decision record has an answer to write down: none per touch, marketing mix modeling plus scheduled holdouts.
- If Q8 flagged self-scoring: recommend a neutral ledger, a win-touch review (a look back at which teams touched the deals that actually closed) run by someone not scored on the number.
- If Q9 found a mismatch: name it plainly as the thing to fix before any tooling; a credit rule that pays for the wrong behavior gets the wrong behavior.
- Verification, scaled to volume. If the outcome happens often enough that turning a channel off would visibly move it, schedule that test: slow season, or one segment, and watch whether the outcome changes. Set the goal and the measurement before the test and do not change them after.
- If volumes are too small for a holdout to resolve anything, which is most of the bottom band and much of the middle one, do not run one. An inconclusive holdout gets read as "no effect" and cuts the wrong channel. Change one thing at a time, watch a rate rather than a volume, and write down the goal and the measurement before you start.

## Stage 5: Output, the attribution decision record

Fill this with the user and hand it over:

```markdown
# Attribution decision record: [TODO: company or product name]

- Decided on: [TODO: date]
- Owner of this record: [TODO: one name, whoever keeps it current]
- Outcome attributed: [TODO]
- Credit rule chosen: [TODO: rule and why, one sentence]
- Window: [TODO: how long a touch counts, written down here on purpose]
- Who is paid or scored on this number: [TODO: teams]
- Who keeps the ledger: [TODO: someone not scored on the number]
- Behavior this rule pays for: [TODO: and confirmation it matches what the company wants more of]
- Verification: [TODO: the holdout, or the one-thing-at-a-time test if volumes are too small; what gets changed, when, in which segment, and what number is watched]
- Revisit when: [TODO: the complexity trigger, meaning a new segment, a new territory, or a new team incentive, not a calendar date]
```
