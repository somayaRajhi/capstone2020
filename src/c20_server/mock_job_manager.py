from c20_server.job_manager import JobManager


class MockJobManager(JobManager):

    def __init__(self):
        super().__init__()
        self.request_job_called = False
        self.add_job_called = False

    def request_job(self, user):
        self.request_job_called = True
        return super().request_job(user)

    def add_job(self, job):
        self.add_job_called = True
        super().add_job(job)
