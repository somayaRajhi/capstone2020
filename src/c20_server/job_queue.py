
"""
implementation of Job_Queue class

"""
from c20_server import job_queue_errors


class JobQueue:

    def __init__(self):
        self.unassigned_jobs_list = []

    def add_job(self, job):
        self.unassigned_jobs_list.append(job)

    def get_job(self):
        if len(self.unassigned_jobs_list) == 0:
            raise job_queue_errors.NoJobsAvailableException
        return self.unassigned_jobs_list.pop(0)

    def get_num_unassigned_jobs(self):
        return len(self.unassigned_jobs_list)
