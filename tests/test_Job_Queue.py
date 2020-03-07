
"""
Test class for Job-Queue Class.
"""
from c20_server.Job_Queue import JobQueue


def test_add_job_():
    """
    Test for adding a new Job to the Job_Queue.
    """
    job_id = 6032020
    job_queue = JobQueue()

    assert job_queue.get_num_unsigned_jobs() == 0
    job_queue.add_job(job_id)
    assert job_queue.get_num_unsigned_jobs() == 1


def test_get_job_():
    """
    Test for getting a Job from the Job_Queue.
    """
    job_queue = JobQueue()
    assert job_queue.get_job() == 6032020
    assert job_queue.get_num_unsigned_jobs() == 0
