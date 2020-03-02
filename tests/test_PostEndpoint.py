from c20_server.PostEndpoint import app
import pytest
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_return_result_success(client):
        json_data = {'title': u'foo'}
        result = client.post('/return_result', data=json.dumps(json_data), content_type='application/json')
        assert result.status_code == 200

def test_return_result_empty_paramete(client):
        result = client.post('/return_result',data={})
        assert result.status_code == 400

def test_return_result_wrong_parameter(client):
    result = client.post('/return_results/sooo', data={})
    assert result.status_code == 400

def test_return_result_Right_parameter(client):
    result = client.post('/return_results/soma', data={})
    assert result.status_code == 200