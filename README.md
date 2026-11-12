# SQE Assignment 2: Student Course Registration Testing

SE3002 Software Quality Engineering. The supplied Python registration module is the system under test; `REQUIREMENTS.md` and `Student_Registration_SRS.docx` define expected behavior.

## Progress

Stages 1–3 are complete, including the merges of withdrawal PR #2 and primary black-box PR #7. Their approvals were submitted with Codex assistance disclosed.

Stage 4 adds five structural tests and a control-flow graph with explicit short-circuit analysis. The original source is unchanged: **78 tests, 48 passed, 30 failed**, **96.23% statement coverage**, **92.31% branch coverage**. The five existing application defects remain unfixed. See [white-box analysis](docs/WHITEBOX_ANALYSIS.md), [CFG](docs/cfg.png), and [original black-box evidence](docs/BLACKBOX_EXECUTION.md). This branch is awaiting review; Stage 5 fixes and the final report are not yet complete.

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

Run both implemented suites:

```bash
python -m pytest tests/ --cov=registration --cov-branch --cov-report=term-missing
```

Both original-source runs are recorded separately in docs/evidence. Correct requirements-based tests currently fail; preserve those failures before fixing the implementation.

## Collaboration and remaining work

Primary student: `muhammadaaribali`; collaborator: `shafaynaeem`. Codex prepared the implementation, tests and analysis at the primary student's request. Withdrawal tests were submitted through Shafay's signed-in account with disclosure. The primary student walked through both withdrawal cases and requested approval submission; the primary student later confirmed Shafay's understanding and requested his assisted approval on PR #7. Both review submissions disclose the assistance and do not claim independent execution by Shafay.

Next: discuss and review the Stage 4 contribution, then proceed to Stage 5 fixes only after the user's go-ahead. Final reporting and viva preparation follow later.

## Evidence rules

- Keep `registration.py` unchanged until original-source black-box and white-box evidence is saved.
- Derive expected results from the SRS; do not change correct expectations just to make tests pass.
- Use separate black-box and white-box pytest suites and a separate fixes branch.
- Both members review another member's PR and explain their own work.
- `docs/starter_manifest.json` records original file checksums. README changes are intentional; the original README is retained in baseline history.
