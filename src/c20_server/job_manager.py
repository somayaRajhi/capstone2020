from c20_server.job_queue import JobQueue
from c20_server.in_progress import InProgress


class JobManager:

    @staticmethod
    def add_job(job):
        JobQueue().add_job(job)

    @staticmethod
    def request_job(user):
        job = JobQueue().get_job()
        InProgress().assign(job, user)

    @staticmethod
    def report_success(user, job):
        InProgress().unassign(job, user)

    @staticmethod
    def report_failure(user, job):
        InProgress().unassign(job, user)
        JobQueue().add_job(job)

    @staticmethod
    def reset_stale_job():
        return

    @staticmethod
    def num_assigned():
        return InProgress().get_num_assigned_jobs()

    @staticmethod
    def num_unassigned():
        return JobQueue().get_num_unassigned_jobs()
