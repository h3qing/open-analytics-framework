---
id: ltv
title: Lifetime value
type: topic
status: drafted # sourced draft; author opening and interview questions open
summary: >
  What a customer is worth before they leave, how to compute it from your
  own cohort table without building a model, and what the number is for:
  the ceiling on what you can pay to acquire the next customer, the payback
  window that decides whether you can afford that price, and the comparisons
  between channels and segments it makes possible. Also the two ways the
  number goes wrong, both in known directions, and what the famous five
  percent claim actually says in the document it comes from.
keywords:
  - LTV
  - lifetime value
  - CLV
  - CAC
  - LTV to CAC
  - CAC payback
  - contribution margin
  - discount rate
  - churn rate
  - customer lifetime
  - unit economics
---

# Lifetime value

<!-- TODO(heqing): interview — the opening is yours, as on the other pages. The argument to land: this is the page where the other two meet. Entity retention says whether they stayed, value retention says how much they kept, and LTV multiplies the two into one number that a lot of people then steer the whole company by. -->

The [entity page](retention.md) asks whether customers came back. The [value page](value-retention.md) asks how much of what they had they kept. This page is where the two meet: lifetime value, LTV, is what one customer is worth in total before they leave, and it is a survival curve multiplied by a margin.

That makes it the most useful number on these three pages and the easiest one to get badly wrong, because every error in the two inputs arrives here multiplied. It is also the number that decides how much you can pay for the next customer, which is the largest recurring spending decision most companies make. CAC is customer acquisition cost: the acquisition spend divided by the customers that spend produced.

