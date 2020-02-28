from c20_server.PostEndpoint import app
import pytest
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_empty_json(client):
    result = client.get('/empty_json')
    assert result.status_code == 200


def test_get_job_success(client):
    result = client.get('/get_job?client_id=soma')
    assert result.status_code == 200


def test_get_job_fail(client):
    result = client.get('/get_job?client_id=bas_id')
    assert result.status_code == 403


def test_return_result_success(client):
    result = client.post('/return_result', data={'name': 'foo'})
    assert result.status_code == 200


def test_return_result_fail(client):
    result = client.post('/return_result')
    assert result.status_code == 400
