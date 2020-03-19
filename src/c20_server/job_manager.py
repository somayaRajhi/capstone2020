from c20_server.job_queue import JobQueue


class JobManager:

    @staticmethod
    def add_job(job):
        JobQueue().add_job(job)

    @staticmethod
    def request_job(user):
        return JobQueue().get_job()

    def report_success(self, user, job):
        return

    def report_failure(self, user, job):
        return

    def reset_stale_job(self):
        return

    def num_assigned(self):
        return

    def num_unassigned(self):
        return
