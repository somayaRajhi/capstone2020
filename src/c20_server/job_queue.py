
"""
implementation of Job_Queue class

"""
from c20_server.job import Job
from c20_server import job_queue_errors


class JobQueue:
    """
    Job Queue class.
    """
    unsigned_jobs_list = []
    job = Job

    def add_job(self, job):
        """
        Add a new job to the unassigned_jobs_list.
        """
        self.unsigned_jobs_list.append(job)

    def get_job(self):
        """
        Get a job from the unassigned_jobs_list, and then return it. If there is no jobs available
        raise an Exception.
        """
        if not self.unsigned_jobs_list:
            raise job_queue_errors.NoJobsAvailableException
        return self.unsigned_jobs_list.pop(0)

    def get_num_unsigned_jobs(self):
        """
        Get the number of jobs in the unassigned_jobs_list, and then return it.
        """
        return len(self.unsigned_jobs_list)
