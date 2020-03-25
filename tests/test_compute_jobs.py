
import pytest
import requests_mock
from c20_server.compute_jobs import compute_jobs, get_number_of_docs

from c20_client import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
API_KEY = "Valid"
START_DATE = "01/01/20"


def test_good_response():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 100})
        response = compute_jobs(API_KEY, START_DATE)

        assert response == {"result": "The test is successful",
                            "totalNumRecords": 100}


def test_10_number_of_records():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 10})
        response = compute_jobs(API_KEY, START_DATE)

        assert response.get("totalNumRecords") == 10


def test_response_with_num_records():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 10})
        response = compute_jobs(API_KEY, START_DATE)
        total_num_records = get_number_of_docs(response)

        assert total_num_records == 10


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
