import requests_mock

import pytest
from c20_client.client import do_job
from c20_client.connection_error import NoConnectionError

CLIENT_ID = 1
JOB_ID = 1
API_KEY = ''
OFFSET = '1000'
START_DATE = '11/06/13'
END_DATE = '03/06/14'
DATE = START_DATE + '-' + END_DATE
URL = "https://api.data.gov/regulations/v3/download?" \
      "documentId=EPA-HQ-OAR-2011-0028-0108&contentType=pdf&" \
      "api_key=" + API_KEY


def test_do_job_documents_endpoint_call():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'documents', "page_offset": OFFSET,
                       'start_date': START_DATE, 'end_date': END_DATE,
                       'job_id': JOB_ID})
        mock.get('https://api.data.gov:443/regulations' +
                 '/v3/documents.json?api_key=' + API_KEY +
                 '&po=' + OFFSET + '&crd=' + DATE,
                 json={'documents': [{
                     "agencyAcronym": 'NBA',
                     'docketId': 'NBA-ABC',
                     'documentId': 'NBA-ABC-123'}]
                      })
        data = [{
            'folder_name': 'NBA/NBA-ABC/NBA-ABC-123',
            'file_name': 'basic_documents.json',
            'data': {"agencyAcronym": 'NBA',
                     'docketId': 'NBA-ABC',
                     'documentId': 'NBA-ABC-123'}
            }]
        job = [
            {
                'job_type': 'document',
                'document_id': 'NBA-ABC-123'
            },
            {
                'job_type': 'docketId',
                'document_id': 'NBA-ABC'
            }
        ]
        mock.post('http://capstone.cs.moravian.edu',
                  json={'client_id': CLIENT_ID,
                        'job_id': JOB_ID,
                        'data': data,
                        'jobs': job})

        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_do_job_document_endpoint_call():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'document', 'job_id': JOB_ID,
                       'document_id': 'NBA-ABC-123'})
        mock.get('https://api.data.gov:443/regulations/v3/document.json?' +
                 '&api_key=' + API_KEY + "&documentId=NBA-ABC-123",
                 json={
                     "agencyAcronym": {'value': 'NBA'},
                     'fileFormats': 'url',
                     'docketId': {'value': 'NBA-ABC'},
                     'documentId': {'value': 'NBA-ABC-123'}})
        data = [{
            'folder_name': 'NBA/NBA-ABC/NBA-ABC-123',
            'file_name': 'document.json',
            'data': {"agencyAcronym": 'NBA',
                     'fileFormats': 'url'}
            }]
        jobs = [
            'url'
        ]
        mock.post('http://capstone.cs.moravian.edu',
                  json={'client_id': CLIENT_ID,
                        'job_id': JOB_ID,
                        'data': data,
                        'jobs': jobs})

        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url


def test_do_job_docket_endpoint_call():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'docket', 'job_id': JOB_ID,
                       'docket_id': 'ABC'})
        mock.get("https://api.data.gov:443/" +
                 "regulations/v3/docket.json?api_key=" +
                 API_KEY + "&docketId=ABC",
                 json={
                     "agencyAcronym": 'NBA',
                     'information': 'some data',
                     'docketId': 'NBA-ABC'})
        data = [{
            'folder_name': 'NBA/NBA-ABC/',
            'file_name': 'docket.json',
            'data': {"agencyAcronym": 'NBA',
                     'information': 'some data'}
            }]
        mock.post('http://capstone.cs.moravian.edu',
                  json={'client_id': CLIENT_ID,
                        'job_id': JOB_ID,
                        'data': data})

        do_job()
        history = mock.request_history

        assert len(history) == 3
        assert 'capstone' in history[0].url
        assert 'api.data.gov' in history[1].url
        assert 'capstone' in history[2].url

def test_do_job_download_endpoint_call():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_job',
                 json={'job_type': 'download', 'job_id': JOB_ID,
                       'url': URL})
        mock.get('https://api.data.gov/regulations/v3/download?'
                 'documentId=EPA-HQ-OAR-2011-0028-0108&contentType=pdf' +
                 '&api_key=' + API_KEY,
                 json={
                     "agencyAcronym": {'value': 'NBA'},
                     'fileContent': 'some data',
                     'docketId': 'NBA-ABC',
                     'documentId': {'value': 'NBA-ABC-123'}})
        data = [{
            'folder_name': {'agency':'NBA',
                           'docketid':'/NBA-ABC/',
                            'documentid':'NBA-ABC-123/'},
            'file_name': {'documentid':'NBA-ABC-123','.''file_type':'pdf'},
            'data': {"agencyAcronym": 'NBA',
                    'fileContent': 'some data'}
        }]
        mock.post('http://capstone.cs.moravian.edu',
                  json={'client_id': CLIENT_ID,
                        'job_id': JOB_ID,
                        'data': data})

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
