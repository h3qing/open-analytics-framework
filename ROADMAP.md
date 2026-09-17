# Roadmap

Each tag below is a real git tag and a GitHub release with notes, aligned to [CHANGELOG.md](CHANGELOG.md).

| Tag | Contents | Status |
|---|---|---|
| — | Repo public, skeleton, four charters | done |
| — | Prior-art review | done for the first pattern; rows for the patterns drafted since are pending |
| — | One pasted line gets a reader in: `llms.txt`, the line on the README, CI that keeps the file current | done, 2026-09-16 |
| — | Diagnostic skill v0.1 published | not started; the first guided skill, attribution design, is drafted |
| v0.1.0 | Module 1's core patterns: the 1B integrity patterns, on the 1A topic pages already drafted | drafted and on main: single point of computation, statistical process control, plausible-but-wrong, golden question sets, schema drift; the tag follows the author's voice pass |
| v0.2.0 | Module 1 complete, both halves, and the first reference architecture | in progress: agreement measurement and the segmentation topic page are in review; four 1B patterns, the reference architecture, and the remaining 1A pages are open |
| v0.3.0 | Second module core patterns, first implementation guide, skill v1.0 | not started; the module 3 context-file pattern and its template are already on main |
| v1.0.0 | All four modules at first complete draft | not started |

## Each module's own roadmap

The table above is the release view. The build order inside each module lives in its charter, one track at a time, with what goes wrong if the track is skipped. Row-level status is in [CONTENT_BACKLOG.md](CONTENT_BACKLOG.md).

- Module 1, data quality: [1A definition quality](docs/modules/01-ai-data-quality/README.md#1a--definition-quality), the metrics library and the guided skills, and [1B data integrity](docs/modules/01-ai-data-quality/README.md#1b--data-integrity), the patterns in version order.
- Module 2, infrastructure: [2A what you build](docs/modules/02-infrastructure-design/README.md#2a--what-you-build), tracks 0 to 4 ordered by what expires first, and [2B how you run it](docs/modules/02-infrastructure-design/README.md#2b--how-you-run-it), tracks 5 to 7.
- Module 3, agent integration: [3A what it can reach](docs/modules/03-ai-agent-integration/README.md#3a--what-it-can-reach), tracks 0 to 4, and [3B what it tells you](docs/modules/03-ai-agent-integration/README.md#3b--what-it-tells-you), tracks 5 to 7.
- Module 4, governance and financial reporting: [4A what you must be able to show](docs/modules/04-governance-and-financial-reporting/README.md#4a--what-you-must-be-able-to-show), tracks 0 to 4, and [4B the money numbers](docs/modules/04-governance-and-financial-reporting/README.md#4b--the-money-numbers-themselves), tracks 5 to 7.
- The knowledge layer: the [metrics library topics](docs/metrics/README.md#topics), with the pages planned next at the end of that list.
- The artifacts: [templates](templates/README.md) and [guided skills](skill/README.md), one row per module.

## Beyond v1.0

Stated as intentions, no dates: conference presentations, appearances on data analytics podcasts and video channels, and an annual *State of Analytics in U.S. AI* report synthesizing lessons from adopting companies.

## Validation is rolling, not final

Practitioner review starts as soon as Module 1 has something worth reading: specific asks on specific patterns, routed through public issues and PRs so the discussion is durable and attributable.
