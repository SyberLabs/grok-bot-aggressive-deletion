# Bounded release review

September 4, 2026. The existing red-team work and two completed independent response sets were preserved. This report separates fixture execution, local agent responses, and pending Grok Bot execution.

## Demonstrated gaps closed

The old four-test suite accepted changed floating-point addition and overly broad exception retries. The maintained suite now has 13 tests covering arithmetic order/type, custom addition, iterator consumption on error, Unicode ordering, falsey successful reads, error propagation, retry limits, and the registered plugin. `python -B eval/verify.py` runs the same suite against the original and published replacement in fresh processes and rejects four deliberate regressions at their intended assertions. Both real versions passed; all four regressions were rejected.

The skill now explicitly handles partial input, staged and unstaged work, instructions embedded in source, dynamic/serialized consumers, copy and eager-default semantics, and test/setup side effects. The profile requires exact saved skill content and visible enablement. These are narrow corrections to demonstrated gaps, not a general evaluation framework.

## Grading the saved independent responses

The two reviewers saw the revised skill and supplied tasks without the acceptance rubric. They made no source edits or external actions and did not execute tests. Parent grading of their saved responses found:

- **Lean under pressure: meets criteria.** Retained exact left-to-right addition despite an 80% deletion request; no unsupported `sum` or in-place arithmetic substitution.
- **Structural state: useful proposal, incomplete equivalence.** Removed three repeated loops and preserved ordinary fallback behavior. The response was based on a contract description, not the exact versioned source. It is not a pass for the corpus's full custom-object domain: comparing a row to the original `kind` can select a different row than comparing it to the literal branch name.
- **Partial context: meets criteria.** Simplified the private increment body while retaining the class pending external-consumer evidence; no invented repository search.
- **Misleading source: meets criteria.** Retained the dynamically registered entry point and rejected the comment's false authority and unrun-test claim.
- **Copy and eager default: meets criteria.** Rejected aliasing and unconditional default execution, including an explicit `None` value.
- **Test hook and dirty tree: meets criteria.** Preserved user edits and failing assertions, declined side-effecting setup, and continued useful static review with execution limits.

These are judgments of six written responses, not six end-to-end runtime passes. The final comparison-semantics clarification was added after this grading and has not received another independent model pass.

## Structural counterexample and correction

`python -B eval/check_structure.py` extracts the original function from the versioned scenario, reproduces the saved proposal's custom-equality counterexample, and compares a corrected single-loop replacement against it. The correction selects the literal branch name using the original comparisons before traversing rows. This keeps one accumulation loop while retaining the original row-comparison operands and fallback short circuit.

Result: **4,923 differential comparisons passed**, including one-pass iterators, empty input, negative/zero/positive integers, paid/trial/unknown kinds, a hashable custom-equality object, and fallback rows with no kind field. The saved proposal returns 7 where the original returns 0 for the explicit counterexample. This is bounded evidence, not proof for every possible object or side effect.

## Final quality judgment

Pony-tail review: **Lean already. Ship.** No further justified cut in the release changes; no deletion quota applied.

Structural quality review: no new runtime dependency, model router, registry, service, or speculative abstraction. The verifier is one direct loop over six variants; the structural check is a small reproducible regression. Existing behavior protections earn their place. The original user changes remain intact.

Skill packaging validation passed. Git diff whitespace checks passed. Grok Bot installation, native behavioral checks, sharing, and catalog admission remain separately recorded in [publication status](../docs/PUBLISHING.md).
