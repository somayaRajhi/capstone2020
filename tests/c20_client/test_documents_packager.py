import requests_mock
import pytest
from c20_client import documents_packager

CLIENT_ID = 1
JOB_ID = 1

TEST_JSON = {
    'documents': [{
        'agencyAcronym': 'test',
        'data': 'test Documents',
        'docketId': 'docket-number-3',
        'documentId': 'document-number-15'
    }]
}

TEST_JSON2 = {
    'documents': [{
        'agencyAcronym': 'test',
        'data': 'test Documents',
        'docketId': 'docket-number-3',
        'documentId': 'document-number-15'
    }, {
        'agencyAcronym': 'test',
        'data': 'test Documents 2',
        'docketId': 'docket-number-4',
        'documentId': 'document-number-16'
    }]
}


@pytest.fixture(name='single_documents')
def fixture_single_documents():
    with requests_mock.Mocker() as mock:
        mock.post('http://capstone.cs.moravian.edu',
                  json={'client_id': CLIENT_ID,
                        'job_id': JOB_ID,
                        'data': TEST_JSON,
                        'jobs': 'jobs'})
        response = documents_packager.package_documents(TEST_JSON,
                                                        CLIENT_ID,
                                                        JOB_ID)
        history = mock.request_history

        assert len(history) == 1
        assert 'capstone' in history[0].url
        return response


@pytest.fixture(name='multiple_documents')
def fixture_multiple_documents():
    with requests_mock.Mocker() as mock:
        mock.post('http://capstone.cs.moravian.edu',
                  json={'client_id': CLIENT_ID,
                        'job_id': JOB_ID,
                        'data': TEST_JSON2,
                        'jobs': 'jobs'})
        response = documents_packager.package_documents(TEST_JSON2,
                                                        CLIENT_ID,
                                                        JOB_ID)
        history = mock.request_history

        assert len(history) == 1
        assert 'capstone' in history[0].url
        return response


def test_get_documents(single_documents):
    assert single_documents == {
        'client_id': CLIENT_ID,
        'job_id': JOB_ID,
        'data': [{
            'folder_name': 'test/docket-number-3/document-number-15/',
            'file_name': 'basic_documents.json',
            'data': {
                'agencyAcronym': 'test',
                'data': 'test Documents',
                'docketId': 'docket-number-3',
                'documentId': 'document-number-15'
            }
        }],
        'jobs': 'jobs'
    }


def test_client_id(single_documents):
    assert single_documents['client_id'] == CLIENT_ID


def test_folder_name(single_documents):
    assert single_documents['data'][0]['folder_name'] == \
        'test/docket-number-3/document-number-15/'


def test_file_name(single_documents):
    assert single_documents['data'][0]['file_name'] == \
           'basic_documents.json'


def test_agency_acronym(single_documents):
    assert single_documents['data'][0]['data']['agencyAcronym'] == \
           'test'


def test_data(single_documents):
    assert single_documents['data'][0]['data']['data'] == \
           'test Documents'


def test_docket_id(single_documents):
    assert single_documents['data'][0]['data']['docketId'] == \
           'docket-number-3'


def test_document_id(single_documents):
    assert single_documents['data'][0]['data']['documentId'] == \
           'document-number-15'


def test_get_many_documents(multiple_documents):
    assert multiple_documents['data'][1] == {
        'folder_name': 'test/docket-number-4/document-number-16/',
        'file_name': 'basic_documents.json',
        'data': {
            'agencyAcronym': 'test',
            'data': 'test Documents 2',
            'docketId': 'docket-number-4',
            'documentId': 'document-number-16'
        }
    }


def test_many_folder_name(multiple_documents):
    assert multiple_documents['data'][0]['folder_name'] == \
        'test/docket-number-3/document-number-15/'
    assert multiple_documents['data'][1]['folder_name'] == \
        'test/docket-number-4/document-number-16/'


def test_many_file_name(multiple_documents):
    assert multiple_documents['data'][0]['file_name'] == \
        'basic_documents.json'
    assert multiple_documents['data'][1]['file_name'] == \
        'basic_documents.json'


def test_many_agency_acronym(multiple_documents):
    assert multiple_documents['data'][0]['data']['agencyAcronym'] == \
        'test'
    assert multiple_documents['data'][1]['data']['agencyAcronym'] == \
        'test'


def test_many_data(multiple_documents):
    assert multiple_documents['data'][0]['data']['data'] == \
        'test Documents'
    assert multiple_documents['data'][1]['data']['data'] == \
        'test Documents 2'


def test_many_docket_id(multiple_documents):
    assert multiple_documents['data'][0]['data']['docketId'] == \
        'docket-number-3'
    assert multiple_documents['data'][1]['data']['docketId'] == \
        'docket-number-4'


def test_many_document_id(multiple_documents):
    assert multiple_documents['data'][0]['data']['documentId'] == \
        'document-number-15'
    assert multiple_documents['data'][1]['data']['documentId'] == \
        'document-number-16'
