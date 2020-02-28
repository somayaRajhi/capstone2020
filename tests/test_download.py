from dotenv import load_dotenv, find_dotenv
from c20_server import document_download
from c20_server import regulations_api_errors
import os
import pytest
import requests_mock

URL = "https://api.data.gov:443/regulations/v3/documents.json?"
load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")
document_id = "EPA-HQ-OAR-2011-0028-0108"


def test_mock_response():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + '&rpp=1', json='document received')
        response = document_download.download_document(api_key)
        assert response == 'document received'


def test_no_api_key():
    with requests_mock.Mocker() as m:
        m.get(URL + '' + '&rpp=1', json={'a': 'b'}, status_code=403)
        with pytest.raises(regulations_api_errors.IncorrectApiKey):
            document_download.download_document("")


def test_1000_calls():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + '&rpp=1', json={'a': 'b'}, status_code=429)
        with pytest.raises(regulations_api_errors.ThousandCalls):
            document_download.download_document(api_key)


def test_document_id():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + "documentId=" + document_id, json='Json response')
        response = document_download.download_document(api_key, document_id)
        assert response == 'Json response'


def test_bad_document_id():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + "documentId=" + document_id, json={'a': 'b'}, status_code=404)
        with pytest.raises(regulations_api_errors.BadID):
            document_download.download_document(api_key, document_id)


def test_document_id_and_no_document_id():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + "documentId=" + document_id, json='document ID response')
        m.get(URL + api_key + '&rpp=1', json='non-document ID response')
        id_response = document_download.download_document(api_key, document_id)
        response = document_download.download_document(api_key)
        assert response == 'non-document ID response'
        assert id_response == 'document ID response'
