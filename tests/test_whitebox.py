"""Structural additions for the unchanged starter; expectations remain SRS-based.

These tests do not patch the application or manufacture unreachable branches.
See docs/WHITEBOX_ANALYSIS.md for paths, coverage gaps and MC/DC.
"""

from copy import deepcopy

import pytest

from registration import Course, Student, registration_decision


@pytest.fixture
def eligible_pair():
    """Fresh valid records; only each test's targeted input is changed."""
    student = Student(
        student_id="S001", completed_courses={"CS101", "MATH101"},
        current_credits=12, outstanding_dues=0, registered_courses={"CS100"},
    )
    course = Course(
        code="CS201", credit_hours=3, capacity=30, enrolled=29,
        prerequisites={"CS101", "MATH101"}, waitlist=["S999"],
    )
    return student, course


@pytest.mark.parametrize(
    "dues, expected",
    [(1001, "DUES_BLOCK"), (1000, "DUES_BLOCK")],
    ids=["WB-001", "WB-002"],
)
def test_dues_implementation_boundary(eligible_pair, dues, expected):
    """FR-04/10: exercise both sides of line 50's incorrect 1000 threshold."""
    student, course = eligible_pair
    student.outstanding_dues = dues
    before = deepcopy((student, course))
    try:
        assert registration_decision(student, course) == expected
    finally:
        assert (student, course) == before


def test_wb_003_no_prerequisite_overlap(eligible_pair):
    """FR-06/10: line 54 True reaches the previously uncovered line 55."""
    student, course = eligible_pair
    student.completed_courses = {"ENG101"}
    before = deepcopy((student, course))
    try:
        assert registration_decision(student, course) == "PREREQUISITES_MISSING"
    finally:
        assert (student, course) == before


@pytest.mark.parametrize(
    "current, new, message",
    [(-1, 3, "Invalid current credits"), (12, 0, "Invalid course credits")],
    ids=["WB-004", "WB-005"],
)
def test_credit_helper_error_propagation(eligible_pair, current, new, message):
    """FR-02/10: traverse line 56 into each helper validation exception."""
    student, course = eligible_pair
    student.current_credits = current
    course.credit_hours = new
    before = deepcopy((student, course))
    try:
        with pytest.raises(ValueError) as error:
            registration_decision(student, course)
        assert str(error.value) == message
    finally:
        assert (student, course) == before
