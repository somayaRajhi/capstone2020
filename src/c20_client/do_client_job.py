import argparse
import requests

from c20_client.client_logger import LOGGER

from c20_client.connection_error import NoConnectionError
from c20_client.client import get_result_for_job
from c20_client.do_wait import wait_between_jobs


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
            wait_between_jobs()

    except Exception:
        raise NoConnectionError


def main():
    parser = argparse.ArgumentParser(
        description="get files from regulations.gov")
    parser.add_argument("API_key", help="api key for regulations.gov")
    args = parser.parse_args()
    do_multiple_job(args.API_key)


if __name__ == '__main__':
    main()
