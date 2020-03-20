
import pytest
import requests_mock
from c20_server.compute_jobs import compute_jobs

from c20_client import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
API_KEY = "VALID"
START_DATE = "01/01/20"


def test_compute_jobs():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json='The test is successful')
        response = compute_jobs(API_KEY, START_DATE)

        assert response == 'The test is successful'


def test_bad_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + 'INVALID',
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            compute_jobs('INVALID', START_DATE)


def test_overused_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json='The test yields a overused api key', status_code=429)

        with pytest.raises(reggov_api_doc_error.ExceedCallLimitException):
            compute_jobs(API_KEY, START_DATE)
