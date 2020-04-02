
class Job:

    def __init__(self, job_id):
        self.job_id = job_id


class DocumentsJob(Job):

    def __init__(self, job_id, page_offset, start_date, end_date):
        super().__init__(job_id)
        self.page_offset = page_offset
        self.start_date = start_date
        self.end_date = end_date
