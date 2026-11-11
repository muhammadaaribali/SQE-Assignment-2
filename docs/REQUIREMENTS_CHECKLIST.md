# Requirements checklist

Source: the supplied REQUIREMENTS.md and matching Student_Registration_SRS.docx. This is a requirements checklist, not execution evidence. Stage 2 design is now recorded in blackbox_test_design.xlsx, decision_table.xlsx and blackbox_cases.json. Stable BB test IDs map all requirements to planned executions; implementation and results remain pending Stage 3.

| Requirement | Required behavior to verify | Planned checks | Owner |
|---|---|---|---|
| FR-01 | Valid total credits <= 18 returns True; above 18 returns False | Totals below, equal to, and above 18 with valid individual arguments | Primary |
| FR-02 | Current credits outside 0-18 raise Invalid current credits; new credits outside 1-4 raise Invalid course credits; current credits checked first | Both limits and immediately outside values; both invalid to check priority; exact exception messages | Primary |
| FR-03 | All prerequisites must be completed; empty requirements return True | None required; all completed; partial completion; none completed | Primary |
| FR-04 | Any positive dues block registration with DUES_BLOCK | Zero, one rupee, representative positive balance | Primary |
| FR-05 | Existing registration returns ALREADY_REGISTERED | Target course already in registered_courses with earlier-priority checks satisfied | Primary |
| FR-06 | Any missing prerequisite gives PREREQUISITES_MISSING | Partial and fully missing prerequisites with earlier checks satisfied | Primary |
| FR-07 | Adding a course above 18 credits gives CREDIT_LIMIT | Valid arguments producing totals exactly 18 and above 18 | Primary |
| FR-08 | Full course gives WAITLISTED; available seat gives REGISTERED | Otherwise eligible student; enrolled below/equal to capacity, including capacity one | Primary |
| FR-09 | Decision priority: dues, duplicate, prerequisites, credit limit, availability | Decision table covering all six statuses and meaningful overlapping rejection reasons | Primary |
| FR-10 | registration_decision never mutates student or course | Compare complete independent before/after snapshots across outcomes and applicable validation errors | Primary |
| FR-11 | Successful registration adds course, adds its credits, increments enrollment | Exact state differences; unrelated fields unchanged | Primary |
| FR-12 | Waitlisting adds ID only if absent; no other state changes; rejected registration changes nothing | First and repeat waitlisting; complete snapshots for blocked outcomes | Primary |
| FR-13 | Registered withdrawal returns True, removes course, subtracts credits, decreases enrollment by one | Coherent starting state; exact changes and unrelated-field preservation | Collaborator (reserved) |
| FR-14 | Nonregistered withdrawal returns False and changes neither object | Coherent nonregistered state; full snapshots; repeat withdrawal if appropriate | Collaborator (reserved) |
| FR-15 | Negative dues raise Invalid dues; capacity < 1 or enrollment outside 0-capacity raises Invalid capacity or enrollment; dues validated first | Negative/zero dues; capacity zero/one; enrollment -1/0/capacity/capacity+1; simultaneous invalid dues and capacity | Primary |

## Validation scope

- Assume valid string identifiers and correct collection types as instructed by the SRS.
- Numeric inputs use the stated integer domains. Do not invent requirements for floats, strings, concurrency, databases, or automatic waitlist promotion.
- Exercise current/new credit range validation directly through check_credit_limit. In registration_decision, respect earlier validation and decision returns; do not assume credit checks always execute after an earlier outcome.
- For rejection-priority cases, use otherwise valid numeric fields so invalid-input exceptions do not obscure the intended business decision.
- Use coherent student/course state for state-change tests. Deep-copy mutable collections for before/after comparisons.

## Meaning of the main testing techniques

- Equivalence class partitioning: group inputs with the same specified treatment and choose representatives from valid and invalid groups. Minimum: 8 cases.
- Boundary value analysis: check limits and applicable adjacent values for current credits, course credits, total credits, capacity/enrollment, and dues. Minimum: 10 cases.
- Decision table: combine conditions and specify the first applicable result under the required priority.
- White-box testing: after black-box design/execution, inspect branches and paths to identify structural gaps.
- MC/DC: demonstrate each atomic condition's independent effect on a selected compound decision with defensible test pairs, recording conditions skipped by Python short-circuiting.

## Illustrative specification examples (not execution results)

1. 15 current credits plus a 3-credit course fits exactly within 18.
2. One rupee of dues blocks new registration.
3. Completing only CS101 does not satisfy prerequisites {CS101, MATH101}.
4. An eligible student facing 30 enrolled students in a capacity-30 course must be waitlisted.
5. Withdrawing an enrolled student decreases both their credits and the course enrollment count.
