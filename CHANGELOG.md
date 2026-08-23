# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Module 1 now names its two halves — 1A definition quality (what to measure) and 1B data integrity (whether the number is right) — mapped to DMAIC's Define versus Measure-through-Control. The metrics library is 1A's knowledge layer rather than an unhomed layer, the four-module set is re-fixed, and every backlog row carries a module.
- Module 2 now names its two halves — 2A what you build (what should exist at your size, and in what order) and 2B how you run it (whether it stays true as the company grows) — mapped to DMAIC's Improve versus Control. Its build order is ordered by what expires rather than by importance, and `topic` is retired as a routable type outside the metrics library.
- Module 3 now names its two halves — 3A what the agent can reach and 3B what it tells you — read 3A first because it is the half that fails irreversibly. The module is ordered by whether the consequence can be reversed rather than the decision.
- Module 4 now names its two halves — 4A what you must be able to show and 4B the money numbers themselves — and the Module 3 / Module 4 line is settled: Module 3 owns the run, and Module 4 owns the record. Evaluation is settled across three modules: Module 1 builds the golden set, Module 3 runs it as a monitor, Module 4 uses it as a gate on a definition change.

### Added

- Repository skeleton: module charters, pattern template, prior-art and references scaffolding, deliverable-type homes, community files, CI.
- First pattern draft: state-based retention measurement (M1-11, Adapted from Duolingo's published growth model), with Module 1's first control-plan template, first prior-art row, and first verified REFERENCES entries.
