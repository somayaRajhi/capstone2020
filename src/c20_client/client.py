"""
Gets a job from the server and handles the job based on the type of job
"""
import requests
from c20_client.connection_error import NoConnectionError
from c20_client.get_documents import get_documents
from c20_client.
CLIENT_ID=1
API_KEY=""
def do_job():
    """
    Gets a job from the server and handles the job based on the type of job
    """
    try:
        job = requests.get('http://capstone.cs.moravian.edu/get_job')
        job = job.json()


    except Exception:
        raise NoConnectionError

    get_result_for_job(job)

    requests.post('http://capstone.cs.moravian.edu')


def get_result_for_job(job):
    """
    Makes request to correct endpoint at reg.gov
    """
    job_id = job['job_id']
    job_type = job['job_type']
    if job_type == 'documents':
       data= get_documents(API_KEY,job["page_offset"],job["start_date"],job["end_date"])
