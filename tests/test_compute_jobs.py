
import pytest
import requests_mock

from c20_server.job import DocumentsJob
from c20_server.compute_jobs import (
    reggov_api_doc_error,
    compute_jobs,
    get_number_of_docs,
    get_response_from_api
)

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
API_KEY = "Valid"
START_DATE = "01/01/20"
END_DATE = "03/31/20"


def test_good_response_from_api():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 100})
        response = get_response_from_api(API_KEY, START_DATE, END_DATE)

        assert response == {"result": "The test is successful",
                            "totalNumRecords": 100}


def test_valid_jobs_list():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 1000})
        job_list = compute_jobs(API_KEY, START_DATE, END_DATE)
        job = DocumentsJob("DocsJob0", 0, START_DATE, END_DATE)

        assert job_list == [job]


def test_response_with_num_records():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 10})
        response = get_response_from_api(API_KEY, START_DATE, END_DATE)
        total_num_records = get_number_of_docs(response)

        assert total_num_records == 10


def test_bad_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + 'INVALID',
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            get_response_from_api('INVALID', START_DATE, END_DATE)


def test_overused_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json='The test yields a overused api key', status_code=429)

        with pytest.raises(reggov_api_doc_error.ExceedCallLimitException):
            get_response_from_api(API_KEY, START_DATE, END_DATE)
