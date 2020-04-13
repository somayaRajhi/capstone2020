import pytest
from c20_server.job_manager import JobManager
from c20_server.job import Job
from c20_server.user import User


@pytest.fixture(name='job_manager')
def make_job_manager():
    return JobManager()


@pytest.fixture(name='job1')
def make_first_job():
    return Job(1)


@pytest.fixture(name='job2')
def make_second_job():
    return Job(2)


@pytest.fixture(name='user1')
def make_first_user():
    return User(100)


@pytest.fixture(name='user2')
def make_second_user():
    return User(101)


def test_new_instance_is_empty(job_manager):
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 0


def test_when_job_added_it_goes_into_unassigned(job_manager, job1, user1):
    job_manager.add_job(job1)
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 1
    j = job_manager.request_job(user1)
    assert j.job_id == 1


def test_when_job_requested_it_moves_to_assigned(job_manager, job1, user1):
    job_manager.add_job(job1)
    job_manager.request_job(user1)
    assert job_manager.num_assigned() == 1
    assert job_manager.num_unassigned() == 0


def test_successful_job_is_removed_from_manager(job_manager, job1, user1):
    job_manager.add_job(job1)
    job_manager.request_job(user1)
    job_manager.report_success(user1)
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 0


def test_failed_job_is_moved_back_to_unassigned(job_manager, job1, user1):
    job_manager.add_job(job1)
    job_manager.request_job(user1)
    job_manager.report_failure(user1)
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 1


def test_adding_multiple_jobs_into_unassigned(job_manager, job1, job2):
    job_manager.add_job(job1)
    job_manager.add_job(job2)
    assert job_manager.num_assigned() == 0
    assert job_manager.num_unassigned() == 2


def test_multiple_jobs_move_to_assigned(job_manager, job1, user1, user2):
    job_manager.add_job(job1)
    job_manager.add_job(Job(2))
    job_manager.request_job(user1)
    job_manager.request_job(user2)
    assert job_manager.num_assigned() == 2
    assert job_manager.num_unassigned() == 0


def test_empty_job_queue_gives_none(job_manager, user1):
    job = job_manager.request_job(user1)
    assert job.job_id == -1

# stale job
