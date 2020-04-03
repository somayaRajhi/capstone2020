from collections import namedtuple


class Job:

    def __init__(self, job_id):
        self.job_id = job_id


class DocumentsJob(namedtuple('DocumentsJob',
                              ['job_id',
                               'page_offset',
                               'start_date',
                               'end_date']
                              )):
    pass
