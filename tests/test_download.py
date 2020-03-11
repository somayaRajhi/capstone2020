import pytest
import requests_mock
from c20_server import document_download
from c20_server import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?"
DOC_ID = "EPA-HQ-OAR-2011-0028-0108"
API_KEY = "12345"


def test_mock_response():
    with requests_mock.Mocker() as mock:
        mock.get(URL + "12345" + '&rpp=1', json='document received')
        response = document_download.download_document(API_KEY)
        assert response == 'document received'


def test_document_id():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "documentId=" + DOC_ID,
                 json='Json response')
        response = document_download.download_document(API_KEY, DOC_ID)
        assert response == 'Json response'


def test_document_id_and_no_document_id():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "documentId=" + DOC_ID,
                 json='document ID response')
        mock.get(URL + API_KEY + '&rpp=1', json='non-document ID response')
        id_response = document_download.download_document(API_KEY, DOC_ID)
        response = document_download.download_document(API_KEY)
        assert response == 'non-document ID response'
        assert id_response == 'document ID response'


def test_incorrect_id_pattern():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + '&rpp=1', json={'a': 'b'}, status_code=400)
        with pytest.raises(reggov_api_doc_error.IncorrectIDPatternException):
            document_download.download_document(API_KEY)


def test_incorrect_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + '' + '&rpp=1', json={'a': 'b'}, status_code=403)
        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            document_download.download_document("")


def test_bad_document_id():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "documentId=" + DOC_ID,
                 json={'a': 'b'}, status_code=404)
        with pytest.raises(reggov_api_doc_error.BadDocIDException):
            document_download.download_document(API_KEY, DOC_ID)


def test_exceed_call_limit():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + '&rpp=1', json={'a': 'b'}, status_code=429)
        with pytest.raises(reggov_api_doc_error.ExceedCallLimitException):
            document_download.download_document(API_KEY)
