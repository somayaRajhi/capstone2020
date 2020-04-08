import json
import uuid
from c20_server import job_translator_errors
from c20_server.job import DocumentsJob

DOCUMENTS = "documents"
DOCUMENT = "document"
DOCKET = "docket"
DOWNLOAD = "download"
NONE = "none"


def job_to_json(job_object):
    job_type = "none"
    if isinstance(job_object, DocumentsJob):
        job_type = DOCUMENTS
    return encode_job(job_type, job_object)


def encode_job(job_type, job_object):
    json_data = job_object._asdict()
    if job_type == DOCUMENTS:
        json_data["job_type"] = "documents"
    json_job = json.dumps(json_data)
    return json_job


def handle_jobs(json_data):
    """
    handle_jobs will take the return result json from client and split it up
    into multiple json objects that get sent to json_to_job
    """

    job_list = []

    try:
        json_data = json.loads(json_data)
    except TypeError:
        return {}

    json_jobs = json_data["jobs"]

    index = 0
    while index < len(json_jobs):
        job = json_to_job(json_jobs[index])
        job_list.append(job)
        index += 1
    return job_list


def json_to_job(json_job):
    job_id = str(uuid.uuid4())
    json_job["job_id"] = job_id
    job_type = json_job["job_type"]

    if job_type == DOCUMENTS:
        page_offset = json_job["page_offset"]
        start_date = json_job["start_date"]
        end_date = json_job["end_date"]
        return DocumentsJob(job_id, page_offset, start_date, end_date)

    raise job_translator_errors.UnrecognizedJobTypeException
