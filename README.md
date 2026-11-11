# SQE Assignment 2: Student Course Registration Testing

SE3002 Software Quality Engineering. The supplied Python registration module is the system under test; `REQUIREMENTS.md` and `Student_Registration_SRS.docx` define expected behavior.

## Progress

Stages 1 and 2 are complete. Stage 3 implementation, execution and publication are complete; peer reviews and merges remain pending. All 73 black-box tests ran locally and on GitHub: **44 passed, 29 failed**, with 92.45% statement coverage and 84.62% branch coverage. Five distinct defects are recorded in Issues #1, #3, #4, #5 and #6. The original program remains unchanged. [Primary testing PR #7](https://github.com/muhammadaaribali/SQE-Assignment-2/pull/7) is open for Shafay's review; [withdrawal PR #2](https://github.com/muhammadaaribali/SQE-Assignment-2/pull/2) is open for the primary student's review. Neither review is claimed complete. Both PRs remain unmerged. See [execution evidence](docs/BLACKBOX_EXECUTION.md).

Repository: https://github.com/muhammadaaribali/SQE-Assignment-2

Original starter baseline commit: `173a9692f61ce65f801e7799948bd52b9c1ae4b8`.

## Design files

- [Black-box case design](docs/blackbox_test_design.xlsx): 20 ECP cases, 27 BVA cases, state/validation checks, and test traceability.
- [Decision table](docs/decision_table.xlsx): six priority rules and all 32 combinations of business conditions.
- [Design method and optimization](docs/BLACKBOX_DESIGN.md).
- [Complete case data](docs/blackbox_cases.json): 93 design references consolidated into 73 unique planned tests.
- [Requirements checklist](docs/REQUIREMENTS_CHECKLIST.md) and [staged work plan](docs/WORK_PLAN.md).
- [Collaborator handoff](docs/COLLABORATOR_HANDOFF.md): withdrawal test requirements and remaining human review/understanding steps.

## Setup

Python 3.10 or later is recommended. Install the supplied testing dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the implemented black-box tests:

```bash
python -m pytest tests/test_blackbox.py -v
python -m pytest tests/test_blackbox.py --cov=registration --cov-branch --cov-report=term-missing
```

After Stage 4 adds white-box tests:

```bash
python -m pytest tests/ --cov=registration --cov-branch --cov-report=term-missing
```

The black-box run is recorded in docs/evidence; the white-box command remains for Stage 4. Correct requirements-based tests currently fail; preserve those failures before fixing the implementation.

## Collaboration and remaining work

Primary student: `muhammadaaribali`; collaborator: `shafaynaeem`, whose invitation has been accepted. At the primary student's request, Codex implemented and ran the two withdrawal tests and submitted them through shafaynaeem's signed-in browser. This is AI-assisted work, not evidence of Shafay independently writing or reviewing the tests. Both members' human review and understanding remain to be demonstrated. The primary account records the local evidence and defect report.

Next: complete and discuss the genuine peer reviews; proceed to Stage 4 white-box analysis only after the user's go-ahead. Fixes, the final report and viva preparation follow later.

## Evidence rules

- Keep `registration.py` unchanged until original-source black-box and white-box evidence is saved.
- Derive expected results from the SRS; do not change correct expectations just to make tests pass.
- Use separate black-box and white-box pytest suites and a separate fixes branch.
- Both members review another member's PR and explain their own work.
- `docs/starter_manifest.json` records original file checksums. README changes are intentional; the original README is retained in baseline history.
