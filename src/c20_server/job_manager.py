import pickle
from c20_server.job_queue import JobQueue
from c20_server.in_progress import InProgress
from c20_server.job import NoneJob


class JobManager:

    def __init__(self, database):
        self.r_database = database
        self.job_queue = JobQueue(self.r_database)
        self.in_progress_jobs = InProgress(self.r_database)

    def add_job(self, job):
        self.job_queue.add_job(job)

    def request_job(self, user):
        if self.num_unassigned() == 0:
            return NoneJob(-1)
        job = self.job_queue.get_job()
        self.in_progress_jobs.assign(job, user.user_id)
        return job

    def report_success(self, user):
        self.in_progress_jobs.unassign(user.user_id)

    def report_failure(self, user):
        job = self.in_progress_jobs.unassign(user.user_id)
        self.job_queue.add_job(job)

    def reset_stale_job(self, time_to_expire):
        for user in self.r_database.hgetall('assigned_jobs'):
            job_info = self.r_database.hget('assigned_jobs', user)
            time_, job = pickle.loads(job_info)
            if time_ < time_to_expire:
                job = self.in_progress_jobs.unassign(user)
                self.job_queue.add_job(job)

    def num_assigned(self):
        return self.in_progress_jobs.get_num_assigned_jobs()

    def num_unassigned(self):
        return self.job_queue.get_num_unassigned_jobs()
