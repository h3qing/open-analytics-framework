# The Open Analytics Framework

Structured foundations for building analytics operations, for organizations that lack dedicated analytics resources. Free and open: documentation under CC BY 4.0, code and templates under MIT.

## Start here

- **Read the first pattern:** [State-based retention measurement](docs/modules/01-ai-data-quality/state-based-retention-measurement.md) — decompose DAU into user states and find the one retention rate worth a team's focus, drawn from the Duolingo growth story.
- **Learn a metric:** the [metrics library](docs/metrics/README.md), the knowledge layer of Module 1A. Classical metric knowledge, one page per topic. The two finished pages are [attribution](docs/metrics/attribution.md) and [conversion rate](docs/metrics/conversion-rate.md); start with either.
- **No analyst, ninety minutes:** read [attribution](docs/metrics/attribution.md), then [conversion rate](docs/metrics/conversion-rate.md). Between them they cover who gets credit for an outcome and how to find the step that is losing you the most people.
- **Copy something usable:** [templates](templates/README.md) — control plans, machine-readable specs, and agent prompts to drop into your own stack.
- **Browse the framework:** [reading guide](docs/index.md), then the four modules — [data quality](docs/modules/01-ai-data-quality/README.md) · [infrastructure](docs/modules/02-infrastructure-design/README.md) · [agent integration](docs/modules/03-ai-agent-integration/README.md) · [governance & financial reporting](docs/modules/04-governance-and-financial-reporting/README.md).

## The problem

Two versions of the same gap. Early-stage and AI-native companies rebuild the same foundational analytics systems from scratch, losing six to twelve months on work that could be standardized. Small and mid-sized businesses never build those foundations at all, and operate without reliable access to their own data. Neither group has a playbook.

## The thesis

These systems fail at deployment, not at the model layer. Model capability is generalized and largely solved; what it lacks is opinion and industry experience — consistent metric definitions, schemas that hold, outputs that can be trusted without re-checking, and the organizational adoption that follows. That is a process and systems problem, which is why this framework applies industrial-engineering methodology (Six Sigma, DMAIC) to analytics.

## How it is organized

Four modules, fixed. Three layers cut across them: knowledge, patterns, artifacts.

```text
Modules   1. AI data quality   2. Infrastructure   3. Agent integration   4. Governance & finance
              1A definition       2A what you build   3A what it can reach   4A what you can show
              1B integrity        2B how you run it   3B what it tells you   4B the money numbers
              |
Knowledge  docs/metrics/        one page per classical metric — what it is, why it matters, how to see it
Patterns   docs/modules/        sourced ways of working, eight fixed sections, DMAIC-shaped
Artifacts  templates/ skill/    control plans, specs and prompts to copy; guided interviews to run
           reference-architectures/  implementation-guides/
```

- **Modules** are the framework's spine and match the four committed in the project specification. They do not change.
- **Knowledge** is the [metrics library](docs/metrics/README.md). It is a layer, not a fifth module: its home is Module 1A, and the revenue, cost and margin pages will also serve Module 4.
- **Patterns** hang off a metric. Retention is the metric; [state-based retention measurement](docs/modules/01-ai-data-quality/state-based-retention-measurement.md) is one sourced way of working on it.
- **Artifacts** are what you take with you. Every module ships at least one copyable control plan.

## The four modules

1. **AI data quality measurement and improvement** — the quality of the whole measurement system, in two halves. **1A, definition quality:** are you measuring the right thing, defined once and defined well. **1B, data integrity:** does the pipeline return that number correctly and stay in control. A precisely computed wrong metric and a correctly defined bad join are both quality defects, and they have different fixes.
2. **Analytics infrastructure design for rapid growth** — infrastructure that holds up as the organization scales.
3. **AI agent integration into analytics workflows** — deployment, validation, governance, and adoption of AI analytics agents. Integration, not agent-building.
4. **Data governance and financial reporting specific to AI companies** — both halves; the financial-reporting patterns are the least likely to exist anywhere else in public.

The primary worked case is early-stage and AI-native companies; the patterns generalize to any organization without an analytics team.

## What ships

Four deliverable types, each with a visible home here: the framework itself (`docs/modules/`), best-practices documentation, reference architectures (`reference-architectures/`), and implementation guides (`implementation-guides/`). Every module ships at least one copyable control-plan template in `templates/`. A diagnostic skill (`skill/`) assesses an organization's readiness before it deploys an AI analytics agent.

## Sources

Every pattern lists the stories and research it draws from — the Duolingo growth model, practitioner writing, prior-art research recorded in [docs/prior-art.md](docs/prior-art.md) — so you can go back to the originals if you want to go deeper. All citations resolve to [REFERENCES.md](REFERENCES.md).

## Status

Pre-release. Prior-art review in progress; module content follows. See [ROADMAP.md](ROADMAP.md).

## Contributing

Pattern proposals and case studies are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Substantive review of a single pattern is the most valuable contribution this project can receive.

## License

Documentation: [CC BY 4.0](LICENSE). Code and templates: [MIT](LICENSE).

## Author

<!-- TODO(heqing): author bio -->
