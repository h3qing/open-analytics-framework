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

1. Read `AGENTS.md`, `CONTENT_BACKLOG.md`, and `DECISIONS.md`. Also read `AGENTS.local.md` if present — machine-local working notes, untracked; in a linked worktree it lives at the main checkout root.
2. Read `docs/prior-art.md` if the session touches a pattern.
3. Confirm the unit. Default to the next `ready` row in the backlog.
4. **Interview.** Ask questions one or two at a time. Push back on vague answers. Do not accept best-practices language, passive constructions that hide the actor, or claims without a mechanism. If I say "we improved data quality," ask what was measured, what the number was before, and who noticed.
5. Draft structure from my answers only.
6. I edit for voice. You do not re-edit my prose.
7. Update the backlog row status. Add a `DECISIONS.md` entry if a judgment call was made.
8. One commit, real timestamp, plain descriptive message.

Sessions are 60 to 90 minutes. If a unit will not finish in one, split it in the backlog rather than running long.

## Pattern template

`docs/pattern-template.md` defines the fixed shape every pattern doc uses: eight sections, the DMAIC mapping, and the Sources & Stories section. Stub every content file against it. Every module ships at least one control-plan template in `templates/`.

## Sources & traceability

The goal is to be helpful. The pattern itself is the primary artifact — the thing teams can take and apply to their own metrics and analytics.

We do real industry research (see `docs/prior-art.md`) so the patterns synthesize more than just one person's opinion. Sources are listed so readers can trace back to the original stories or research if they want to go deeper ("the Duolingo story", "practices described by Benn Stancil", etc.).

All citation keys must resolve in `REFERENCES.md`. CI still requires a "Sources & Stories" section in every pattern and that cited keys exist.

## Structural model

- Every unit has the same internal shape. One template, applied consistently.
- Reference and guide are separate: canonical pattern statements and long-form guides live in different places.
- Plain markdown for the framework itself. Nothing to install to read it.
- Something to adopt, not just read. Ship copyable artifacts alongside prose.
- Content over scaffolding. A reader landing on the README reaches a finished pattern in one click. Process files (backlog, decisions, this file) exist for the maintainer and stay out of the reader's path.
- Match the fidelity of the sources. Where the original story used a chart or a diagram, the page shows one. Dense unbroken prose is a defect — see the Presentation section of `docs/pattern-template.md`.
- **Write for the reader, not about the research.** Every page exists to help a company without analytics resources act, and to give their AI agents something precise to work from. It is not a literature review. Sourcing status, verification caveats, and accounts of what could not be found belong in Sources & Stories, never in the body. Where the framework makes a claim of its own, state it plainly and mark it as the framework's position in a clause.
- **Prose explains, tables list.** A table carries inventory; the argument goes in the prose above it. When a table column is asked to do the teaching, every row turns into a work item and the page reads as a project plan rather than as knowledge being shared. The tell is a row that only makes sense to someone who watched the work happen: a unit described as "which of the competing first moves goes first" is describing the maintainer's problem, not the reader's. Say what goes wrong for the reader without it.
- **Organize around decisions.** A reader with ninety minutes and no analyst reads what tells them what to do. Pages that answer "which one, at my size, and who owns it" get read; pages organized around the concept get skimmed. Where a page presents a genuine choice between approaches, route it by size and say what to do in each band rather than surveying the options. Where there is no choice to route, because the page teaches one technique, the equivalent is telling the reader what they can do this week and what they can safely ignore. Do not bolt a size table onto a page that has no menu.
- **Every recommendation needs a version for a team of ten.** The audience has no sales ops, no traffic for a clean holdout, and nobody spare to keep a neutral ledger. A recommendation that assumes staff the reader does not have is not advice, and the small-company version belongs beside it.
- **Do not repeat a number the framework has not verified.** Famous benchmarks in this field frequently fail tracing. Say plainly that no citable figure survived checking rather than passing folklore along with a caveat.

## When to stop and ask

Ask rather than guess if: the repo name is taken, a fixed-specification item seems wrong, a tooling choice adds a dependency I would have to maintain, you cannot verify a citation, a question you want to ask would require me to disclose something employer-specific, or anything is ambiguous enough that guessing wrong costs a rewrite.
