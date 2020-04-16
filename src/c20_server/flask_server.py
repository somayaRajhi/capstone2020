import json
from flask import Flask, request
from c20_server.user import User
from c20_server.job_translator import job_to_json, handle_jobs


def create_app(job_manager):
    app = Flask(__name__)

    # Note: endpoint names begin with an "_" so that Pylint does not complain
    # about unused functions.

    @app.route('/get_job')
    def _get_job():
        requested_job = job_manager.request_job(User(100))
        if requested_job.job_id < 0:
            return {'job_type': 'none'}
        job = job_to_json(requested_job)
        return job

    @app.route('/return_result', methods=['POST'])
    def _return_result():
        client_data = request.json
        if client_data is None:
            return {}, 400

        json_data = json.dumps(client_data)
        job_list = handle_jobs(json_data)
        for job in job_list:
            job_manager.add_job(job)
        return {}, 200
    return app
