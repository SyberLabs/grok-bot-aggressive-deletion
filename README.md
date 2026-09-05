# Aggressive Deletion Bot

A focused Grok Bot template from SyberLabs for removing unnecessary code, dependencies, branches, and architectural layers while preserving required behavior.

It asks what the system actually needs to do, identifies what can disappear, and produces a concise review or a local patch when edits are requested. It reports the checks actually run and marks missing validation. It does not optimize for a deletion quota.

## Use

The canonical operating instructions are in [skills/aggressive-deletion/SKILL.md](skills/aggressive-deletion/SKILL.md). The [Bot profile](bot/PROFILE.md) contains the name, description, and setup message for Grok Bot. The profile and skill are portable instructions; this repository is not a hosted service or an automatic marketplace installer.

Try:

> Review this branch for unnecessary complexity. Find the largest simplification that preserves its behavior. Return only high-confidence findings with exact locations and replacements. Do not edit.

Or:

> Simplify this module. Apply reversible local changes, preserve its public contract, run the relevant tests, and show what disappeared. Do not push or publish.

## What it targets

- Dead paths whose consumers have actually been checked.
- Wrappers, factories, modes, and configuration without a demonstrated purpose.
- Handwritten code already covered by the standard library or platform.
- Repeated branching that can disappear through a simpler state or data model.
- Dependencies or cross-layer plumbing that cost more than the behavior they provide.

It preserves required compatibility, recovery, accessibility, security controls, and tests. A single implementation, a low line count, or a large file alone does not determine good design.

## Evidence and release status

See [evaluation](eval/README.md) for fixtures, independent behavioral review, and limitations. Local checks do not prove identical behavior in Grok Bot; the platform controls its own runtime and model selection. See [publication status](docs/PUBLISHING.md) for the verified sharing/catalog state.

GitHub source is public. The Bot share has not been created, marketplace submission has not occurred, and no live listing is verified. Desktop input currently blocks Bot setup; the publication record gives the observed error.

Run `python eval/verify.py` to check the original and simplified example against the same contract tests, then confirm the tests reject four deliberately broken rewrites. This tests the examples and the regression suite, not the reasoning quality of an arbitrary model.

Run `python eval/check_structure.py` for the structural counterexample and corrected replacement. The [bounded review](eval/RED-TEAM.md) records the six written-response judgments and actual limitations.

## Background

The method combines first-principles requirement challenges, concise over-engineering review, and ambitious structural simplification. [Design notes](docs/DESIGN.md) explain how conflicting heuristics were resolved. Broader Grok Bot marketplace research is retained under [research](research/), as background rather than additional active products.
