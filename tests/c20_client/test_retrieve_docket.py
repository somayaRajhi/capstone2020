"""
Test the retrieve_docket.py file
"""
import requests_mock
import pytest
from c20_client.retrieve_docket import get_docket
from c20_client import reggov_api_doc_error
from c20_client.client import handling_erorr

CLIENT_ID = 1
JOB_ID = 1
URL = "https://api.data.gov:443/regulations/v3/docket.json?api_key="
API_KEY = "VALID KEY"
DOCKET_ID = "EPA-HQ-OAR-2011-0028"


def test_get_docket():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json={'test': 'The test is successful'})
        response = get_docket(API_KEY, DOCKET_ID)

        assert (response ==
                {'test': 'The test is successful'})


def test_bad_docket_id():
    with requests_mock.Mocker() as mock:
        bad_docket = DOCKET_ID + '-0101'
        mock.get(URL + API_KEY + "&docketID=" + bad_docket,
                 json='The test yields a bad id', status_code=404)

        with pytest.raises(reggov_api_doc_error.BadDocIDException):
            get_docket(API_KEY, bad_docket)
            result = handling_erorr(URL + API_KEY + "&docketID=" + bad_docket, message_report= ":received 404:Not Found")
            mock.post('http://capstone.cs.moravian.edu/report_failure',
                      json={'client_id': CLIENT_ID,
                            'job_id': JOB_ID,
                            'message': result})


def test_no_docket_id():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "&docketID=",
                 json='The test yields a bad id', status_code=404)

        with pytest.raises(reggov_api_doc_error.BadDocIDException):
            get_docket(API_KEY, '')
            result = handling_erorr(URL + API_KEY + "&docketID=", message_report = ":received 404:Not Found")
            mock.post('http://capstone.cs.moravian.edu/report_failure',
                      json={'client_id': CLIENT_ID,
                            'job_id': JOB_ID,
                            'message': result})


def test_bad_docket_id_pattern():
    with requests_mock.Mocker() as mock:
        bad_docket = 'b4d' + DOCKET_ID + 'b4d'
        mock.get(URL + API_KEY + "&docketID=" + bad_docket,
                 json='The test yields a bad id pattern', status_code=400)

        with pytest.raises(reggov_api_doc_error.IncorrectIDPatternException):
            get_docket(API_KEY, bad_docket)
            result = handling_erorr(URL + API_KEY + "&docketID=" + bad_docket, message_report = ":received 400:Bad request")
            mock.post('http://capstone.cs.moravian.edu/report_failure',
                      json={'client_id': CLIENT_ID,
                            'job_id': JOB_ID,
                            'message': result})


def test_bad_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + 'INVALID' + "&docketID=" + DOCKET_ID,
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            get_docket('INVALID', DOCKET_ID)
            result = handling_erorr(URL + 'INVALID' + "&docketID=" + DOCKET_ID
                                    , message_report=":received 403:Forbidden")
            mock.post('http://capstone.cs.moravian.edu/report_failure',
                      json={'client_id': CLIENT_ID,
                            'job_id': JOB_ID,
                            'message': result})


def test_no_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + "&docketID=" + DOCKET_ID,
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            get_docket('', DOCKET_ID)
            result = handling_erorr(URL + "&docketID=" + DOCKET_ID
                                    , message_report=":received 403:Forbidden")
            mock.post('http://capstone.cs.moravian.edu/report_failure',
                      json={'client_id': CLIENT_ID,
                            'job_id': JOB_ID,
                            'message': result})


def test_maxed_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json='The test yields a overused api key', status_code=429)

        with pytest.raises(reggov_api_doc_error.ExceedCallLimitException):
            get_docket(API_KEY, DOCKET_ID)
            result = handling_erorr(URL + API_KEY + "&docketID=" + DOCKET_ID
                                    , message_report=":received 429:Too Many Requests")
            mock.post('http://capstone.cs.moravian.edu/report_failure',
                      json={'client_id': CLIENT_ID,
                            'job_id': JOB_ID,
                            'message': result})
