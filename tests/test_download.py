from dotenv import load_dotenv, find_dotenv
from c20_server import file_download
from c20_server import customError
import os
import pytest
import requests_mock

URL = "https://api.data.gov:443/regulations/v3/documents.json?"
load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")
document_Id = "EPA-HQ-OAR-2011-0028-0108"


def test_mock_response():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + '&rpp=1', json='document received')
        response = file_download.download_file(URL, api_key)
        assert response == 'document received'


def test_no_api_key():
    with requests_mock.Mocker() as m:
        m.get(URL + '' + '&rpp=1', exc=customError.IncorrectApiKey)
        with pytest.raises(customError.IncorrectApiKey):
            file_download.download_file(URL, "")


def test_1000_calls():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + '&rpp=1', exc=customError.ThousandCalls)
        with pytest.raises(customError.ThousandCalls):
            file_download.download_file(URL, api_key)


def test_document_id():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + "documentId=" + document_Id, json='Json response')
        response = file_download.download_file(URL, api_key, document_Id)
        assert response == 'Json response'


def test_bad_document_id():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + "documentId=" + document_Id, exc=customError.BadID)
        with pytest.raises(customError.BadID):
            file_download.download_file(URL, api_key, document_Id)


def test_document_id_and_no_document_id():
    with requests_mock.Mocker() as m:
        m.get(URL + api_key + "documentId=" + document_Id, json='document ID response')
        m.get(URL + api_key + '&rpp=1', json='non-document ID response')
        id_response = file_download.download_file(URL, api_key, document_Id)
        response = file_download.download_file(URL, api_key)
        assert response == 'non-document ID response'
        assert id_response == 'document ID response'
