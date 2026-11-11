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

Stage 3 implementation, execution and publication are complete; peer reviews and merges remain pending. All 73 black-box tests ran locally and on GitHub: **44 passed, 29 failed**, with 92.45% statement coverage and 84.62% branch coverage. Five distinct defects are recorded in Issues #1, #3, #4, #5 and #6. The original program remains unchanged. [Primary testing PR #7](https://github.com/muhammadaaribali/SQE-Assignment-2/pull/7) is open for Shafay's review; [withdrawal PR #2](https://github.com/muhammadaaribali/SQE-Assignment-2/pull/2) is open for the primary student's review. Neither review is claimed complete. Both PRs remain unmerged.

[Actions run 42997171307](https://github.com/muhammadaaribali/SQE-Assignment-2/actions/runs/42997171307) completed with a genuine test failure, exit 1: 29 failed, 44 passed, no errors or skipped tests. Installation and artifact upload both succeeded. Downloaded JUnit and coverage artifacts confirm the same counts and coverage as the local run. CI used Python 3.14.10; local Python was 3.14.4.

The tested branch head is `9db9d47643e8605f73964d7ac4082b01be3a2fcd`. The PR run checked out temporary merge commit `9b392471e6dfe5391e3a6aa7cb7f54593a48934a`. Artifact `test-evidence-42997171307-1` (ID 13844556354) contains 16 files and expires on 9 February 2027. Durable copies of the CI log, JUnit, coverage JSON, dependencies and run metadata are also preserved as `evidence/blackbox-ci*`.

The published `.github/workflows/tests.yml` runs on pushes and PRs, retains pytest's failing exit status with pipefail, and uploads reports using always(). Its operation was verified by this completed run. Action versions follow the official [checkout](https://github.com/actions/checkout), [setup-python](https://github.com/actions/setup-python), and [upload-artifact](https://github.com/actions/upload-artifact) documentation.

Primary contribution prepared with Codex assistance; original withdrawal commits retained with their existing disclosures. Automated work does not constitute independent human review. Pause at the Stage 3 review checkpoint before starting Stage 4 or fixing source defects.
