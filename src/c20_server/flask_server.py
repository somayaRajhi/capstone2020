from flask import Flask, request
from c20_server.job_manager import JobManager
from c20_server.user import User


APP = Flask(__name__)


@APP.route('/get_job')
def get_job():
    job_manager = JobManager()
    job = {"end_date": "04-01-2020", "job_id": "1", "page_offset": "0", "start_date": "04-01-2020"}
    job_manager.add_job(job)
    requested_job = job_manager.request_job(User(100))
    # Translate Job
    return requested_job


@APP.route('/return_result', methods=['POST'])
def return_result():
    # Get result from client
    # Translate result
    # Return jobs to Job Manager
    json_data = request.json
    if json_data is None:
        return{}, 400
    return {}, 200
