import json
import uuid
from collections import namedtuple
from c20_server import job_translator_errors
from c20_server.job import DocumentsJob, DocumentJob, DocketJob, DownloadJob

DOCUMENTS = "documents"
DOCUMENT = "document"
DOCKET = "docket"
DOWNLOAD = "download"


def job_to_json(job_object):
    job_type = ""

    if isinstance(job_object, DocumentsJob):
        job_type = DOCUMENTS
    elif isinstance(job_object, DocumentJob):
        job_type = DOCUMENT
    elif isinstance(job_object, DocketJob):
        job_type = DOCKET
    elif isinstance(job_object, DownloadJob):
        job_type = DOWNLOAD

    return encode_job(job_type, job_object)


def encode_job(job_type, job_object):
    json_data = job_object._asdict()
    json_data["job_type"] = job_type
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
    Record = namedtuple('Record', 'job_id job_type')
    input_array_line = [job_id, job_type]
    record = Record(*input_array_line)

    return add_specific_job_data(record, json_job)


def add_specific_job_data(record, json_job):
    if record.job_type == DOCUMENTS:
        page_offset = json_job["page_offset"]
        start_date = json_job["start_date"]
        end_date = json_job["end_date"]
        return DocumentsJob(record.job_id, page_offset, start_date, end_date)

    if record.job_type == DOCUMENT:
        document_id = json_job["document_id"]
        return DocumentJob(record.job_id, document_id)

    if record.job_type == DOCKET:
        docket_id = json_job["docket_id"]
        return DocketJob(record.job_id, docket_id)

    if record.job_type == DOWNLOAD:
        url = json_job["url"]
        return DownloadJob(record.job_id, url)

    raise job_translator_errors.UnrecognizedJobTypeException
