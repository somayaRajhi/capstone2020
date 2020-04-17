"""
Implementation of In-Progress class
"""
import pickle
from c20_server import job_queue_errors


class InProgress:

    def __init__(self, database):
        self.r_database = database

    def assign(self, job, user_id):
        job = pickle.dumps(job)
        self.r_database.hset('assigned_jobs', user_id, job)

    def unassign(self, user_id):
        if not self.r_database.hexists('assigned_jobs', user_id):
            raise job_queue_errors.UnassignInvalidDataException
        job = self.r_database.hget('assigned_jobs', user_id)
        self.r_database.hdel('assigned_jobs', user_id)
        job = pickle.loads(job)
        return job

    def get_num_assigned_jobs(self):
        return self.r_database.hlen('assigned_jobs')
