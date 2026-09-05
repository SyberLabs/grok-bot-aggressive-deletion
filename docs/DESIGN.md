# Design decisions

## One job

This release addresses unnecessary code and architectural complexity. Ideation, broad first-principles consulting, general red teaming, and product design remain research concepts, not active roles inside the Bot.

The user requested inspiration from three existing skills:

- **elon-principles:** start from the required outcome; question, delete, simplify, accelerate, automate in that order.
- **pony-tail-review:** identify over-engineering concisely, prefer canonical/native mechanisms, provide exact locations and replacements, and accept a clean verdict.
- **thermo-nuclear-code-quality-review:** seek structural simplifications that eliminate concepts and special cases, preserve clean boundaries, and inspect large changes rigorously.

This is an original synthesis, not a verbatim redistribution of those local skill files or another creator's marketplace template.

## Conflicts resolved

Deletion percentages and net lines are diagnostics, never targets. Preserving behavior and reducing conceptual burden determine success. One implementation does not prove an abstraction is unnecessary. A 1,000-line file is a cohesion warning, not an automatic requirement for more modules. Typed boundaries can simplify a tangled model, but an extra layer is justified only if total complexity falls. A shorter validator is not a replacement unless the actual validation contract survives.

Review means findings; an explicit apply/fix request authorizes routine reversible local work. No extra approval loop is introduced for already-authorized edits. Unrelated production changes, remote deletion, sends, and publication are outside an ordinary code-review request.

## Quality bar

Correct required behavior, high-precision findings, fewer concepts, useful evidence, and verified artifacts. A finding needs a removal mechanism and a preservation argument. Missing evidence is a candidate to investigate, not an asserted defect. The Bot may conclude the code is already lean.

The skill intentionally needs no bespoke runtime, model router, paid API, orchestrator, database, or scheduled audit. Add machinery only when a real repeated failure demonstrates its value.
