# Black-box design baseline

This design uses REQUIREMENTS.md as the expected-behavior source. It is not an execution report. The implementation remains the original starter. The assistant viewed the implementation during the initial assignment review; this document does not claim that source had never been viewed. Structural test design has not started.

## Design inventory

| Technique | Design references |
|---|---:|
| Equivalence class partitioning | 20 |
| Boundary value analysis | 27 |
| Decision-table combinations | 32 |
| Additional validation-priority checks | 3 |
| State changes and non-mutation | 11 |
| Total | 93 |

These references map to **73 unique planned tests**, with **20 duplicate executions removed**. The primary student's scope is 71 tests; two withdrawal tests are reserved for the collaborator. No pytest tests have been implemented or executed at this stage.

## Files and test identity

- `blackbox_test_design.xlsx`: ECP, BVA, state/validation cases, and consolidated traceability.
- `decision_table.xlsx`: six priority rules and all 32 business-condition combinations.
- `blackbox_cases.json`: complete starting states, explicit expected outcomes/after-states, test IDs, ownership, and technique mappings. Lists representing sets are identified in the file; waitlists retain order.

`BB-nnn` identifies a single execution. `ECP-nn`, `BVA-nn`, `DT-nn`, `VAL-nn`, and `STATE-nn` identify design references. In Stage 3, preserve BB IDs in pytest parameter IDs or test names and report evidence against these IDs. Expected values in the JSON are fixed specification-derived data; do not compute expected outcomes by calling the implementation under test.

## Equivalence classes and boundaries

ECP includes valid and invalid credit values, valid credit sums, empty/all/partial/missing prerequisites, zero/positive/negative dues, duplicate registration, available/full seats, and invalid capacity/enrollment.

BVA checks current credits -1, 0, 1, 17, 18, 19; course credits 0, 1, 2, 3, 4, 5; totals 17, 18, 19; dues -1, 0, 1; capacity 0, 1, 2; and enrollment -1, 0, 1, 29, 30, 31 for capacity 30. Numeric exceptions check exact messages. When checking one boundary, other inputs are valid unless the explicit purpose is validation priority.

## Decision table

The five business facts are positive dues, duplicate registration, prerequisites met, credit eligibility, and seat availability. All 2^5 = 32 combinations are represented. Apply priority in this order: dues, duplicate, prerequisites, credits, availability. Six condensed rules cover 16, 8, 4, 2, 1, and 1 combinations respectively.

Numeric input validation precedes business outcomes. Invalid input cases are separate from the 32 business combinations. T/F in this decision table describes the input facts, not whether Python evaluates a condition at runtime. The later white-box phase will separately use True/False/not-evaluated condition tables.

## Exact duplicate optimization

Deduplicate only when the operation, complete initial state/arguments, expected return or exception, and state assertions all match. Requirement labels and technique labels may differ without changing the execution. Every original design reference is retained in the Traceability sheet and JSON.

Examples:

- ECP-01 and BVA-10 both call check_credit_limit(12, 3), expect True, and map to BB-001.
- ECP-03 and BVA-01 both call check_credit_limit(-1, 1), expect ValueError("Invalid current credits"), and map to BB-003.
- A registration_decision case and a register_course case are not duplicates even when the starting state and returned status match, because the operations and mutation contracts differ.
- Cases returning DUES_BLOCK with different combinations of later conditions are retained to verify priority; equal output alone does not establish duplication.

## State and fixture rules

Each test creates fresh objects. Snapshot both objects with a deep copy before calling the target function. Compare all fields, including completed courses, prerequisites, and existing waitlist entries. Decision calls leave both objects unchanged. Successful registration updates course membership, credits, and enrollment. Waitlisting changes only the waitlist and does not append a duplicate ID. Rejected registration leaves all fields unchanged. Withdrawal tests are reserved as described in COLLABORATOR_HANDOFF.md.

Use the explicit numeric-validation scope in the SRS. Do not add invented requirements for wrong types, persistence, concurrency, or automatic waitlist promotion. Current/course credit validation is directly tested through check_credit_limit; decision tests respect earlier returns.

## Stage 3 evidence to collect

Implement `tests/test_blackbox.py`, including the collaborator's two cases before finalizing the baseline. Run the original source and retain verbose pytest output, JUnit/coverage artifacts, commit SHA, and Actions run links. Log distinct confirmed defects with requirement IDs, reproduction, expected/actual behavior, failed test IDs and status. No pass/fail or coverage claims are made until those executions occur.
