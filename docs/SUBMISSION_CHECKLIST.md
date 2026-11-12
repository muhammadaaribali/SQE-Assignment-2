# Submission checklist

## Prepared repository artifacts

- [x] Corrected registration.py and original starter history.
- [x] REQUIREMENTS.md, requirements.txt, README.md.
- [x] Separate black-box and white-box pytest suites: 73 + 5 = 78 tests.
- [x] docs/blackbox_test_design.xlsx and docs/decision_table.xlsx.
- [x] docs/cfg.png, complexity/basis-path/condition/MC-DC analysis.
- [x] docs/testing_report.pdf, with both supplied names and roll numbers.
- [x] Original legitimate failures and corrected successful runs retained under docs/evidence.
- [x] Five defect Issues (#1, #3, #4, #5, #6) fixed and closed by PR #9.
- [x] PRs #2, #7, #8 and #9 merged, with disclosed assisted review records.
- [x] GitHub Actions runs tests on push/PR and preserves evidence.

Repository: https://github.com/muhammadaaribali/SQE-Assignment-2

Report: docs/testing_report.pdf (12 pages). Names: Muhammad Aarib Ali / 24P-3036; Shafay Naeem / 3089, exactly as supplied. Original CFG and pre-fix analyses remain historical artifacts, not diagrams of corrected predicates. The frozen design JSON and spreadsheets preserve their planning snapshot; JUnit/logs are the execution record.

## Student checks before handing in

- [ ] Confirm names and roll numbers, including whether Shafay's supplied 3089 needs a prefix.
- [ ] Personally inspect each member's contribution and be ready to explain it in the viva. Assisted cross-account review submissions do not establish independent human review/execution.
- [ ] Ensure the instructor can access this private repository through the course-approved sharing method.
- [ ] Submit the repository link, PDF, design sheets and any requested evidence through the course portal. No portal submission has been performed.

## Reproduction

```bash
python -m pip install -r requirements.txt
python -m pytest tests/ -v --tb=short --cov=registration --cov-branch --cov-report=term-missing
```

Corrected source: 78 passed, exit 0, 54/54 statements and 26/26 branches. This does not prove correctness for all possible inputs.
