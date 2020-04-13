from flask import Flask, request
from c20_server.job_manager import JobManager
from c20_server.user import User


def create_app(job_manager):
    app = Flask(__name__)

    @app.route('/get_job')
    def get_job():
        requested_job = job_manager.request_job(User(100))
        if requested_job.job_id < 0:
            return {'job_type': 'none'}

        # Translate Job - Will be in Job Translator
        job = {'job_id': requested_job.job_id,
               'page_offset': requested_job.page_offset,
               'start_date': requested_job.start_date,
               'end_date': requested_job.end_date}
        #
        return job

    @app.route('/return_result', methods=['POST'])
    def return_result():
        json_data = request.json
        if json_data is None:
            return{}, 400
        # Send result to job translator

        # Send jobs to Job Manager
        # Send data to Data Manager
        return json_data, 200
    return app
