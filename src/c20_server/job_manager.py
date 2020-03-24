from c20_server.job_queue import JobQueue
from c20_server.in_progress import InProgress


class JobManager:

    def __init__(self):
        self.job_queue = JobQueue()
        self.in_progress_jobs = InProgress()

    def add_job(self, job):
        self.job_queue.add_job(job)

    def request_job(self, user):
        job = self.job_queue.get_job()
        self.in_progress_jobs.assign(job, user)

    def report_success(self, user, job):
        self.in_progress_jobs.unassign(job, user)

    def report_failure(self, user, job):
        self.in_progress_jobs.unassign(job, user)
        self.job_queue.add_job(job)

    @staticmethod
    def reset_stale_job():
        return

    def num_assigned(self):
        return self.in_progress_jobs.get_num_assigned_jobs()

    def num_unassigned(self):
        return self.job_queue.get_num_unassigned_jobs()
