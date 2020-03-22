from c20_server.job_manager import JobManager
from c20_server.job import Job
from c20_server.user import User


JOB1 = Job(1)
JOB2 = Job(2)
USER1 = User(5)
USER2 = User(11)


def test_no_unassigned_jobs():
    assert JobManager().num_unassigned() == 0


def test_no_assigned_jobs():
    assert JobManager().num_assigned() == 0


def test_add_first_job():
    JobManager().add_job(JOB1)
    assert JobManager().num_unassigned() == 1


def test_add_second_job():
    JobManager().add_job(JOB2)
    assert JobManager().num_unassigned() == 2


def test_request_job():
    JobManager().request_job(USER1)
    assert JobManager().num_unassigned() == 1


def test_one_in_progress_job():
    assert JobManager().num_assigned() == 1


def test_one_unassigned_job_after_request():
    assert JobManager().num_unassigned() == 1


def test_request_second_job():
    JobManager().request_job(USER2)
    assert JobManager().num_unassigned() == 0


def test_two_assigned_jobs():
    assert JobManager().num_assigned() == 2


def test_one_successful_job():
    JobManager().report_success(USER1, JOB1)
    assert JobManager().num_assigned() == 1


def test_one_failed_job():
    JobManager().report_failure(USER2, JOB2)
    assert JobManager().num_assigned() == 0


def test_one_unassigned_job_after_failure():
    assert JobManager().num_unassigned() == 1


def test_no_jobs_after_second_success():
    JobManager().request_job(USER1)
    JobManager().report_success(USER1, JOB2)
    assert JobManager().num_unassigned() == 0
    assert JobManager().num_assigned() == 0
