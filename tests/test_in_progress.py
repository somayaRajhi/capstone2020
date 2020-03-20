
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


def test_no_assigned_jobs():
    assert InProgress().get_num_assigned_jobs() == 0


def test_assign_one_job():
    assert InProgress().get_num_assigned_jobs() == 0
    InProgress().assign(JOB1, USER1)
    assert InProgress().get_num_assigned_jobs() == 1


def test_unassign_invalid_job():
    invalid_job = Job(222)
    with pytest.raises(job_queue_errors.UnassignInvalidDataException):
        InProgress().unassign(invalid_job, USER1)


def test_unassign_invalid_user():
    invalid_user = User(66)
    with pytest.raises(job_queue_errors.UnassignInvalidDataException):
        InProgress().unassign(JOB1, invalid_user)


def test_unassign_one_job():
    assert InProgress().get_num_assigned_jobs() == 1
    InProgress().unassign(JOB1, USER1)
    assert InProgress().get_num_assigned_jobs() == 0
