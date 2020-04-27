import json
from unittest.mock import patch
import fakeredis
import pytest
from c20_server.flask_server import create_app, redis_connect
from c20_server.mock_job_manager import MockJobManager
from c20_server.job import DocumentsJob


def make_redis_database():
    r_database = fakeredis.FakeRedis()
    r_database.flushall()
    return r_database


@pytest.fixture(name='job_manager')
def job_manager_fixture():
    r_database = make_redis_database()
    job_manager = MockJobManager(r_database)
    return job_manager


@pytest.fixture(name='client')
def client_fixture(job_manager):
    app = create_app(job_manager)
    app.config['TESTING'] = True
    return app.test_client()


def test_return_result_success(job_manager):
    app = create_app(job_manager)
    app.config['TESTING'] = True
    client = app.test_client()

    json_data = {
        'client_id': 'client1',
        'job_id': 'job1',
        'data': [
            {
                'folder_name': 'thisisafoldername',
                'file_name': 'thisisafilename',
                'data': {}
            }
        ],
        'jobs': [
            {
                'job_type': 'documents',
                'job_id': 'thisiajobid',
                'page_offset': 'thisiapageoffset',
                'start_date': 'thisisastartdate',
                'end_date': 'thisisanenddate'
            },
        ]
    }
    result = client.post('/return_result', data=json.dumps(json_data),
                         content_type='application/json')
    assert result.status_code == 200
    assert job_manager.add_job_called
    assert job_manager.num_unassigned() == 1


def test_return_result_empty_data(client):
    result = client.post('/return_result', data={})
    assert result.status_code == 400


def test_single_job_return(job_manager):
    job_manager.add_job(DocumentsJob(job_id=1, page_offset=0,
                                     start_date='03-01-2020',
                                     end_date='04-01-2020'))
    app = create_app(job_manager)
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/get_job')
    assert job_manager.request_job_called
    assert result.data == b'{"job_id": 1,' \
                          b' "page_offset": 0,' \
                          b' "start_date": "03-01-2020",' \
                          b' "end_date": "04-01-2020",' \
                          b' "job_type": "documents"}'


def test_none_job_return_when_no_job(job_manager):
    app = create_app(job_manager)
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/get_job')
    assert job_manager.request_job_called
    job = json.loads(result.data)
    assert job['job_type'] == 'none'


def test_report_one_job_as_failure(job_manager):
    job_manager.add_job(DocumentsJob(job_id=1, page_offset=0,
                                     start_date='03-01-2020',
                                     end_date='04-01-2020'))
    app = create_app(job_manager)
    app.config['TESTING'] = True
    client = app.test_client()
    assert job_manager.num_unassigned() == 1

    client.get('/get_job')
    assert job_manager.request_job_called
    assert job_manager.num_unassigned() == 0

    json_data = {
        'client_id': 100,
        'job_id': 0,
        'client_message': 'Regulations.gov API is not working.'
    }
    result = client.post('/report_failure', data=json.dumps(json_data),
                         content_type='application/json')
    assert result.status_code == 200
    assert job_manager.num_unassigned() == 1


def test_run_server_with_no_redis_connection():
    with patch('sys.exit') as exit_server:
        redis_connect()
        assert exit_server.called
