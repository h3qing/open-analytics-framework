# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Module 1A now groups metrics into six categories — acquisition, conversion, engagement, retention, money, and cross-cutting — and lists the topics, patterns and skills under each.
- [Redefining a metric in the open](docs/modules/01-ai-data-quality/redefining-a-metric-in-the-open.md) (M1-12): how to change a metric definition, or repair one that broke, without losing trust in the number.
- [Check attribution by turning it off](docs/modules/01-ai-data-quality/checking-attribution-by-turning-it-off.md) (M1-13): auditing an attribution belief by removing the spend in a bounded slice, from a geographic holdout down to a slow-season pause.
- Module 1 says why it exists.

### Changed

- Module 1 now names its two halves — 1A definition quality (what to measure) and 1B data integrity (whether the number is right) — mapped to DMAIC's Define versus Measure-through-Control. The metrics library is 1A's knowledge layer rather than an unhomed layer, the four-module set is re-fixed, and every backlog row carries a module.
- Module 2 now names its two halves — 2A what you build (what should exist at your size, and in what order) and 2B how you run it (whether it stays true as the company grows) — mapped to DMAIC's Improve versus Control. Its build order is ordered by what expires rather than by importance, and `topic` is retired as a routable type outside the metrics library.

### Added

- Repository skeleton: module charters, pattern template, prior-art and references scaffolding, deliverable-type homes, community files, CI.
- First pattern draft: state-based retention measurement (M1-11, Adapted from Duolingo's published growth model), with Module 1's first control-plan template, first prior-art row, and first verified REFERENCES entries.