Where to jump: [what the number is](#what-lifetime-value-is) fixes the four decisions that set what your figure means, [how to compute it](#how-to-compute-it-from-your-own-cohort-table) is the arithmetic with a worked example, [the two ways it goes wrong](#the-two-ways-the-number-goes-wrong) is where almost everyone loses it, [what the number is for](#what-the-number-is-for) is the acquisition ceiling and the payback window, and [the five percent claim](#what-the-five-percent-claim-actually-says) is the most quoted sentence in this subject read against its source.

## What lifetime value is

Lifetime value is the total margin one customer produces over the whole relationship, expressed in today's money. Three things go into it and nothing else: how long they stay, how much margin they leave behind each period they are there, and what future money is worth today.

```mermaid
flowchart LR
    C["Survival curve<br/>share of the cohort still paying"] --> V["E(LTV)<br/>survival x margin, discounted"]
    M["Margin per period<br/>revenue minus cost to serve"] --> V
    V --> R["The ceiling<br/>what you can pay for the next customer"]
    V --> P["The payback month<br/>when the money comes back"]
```

Four decisions fix what your number actually means. Each has a common wrong answer, and all four move the figure in a direction you can predict.

| The decision | The common answer, and what it costs | Use instead |
|---|---|---|
| Revenue or margin | Revenue, because it is the number already in the dashboard. It counts money you never keep, and overstates lifetime value by exactly your cost to serve: at a 70 percent gross margin, a revenue-based figure is about 1.4 times too big. | Contribution margin: that customer's revenue minus what it costs to serve them. Acquisition spend stays out of it, because it is the other side of the comparison. |
| Whose lifetime, counted from when | One number for both questions. The value of a customer at the moment you win them and the value remaining in a customer you already have are different numbers with different uses. | The at-acquisition figure for acquisition decisions. The remaining, or residual, value for deciding what to spend keeping someone, and for valuing the base you already have. |
| One customer or the average one | A single company-wide figure. There is no average customer; a base is a mixture, which is the whole subject of [why curves flatten](retention.md#why-curves-flatten). | One figure per segment that behaves differently, and never a blended figure divided by a blended CAC. |
| How far into the future | Silence about the horizon. A sum that stops at month 24 gets quoted as the lifetime value. | Compute over the periods you can actually see, and label it: that number is a floor, because the value beyond your data is real and missing from it [^fader-hardie-2014]. |

One more thing is true of every version of this number. It is a forecast about people who have not left yet, so it is an expected value with a range around it rather than a fact about a customer, which is why the careful notation is E(LTV) [^fader-hardie-2014].

## How to compute it from your own cohort table

The formula is one line, and every term in it comes off a spreadsheet you can already build:

> **E(LTV) = the sum, over each period _t_ = 0, 1, 2 and so on, of margin in period _t_ x share of the cohort still paying in period _t_, divided by (1 + _d_) to the power _t_**, where _d_ is the discount rate for one period and period 0 is the period the customer arrives in, which is why the first period is not discounted.

Five steps, none of which need a model.

1. **Take the survival curve off your cohort table.** One cohort, period by period, the share of it still paying. This is the [triangle](retention.md#reading-a-cohort-curve) from the entity page. Use the survival curve, the share still subscribed, rather than an activity curve, because a customer who stops paying does not come back into the count.
2. **Compute margin per surviving customer per period.** Revenue in that period minus what it costs to serve that customer: infrastructure, payment fees, support, anything third-party that scales with them. Leave sales and marketing out; that is CAC, and double-counting it here is the most common way this number gets quietly deflated.
3. **Pick a discount rate and write it down.** Money three years out is worth less than money now. If nobody in the company can tell you a cost of capital, run the arithmetic at 5 and at 15 percent a year and see whether the decision you are making flips between them. If it does, the decision was too close to call on this number.
4. **Multiply the three columns together and add them up.** That is the whole calculation.
5. **Stop where your data stops, and label what you stopped at.** A sum that ends at month 24 is the value of the first 24 months. Calling it the lifetime value is how a floor turns into a forecast [^fader-hardie-2014].

**Worked, on an illustrative cohort.** Monthly survival off the cohort table, $20 of contribution margin a month per surviving customer, discounted at 10 percent a year, which is a factor of about 0.992 per month:

| Month | Still paying | Margin that month | Discount factor | Discounted | Running total |
|---|---|---|---|---|---|
| 1 | 100.0% | $20.00 | 1.000 | $20.00 | $20.00 |
| 2 | 88.0% | $17.60 | 0.992 | $17.46 | $37.46 |
| 3 | 79.0% | $15.79 | 0.984 | $15.54 | $53.00 |
| 4 | 72.0% | $14.40 | 0.976 | $14.06 | $67.06 |
| 5 | 66.5% | $13.30 | 0.969 | $12.89 | $79.95 |
| 6 | 62.1% | $12.42 | 0.961 | $11.94 | $91.89 |

Carried out to month 24 the same three columns reach $236, and the curve is still climbing when the data runs out. That is the entire method. It assumes nothing about the shape of the curve, which is the point, and it is arithmetic a spreadsheet does in a column.

**The shortcut that looks like a formula.** If retention really were constant at rate _r_ every period and margin constant at _m_, the sum above collapses to _m_ x _r_ / (1 + _d_ − _r_), the version taught as the lifetime value formula. The algebra is exact; the premise is what fails, and it fails in the direction described in the next section. Use it as a sanity check on a number you computed the long way, never as the number itself.

<!-- TODO(heqing): interview — how deep into the math should this page go for a reader with no analyst? The worked table above, or the formulas with a diagram? This was left open on the old combined page too. -->

## The two ways the number goes wrong

**One over the churn rate is not a lifetime.** The standard way to get from a churn rate to a lifetime is to divide one by the churn rate: 5 percent monthly churn becomes a 20-month average lifetime, and it is quick enough that it rarely gets questioned. It holds only if lifetimes follow a geometric distribution, meaning every customer really does have the same constant chance of leaving in every period, and real customer bases do not look like that. Under the formula, a Netflix 8-K reporting 7.2 percent monthly churn implies an average lifetime of 13.9 months, and a Peloton S-1 implies 154 months [^fader-hardie-2026a].

The mechanism is the [sorting effect](retention.md#why-curves-flatten): your churn rate is a mixture rather than a constant, and it keeps re-weighting itself underneath you as the fragile customers leave first. In the worked cohort above, first-month churn is 12 percent, so the shortcut gives an 8.3-month lifetime and an LTV of $167. The two years actually observed are worth $236, and that figure is itself a floor with the curve still climbing. The shortcut does not shave the number; it loses a third of it before the horizon even runs out.

**Pooling cohorts understates the base, which is unusually good news.** Collapsing a multi-cohort retention table into one aggregate retention rate, 0.6912 in one published worked example, understated the residual value of the customer base by 38 percent. The bias runs the same way whenever cohort-level rates rise, which is whenever the base is heterogeneous, which is essentially always [^fader-hardie-2010]. For a small team that is worth more than it sounds: the pooled number is not merely noisy, it is systematically low, so you know which way you are wrong before you do any work.

Both errors are worth knowing together, because they do not cancel. Skipping the discount inflates the answer, by about 8 percent over the two years in the worked example and more over a longer horizon. Dividing one by a churn rate deflates it, by a third over the same two years and by more the flatter the curve gets. A company that makes both mistakes lands on a plausible-looking number and is wrong twice.

## What the number is for

An LTV nobody spends against is trivia. The number exists to answer planning questions, and the biggest one is what you are allowed to pay for the next customer.

**It sets the ceiling on acquisition cost.** Break-even is CAC equal to LTV. Nobody sensible works there, because LTV is a forecast and CAC is a receipt: one of those two numbers can be wrong by half. The convention is to require lifetime value of at least three times acquisition cost [^skok-2013], which buys the margin for error. Treat the three as a convention rather than a finding: it is practitioner guidance rather than a result from a study, and checking a travelling number before steering by it is the reason [benchmarks](README.md) are on this library's list.

**The ratio does not tell you whether you can afford it.** A ratio compares totals; a company dies of timing. The second number is the payback month: how long until the cumulative margin from a customer covers what you paid to get them.

![One cumulative discounted margin curve for an illustrative cohort over 24 months, with two acquisition prices drawn across it. At a CAC of $90 the curve crosses in month 6; at $220 it crosses in month 22. The curve is still climbing at month 24, where the observed data ends. The numbers are illustrative.](figures/cac-payback-curve.svg)

Same customer, same curve, two prices. Both sit below what that customer is worth over the full relationship, so neither loses money in the end. Only one of them is a price a company with ten people can actually pay, because the other is a 22-month loan it has to fund out of its own cash before any of it comes back. The commonly cited threshold is to recover acquisition cost inside twelve months [^skok-2013]; the useful discipline is simply to know the month, and to know it per channel.

**Prices are per channel and per segment, and they move while you spend.** A blended LTV divided by a blended CAC is the single most misleading slide in this subject, because the decision is never about the average customer already bought — it is about the next one. As spend goes up in a channel, acquisition cost goes up with it, and the customers the extra spend buys tend to retain worse, so both sides of the ratio move against you at once. Lifetime value earns its keep as a tool for comparing one channel or campaign against another, and stops being one the moment it becomes the plan itself [^gurley-2012].

Two rules keep the comparison honest, and both are free: compute CAC and LTV over the same cohort, so this quarter's spend is not being divided by customers won last year, and compute both per channel and per segment before averaging anything.

**Where the next dollar goes.** Retention, margin and acquisition cost are three levers on the same number, and they are not the same size. Improving customer retention by 1 percent improves customer and firm value by 3 to 7 percent; the same 1 percent improvement in margin is worth about 1 percent, and in acquisition cost between 0.02 and 0.3 percent [^gupta-2004]. Two caveats travel with that finding, and both are the authors' own: the cost of buying the retention improvement is not in the number, so it does not follow that a firm should always improve retention, and eliminating churn entirely is not advisable, because a firm with 100 percent customer loyalty may simply be underpricing [^gupta-2004].

**What else the number decides**, once it exists and is trusted: what a price change is worth, since a margin improvement compounds over the same lifetime; how much service and support a segment justifies; which segments the product should be built for next, because the spread between segment lifetime values is usually wider than the spread between channels; and what the customer base you already have is worth, which is the residual-value question and the one the [pooling bias](#the-two-ways-the-number-goes-wrong) distorts [^fader-hardie-2010].

**When not to compute it at all.** With a year of data and a curve that has not flattened, an LTV is a forecast with an error bar wider than the number, and it will still get quoted to two decimal places. You do not need lifetime value to know that retention is bad, that a channel is expensive, or that payback is longer than your runway; all three are visible in the cohort table and the payback month, which is why both come first on this page.

<!-- TODO(heqing): interview — at what size does a company actually need LTV as a number, rather than just needing to know that retention is bad? You have made the argument before that a lot of small companies compute this far too early. -->

## What the five percent claim actually says

Almost every argument for spending on retention ends at one sentence: a 5 percent increase in retention increases profits by 25 to 95 percent. The document behind it does not say that.

| | The source | The version in circulation |
|---|---|---|
| Where | A Bain brief by Fred Reichheld [^bain-2001] | A 2014 _Harvard Business Review_ piece, which links to the brief [^gallo-2014] |
| The sentence | "In financial services, for example, a 5% increase in customer retention produces more than a 25% increase in profit." | "increasing customer retention rates by 5% increases profits by 25% to 95%" |
| What moved | One named sector, offered as an example, stated as a floor. The number 95 appears nowhere in the document. | The sector is dropped, the "for example" is dropped, the floor becomes a range, and a 95 percent ceiling arrives from nowhere. |

**And the arithmetic nobody does.** A 5 percent increase in retention means moving a retention rate from 90 percent to 95 percent, which is cutting churn in half. Halving churn is the hardest thing most subscription businesses ever attempt, and a company that could do it on demand would have done it already. Read that way the claim is far less surprising and much less useful as a target. That reading is this framework's, and it needs no citation, because it is arithmetic you can check in your head.

The defensible version of the same argument is the elasticity finding in [where the next dollar goes](#what-the-number-is-for): retention is the strongest of the three levers, by a factor you can defend, with the authors' own caveats attached.

**One line to stop repeating.** You will also hear that keeping a customer costs five times less than winning one. No primary source for it is traceable. Keep it as a slogan if it helps you argue, but do not put it in a plan as a number.

<!-- TODO(heqing): interview — the strongest version of the retention-is-worth-paying-for argument you would actually make to a founder, now that the famous number turns out to be one sector and a floor. Your entity-page answer was the leaky bucket; is this the same argument with money attached, or a different one? -->

## What a team of ten does

Do not build a customer-base valuation model. Four steps, in this order, all of them free:

- **Compute the payback month before you compute anything else.** Margin per customer per month, acquisition spend per channel over the window that produced those customers, and the month the first covers the second. If it is past twelve months you have a cash problem now, and you did not need an LTV to find it.
- **Run the survivor-ratio check** on your own cohort table: each period's survivors divided by the period before. Rising ratios mean the base is a mixture and no single churn rate describes it [^fader-hardie-2026a].
- **If they rise, know which way you are wrong.** Any lifetime from dividing one by a churn rate is too short, any LTV built on it is too low, and any LTV-to-CAC ratio you are steering by is understated. Direction and rough size is most of what a model would have bought you.
- **Then add up the three columns** — survival, margin, discount factor — stop where your data stops, and label the result as the value of the first _N_ months rather than as the lifetime.

One thing not to do: put a blended LTV over a blended CAC on a slide. It is the number most likely to be quoted back at you in a board meeting and least likely to survive being asked which customers it describes.

## Patterns & case studies

No pattern page yet. Three candidates:

- **The lifetime you can defend.** Survivor ratios, the added-up survival curve, and the error direction, as a repeatable check rather than a model [^fader-hardie-2026a] [^fader-hardie-2010].
- **What you can pay for a customer.** The payback ledger, computed per channel on one cohort, with the ceiling and the cash constraint kept separate [^skok-2013] [^gurley-2012].
- **Checking a number before you steer by it.** The five percent claim traced from restatement to source, as the worked example of a general method [^bain-2001] [^gallo-2014].

## Sources & Stories

The two mechanical failures are Fader and Hardie's. The average-lifetime argument and the Netflix and Peloton filings worked through under the formula come from a self-published technical note, read in full [^fader-hardie-2026a]. The pooling bias, the 0.6912 aggregate rate and the 38 percent understatement come from their _Marketing Science_ article, read in full [^fader-hardie-2010]. The sorting effect that explains why both happen is on the [entity page](retention.md) and is not re-derived here. Their December 2014 note on what is wrong with the standard CLV formula is the source for the E(LTV) notation and for the point that a bounded sum ignores everything past the horizon; it could not be fetched from this session's network, so it is cited at thesis level and its entry carries a verification note [^fader-hardie-2014].

The calculation section is method rather than citation. The five steps, the worked table, the two-rate test for the discount rate, and the instruction to label the horizon are this framework's, and the arithmetic is checkable by anyone with a spreadsheet. The closed-form shortcut is the geometric-series collapse of the same sum, derived here rather than imported, and it is presented as a sanity check because its constant-retention premise is the one the rest of the page dismantles.

The elasticity finding is peer-reviewed and was read in full through the authors' hosted copy [^gupta-2004]. Both caveats stated alongside it are the authors' own words rather than this page's hedging, which matters, because the finding is usually quoted without them.

The five percent set piece rests on two documents that were both read directly. The Bain brief was fetched and its full text extracted, and the sentence quoted here is verbatim: one sector, offered as an example, stated as a floor, with no 95 anywhere in it [^bain-2001]. Worth recording that earlier work in this repository listed this document as unreachable; it is reachable, and the entry now carries a working link. The _Harvard Business Review_ restatement is paywalled, but the sentence that matters and its link back to the Bain brief are both in the readable portion [^gallo-2014]. The halving-of-churn reading is this framework's own and needs no citation, because it is arithmetic.

The acquisition-side guidelines are practitioner conventions and are labeled as such on the page. Both the three-times ratio and the twelve-month payback threshold come from David Skok's SaaS metrics writing [^skok-2013]; the article host was unreachable from this session, so the entry records what is cited from it and marks the specifics for verification against the live page, including whether the lifetime value in his ratio is margin-adjusted. Bill Gurley's essay is the source for lifetime value as a tool for comparing channels rather than a plan, and for the observation that acquisition cost rises and customer quality falls as spend is pushed into a channel [^gurley-2012]; it was also unreachable from this session and is cited at thesis level with the same note. Neither source is quoted directly here.

One source is deliberately not used for its numbers. The _Harvard Business Review_ article usually cited as the counterweight, that long-lived customers are not automatically profitable ones, is paywalled beyond its opening [^reinartz-2002]. The figures commonly attributed to it could not be verified, so they do not appear on this page and should not be added without a copy in hand.

The figure is illustrative and says so on its face. It plots the same cohort as the worked table above, carried from month 6 out to month 24, so the table really is the first six rows of what the chart draws: monthly retention starting at 88 percent and drifting up as the fragile customers leave first, $20 of contribution margin a month, discounted at 10 percent a year. The two acquisition prices on it are chosen to make the payback point, not drawn from any company.

Interview questions on this page are unanswered by design, per this repository's working method.

<!-- Footnote targets; full entries with links and caveats live in REFERENCES.md -->

[^bain-2001]: [[BAIN-2001]](../../REFERENCES.md)
[^fader-hardie-2010]: [[FADER-HARDIE-2010]](../../REFERENCES.md)
[^fader-hardie-2014]: [[FADER-HARDIE-2014]](../../REFERENCES.md)
[^fader-hardie-2026a]: [[FADER-HARDIE-2026A]](../../REFERENCES.md)
[^gallo-2014]: [[GALLO-2014]](../../REFERENCES.md)
[^gupta-2004]: [[GUPTA-2004]](../../REFERENCES.md)
[^gurley-2012]: [[GURLEY-2012]](../../REFERENCES.md)
[^reinartz-2002]: [[REINARTZ-2002]](../../REFERENCES.md)
[^skok-2013]: [[SKOK-2013]](../../REFERENCES.md)
