from c20_server.get_job import app
import pytest


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_connection(client):
    response = client.get('/')
    assert response.status_code == 200


def test_get_job(client):
    response = client.get('/')
    assert response.data == b'{"docketId":"CMS-2014-0115"}\n'


def test_url(client):
    response = client.get('/job/')
    assert response.status_code == 404


def test_user(client):
    response = client.get('/request/CMS')
    assert response.data == b'{"Success":"Access Granted"}\n'


