"""
Gets a job from the server and handles the job based on the type of job
"""
import argparse
import requests
from c20_client.connection_error import NoConnectionError

from c20_client.get_documents import get_documents
from c20_client.get_document import download_document
from c20_client.retrieve_docket import get_docket

from c20_client.documents_packager import package_documents
from c20_client.docket_packager import package_docket
from c20_client.document_packager import package_document

from c20_client.client_logger import LOGGER

CLIENT_ID = '1'


def do_job(api_key):
    """
    Gets a job from the server and handles the job based on the type of job
    """
    try:
        LOGGER.info('Getting job from server...')
        job = requests.get('http://capstone.cs.moravian.edu/get_job')
        job = job.json()
        LOGGER.info("Job has been aquired")

    except Exception:
        LOGGER.error("A connection error has occurred")
        raise NoConnectionError

    get_result_for_job(job, api_key)


def documents_handler(job, api_key):
    job_id = job['job_id']
    data = get_documents(
        api_key,
        job["page_offset"],
        job["start_date"],
        job["end_date"])
    LOGGER.info("Job#%s: Packaging documents...", str(job_id))
    result = package_documents(data, CLIENT_ID, job_id)
    return result


def document_handler(job, api_key):
    job_id = job['job_id']
    data = download_document(
        api_key,
        job['document_id'])
    LOGGER.info("Job#%s: Packaging document...", str(job_id))
    results = package_document(data, CLIENT_ID, job_id)
    return results


def docket_handler(job, api_key):
    job_id = job['job_id']
    data = get_docket(
        api_key,
        job['docket_id'])
    LOGGER.info("Job#%s: Packaging docket..", str(job_id))
    results = package_docket(data, CLIENT_ID, job_id)
    return results


def get_result_for_job(job, api_key):
    """
    Makes request to correct endpoint at reg.gov
    """
    job_id = job['job_id']
    job_type = job['job_type']
    if job_type == 'documents':
        results = documents_handler(job, api_key)

    elif job_type == 'document':
        results = document_handler(job, api_key)

    elif job_type == 'docket':
        results = docket_handler(job, api_key)

    post_job(job_id, results)


def post_job(job_id, results):
    LOGGER.info("Packaging successful!")
    LOGGER.info("Posting Job#%s to server", str(job_id))
    requests.post('http://capstone.cs.moravian.edu/return_result',
                  json=results)
    LOGGER.info("Job#%s has successfully been posted!", str(job_id))


def main():
    parser = argparse.ArgumentParser(
        description="get files from regulations.gov")
    parser.add_argument("API_key", help="api key for regulations.gov")
    args = parser.parse_args()
    do_job(args.API_key)


if __name__ == '__main__':
    main()
