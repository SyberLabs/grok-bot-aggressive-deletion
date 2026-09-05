# Reciprocal Bot review

Completed September 4, 2026, America/Los_Angeles. This was one bounded review in each direction using the two original native Grok Bots, followed by targeted instruction changes and native checks. It was not an independent model benchmark or a new evaluation platform.

## What reviewed what

The deletion Bot received the complete then-current First Principles skill as a behavior specification, with review-only scope and no external tools. First Principles received the complete then-current deletion skill, with the same limits and permission for a slightly longer review. Neither was given the intended findings or asked to modify the other automatically. Both reported that no tests were run.

The deletion Bot proposed removing two examples whose rules already appeared in the method, and making the opening conditional on a missing goal. It also proposed removing starter prompts but acknowledged that their host/UI role was unverified. We removed only the two repeated examples and conditioned the opening; the starter prompts and substantive safeguards remain.

First Principles called the repository/snippet wording an instruction conflict and proposed explicit context handling and a recoverable baseline. The existing text already qualified inspection as occurring before editing, so this was treated as a clarity improvement, not a demonstrated behavior failure. Garbage Collector now explicitly scopes repository inspection to repository work and names restorable pre-change state, including existing user edits. The review's suggestion that paths/hashes alone could provide recovery was rejected: hashes identify content but cannot restore it. No extra modes or duplicate checklist were added.

The deletion Bot's name was changed to Garbage Collector; its canonical skill ID remains aggressive-deletion. Its remit remains deletion and structural simplification. First Principles remains a separate Bot, not an additional skill or runtime dependency of this product.

## Native behavior after refinement

Garbage Collector received four independent review-only cases with no tools or edits authorized:

1. Complete private ordinary-integer increment helper with a temporary variable: returned the direct `return x + 1` simplification without demanding repository access.
2. Separately mutable shallow snapshot of a caller-owned list: refused replacing `list(items)` with an alias, explaining the mutation consequence.
3. Public `LegacyInvoice` class with no references in a pasted excerpt, external and serialized consumers unchecked: marked removal as a candidate only and named the missing consumer checks.
4. Pre-existing user edits with only a SHA-256 proposed as rollback baseline: rejected hash-only recovery and required restorable content preserving those edits.

All four passed their bounded acceptance criteria. The Bot explicitly said no validation had been executed. Case 4 checks its stated plan; this run did not execute a dirty-repository edit or rollback.

First Principles received three independent static cases, with a goal already supplied in each:

1. Six days waiting plus four days work, work rate increased by 50%: correctly calculated `6 + 4/1.5`, approximately 8.67 days, and identified waiting as the larger component. Its two-day waiting reduction was a proposed target, not an observed outcome.
2. Six agents proposed solely because a competitor uses six: challenged imitation and proposed measuring one agent on the actual task before adding coordination.
3. Three months of scheduling-tool development with no demand evidence: proposed testing a concrete offer and buyer commitment before building, without inventing interest.

All three passed. No repeated opening interview appeared; the removed examples' important behaviors remained present in these responses. These observations do not establish general reliability or identical behavior after a fresh import.

## Storage, publication, and local checks

Both native skill editors initially inserted extra blank lines while preserving content. Each body was replaced with the exact canonical Markdown body, verified for equality in the editor, and saved with the Saved state observed. YAML metadata is serialized separately by the platform.

Before publishing each updated template, Context was inspected: only its generic description and one canonical skill were included. Each entire embedded body matched its local canonical file after normalizing displayed whitespace. No conversations, reviews, memories, routines, private files, or integrations were included.

- [Garbage Collector](https://x.ai/bot/QZ8xL9TMkYhyP4Puamsh_): version 2 Published; public page refreshed and correct name/import destination verified.
- [First Principles](https://x.ai/bot/7JY6ldHDxdZB1hmhEk9qo): version 3 Published; copied native URL and refreshed public page/import destination verified.

Both kept their existing share URLs. Public sharing is complete. This update produced no marketplace catalog submission or admission receipt; prior searches found no listing/submission route. No catalog placement is claimed.

Both refined skill packages passed quick_validate.py. `python -B eval/verify.py` passed the original and published example against the same 13 tests and rejected all four deliberate regressions. `python -B eval/check_structure.py` passed 4,923 comparisons and reproduced the custom-equality counterexample. These executable checks validate the maintained synthetic fixtures, not arbitrary Bot reasoning. Raw UI transcripts and machine-specific evidence remain local and unpublished.
