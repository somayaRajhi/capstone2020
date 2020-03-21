"""
Gets a job from the server and handles the job based on the type of job
"""
import requests


def do_job():
    """
    Gets a job from the server and handles the job based on the type of job
    """
    try:
        job = requests.get('http://capstone.cs.moravian.edu/get_job')
        job = job.json()
        url = job['url']
        job_type = job['job_type']

    except Exception as exception:
        print(exception)

    if job_type == 'documents':
        requests.get(url)
    elif job_type == 'docket':
        requests.get(url)
    elif job_type == 'document':
        requests.get(url)
    elif job_type == 'download':
        requests.get(url)
    elif job_type == 'none':
        requests.get(url)

    requests.post('http://capstone.cs.moravian.edu')
