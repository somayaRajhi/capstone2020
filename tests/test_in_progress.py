
"""
Test class for In-Progress Class.
"""
import pytest
from c20_server import job_queue_errors
from c20_server.job import Job
from c20_server.user import User
from c20_server.in_progress import InProgress


JOB1 = Job(123)
USER1 = User(1)
IN_PROGRESS_JOBS = InProgress()


@pytest.fixture(name='in_progress')
def make_in_progress():
    return InProgress()


def test_new_instance_empty(in_progress):
    assert in_progress.get_num_assigned_jobs() == 0


def test_when_job_assigned_it_is_added_to_assigned_jobs(in_progress):
    in_progress.assign(Job(1), User(100))
    assert in_progress.get_num_assigned_jobs() == 1


def test_no_assigned_jobs():
    assert IN_PROGRESS_JOBS.get_num_assigned_jobs() == 0


def test_assign_one_job():
    assert IN_PROGRESS_JOBS.get_num_assigned_jobs() == 0
    IN_PROGRESS_JOBS.assign(JOB1, USER1)
    assert IN_PROGRESS_JOBS.get_num_assigned_jobs() == 1


def test_unassign_invalid_job():
    invalid_job = Job(222)
    with pytest.raises(job_queue_errors.UnassignInvalidDataException):
        IN_PROGRESS_JOBS.unassign(invalid_job, USER1)


def test_unassign_invalid_user():
    invalid_user = User(66)
    with pytest.raises(job_queue_errors.UnassignInvalidDataException):
        IN_PROGRESS_JOBS.unassign(JOB1, invalid_user)


def test_unassign_one_job():
    assert IN_PROGRESS_JOBS.get_num_assigned_jobs() == 1
    IN_PROGRESS_JOBS.unassign(JOB1, USER1)
    assert IN_PROGRESS_JOBS.get_num_assigned_jobs() == 0
