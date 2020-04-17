import json
from flask import Flask, request
from c20_server.user import User
from c20_server.job import DocumentsJob
from c20_server.job_manager import JobManager
from c20_server.job_translator import job_to_json, handle_jobs


def create_app(job_manager):
    app = Flask(__name__)

    # Note: endpoint names begin with an "_" so that Pylint does not complain
    # about unused functions.

    @app.route('/get_job')
    def _get_job():
        print('Server: Requesting Job From Job Queue...\n')
        requested_job = job_manager.request_job(User(100))
        if int(requested_job.job_id) < 0:
            return {'job_type': 'none'}
        else:
            job = job_to_json(requested_job)
        print('Server: Sending Job to client...\n')
        print('Job being sent: ', job, '\n')
        return job

    @app.route('/return_result', methods=['POST'])
    def _return_result():
        print('Receiving Data from Client ...\n')
        client_data = request.json
        print(client_data)
        if client_data is None:
            return {}, 400

        json_data = json.dumps(client_data)
        job_list = handle_jobs(json_data)
        print()
        for job in job_list:
            job_manager.add_job(job)
            print('Adding Job To Job Manager...')
            print(job, '\n')
        return {}, 200
    return app

if __name__ == '__main__':
    job_manager = JobManager()
    job_manager.add_job(DocumentsJob('1', 0, '12/28/19', '1/23/20'))
    app = create_app(job_manager)
    app.run()
