"""Requirements-based withdrawal tests: BB-072/FR-13 and BB-073/FR-14."""

from copy import deepcopy

from registration import Course, Student, withdraw_course


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
