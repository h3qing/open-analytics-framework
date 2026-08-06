---
id: active-users
title: Active users
type: topic
status: stub # structure and interview questions only, per AGENTS.md constraint 6; research rounds launched 2026-08-05
summary: >
  What an active user is, why the definition of "active" is the whole
  game, the windows and ratios (DAU, WAU, MAU, stickiness), when the
  aggregate is a north star and when it is a vanity number, and how to
  decompose it into states you can actually move.
keywords:
  - active users
  - DAU
  - WAU
  - MAU
  - stickiness
  - north star
  - engagement
  - user states
---

# Active users

[TODO(heqing): one-paragraph opening in your voice — what question active users answers about a business, for a reader who has never had an analyst.]

## What an active user is

Scope: three choices make the number. The entity (user, account, workspace, seat), the action that counts as "active," and the window (a day, a week, a month). The formal reference example already in this library: Facebook's S-1 definition, a registered user who logged in and visited within the window, with its edge cases documented, duplicate accounts and devices that contact servers without user action [[FACEBOOK-2012]](../../REFERENCES.md). The single-definition discipline story, one company-level definition held to inside and out, lives on the [conversion page](conversion.md) [[SCHULTZ-2014]](../../REFERENCES.md).

- [TODO(heqing): interview — the default choices you would recommend: what entity and what action for a B2C product vs. a B2B product, where seats, accounts, and workspaces compete for the definition?]
- [TODO(heqing): interview — logged-in vs. a value action: when is "opened the app" an honest definition of active, and when is it flattering noise?]

## The windows and the ratios

Scope: DAU, WAU, MAU as the same definition at three windows; the stickiness ratio (DAU/MAU) and what it does and does not say; matching the window to the product's natural cadence rather than to convention, the same argument the [retention page](retention.md) makes for retention windows.

- [TODO(heqing): interview — how should a team pick its primary window? What products have you seen goal on DAU when their honest cadence was weekly?]
- [TODO: research round in progress — verified sources on stickiness, engagement ratios, and cadence-matching.]

## Worth measuring, or vanity

Scope: when the active-user aggregate deserves north-star status and when it is a vanity number that only ever goes up. The registered-users-vs-active-users contrast is the founding story of the distinction [[SCHULTZ-2014]](../../REFERENCES.md).

- [TODO(heqing): interview — a class-level vanity-metric trap you have seen: the number that looked like health and was not.]
- [TODO: research round in progress — who has written the honest vanity-metrics critique, with real provenance.]

## Decomposing the aggregate

Scope: the aggregate is a sum of flows, not a lever. DAU decomposes into new, current, reactivated, and resurrected users; WAU and MAU add the at-risk pools [[GUSTAFSON-2023]](../../REFERENCES.md) [[MAZAL-2023]](../../REFERENCES.md). The full treatment, states, transition rates, and the sensitivity analysis that finds the one rate worth a team's focus, is the [state-based retention measurement pattern](../modules/01-ai-data-quality/state-based-retention-measurement.md), with the state diagram drawn there.

## Classical ways to see it

Scope: the standard visualizations, each with a figure per the presentation guidance: the topline trend and its weekly seasonality, the stacked view of DAU by state (which makes "up and to the right" honest or dishonest at a glance), and the stickiness trend.

- [TODO: figures — topline with placeholder seasonality, stacked-by-state area, stickiness line, all with obviously-placeholder numbers.]
- [TODO: research round in progress — canonical treatments of each chart, if any exist.]

## Patterns & case studies

- [State-based retention measurement](../modules/01-ai-data-quality/state-based-retention-measurement.md) — the Duolingo growth model: decompose DAU into states, goal one transition rate [[GUSTAFSON-2023]](../../REFERENCES.md) [[MAZAL-2023]](../../REFERENCES.md).
- [TODO: research round in progress — public-company definition stories: metric redefinitions, what changed and why, from primary filings and first-party accounts.]

## Sources & Stories

Already in the bibliography from earlier topics: the Facebook S-1 definition and its caveats [[FACEBOOK-2012]](../../REFERENCES.md), the single-definition discipline story [[SCHULTZ-2014]](../../REFERENCES.md), and the Duolingo decomposition [[GUSTAFSON-2023]](../../REFERENCES.md) [[MAZAL-2023]](../../REFERENCES.md).

[TODO: research rounds in progress — definitions, ratios, and vanity critiques in one thread; public-company redefinition stories from primary filings in the other. Every source fetched and verified before it is cited here.]
