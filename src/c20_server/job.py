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


class DocumentJob(namedtuple('DocumentJob',
                             ['job_id',
                              'document_id'])):
    pass


class DocketJob(namedtuple('DocketJob',
                           ['job_id',
                            'docket_id'])):
    pass


class DownloadJob(namedtuple('DownloadJob',
                             ['job_id',
                              'url']
                             )):
    pass
