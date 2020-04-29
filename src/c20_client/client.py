"""
Gets a job from the server and handles the job based on the type of job
"""
import argparse
import requests
from c20_client.connection_error import NoConnectionError

from c20_client.client_decide_call import handle_specific_job

from c20_client.client_logger import LOGGER
from c20_client import reggov_api_doc_error
from c20_client import connection_error


def do_job(api_key):
    """
    Gets a job from the server and handles the job based on the type of job
    """
    try:
        LOGGER.info('Getting job from server...')
        job = requests.get('http://capstone.cs.moravian.edu/get_job')
        job = job.json()
        LOGGER.info("Job aquired")

    except Exception:
        raise NoConnectionError

    results = handle_specific_job(job, api_key)

    if results is None:
        return

    LOGGER.info("Packaging Successful")
    LOGGER.info("Posting data to server")
    requests.post('http://capstone.cs.moravian.edu/return_result',
                  json=results)
    LOGGER.info("Data successfully posted to server!")


def handling_erorr(URL, massage_report=list()):
    result = requests.get(URL)
    if result.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
        massage_report.append(URL, ":received 400:Bad Requests")
    if result.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
        massage_report.append(URL, ":received 403:Forbidden")
    if result.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
        massage_report.append(URL, ":received 404:Not Found")
    if result.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException
        massage_report.append(URL, ":received 404:Too Many Requests")
    if result.status_code == 503:
        raise connection_error.NoConnectionError
        massage_report.append(URL, "received 503:Service Unavailable Error")
    return result


def main():
    parser = argparse.ArgumentParser(
        description="get files from regulations.gov")
    parser.add_argument("API_key", help="api key for regulations.gov")
    args = parser.parse_args()
    do_job(args.API_key)


if __name__ == '__main__':
    main()
