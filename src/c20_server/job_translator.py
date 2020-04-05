from c20_server import job_translator_errors
from c20_server.job import DocumentsJob
import json

DOCUMENTS = 'documents'
DOCUMENT = 'document'
DOCKET = 'docket'
DOWNLOAD = 'download'

"""
handle_jobs will take the return result json from client and split it up
into multiple json objects that get sent to json_to_job
"""


def handle_jobs(json_data):
    try:
        json_data = json.loads(json_data)
    except TypeError:
        return {}
    json_jobs = json_data['jobs']
    for index in range(len(json_jobs)):
        json_to_job(json_jobs[index])


def json_to_job(json_job):
    job_type = json_job['job_type']
    job_id = json_job['job_id']
    if job_type == DOCUMENTS:
        page_offset = json_job['page_offset']
        start_date = json_job['start_date']
        end_date = json_job['end_date']
        return DocumentsJob(job_id, page_offset, start_date, end_date)
    else:
        raise job_translator_errors.UnrecognizedJobTypeException

