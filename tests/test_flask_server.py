import json
import pytest
from c20_server.flask_server import create_app


@pytest.fixture(name='client')
def client_fixture():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_get_job(client):
    response = client.get('/get_job')
    assert response.status_code == 200
    assert response.data == b'{"end_date":"04-01-2020","job_id":"1","page_offset":"0","start_date":"04-01-2020"}\n'
    response = client.get('/get_job')
    assert response.status_code == 200
    assert response.data == b'{"end_date":"04-01-2020","job_id":"2","page_offset":"0","start_date":"04-01-2020"}\n'


def test_return_result_success(client):
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


def test_return_result_empty_data(client):
    result = client.post('/return_result', data={})
    assert result.status_code == 400
