from c20_server.job_manager import JobManager
from c20_server.job import Job
from c20_server.user import User


job1 = Job(1)
job2 = Job(2)
user1 = User(5)
user2 = User(11)


def test_no_unassigned_jobs():
    assert JobManager().num_unassigned() == 0


def test_no_assigned_jobs():
    assert JobManager().num_assigned() == 0


def test_add_first_job():
    JobManager().add_job(job1)
    assert JobManager().num_unassigned() == 1


def test_add_second_job():
    JobManager().add_job(job2)
    assert JobManager().num_unassigned() == 2


def test_request_job():
    JobManager().request_job(user1)
    assert JobManager().num_unassigned() == 1


def test_one_in_progress_job():
    assert JobManager().num_assigned() == 1


def test_one_unassigned_job_after_request():
    assert JobManager().num_unassigned() == 1


def test_request_second_job():
    JobManager().request_job(user2)
    assert JobManager().num_unassigned() == 0


def test_two_assigned_jobs():
    assert JobManager().num_assigned() == 2


def test_one_successful_job():
    JobManager().report_success(user1, job1)
    assert JobManager().num_assigned() == 1


def test_one_failed_job():
    JobManager().report_failure(user2, job2)
    assert JobManager().num_assigned() == 0


def test_one_unassigned_job_after_failure():
    assert JobManager().num_unassigned() == 1


def test_no_jobs_after_second_success():
    JobManager().request_job(user1)
    JobManager().report_success(user1, job2)
    assert JobManager().num_unassigned() == 0
    assert JobManager().num_assigned() == 0
