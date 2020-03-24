"""
Implementation of In-Progress class
"""
from c20_server import job_queue_errors


class InProgress:

    def __init__(self):
        self.assigned_jobs_list = []

    def assign(self, job, user):
        self.assigned_jobs_list.append((job, user))

    def unassign(self, job, user):
        if (job, user) not in self.assigned_jobs_list:
            raise job_queue_errors.UnassignInvalidDataException
        self.assigned_jobs_list.remove((job, user))

    def get_num_assigned_jobs(self):
        return len(self.assigned_jobs_list)
