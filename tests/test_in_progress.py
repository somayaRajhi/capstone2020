
"""
Test class for In-Progress Class.
"""
import pytest
import fakeredis
from c20_server import job_queue_errors
from c20_server.job import Job
from c20_server.user import User
from c20_server.in_progress import InProgress


@pytest.fixture(name='in_progress')
def make_in_progress():
    r_database = fakeredis.FakeRedis()
    r_database.flushall()
    return InProgress(r_database)


def test_new_instance_empty(in_progress):
    assert in_progress.get_num_assigned_jobs() == 0


def test_when_job_assigned_it_is_added_to_assigned_jobs(in_progress):
    in_progress.assign(Job(1), User(100).user_id)
    assert in_progress.get_num_assigned_jobs() == 1


def test_when_job_unassigned_it_is_removed_from_assigned_jobs(in_progress):
    in_progress.assign(Job(1), User(100).user_id)
    assert in_progress.get_num_assigned_jobs() == 1
    in_progress.unassign(User(100).user_id)
    assert in_progress.get_num_assigned_jobs() == 0


def test_when_job_unassigned_it_returned_from_assigned_jobs(in_progress):
    in_progress.assign(Job('job01'), User(100).user_id)
    assert in_progress.get_num_assigned_jobs() == 1
    returned_job = in_progress.unassign(User(100).user_id)
    assert returned_job.job_id == 'job01'
    assert in_progress.get_num_assigned_jobs() == 0


def test_unassign_job_with_invalid_user(in_progress):
    assert in_progress.get_num_assigned_jobs() == 0
    in_progress.assign(Job(1), User(100).user_id)
    invalid_user = User(20)
    with pytest.raises(job_queue_errors.UnassignInvalidDataException):
        in_progress.unassign(invalid_user.user_id)


def test_unassign_invalid_job(in_progress):
    with pytest.raises(job_queue_errors.UnassignInvalidDataException):
        in_progress.unassign(User(100).user_id)
