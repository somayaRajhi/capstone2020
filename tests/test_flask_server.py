import json
import pytest
from c20_server.flask_server import create_app
from c20_server.mock_job_manager import MockJobManager
from c20_server.job import DocumentsJob


@pytest.fixture(name='manager')
def job_manager_fixture():
    job_manager = MockJobManager()
    job = DocumentsJob(job_id=1, page_offset=0, start_date='03-01-2020',
                       end_date='04-01-2020')
    job_manager.add_job(job)
    return job_manager


@pytest.fixture(name='client')
def client_fixture(manager):
    app = create_app(manager)
    app.config['TESTING'] = True
    return app.test_client()


def test_return_result_success():
    mock_job_manager = MockJobManager()
    app = create_app(mock_job_manager)
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
    assert mock_job_manager.add_job_called
    assert mock_job_manager.num_unassigned() == 1


def test_return_result_empty_data(client):
    result = client.post('/return_result', data={})
    assert result.status_code == 400


def test_single_job_return():
    mock_job_manager = MockJobManager()
    mock_job_manager.add_job(DocumentsJob(job_id=1, page_offset=0,
                                          start_date='03-01-2020',
                                          end_date='04-01-2020'))
    app = create_app(mock_job_manager)
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/get_job')
    assert mock_job_manager.request_job_called
    assert result.data == b'{"job_id": 1,' \
                          b' "page_offset": 0,' \
                          b' "start_date": "03-01-2020",' \
                          b' "end_date": "04-01-2020",' \
                          b' "job_type": "documents"}'


def test_none_job_return_when_no_job():
    mock_job_manager = MockJobManager()
    app = create_app(mock_job_manager)
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/get_job')
    assert mock_job_manager.request_job_called
    job = json.loads(result.data)
    assert job['job_type'] == 'none'
