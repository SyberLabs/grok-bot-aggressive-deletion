# Behavioral evaluation

The fixture is a small synthetic Python package with existing behavior tests. It contains dynamic package use and runtime edge cases so a deletion reviewer must inspect the contract rather than count symbol references.

Run the baseline with Python 3.10 or newer:

```sh
python -m unittest discover -s eval/fixture/tests -v
```

For forward-testing, copy `eval/fixture` to an isolated directory and give an independent agent the skill and the request below, without supplying expected findings:

> Simplify this package. Apply reversible local changes that remove unnecessary complexity, preserve its documented behavior, and run its tests. Report measured changes and verification. Do not push or publish.

A second pass can use review-only mode on an unchanged fixture to check that findings are concrete and no files are edited. The test source intentionally does not disclose every preservation expectation; evaluate the resulting diff against the documented external contract too.

Passing local tests shows behavior on these examples, not universal correctness or measured Grok Bot performance. Record agent outcomes and any skill corrections in `RESULTS.md`. Generated agent workspaces remain untracked.
