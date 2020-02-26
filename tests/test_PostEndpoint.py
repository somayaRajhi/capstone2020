


from c20_server.PostEndpoint import app


def empty_json():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/empty_json')
    assert result.status_code == 200
