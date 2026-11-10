# Collaborator task: two withdrawal tests

Your reserved contribution is to implement two requirements-based pytest tests yourself, run them against the unchanged starter, and open a pull request. The design is supplied; the executable tests and your review must be your own contribution.

## Access and branch

Repository: https://github.com/muhammadaaribali/SQE-Assignment-2 (private).

First send your GitHub username to the primary student. They need to arrange your collaborator access; accept the invitation before cloning. An invitation has not yet been sent.

Once access is available:

```bash
git clone https://github.com/muhammadaaribali/SQE-Assignment-2.git
cd SQE-Assignment-2
git switch blackbox-testing
git switch -c collaborator-withdrawal-tests
python -m pip install -r requirements.txt
```

Create or append to `tests/test_blackbox.py`. Keep the primary student's tests intact. Import `Student`, `Course`, and `withdraw_course` from `registration`. Use local setup in each test so your work does not depend on fixtures that are still being developed. Convert the sets specified below into Python sets; the waitlist is a list. Use independent deep copies to check unchanged state.

## BB-072 / STATE-10 / FR-13

Function name: `test_bb_072_withdraw_registered_student`.

Starting student:

- student_id: S001
- completed_courses: {CS101, MATH101}
- current_credits: 15
- outstanding_dues: 0
- registered_courses: {CS100, CS201}

Starting course:

- code: CS201
- credit_hours: 3
- capacity: 30
- enrolled: 30
- prerequisites: {CS101, MATH101}
- waitlist: [S999]

Call `withdraw_course(student, course)` once. Assert that the return is `True`, registered_courses is {CS100}, current_credits is 12, and enrolled is 29. All other fields must remain unchanged. Construct the expected after-state independently from the before-state and compare both complete objects. Do not call register_course to set up this test: that would make a withdrawal test depend on registration behavior.

## BB-073 / STATE-11 / FR-14

Function name: `test_bb_073_withdraw_unregistered_student`.

Use the same data as above except student.current_credits is 12, registered_courses is {CS100}, and course.enrolled is 29. Call `withdraw_course` once. Assert the return is `False` and both complete objects exactly match deep snapshots taken before the call.

## Run and submit your actual results

```bash
python -m pytest tests/test_blackbox.py -k "bb_072 or bb_073" -v
git add tests/test_blackbox.py
git commit -m "test: cover registered and unregistered withdrawal"
git push -u origin collaborator-withdrawal-tests
```

Open a PR with **base: blackbox-testing** and **compare: collaborator-withdrawal-tests**. This keeps your review separate while your tests are integrated into the primary testing branch. In the PR, explain FR-13/FR-14, test IDs, what each test asserts, and the actual test results. Include the command output or a link to the actual run. A failure against the original starter can be legitimate; retain the correct SRS expectation and do not change registration.py or add xfail/skip to hide it.

The primary student reviews your PR. Address any valid feedback with another commit. Later, review the primary student's black-box PR against main: inspect the tests and requirements, leave a specific review based on what you checked, and do not approve without reading. Do not invent feedback just to create activity.

We will record your actual commit/PR/review links in the final report. You should be able to explain why withdrawal changes enrollment, why a failed withdrawal must leave all data unchanged, and why deep snapshots matter.
