import requests_mock
import json
import pytest
from c20_client.client import do_job
from c20_client.connection_error import NoConnectionError
from c20_client.get_documents import get_documents



def test_client_calls_documents_endpoint_for_documents_job():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'documents',
                       "url": 'https://api.data.gov:443/regulations/v3/documents=abc'})
        documents_response=get_documents('VALID KEY', '1000', '11/06/13', "03/06/14")
        mock.get('https://api.data.gov:443/regulations/v3/documents.json?api_key=',
                 json={"result":json.dumps()})
        mock.post('http://capstone.cs.moravian.edu',
                  data={})

        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_client_calls_document_endpoint_for_document_job():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'document',
                       "url": "https://api.data.gov/json?documentid=abc"})
        mock.get('https://api.data.gov/json?documentid=abc',
                 json={})
        mock.post('http://capstone.cs.moravian.edu',
                  json={})
        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_client_calls_docket_endpoint_for_docket_job():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'docket',
                       "url": "https://api.data.gov/json?docketid=abc"})
        mock.get('https://api.data.gov/json?docketid=abc',
                 json={})
        mock.post('http://capstone.cs.moravian.edu',
                  json={})
        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_client_calls_download_endpoint_for_download_job():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'download',
                       "url": "https://api.data.gov/json?download=abc"})
        mock.get('https://api.data.gov/json?download=abc',
                 json={})
        mock.post('http://capstone.cs.moravian.edu',
                  json={})
        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_client_got_bad_job_from_server():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'none',
                       "url": "https://api.data.gov/json?"})
        mock.get('https://api.data.gov/json?',
                 json={})
        mock.post('http://capstone.cs.moravian.edu',
                  json={})
        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_no_connection_made_to_server():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 exc=True)

        with pytest.raises(NoConnectionError):
            do_job()
