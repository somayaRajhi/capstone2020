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

def test_return_result_empty_data(client):
        result = client.post('/return_result',data={})
        assert result.status_code == 400

