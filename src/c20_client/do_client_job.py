import time
import requests

from c20_client.client_logger import LOGGER

from c20_client.connection_error import NoConnectionError
from c20_client.do_wait import get_wait_time
from c20_client.client_decide_call import handle_specific_job


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

    results = handle_specific_job(job, api_key)

    if results is None:
        return

    LOGGER.info("Packaging Successful")
    LOGGER.info("Posting data to server")
    requests.post('http://capstone.cs.moravian.edu/return_result',
                  json=results)
    LOGGER.info("Data successfully posted to server!")


def do_multiple_job(api_key):
    """
       Gets multiple job from the server
       and handles the job based on the type of job
    """
    try:
        print("Getting job...\n")
        while True:
            do_job(api_key)
            time.sleep(get_wait_time())

    except Exception:
        raise NoConnectionError
