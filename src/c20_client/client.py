"""
Gets a job from the server and handles the job based on the type of job
"""
import argparse
import time

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
        LOGGER.info("Job acquired")

    except Exception:
        raise NoConnectionError

    get_result_for_job(job, api_key)


def do_multiple_job(api_key):
    """
       Gets multiple job from the server
       and handles the job based on the type of job
    """
    try:
        print("Getting job...\n")
        while True:
            do_job(api_key)
            time.sleep(3.66)

    except Exception:
        raise NoConnectionError


def get_result_for_job(job, api_key):
    """
    Makes request to correct endpoint at reg.gov
    """
    job_id = job['job_id']
    job_type = job['job_type']

    if job_type == 'documents':
        data = get_documents(
            api_key,
            job["page_offset"],
            job["start_date"],
            job["end_date"])
        LOGGER.info("Packaging documents data")
        results = package_documents(data, CLIENT_ID, job_id)

    elif job_type == 'document':
        data = download_document(
            api_key,
            job['document_id']
        )
        LOGGER.info("Packaging document data")
        results = package_document(data, CLIENT_ID, job_id)

    elif job_type == 'docket':
        data = get_docket(
            api_key,
            job['docket_id']
        )
        LOGGER.info("Packaging docket data")
        results = package_docket(data, CLIENT_ID, job_id)

    LOGGER.info("Packaging Successful")
    LOGGER.info("Posting data to server")
    requests.post('http://capstone.cs.moravian.edu/return_result',
                  json=results)
    LOGGER.info("Data successfully posted to server!")


def main():
    parser = argparse.ArgumentParser(
        description="get files from regulations.gov")
    parser.add_argument("API_key", help="api key for regulations.gov")
    args = parser.parse_args()
    do_multiple_job(args.API_key)


if __name__ == '__main__':
    main()
