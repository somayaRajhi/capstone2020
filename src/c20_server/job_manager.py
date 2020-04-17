from c20_server.job_queue import JobQueue
from c20_server.in_progress import InProgress
from c20_server.job import Job


class JobManager:

    def __init__(self):
        self.job_queue = JobQueue()
        self.in_progress_jobs = InProgress()

    def add_job(self, job):
        self.job_queue.add_job(job)

    def request_job(self, user):
        if self.num_unassigned() == 0:
            return Job(-1)
        job = self.job_queue.get_job()
        self.in_progress_jobs.assign(job, user.user_id)
        return job

    def report_success(self, user):
        self.in_progress_jobs.unassign(user.user_id)

    def report_failure(self, user):
        job = self.in_progress_jobs.unassign(user.user_id)
        self.job_queue.add_job(job)

    @staticmethod
    def reset_stale_job():
        return

    def num_assigned(self):
        return self.in_progress_jobs.get_num_assigned_jobs()

    def num_unassigned(self):
        return self.job_queue.get_num_unassigned_jobs()
