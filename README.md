# SQE Assignment 2: Student Course Registration Testing

SE3002 Software Quality Engineering. The supplied Python registration module is the system under test; `REQUIREMENTS.md` and `Student_Registration_SRS.docx` define expected behavior.

## Progress

Stages 1 and 2 are complete. This contribution branch adds only withdrawal tests BB-072 and BB-073: a local run produced **1 failed, 1 passed** against the unchanged starter. The remaining 71 planned black-box tests, full-suite coverage, and GitHub Actions are pending Stage 3. No defects have been corrected. See [withdrawal evidence](docs/evidence/withdrawal-initial.txt) and [the confirmed FR-13 defect](https://github.com/muhammadaaribali/SQE-Assignment-2/issues/1).

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

Once Stage 3 adds the tests:

```bash
python -m pytest tests/test_blackbox.py -v
python -m pytest tests/test_blackbox.py --cov=registration --cov-branch --cov-report=term-missing
```

After Stage 4 adds white-box tests:

```bash
python -m pytest tests/ --cov=registration --cov-branch --cov-report=term-missing
```

These are planned commands, not evidence of completed runs. Correct requirements-based tests may initially fail; preserve those failures before fixing the implementation.

## Collaboration and remaining work

Primary student: `muhammadaaribali`; collaborator: `shafaynaeem`, whose invitation has been accepted. At the primary student's request, Codex implemented and ran the two withdrawal tests and submitted them through shafaynaeem's signed-in browser. This is AI-assisted work, not evidence of Shafay independently writing or reviewing the tests. Both members' human review and understanding remain to be demonstrated. The primary account records the local evidence and defect report.

Next: implement the black-box tests, integrate the collaborator's two tests, configure GitHub Actions, preserve original failures and coverage, and file distinct defect Issues. White-box analysis, fixes, reviewed PRs, final report, and viva preparation follow in later stages. The final submission is not complete.

## Evidence rules

- Keep `registration.py` unchanged until original-source black-box and white-box evidence is saved.
- Derive expected results from the SRS; do not change correct expectations just to make tests pass.
- Use separate black-box and white-box pytest suites and a separate fixes branch.
- Both members review another member's PR and explain their own work.
- `docs/starter_manifest.json` records original file checksums. README changes are intentional; the original README is retained in baseline history.
