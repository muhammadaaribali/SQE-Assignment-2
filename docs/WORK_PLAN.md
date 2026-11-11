# Assignment 2: staged work plan

## Current status

11 November 2026: Stages 1 and 2 are complete. Stage 3 local execution now covers all 73 tests: 44 passed, 29 failed against the unchanged original source. Five distinct defects are confirmed. Coverage is 92.45% statements and 84.62% branches. Full evidence and current status are in BLACKBOX_EXECUTION.md.

The new test runner, local execution evidence and Actions workflow are prepared locally. Publishing them, opening four new defect Issues and the primary PR, verifying Actions, and completing human reviews remain pending. Existing withdrawal PR #2 is open and unmerged; the local suite includes its two tests. No source fixes have been applied.

We stop after each part so the student can ask questions before requesting the next part. These are working stages; the assignment's assessed Parts A-D are tracked separately below.

| Stage | Work and completion checkpoint | Assignment coverage |
|---|---|---|
| 1. Setup and scope | Preserve starter; map FR-01 through FR-15; define responsibilities and evidence rules | Preparation |
| 2. GitHub and black-box design | Set up dedicated repository; finalize at least 8 ECP and 10 BVA cases, decision table, test IDs, and duplicate mapping; produce design spreadsheets | A1-A3, A5, C1-C2 |
| 3. Black-box execution | Implement tests on a feature branch; run original source; preserve logs and coverage; create defect Issues; enable Actions; open test PR | A4, C2-C5 |
| 4. White-box analysis | CFG, complexity convention, independent paths, structural tests, manual condition/MC/DC tables; measure coverage before source fixes | B1-B4 |
| 5. Fixes and review | Separate defect-fixes branch and PR; review and address feedback; run regression tests and Actions; retain initial failures | C2-C5 |
| 6. Report and submission | Create final report, verify links and evidence, record actual contributions, prepare viva explanation | D and submission checklist |

## Responsibility split

The primary student (GitHub: muhammadaaribali), with assistant help, owns the principal test design, registration tests, white-box analysis, defect investigation/fixes, automation, spreadsheets, diagram, and report. Student name and roll number are not yet provided.

The collaborator's assigned scope is the withdrawal tests FR-13/FR-14. At the primary student's explicit request, Codex implemented and ran these and submitted them through shafaynaeem's browser, with assistance disclosed in PR #2. This is not independent human implementation or review. Both students' full names and roll numbers remain to be supplied.

Both members must review another member's PR and address feedback. A proposed division is not evidence of completed contributions. Record actual PRs, commits, reviews, and feedback responses when they exist; do not invent them. Both members prepare to explain their own work in the viva.

## Collaborator handoff checkpoints

1. At the end of Stage 2: give the primary student the finalized withdrawal test IDs, interface/fixture conventions, branch instructions, and expected results to forward to the collaborator. Obtain their GitHub username before access setup. Their tests must join the black-box suite before the Stage 3 baseline is finalized.
2. During Stage 3: collaborator implements FR-13/FR-14 checks on their branch and opens a PR. Primary student reviews that PR with guidance. Collaborator reviews the primary student's testing PR.
3. Before final submission: verify the real contribution/review record and each member's understanding.

No collaborator action is needed during Stage 1. The assistant does not send messages to the collaborator on the student's behalf.

## Evidence and sequencing rules

- Expected results come from REQUIREMENTS.md/SRS. The assistant inspected the implementation during the initial explanatory review; do not claim the source had never been viewed. Complete requirements-based black-box design before undertaking structural test design.
- Keep registration.py unchanged through initial test design, original-code executions, and white-box coverage analysis.
- Preserve genuine failing test output. Never weaken an assertion or change a correct expectation to obtain a passing result.
- Link each design case to requirement IDs and executable test IDs. Consolidate only genuinely identical setups, inputs/actions, and assertions; equal outputs alone do not make cases duplicates.
- Keep black-box tests in tests/test_blackbox.py and structural additions in tests/test_whitebox.py.
- Record three distinct measurements: original source with black-box tests; same original source with black-box plus white-box tests; corrected source with the full regression suite. This separates test improvements from source changes.
- Explain unreachable branches and short-circuit conditions. pytest-cov reports statement/branch coverage; condition coverage and MC/DC require manual analysis.
- Actions must retain test/coverage artifacts on failures and still report a failed job for actual test failures. Preserve run links and commit references.
- Use a separate fixes branch and preserve the original baseline in history. Link confirmed defects to Issues and regression tests.
- At least two PRs are required. Planned PRs include primary black-box work, collaborator withdrawal tests, white-box work, and fixes; only actual PRs count.

## Required final outputs

- registration.py, requirements.txt, REQUIREMENTS.md, and updated README.md
- tests/test_blackbox.py and tests/test_whitebox.py
- docs/blackbox_test_design.xlsx and docs/decision_table.xlsx
- docs/cfg.png and docs/testing_report.pdf
- .github/workflows/tests.yml
- Initial and final execution/coverage evidence, including legitimate failing Actions runs
- Repository, Issue, PR, and review links; accurate member contributions

## GitHub status

Private repository: https://github.com/muhammadaaribali/SQE-Assignment-2. The unchanged starter is on main at 173a9692f61ce65f801e7799948bd52b9c1ae4b8. Design is on blackbox-testing. Collaborator shafaynaeem has accepted access. PR #2 contains the AI-assisted withdrawal contribution; Issue #1 records its defect. New Stage 3 local work is not yet published. GitHub connector is disconnected in the current session; browser read access was verified. Recheck remote heads before publishing.
