# Skill template

Every skill in this framework uses this shape. Skills are the third layer: topic pages hold the knowledge, patterns hold the ways of working, and a skill walks one person through applying them to their own business. A skill is a guided conversation, run by an AI agent or read as a checklist by a human, and it ends with an artifact the user keeps.

The interaction model is the same interview method this framework is written with: questions one or two at a time, guidance after each answer, pushback on vague answers.

## The five stages

1. **Frame.** What the user is trying to decide, plus three or four scoping questions: rough size, team shape, current state. Bands are enough; exact numbers are never required.
2. **Route.** Pick the path from the scoping answers. Most skills route by size first, because the right advice changes with scale before it changes with anything else.
3. **Interview.** The core questions, one or two at a time. Wait for each answer. Do not accept best-practices language or a claim without a mechanism; ask what was measured and who noticed. Adapt the path to the answers.
4. **Recommend.** Every recommendation traces to a topic page or pattern in this framework, or is labeled plainly as judgment. No invented numbers, no benchmarks the library has not verified.
5. **Output.** A filled decision record the user keeps: the choices made, who owns them, and when to revisit. Placeholders in the template are obviously placeholders until the conversation fills them.

## Rules for every skill

- **One or two questions at a time.** A skill that dumps its whole questionnaire is a form, not a conversation.
- **Privacy gate.** Never require confidential specifics: no internal metric values, customer names, or system details. Class-level answers are always enough, and the skill says so up front. Warn before any step that would search the web or leave the conversation.
- **Plain language.** Every term of art gets a one-clause gloss the first time it appears.
- **Cite the topic page, not the raw sources.** The topic page carries the footnotes and the caveats; the skill links to it and inherits its sourcing.
- **The output is the point.** If the conversation ends without a filled artifact, the skill did not finish.

## File shape

Each skill lives in its own directory under `skill/` as a `SKILL.md`: frontmatter (`name`, `description`, `topic` link, `status`), then the five stages with the actual questions written out, then the output template as a copyable block. `references/` and `assets/` subdirectories are optional, per the layout planned for the diagnostic skill.
