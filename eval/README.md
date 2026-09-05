# Behavioral evaluation

The fixture is a small synthetic Python package with existing behavior tests. It contains dynamic package use and runtime edge cases so a deletion reviewer must inspect the contract rather than count symbol references.

Run reproducible example and regression checks with Python 3.10 or newer:

```sh
python eval/verify.py
python eval/check_structure.py
```

This runs the original fixture and published simplified example against the same 13 behavior tests in fresh temporary copies. It also rejects four intentional regressions: changed arithmetic, overly broad retries, repeated falsey successes, and weakened Unicode folding. Copies isolate fixture files; they are not a security sandbox. The runner executes only this repository's inspected synthetic code. No model calls, accounts, or network access are required.

For a new agent-generated candidate, copy `eval/fixture` to an isolated directory and give an independent agent the skill and the request below, without supplying expected findings:

> Simplify this package. Apply reversible local changes that remove unnecessary complexity, preserve its documented behavior, and run its tests. Report measured changes and verification. Do not push or publish.

A second pass can use review-only mode on an unchanged fixture to check that findings are concrete and no sources are edited. Inspect commands and test setup before execution; imports and tests can have side effects. Also use the [scenario corpus](scenarios.json) for no-cut, structural, partial-context, and misleading-source cases. Give agents only the case's `task`, then grade their artifacts using `acceptance` afterward.

The structural check reproduces a flaw in the saved review proposal and checks a corrected single-loop replacement against the exact versioned scenario. See [current red-team results](RED-TEAM.md) for the six response judgments and limitations.

Passing local tests shows behavior on these examples, not universal correctness or measured Grok Bot performance. Record agent outcomes and any skill corrections in `RESULTS.md`. Generated agent workspaces remain untracked.
