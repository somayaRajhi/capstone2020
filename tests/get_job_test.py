from c20_server.get_job import app


def test_connection():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_getJob():
    response = app.test_client().get('/')
    assert response.data == b'{"docketId":"CMS-2014-0115"}\n'


def test_url():
    response2 = app.test_client().get('/job/')
    assert response2.status_code == 404


def test_user():
    response3 = app.test_client().get('/request/CMS')
    assert response3.data == b'{"Success":"Access Granted"}\n'


