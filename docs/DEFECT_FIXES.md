# Stage 5: corrected-source regression results

## What changed

PR #8 was technically reviewed with Codex assistance (review 5878893248) and merged at the primary student's explicit request. This is not an independent collaborator approval. Merge commit: `e72449f60343dc75f64f5fddc83a4f21fe1d6b2d`. The separate `defect-fixes` branch starts from that preserved original-source checkpoint.

Only five source corrections were made. Tests and the frozen design data are byte-for-byte unchanged, verified against Stage 4 SHA-256 records. All expected outcomes still come from REQUIREMENTS.md.

| Issue | Requirement | Original defect | Correction | Existing regression witnesses |
|---|---|---|---|---|
| #3 | FR-01 | Total exactly 18 rejected (`< 18`) | Allow `<= 18` | BB-023, BB-029 |
| #4 | FR-03/06 | Any prerequisite overlap accepted | Require `required.issubset(completed)` | BB-009, BB-016; WB-003 retains no-overlap rejection |
| #5 | FR-04/09 | Only dues above 1000 blocked | Block any dues `> 0` | BB-014, WB-002; priority cases BB-045 onward |
| #6 | FR-08/12 | Full course registered; waitlist route unreachable | Waitlist when `enrolled == capacity` | BB-012, BB-064/065 (new/existing waitlist entry) |
| #1 | FR-13/14 | Withdrawal left enrollment unchanged | Decrement enrollment once after successful withdrawal | BB-072; BB-073 retains no-change rejection |

Numeric validation order, business priority, public function signatures and status/error strings remain unchanged. No extra behavior for invalid identifiers/types or inconsistent withdrawal records was invented beyond the SRS scope.

## Before-and-after evidence

| Measurement | Original black-box | Original full suite (Stage 4) | Fixed full suite (Stage 5 local) |
|---|---:|---:|---:|
| Tests | 73 | 78 | 78 |
| Passed | 44 | 48 | 78 |
| Failed | 29 | 30 | 0 |
| Statement coverage | 49/53 = 92.45% | 51/53 = 96.23% | 54/54 = 100% |
| Branch coverage | 22/26 = 84.62% | 24/26 = 92.31% | 26/26 = 100% |

The extra statement is the new enrollment decrement. All 30 previously failing test cases now pass; the 48 previous passes remain passing. JUnit case identities were compared, not only total counts. There are no skips, xfails, mocks or coverage exclusions. 100% measured statement/branch coverage is not a proof that every possible input is correct, nor a measurement of full-program MC/DC.

The original `docs/cfg.png`, WHITEBOX_ANALYSIS.md and their evidence remain historical analyses of the unmodified source. Their dues threshold and infeasible waitlist explanation must not be presented as descriptions of the corrected source. The corrected function has the same expanded CFG topology/complexity (V=10), but D3 becomes dues > 0 and D7 becomes enrolled == capacity. P9 is now feasible for an otherwise eligible student in a full course. The earlier line-48 compound condition is unchanged.

The nine-predicate manual condition scope from Stage 4 can now achieve both truth outcomes for all nine predicates (18/18): original witnesses still cover D1/A/B/C/D3/D4/D5/D6 and BB-012 covers corrected D7=True while BB-011 covers False. This is a source-based inference using executed witnesses, separate from coverage.py's measured statement/branch results. The selected line-48 MC/DC pairs remain unchanged.

## Reproduction and artifacts

From the project directory with dependencies installed:

```bash
python -m pytest tests/ -v --tb=short --cov=registration --cov-branch --cov-report=term-missing
```

Local run: docs/evidence/fixed-local.txt, fixed-local-junit.xml, fixed-local-coverage.json/.xml and fixed-local-run.json. Metadata records the exact command, source/test hashes, base commit and exit code 0. Original blackbox-original*, whitebox-original* and whitebox-ci* evidence is retained unchanged. GitHub verification will be recorded separately after the fixes PR runs.

## Review checkpoint

Prepared with Codex assistance on the primary student's side. No independent human review or execution is claimed. Keep the fixes PR unmerged until the user reviews this stage and authorizes merging. Issues remain open until the fixes are merged. Stage 6 (final PDF report and submission checks) is not started.
