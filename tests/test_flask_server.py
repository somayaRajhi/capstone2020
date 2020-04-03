import json
import pytest
from c20_server.flask_server import APP


@pytest.fixture(name='client')
def client_fixture():
    APP.config['TESTING'] = True
    return APP.test_client()


def test_get_job(client):
    response = client.get('/get_job')
    assert response.status_code == 200
    assert response.data == b'{"end_date":"04-01-2020","job_id":"1","page_offset":"0","start_date":"04-01-2020"}\n'


def test_return_result_success(client):
    json_data = {'title': u'foo'}
    result = client.post('/return_result', data=json.dumps(json_data),
                         content_type='application/json')
    assert result.status_code == 200


def test_return_result_empty_data(client):
    result = client.post('/return_result', data={})
    assert result.status_code == 400
