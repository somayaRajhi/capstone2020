
"""
implementation of Job_Queue class

"""


class JobQueue:
    """
    Job Queue class.
    """
    unsigned_jobs_list = []

    def add_job(self, job_id):
        """
        add a new job to the unsigned_jobs_list.
        """
        self.unsigned_jobs_list.append(job_id)

    def get_job(self):
        """
        Get a job from the unsigned_jobs_list, and then return it.
        """
        return self.unsigned_jobs_list.pop()

    def get_num_unsigned_jobs(self):
        """
        Get the number of jobs in the unsigned_jobs_list, and then return it.
        """
        return len(self.unsigned_jobs_list)
