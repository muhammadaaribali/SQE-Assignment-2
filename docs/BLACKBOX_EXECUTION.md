# Original-source black-box execution

Local run on 11 November 2026: **73 collected, 44 passed, 29 failed**, exit code 1. The 93 design references map to these 73 unique executable tests. All planned IDs BB-001 through BB-073 were verified against the JUnit output, with no omissions or duplicates.

The primary contribution implements BB-001 through BB-071 as parameterized pytest cases reading the frozen design data. BB-072 and BB-073 retain the withdrawal implementation submitted in PR #2. Each case gets fresh mutable objects. Expected outcomes come from the design, not from the implementation under test. Checks cover exact exceptions/messages, return types/values, and complete object state; state is checked even when a return assertion fails.

## Results and coverage

| Measurement | Result |
|---|---:|
| Passed | 44 |
| Failed | 29 |
| Skipped / expected failures | 0 / 0 |
| Statement coverage | 49 / 53 = 92.45% |
| Branch coverage | 22 / 26 = 84.62% |
| Combined coverage shown by pytest-cov | 71 / 79 = 89.87% (displayed 90%) |

These are coverage.py measurements, not condition coverage or MC/DC. Structural analysis belongs to Stage 4. High coverage does not imply correctness: 29 cases fail despite reaching most statements.

## Confirmed defects

29 failed cases represent five distinct defects, not 29 different bugs. IDs below partition all failures.

| Defect | Requirement | Failed IDs | Expected versus actual |
|---|---|---|---|
| Partial prerequisites accepted | FR-03, FR-06, FR-09, FR-12 | BB-009, BB-016, BB-034, BB-035, BB-036, BB-068 | Completing CS101 alone cannot satisfy both CS101 and MATH101. Actual helper returns True; registration proceeds or reaches a lower-priority credit check. |
| Positive dues ignored | FR-04, FR-09, FR-12 | BB-012, BB-045 through BB-059, BB-066 | Rs. 1 must cause DUES_BLOCK before other business conditions. Actual behavior proceeds to another outcome, including registration and mutation. |
| Exactly 18 credits rejected | FR-01 | BB-023, BB-029 | 17+1 and 15+3 must return True. Actual result is False. |
| Full course over-enrolled | FR-08, FR-12 | BB-014, BB-064, BB-065 | Enrollment 30 of capacity 30 must return WAITLISTED; registration should append only an absent ID and otherwise preserve state. Actual registration increases enrollment to 31 and changes student registration/credits. |
| Withdrawal leaves enrollment unchanged | FR-13 | BB-072 | Dropping the course must reduce enrollment 30 to 29. Actual enrollment stays 30. Existing GitHub Issue #1. |

GitHub defects: [#3 exactly 18 credits](https://github.com/muhammadaaribali/SQE-Assignment-2/issues/3), [#4 partial prerequisites](https://github.com/muhammadaaribali/SQE-Assignment-2/issues/4), [#5 dues](https://github.com/muhammadaaribali/SQE-Assignment-2/issues/5), [#6 full course](https://github.com/muhammadaaribali/SQE-Assignment-2/issues/6), and existing [#1 withdrawal](https://github.com/muhammadaaribali/SQE-Assignment-2/issues/1). No implementation fixes have been applied.

## Reproduction and evidence

From the project root, install requirements.txt, then run:

```bash
python -m pytest tests/test_blackbox.py -v --tb=short --cov=registration --cov-branch --cov-report=term-missing
```

The original run used Python 3.14.4, pytest 9.2.0, pytest-cov 7.1.0 and coverage 7.17.2. Exact invocation, UTC timestamp, return code and SHA-256 checksums are in `evidence/blackbox-original-run.json`. The source is byte-identical to the original starter at commit `173a9692f61ce65f801e7799948bd52b9c1ae4b8`.

- `evidence/blackbox-original.txt`: complete pytest output.
- `evidence/blackbox-original-junit.xml`: machine-readable failures.
- `evidence/blackbox-original-results.json`: per-ID pass/fail mapping.
- `evidence/blackbox-original-coverage.json` and `.xml`: coverage data.
- `evidence/blackbox-original-html/index.html`: browsable local coverage.

The original design JSON and spreadsheets remain the frozen pre-execution design, including their historical “Not run” fields. This execution document and per-ID results are the current run record.

## GitHub and review status

This is a local combined working-copy run, including the two tests from the still-open, unmerged [PR #2](https://github.com/muhammadaaribali/SQE-Assignment-2/pull/2). It is not evidence of a merged contribution or an Actions run. PR #2 was checked in the browser on 11 November and remains open. Human review remains pending.

`.github/workflows/tests.yml` is prepared locally. It runs tests on pushes and PRs and uses pipefail to preserve pytest's failing exit status while tee saves the log. Artifact upload uses always(), so test failures do not suppress evidence. It has not yet been published or executed on GitHub. Action versions follow the official [checkout](https://github.com/actions/checkout), [setup-python](https://github.com/actions/setup-python), and [upload-artifact](https://github.com/actions/upload-artifact) documentation checked on 11 November 2026.

Before Stage 3 is complete: publish the primary contribution and workflow, open the primary testing PR, verify the Actions result/artifacts, and guide the students through their actual peer reviews. Codex assistance must remain disclosed; automated work does not constitute independent human review.
