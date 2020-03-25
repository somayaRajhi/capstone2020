"""
Implementation of In-Progress class
"""
from c20_server import job_queue_errors


class InProgress:

    def __init__(self):
        self.assigned_jobs = {}

    def assign(self, job, user_id):
        self.assigned_jobs[user_id] = job

    def unassign(self, user_id):
        if user_id not in self.assigned_jobs.keys():
            raise job_queue_errors.UnassignInvalidDataException
        job = self.assigned_jobs[user_id]
        del self.assigned_jobs[user_id]
        return job

    def get_num_assigned_jobs(self):
        return len(self.assigned_jobs)
