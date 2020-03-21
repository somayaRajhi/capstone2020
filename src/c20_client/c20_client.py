
import requests
def do_job():
    try:
        job = requests.get('http://capstone.cs.moravian.edu/get_job')
        job=job.json()
        url=job['url']
        job_type = job['job_type']
    except Exception as e:
        print(e)
    if job_type == 'documents':
        requests.get(url)
    elif job_type=='docket':
        requests.get(url)
    elif job_type=='document':
        requests.get(url)
    elif job_type=='download':
        requests.get(url)
    elif job_type == 'none':
        requests.get(url)
    requests.post('http://capstone.cs.moravian.edu')