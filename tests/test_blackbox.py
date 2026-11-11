"""Execute the requirements-based design; retain the two withdrawal tests."""

from copy import deepcopy
import json
from pathlib import Path

import pytest

from registration import (
    Course, Student, check_credit_limit, prerequisites_satisfied,
    register_course, registration_decision, withdraw_course,
)


DESIGN = json.loads(
    (Path(__file__).resolve().parents[1] / "docs" / "blackbox_cases.json")
    .read_text(encoding="utf-8")
)
PRIMARY_CASES = [case for case in DESIGN["cases"] if case["owner"] == "Primary"]
OPERATIONS = {
    "check_credit_limit": check_credit_limit,
    "prerequisites_satisfied": prerequisites_satisfied,
    "registration_decision": registration_decision,
    "register_course": register_course,
}


def make_objects(data):
    """Decode design data into fresh objects without sharing mutable fields."""
    student_data = deepcopy(data["student"])
    course_data = deepcopy(data["course"])
    for field in ("completed_courses", "registered_courses"):
        student_data[field] = set(student_data[field])
    course_data["prerequisites"] = set(course_data["prerequisites"])
    return {"student": Student(**student_data), "course": Course(**course_data)}


@pytest.mark.parametrize("case", PRIMARY_CASES, ids=lambda case: case["test_id"])
def test_designed_blackbox(case):
    """Compare return/exception and complete state with the frozen design."""
    operation = OPERATIONS[case["operation"]]
    inputs = deepcopy(case["inputs"])
    if "student" in inputs:
        inputs = make_objects(inputs)
    elif case["operation"] == "prerequisites_satisfied":
        inputs = {key: set(value) for key, value in inputs.items()}

    expected_inputs = deepcopy(inputs)
    if isinstance(case["state"], dict):
        expected_inputs = make_objects(case["state"]["after"])

    expected = case["expected"]
    try:
        if "exception" in expected:
            assert expected["exception"] == "ValueError"
            with pytest.raises(ValueError) as error:
                operation(**inputs)
            assert str(error.value) == expected["message"]
        else:
            actual = operation(**inputs)
            # Do not accept 1/0 in place of a genuine Boolean result.
            assert type(actual) is type(expected["return"])
            assert actual == expected["return"]
    finally:
        # Also inspect complete state when the return-value assertion fails.
        assert inputs == expected_inputs, f"{case['test_id']}: unexpected state"


def test_bb_072_withdraw_registered_student():
    """FR-13: remove membership and credits, decrement enrollment, preserve other fields."""
    student = Student(
        student_id="S001",
        completed_courses={"CS101", "MATH101"},
        current_credits=15,
        outstanding_dues=0,
        registered_courses={"CS100", "CS201"},
    )
    course = Course(
        code="CS201",
        credit_hours=3,
        capacity=30,
        enrolled=30,
        prerequisites={"CS101", "MATH101"},
        waitlist=["S999"],
    )
    expected_student = deepcopy(student)
    expected_course = deepcopy(course)
    expected_student.registered_courses = {"CS100"}
    expected_student.current_credits = 12
    expected_course.enrolled = 29

    outcome = withdraw_course(student, course)

    assert outcome is True
    assert student == expected_student
    assert course == expected_course


def test_bb_073_withdraw_unregistered_student():
    """FR-14: return False and preserve every field when not registered."""
    student = Student(
        student_id="S001",
        completed_courses={"CS101", "MATH101"},
        current_credits=12,
        outstanding_dues=0,
        registered_courses={"CS100"},
    )
    course = Course(
        code="CS201",
        credit_hours=3,
        capacity=30,
        enrolled=29,
        prerequisites={"CS101", "MATH101"},
        waitlist=["S999"],
    )
    before_student = deepcopy(student)
    before_course = deepcopy(course)

    outcome = withdraw_course(student, course)

    assert outcome is False
    assert student == before_student
    assert course == before_course
