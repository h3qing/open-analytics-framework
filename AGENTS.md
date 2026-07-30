# Working method

Read at the start of every session. If anything elsewhere conflicts with the hard constraints, follow the hard constraints and say so.

## Hard constraints

1. **Never backdate a commit.** No `--date`, no `GIT_AUTHOR_DATE` or `GIT_COMMITTER_DATE`, no rebase or amend that alters an author timestamp. The history is a factual record of when work happened.
2. **Never squash, force-push, or rewrite history on `main`.** If asked later, refuse and remind me.
3. **Zero confidential material.** Do not invent example metrics, internal system names, customer names, architecture details, or numbers, even as realistic-looking placeholders. Placeholders must be obviously placeholders: `[TODO: metric name]`, never `data_quality_score_v3`.
4. **Do not fabricate traction.** No fake contributors, no seeded issues written as if from other people, no invented adoption figures, no testimonials, no sample user feedback.
5. **Vendor neutral throughout.** Do not name specific commercial products the author's employer has used, evaluated, or purchased. Do not write anything that reads as endorsement or criticism of a named vendor. Patterns describe categories of tool and classes of failure, never "product X does this badly." Where a pattern needs a concrete example, describe it generically.
6. **No generated prose in content files.** For every content file, produce structure, section headings, and specific questions I answer. Polished generated paragraphs will be deleted. Structure yes, voice no.
7. **No content without answers.** Do not write the body of a pattern I have not answered questions for. If I ask you to "just fill it in," refuse and run the interview instead. An empty stub is more useful than a plausible one.
8. **Abstraction test.** The framework says "here is how this class of problem behaves," never "here is how my employer does it." Apply this to every answer I give before drafting. If an answer is too specific to abstract safely, tell me and ask for a generalized version.

## Session protocol

Every working session, in order:

1. Read `AGENTS.md`, `CONTENT_BACKLOG.md`, and `DECISIONS.md`.
2. Read `docs/prior-art.md` if the session touches a pattern.
3. Confirm the unit. Default to the next `ready` row in the backlog.
4. **Interview.** Ask questions one or two at a time. Push back on vague answers. Do not accept best-practices language, passive constructions that hide the actor, or claims without a mechanism. If I say "we improved data quality," ask what was measured, what the number was before, and who noticed.
5. Draft structure from my answers only.
6. I edit for voice. You do not re-edit my prose.
7. Update the backlog row status. Add a `DECISIONS.md` entry if a judgment call was made.
8. One commit, real timestamp, plain descriptive message.

Sessions are 60 to 90 minutes. If a unit will not finish in one, split it in the backlog rather than running long.

## Pattern template

`docs/pattern-template.md` defines the fixed shape every pattern doc uses: eight sections, the DMAIC mapping, and the provenance tags. Stub every content file against it. Every module ships at least one control-plan template in `templates/`.

## Provenance discipline

Load-bearing. Every normative claim either cites prior art or is explicitly marked original. No unsourced assertions.

`REFERENCES.md` is a bibliography with stable citation keys, full reference, link where one exists. Do not invent entries or guess at citations. If unsure a source exists, write `[TODO: verify]` rather than a plausible-looking reference.

Every pattern carries exactly one provenance tag — `Established`, `Adapted`, or `Original` — assigned only after the prior-art search for that pattern is recorded in `docs/prior-art.md`. An `Original` tag with no corresponding prior-art row is a defect. CI fails if a pattern doc lacks a provenance tag or cites a key absent from `REFERENCES.md`.

## Structural model

- Every unit has the same internal shape. One template, applied consistently.
- Reference and guide are separate: canonical pattern statements and long-form guides live in different places.
- Plain markdown for the framework itself. Nothing to install to read it.
- Something to adopt, not just read. Ship copyable artifacts alongside prose.

## When to stop and ask

Ask rather than guess if: the repo name is taken, a fixed-specification item seems wrong, a tooling choice adds a dependency I would have to maintain, you cannot verify a citation, a question you want to ask would require me to disclose something employer-specific, or anything is ambiguous enough that guessing wrong costs a rewrite.
