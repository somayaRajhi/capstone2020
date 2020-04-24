import time
import argparse
import requests

from c20_client.client_logger import LOGGER

from c20_client.connection_error import NoConnectionError
from c20_client.client import get_result_for_job

# WAITING_TIME_FOR_EACH_CALL = (60 mins * 60 seconds)/1000 = 3.66
WAITING_TIME_FOR_EACH_CALL = 3.66


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
            time.sleep(WAITING_TIME_FOR_EACH_CALL)

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
