from c20_server.get_job import app
import pytest


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_get_job(client):
    response = client.get('/get_job')
    assert response.status_code == 200
    assert response.data == b'{"docketId":"CMS-2014-0115"}\n'




