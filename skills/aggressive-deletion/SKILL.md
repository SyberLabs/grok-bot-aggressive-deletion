---
name: aggressive-deletion
description: Find and remove unnecessary code, dependencies, configuration, and architectural layers while preserving required behavior. Use for deletion-focused code review or requested structural simplification; keep general bug fixing, product ideation, and unrelated redesign outside the task.
---

# Aggressive Deletion

Reduce the concepts and moving parts needed to deliver the required behavior. Be ambitious about what can disappear and precise about why it is safe. Code moved into another file is not necessarily less complex. Fewer lines are evidence of size, not proof of quality.

## Establish the boundary

Use the user's named diff, files, or workflow as the starting scope. Read applicable repository instructions and inspect the working tree before editing. Preserve unrelated work. For a review request, report findings without edits. For an implementation request, make authorized reversible local changes without asking again for routine steps; pushing, publishing, deleting remote data, and changing access remain separate actions unless authorized.

Identify the observable behavior, consumers, and acceptance checks. Determine why each disputed requirement exists and who or what relies on it; unknown ownership is an unknown, not permission to remove it. Separate actual constraints from untested assumptions. Derive the simplification from those constraints, not resemblance to another design or a famous person's preference.

## Hunt for the largest earned deletion

Question requirements, remove what is unnecessary, simplify what remains, then consider speed and automation. Search for a change in representation or responsibility that eliminates entire modes, branches, interfaces, or handoffs.

Inspect these candidates when present:

- Wrappers and factories that only forward calls; configurable mechanisms with no supported variation.
- Redundant state, identity conversions, impossible states, repeated condition chains, and silent fallbacks hiding an unclear contract.
- Custom implementations already served by a canonical project helper, standard library, or platform feature.
- Dependencies used for a small amount of behavior already available in the runtime.
- Feature-specific logic leaking into shared infrastructure; duplicated orchestration or partial updates a simpler flow can eliminate.

A single caller or implementation is a lead, not a verdict: the boundary may protect a public API, ownership, testing, or volatility. Large files are a cue to inspect cohesion, not a command to split them or invent abstractions. Prefer removal over moving the same complexity. Introduce a small helper or explicit state model only when it reduces the total concepts a maintainer must track.

## Prove the cut

Before recommending removal as safe, inspect relevant imports and callers, tests, configuration, scripts, exports, and package entry points. Search beyond static symbol references when the system uses registries, reflection, plugin loading, serialized names, templates, scheduled jobs, or external clients. No search hit is not proof of no consumer. State the boundary of the evidence you inspected.

For a replacement, compare the behavior that matters: input domain, output types, errors, ordering, encoding, timezones, side effects, compatibility, cancellation, retries, concurrency, and atomicity as relevant. Do not replace a real validation contract with a weaker check merely because it is shorter. Do not discard recovery or monitoring because the happy path passes.

Make high-confidence findings only when the removed responsibility is unnecessary or its replacement demonstrably preserves the contract. Label incomplete evidence as a candidate and name the decisive missing check. Do not invent usage, benchmarks, callers, test results, or expected line savings.

## Apply only within the requested scope

When edits are requested, establish a recoverable baseline, make the smallest complete simplification, and update callers and dependency metadata together. Do not mix unrelated refactoring. Use meaningful existing tests; add a small behavior test when the changed contract lacks coverage. Keep useful smoke tests and edge-case checks. If the baseline already fails, record that before claiming the change caused or fixed it.

Run the relevant checks and inspect the final diff for lost behavior, unrelated edits, and complexity merely displaced elsewhere. If validation is unavailable, label the patch unverified and identify the missing check. Do not claim completion from a command being issued. Restore only your own failing changes when necessary, preserving user edits and providing an honest result.

## Return a compact, actionable result

Rank structural simplifications before local nits. Use one line per finding:

`path:line — tag: what disappears; what replaces it; evidence or required check.`

Tags: `delete`, `stdlib`, `native`, `yagni`, `shrink`, `reframe`.

Separate verified findings from uncertain candidates. In a review, report net removable lines only when measured or defensibly counted; otherwise say unmeasured. In an applied change, report actual changed scope, added/removed lines, removed concepts or dependencies, validation outcome, and rollback path. Never maximize line reduction at the expense of readability or required behavior.

If there is no justified cut, say so and stop. If a new pass adds no material candidate or evidence, stop. Surface a discovered critical unrelated bug briefly for a separate task rather than expanding this review. Do not generate ideation, generic red-team essays, product redesigns, or recurring audits unless requested.
