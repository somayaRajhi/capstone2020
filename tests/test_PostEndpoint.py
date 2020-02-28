from c20_server.PostEndpoint import app
import pytest
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client



def test_empty_json(client):
    result = client.get('/empty_json')
    assert result.status_code == 200

def test_get_job_success(client):
        result = client.get('get_job?clinet_id=soma')
        assert result.status_code == 200

def test_get_job_unsuccess(client):
        result = client.get('/get_job?clinet_id=bas_id')
        assert result.status_code == 403
