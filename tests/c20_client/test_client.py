import requests_mock
from c20_client.c20_client import do_job


def test_client_calls_decuments_endpoint_for_documents_job():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job', json={'job_type': 'documents'
                    ,"url":"https://api.data.gov/json?documents=abc"})
        mock.get('https://api.data.gov/json?documents=abc', json = {'documents':'abc'})
        mock.post('http://capstone.cs.moravian.edu', json={})
        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url

def test_client_calls_decument_endpoint_for_document_job():
            with requests_mock.Mocker() as mock:
                mock.get('http://capstone.cs.moravian.edu/get_job', json={'job_type': 'document'
                    ,"url":"https://api.data.gov/json?documentid=abc"})
                mock.get('https://api.data.gov/json?documentid=abc', json={})
                mock.post('http://capstone.cs.moravian.edu', json={})
                do_job()
                history = mock.request_history

                assert len(history) == 3
                assert 'capstone' in history[0].url
                assert 'api.data.gov' in history[1].url
                assert 'capstone' in history[2].url

def test_client_calls_docket_endpoint_for_docket_job():
            with requests_mock.Mocker() as mock:
                mock.get('http://capstone.cs.moravian.edu/get_job', json={'job_type': 'docket'
                            , "url": "https://api.data.gov/json?docketid=abc"})
                mock.get('https://api.data.gov/json?docketid=abc', json={})
                mock.post('http://capstone.cs.moravian.edu', json={})
                do_job()
                history = mock.request_history

                assert len(history) == 3
                assert 'capstone' in history[0].url
                assert 'api.data.gov' in history[1].url
                assert 'capstone' in history[2].url

def test_client_calls_download_endpoint_for_download_job():
            with requests_mock.Mocker() as mock:
                mock.get('http://capstone.cs.moravian.edu/get_job', json={'job_type': 'download'
                        , "url": "https://api.data.gov/json?download=abc"})
                mock.get('https://api.data.gov/json?download=abc', json={})
                mock.post('http://capstone.cs.moravian.edu', json={})
                do_job()
                history = mock.request_history

                assert len(history) == 3
                assert 'capstone' in history[0].url
                assert 'api.data.gov' in history[1].url
                assert 'capstone' in history[2].url

def test_client_got_bad_job_from_server():
            with requests_mock.Mocker() as mock:
                mock.get('http://capstone.cs.moravian.edu/get_job', json={'job_type': 'none'
                            , "url": "https://api.data.gov/json?"})
                mock.get('https://api.data.gov/json?', json={})
                mock.post('http://capstone.cs.moravian.edu', json={})
                do_job()
                history = mock.request_history

                assert len(history) == 3
                assert 'capstone' in history[0].url
                assert 'api.data.gov' in history[1].url
                assert 'capstone' in history[2].url