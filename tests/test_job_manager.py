from c20_server.job_manager import JobManager
from c20_server.job import Job
from c20_server.job_queue import JobQueue


def test_add_first_job():
    job1 = Job(1)
    JobManager.add_job(job1)
    assert JobQueue().get_num_unassigned_jobs() == 1


def test_add_second_job():
    job1 = Job(1)
    JobManager.add_job(job1)
    assert JobQueue().get_num_unassigned_jobs() == 2


def test_request_job():
    user = 5
    JobManager.request_job(user)
    assert JobQueue().get_num_unassigned_jobs() == 1
