
import pytest
import requests_mock
from c20_server.list_documents import list_documents
from c20_server import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/document.json?api_key="
API_KEY = "VALID"


def test_list_documents():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json='The test is successful')
        response = list_documents(API_KEY)

        assert response == 'The test is successful'


def test_bad_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + 'INVALID',
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            list_documents('INVALID')


def test_overused_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json='The test yields a overused api key', status_code=429)

        with pytest.raises(reggov_api_doc_error.ExceedCallLimitException):
            list_documents(API_KEY)
