# SQE Assignment 2: Student Course Registration Testing

SE3002 Software Quality Engineering. The supplied Python registration module is the system under test; `REQUIREMENTS.md` and `Student_Registration_SRS.docx` define expected behavior.

## Progress

Stages 1–5 are complete. The original-source analysis is preserved in PR #8; the five fixes were merged through PR #9. All **78 unchanged tests pass**, with **54/54 statements and 26/26 branches covered**. Original failing runs remain available.

Stage 6 deliverables: [final testing report](docs/testing_report.pdf), [submission checklist](docs/SUBMISSION_CHECKLIST.md), design workbooks, original CFG and evidence. The report includes all requested analysis and discloses the actual assistance and contribution record. Course-portal submission and each member's viva preparation remain personal steps.

The [white-box analysis](docs/WHITEBOX_ANALYSIS.md) and [CFG](docs/cfg.png) describe the original source (48 passes, 30 failures). [Corrected-source regression results](docs/DEFECT_FIXES.md) describe the five fixes and 78 passing tests.

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

Original failing runs and corrected passing runs are recorded separately in docs/evidence. The frozen design JSON retains its original planning status; execution evidence records actual results.

## Collaboration and remaining work

Primary student: Muhammad Aarib Ali (24P-3036), `muhammadaaribali`; collaborator: Shafay Naeem (3089), `shafaynaeem`. Codex prepared the implementation, tests and analysis at the primary student's request. Withdrawal tests were submitted through Shafay's signed-in account with disclosure. The primary student walked through both withdrawal cases and requested approval submission; the primary student later confirmed Shafay's understanding and requested his assisted approval on PR #7. Both review submissions disclose the assistance and do not claim independent execution by Shafay.

Next: inspect the final report and names/roll numbers, ensure the instructor can access the repository, submit the required files/link through the course portal, and prepare for the viva.

## Evidence rules

- Keep `registration.py` unchanged until original-source black-box and white-box evidence is saved.
- Derive expected results from the SRS; do not change correct expectations just to make tests pass.
- Use separate black-box and white-box pytest suites and a separate fixes branch.
- Both members review another member's PR and explain their own work.
- `docs/starter_manifest.json` records original file checksums. README changes are intentional; the original README is retained in baseline history.
