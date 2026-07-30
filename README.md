# The Open Analytics Framework

Structured foundations for building analytics operations, for organizations that lack dedicated analytics resources. Free and open: documentation under CC BY 4.0, code and templates under MIT.

## The problem

Two versions of the same gap. Early-stage and AI-native companies rebuild the same foundational analytics systems from scratch, losing six to twelve months on work that could be standardized. Small and mid-sized businesses never build those foundations at all, and operate without reliable access to their own data. Neither group has a playbook.

## The thesis

These systems fail at deployment, not at the model layer. Model capability is generalized and largely solved; what it lacks is opinion and industry experience — consistent metric definitions, schemas that hold, outputs that can be trusted without re-checking, and the organizational adoption that follows. That is a process and systems problem, which is why this framework applies industrial-engineering methodology (Six Sigma, DMAIC) to analytics.

## The four modules

1. **AI data quality measurement and improvement** — measuring and improving the quality of data feeding AI-assisted analytics.
2. **Analytics infrastructure design for rapid growth** — infrastructure that holds up as the organization scales.
3. **AI agent integration into analytics workflows** — deployment, validation, governance, and adoption of AI analytics agents. Integration, not agent-building.
4. **Data governance and financial reporting specific to AI companies** — both halves; the financial-reporting patterns are the least likely to exist anywhere else in public.

The primary worked case is early-stage and AI-native companies; the patterns generalize to any organization without an analytics team.

## What ships

Four deliverable types, each with a visible home here: the framework itself (`docs/modules/`), best-practices documentation, reference architectures (`reference-architectures/`), and implementation guides (`implementation-guides/`). Every module ships at least one copyable control-plan template in `templates/`. A diagnostic skill (`skill/`) assesses an organization's readiness before it deploys an AI analytics agent.

## Provenance

Every pattern carries exactly one tag, assigned only after a recorded prior-art search ([docs/prior-art.md](docs/prior-art.md)):

- **Established** — well-documented existing concept, cited.
- **Adapted** — existing concept applied to a domain it was not written for; origin cited, changes stated.
- **Original** — no prior art found, with the empty search recorded so the claim is checkable.

All citations resolve to [REFERENCES.md](REFERENCES.md). No unsourced assertions.

## Status

Pre-release. Prior-art review in progress; module content follows. See [ROADMAP.md](ROADMAP.md).

## Contributing

Pattern proposals and case studies are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Substantive review of a single pattern is the most valuable contribution this project can receive.

## License

Documentation: [CC BY 4.0](LICENSE). Code and templates: [MIT](LICENSE).

## Author

<!-- TODO(heqing): author bio -->
