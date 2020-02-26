


from c20_server.PostEndpoint import app


def empty_json():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/empty_json')
    assert result.status_code == 200

def get_job_success():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/get_job')
    assert result.status_code == 200

def get_job_unsuccess():
        app.config['TESTING'] = True
        client = app.test_client()

        result = client.get('/get_job')
        assert result.status_code == 404
