from flask import Flask, request
from c20_server.job_manager import JobManager
from c20_server.user import User


def create_app():
    app = Flask(__name__)
    job_manager = JobManager()
    job = {"end_date": "04-01-2020", "job_id": "1", "page_offset": "0", "start_date": "04-01-2020"}
    job2 = {"end_date": "04-01-2020", "job_id": "2", "page_offset": "0", "start_date": "04-01-2020"}
    job_manager.add_job(job)
    job_manager.add_job(job2)

    @app.route('/get_job')
    def get_job():
        requested_job = job_manager.request_job(User(100))
        # Translate Job
        return requested_job

    @app.route('/return_result', methods=['POST'])
    def return_result():
        # Get result from client
        # Translate result
        # Return jobs to Job Manager
        json_data = request.json
        if json_data is None:
            return{}, 400
        return json_data, 200
    return app
