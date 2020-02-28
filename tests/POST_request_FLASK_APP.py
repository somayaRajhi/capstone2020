from src.c20_server.POST_request import app

result = app.test_client().get('/json')


def test_json():

    assert 200 in result.data


