---
id: value-retention
title: Value retention
type: topic
status: drafted # sourced draft; author opening and interview answers pending
summary: >
  Whether the contract value you won renews and expands. What net and
  gross revenue retention each count, why a company can lose a quarter
  of its customers and grow revenue in the same year, what five public
  filings mean by the same metric name, and the renewal ledger a team
  with no analyst can keep by hand.
keywords:
  - value retention
  - net revenue retention
  - NRR
  - gross revenue retention
  - GRR
  - dollar churn
  - logo churn
  - expansion
  - renewal
---

# Value retention

<!-- TODO(heqing): interview — the opening is yours to write, as on the other pages. The argument to land: entity retention asks whether they came back, value retention asks whether the money came back, and a business can be winning one and losing the other at the same time. -->

The [entity page](retention.md) asks whether the users and accounts you won come back. This page asks whether the money does. Those are different questions, and a company can be winning one while losing the other.

The thing being retained here is contract value, so the unit is a dollar rather than a person. ARR is annual recurring revenue, the value of the subscriptions on the books restated as a yearly figure, and MRR is its monthly version.

Where to jump: [gross and net](#gross-and-net-and-why-one-number-is-not-enough) is the pair of numbers and the gap between them, [logo churn and dollar churn](#logo-churn-and-dollar-churn) is why a company can lose a quarter of its customers and grow revenue in the same year, [five filings](#five-filings-five-constructions-one-metric-name) is what the same metric name means in five primary documents, and [the renewal ledger](#what-a-team-of-ten-does) is the version of all this you can keep in a spreadsheet.

## Gross and net, and why one number is not enough

Take the set of customers you had a year ago. Ignore everyone you have won since. Ask what that same set is worth today.

Four things happened to those accounts over the year. Some left. Some cut back. Some stayed flat. Some grew. Which of those you count is the whole difference between the two metrics.

![A waterfall of one year of contract value from a fixed set of accounts: starting value 1,000, minus 120 from accounts that left, minus 60 from accounts that cut back, leaving 820, plus 230 from accounts that grew, ending at 1,050. Gross retention reads 82 percent off the fourth bar; net retention reads 105 percent off the last. The numbers are illustrative.](figures/nrr-grr-waterfall.svg)

**Gross revenue retention, GRR,** counts only the losses: accounts that left and accounts that shrank. Expansion is excluded by construction, so the number cannot exceed 100 percent. It answers one question, and answers it cleanly: of the value you already had, how much survived the year.

**Net revenue retention, NRR,** counts the losses and then adds the expansion back. It can exceed 100 percent, and above 100 percent means growth inside the surviving accounts outran everything lost.

The reason to carry both is in the figure. One set of accounts produces 82 percent and 105 percent in the same year, and both are honest. Reported alone, the net figure describes a business that grew; the gross figure describes a base leaking almost a fifth of its value a year. A wide gap between them says the same thing every time: expansion is doing the work, and it is covering for a retention problem that has not been fixed. That reading is this framework's position, not a citation.

**A company that publishes both.** Instructure's annual report for 2022 gives three years of each, with its own definition of how each is computed. Net revenue retention of 117, 109 and 106 percent sits above gross revenue retention of 96, 95 and 94 percent, at the end of 2020, 2021 and 2022 [^instructure-2023]. Read the net series alone and the story is a business growing inside its existing accounts. Read the pair and you learn something the net number cannot tell you: the base lost 4 to 6 percent of its value every year, steadily, and expansion is what covered it. Both series are also falling, which is the second thing the pair shows and either number alone would understate.

There is a second trap sitting inside the net number, and it is about arithmetic rather than judgment. **There are two things called NRR, and only one of them is NRR.** The real one is cohort-based, as above: a fixed set of customers, valued then and now. The imposter, which Dave Kellogg calls lazy NRR, is starting ARR plus net expansion, all over starting ARR. That is a quarterly expansion measure wearing the other metric's name, and it does not answer the question the cohort version answers [^kellogg-2022].

<!-- TODO(heqing): interview — still open, narrowed. Your PayPal answer went into the logo-vs-dollar section above, because what it is really about is a headline entity count that can be bought and is not tied to revenue. The question here is the narrower one: a team reporting the net number alone while the gross number was quietly bad. If you have not seen that specific failure, say so and this prompt comes out. -->

## Logo churn and dollar churn

For one fixed cohort over one fixed window, retention and churn are the same measurement read from opposite ends, and they add to one. A 92 percent annual retention rate is an 8 percent annual churn rate, and neither is more true than the other.

Churn is where the definitional damage concentrates, because a churn rate has more construction choices sitting under it than a retention curve does. Dave Kellogg's enumeration is the useful list: whether you count logos or dollars, where a logo is one customer account regardless of what it pays; whether you measure at the product level or the account level; how much of a shrinking account is offset by expansion elsewhere; when in the period you take the measurement; whether the denominator is your whole revenue pool or only the contracts actually up for renewal that period; and whether a contract is valued at its original or its current price [^kellogg-2016]. The reason to care which one you picked is that the rate compounds: the difference between a 10 percent and a 20 percent churn rate becomes a 100 percent difference in cohort value after seven years [^kellogg-2016].

The one distinction worth carrying everywhere is logo against dollar, because it is the entity-versus-value split wearing different words.

| | Logo churn | Dollar churn |
|---|---|---|
| The unit | One customer account, whatever it pays | One dollar of contract value |
| Who feels it first | Support, onboarding, product | Finance, the board |
| What a bad number means | You are losing customers, usually small ones first | You are losing revenue, usually large accounts |
| The blind spot | Says nothing about size, so losing your largest account and your smallest read identically | Says nothing about count, so a base collapsing to a handful of whales looks stable |

**A logo count can be bought.** PayPal's headline growth number was net new active accounts. It reported 48.9 million added in 2021, ending the year at 426 million. A footnote records that 3.2 million of those arrived in a single month from acquiring Paidy, and that the prior year's figure included 10.2 million from acquiring Honey [^paypal-2022b]. None of that is hidden and none of it is improper. It is what a count of accounts measures: the logo question, whose answer can be purchased outright, and which says nothing about what any of those accounts is worth. The company reports an engagement figure next to it, payment transactions per active account, and that one moves for entirely different reasons [^paypal-2022a].

A company can lose a quarter of its customers and grow its revenue in the same year, and both statements are honest. That is not a paradox, it is what happens when the accounts that leave are small and the accounts that stay expand. Keep both numbers. Picking whichever one reads better is how a customer base quietly consolidating into three large accounts goes unnoticed for a year.

## Five filings, five constructions, one metric name

The metric has no standard definition. Five companies used the same name for five different calculations, and because they were filing with a regulator, all five had to write down what they meant. An S-1 is the registration statement a company files to go public, and a 10-K is its annual report. Every company below warns in its own filing that its number may not be comparable to anyone else's, and reading them side by side shows why.

| Filing | What the metric actually counts | Window | Disclosed |
|---|---|---|---|
| Snowflake S-1, 2020 [^snowflake-2020] | Product revenue from capacity customers who used the platform in the first month of year one; customers who stopped using it stay in the denominator at zero | Trailing two years | 180%, 169%, 223%, 158% |
| Slack S-1, 2019 [^slack-2019] | MRR, excluding new paid customers and free-to-paid conversions | Trailing twelve months | 171%, 152%, 143% |
| HubSpot S-1, 2014 [^hubspot-2014] | Subscription Dollar Retention Rate, computed monthly and then annualized | Monthly, annualized | 71.6%, 82.4%, 82.9%, 90.3% |
| WeWork S-1, 2019 [^wework-2019] | Desks, under the name net membership retention rate | One window | 119% |
| Innovid 10-K, FY2022 [^innovid-2023] | Core clients, with the definition widened to include publishers after an acquisition; prior years not restated | Annual | 111% on the new definition, against 127% and 121% on the prior methodology |

Four things fall out of that table, and two of them are visible at a glance.

![Two panels. Left, Slack's disclosed net dollar retention falling from 171 percent in January 2017 to 152 percent in 2018 to 143 percent in 2019. Right, HubSpot's disclosed Subscription Dollar Retention Rate rising from 71.6 percent in 2011 to 90.3 percent in the second quarter of 2014, every figure below the 100 percent line. Each panel is that company's own series on its own definition.](figures/disclosed-dollar-retention.svg)

**The celebrated number is usually the last one in a falling series.** Snowflake's 158 percent is the figure people quote, and it is the lowest of the four the company disclosed, down from 223 percent. The filing forecasts its own decline and says plainly that its metrics may differ from similarly titled metrics used by other companies [^snowflake-2020]. Slack's series falls the same way without the fanfare. Before you benchmark yourself against a famous number, check where in the series it sits.

**Dollar retention above 100 percent is not the normal condition of a healthy subscription business.** Every figure HubSpot disclosed is below 100 percent, from 71.6 percent in 2011 to 90.3 percent in the second quarter of 2014, and the word churn does not appear anywhere in the filing [^hubspot-2014].

**The name does not tell you the unit.** WeWork's net membership retention rate counts desks, not dollars, in a filing that says outright it is borrowing conventional subscription-software measurement for a real-estate business [^wework-2019]. One data point, one window, and the offering was withdrawn.

**A redefinition and a decline look identical from outside.** Innovid changed which clients counted, reported 111 percent against prior-year figures of 127 and 121 percent computed the old way, and did not restate the prior years [^innovid-2023]. The drop mixes a real change in the business with a change in the definition, and from outside the two cannot be separated. This is not misconduct. It is what happens whenever a definition moves and history does not move with it, which is a thing metric definitions do quietly and constantly [^stancil-2021]. PayPal states the general policy in its own filings: when it detects a significant volume of illegitimate account activity it removes that activity from its key metrics, and generally does not update previously reported metrics unless management judges the retrospective impact material [^paypal-2022a] [^paypal-2022b]. Written down that plainly it is a reasonable policy. It also means the series you are reading was computed under rules that changed inside it.

**Five questions to ask before you believe anyone's number**, including your own, drawn from the filings above and from Kellogg's enumeration [^kellogg-2016] [^kellogg-2022]:

1. Which set of customers, and over what window?
2. Are the customers who left still in the denominator at zero, or dropped out of it?
3. Are new customers and free-to-paid conversions inside or outside the calculation?
4. Is the unit dollars, or something else with a dollars-sounding name?
5. Has the definition changed since the year you are comparing against, and were the prior years restated?

And one more, which is the one to run first at a small company, because it costs nothing and catches most of the others: write the definition down in a single sentence, hand it to a friend, and see whether they get it quickly. If the sentence needs a second sentence to rescue it, the definition is not settled yet, and every number you compute from it will inherit the confusion.

**One disclosure decision worth borrowing.** In its first-quarter 2024 shareholder letter, Netflix announced it would stop reporting quarterly membership numbers and average revenue per membership. The stated reason is a measurement argument rather than a retention one: with several price tiers in the market, each additional membership now has a very different business impact, so a count of memberships no longer maps onto value [^netflix-2024]. When your units stop being interchangeable, counting them stops being informative.

## What a team of ten does

You do not need machinery for this and you should not buy any. You need a renewal ledger: one row per account, the contract value it had twelve months ago and the contract value it has today, taken from the same list of accounts, with the accounts that left still on the list at zero.

That single sheet gives you both numbers. Sum today's column over sum of the year-ago column is net retention. Do it again with every increase capped at its year-ago value, so no account can contribute more than it started with, and you have gross retention. The gap between the two is your expansion, and the accounts driving it are named on the rows.

Three rules keep the ledger honest, and all three are free:

- **Fix the account list once, at the start of the window.** An account that signed up during the year does not belong in either column. If it drifts in, both numbers become flattering and neither is a retention measurement any more.
- **Leave the departures on the sheet at zero.** Deleting the row is the single most common way this calculation gets quietly wrong.
- **Write down the date of the snapshot** and use the same day next year.

This framework's position is that you build the ledger before you buy anything that offers to compute this for you, because the ledger is the only thing you will ever have to check the tool against.

## Patterns & case studies

No pattern page yet. Two candidates from the filings above:

- **The redefinition that looked like a decline.** A metric definition widened mid-series, prior years left unrestated, and a drop that cannot be decomposed from outside [^innovid-2023] [^stancil-2021].
- **The renewal ledger.** The by-hand cohort calculation as a control artifact, and the checks that keep it from drifting [^kellogg-2022].

## Sources & Stories

Dave Kellogg supplies the real-versus-lazy NRR distinction [^kellogg-2022] and the enumeration of the six construction choices that make churn rates non-comparable [^kellogg-2016]. His 10-versus-20 percent figure is a claim about compounding, that the gap becomes a 100 percent difference in cohort value after seven years, and it is stated that way here rather than as a claim about how far a definition can move a rate.

Gross revenue retention is defined on this page from a filing rather than from the general literature, because the readily available treatments of it are vendor marketing pages, which this library does not cite. Instructure's 10-K is the source: it discloses gross and net side by side for three years and writes out its own formula for each, which is what makes the pair usable as a worked example [^instructure-2023]. SecureWorks' FY2024 10-K was checked as a second candidate and discloses net revenue retention only, so it is not cited.

The five-filing table is built entirely from primary SEC documents, each verified directly against the filing rather than through a secondary account [^snowflake-2020] [^slack-2019] [^hubspot-2014] [^wework-2019] [^innovid-2023]. The Netflix disclosure change is likewise from the shareholder letter itself [^netflix-2024], and it is a change in what the company reports rather than an admission that the metric was wrong. One caveat belongs on the record: HubSpot is the company most often named when negative churn is taught, and its own prospectus does not support that teaching. This page therefore states only what the filing says and draws no conclusion about any secondary source. The definition-drift mechanism is Benn Stancil's [^stancil-2021], noted here with his BI-vendor affiliation.

The PayPal passages are from the company's own 10-K and its fourth-quarter 2021 results, both read directly [^paypal-2022a] [^paypal-2022b]. The acquisition additions to net new active accounts are the company's own footnote, and are cited here as an illustration of what an account count measures rather than as any criticism of the disclosure, which is plain on the face of the document. Two verified negatives are worth recording, because the story circulates with numbers attached that these documents do not contain: neither filing states a 750 million active-account target, and neither gives a count of illegitimate accounts removed. Anything of that kind would have to come from the earnings call or an investor-day deck, and neither has been checked, so neither is claimed here.

The gross-versus-net gap as a diagnostic, the logo-versus-dollar blind-spot table, the renewal-ledger procedure and its three rules, the one-sentence definition test, and the small-team framing throughout are this framework's positions rather than sourced claims, and are marked as such where they appear. The author's contributions to this page are from the session of 2026-08-16. The first figure is illustrative and says so on its face. The second plots each company's own disclosed figures, read from the filings cited above; the two panels are drawn separately because the two series are not computed the same way. Interview questions on this page are unanswered by design, per this repository's working method.

<!-- Footnote targets; full entries with links and caveats live in REFERENCES.md -->

[^hubspot-2014]: [[HUBSPOT-2014]](../../REFERENCES.md)
[^innovid-2023]: [[INNOVID-2023]](../../REFERENCES.md)
[^instructure-2023]: [[INSTRUCTURE-2023]](../../REFERENCES.md)
[^kellogg-2016]: [[KELLOGG-2016]](../../REFERENCES.md)
[^kellogg-2022]: [[KELLOGG-2022]](../../REFERENCES.md)
[^netflix-2024]: [[NETFLIX-2024]](../../REFERENCES.md)
[^paypal-2022a]: [[PAYPAL-2022A]](../../REFERENCES.md)
[^paypal-2022b]: [[PAYPAL-2022B]](../../REFERENCES.md)
[^slack-2019]: [[SLACK-2019]](../../REFERENCES.md)
[^snowflake-2020]: [[SNOWFLAKE-2020]](../../REFERENCES.md)
[^stancil-2021]: [[STANCIL-2021]](../../REFERENCES.md)
[^wework-2019]: [[WEWORK-2019]](../../REFERENCES.md)
