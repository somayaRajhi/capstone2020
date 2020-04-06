import pytest
from c20_client import docket_packager

CLIENT_ID = 1
JOB_ID = 1

TEST_JSON = {
    "agencyAcronym": "test",
    "docketId": "123",
}


@pytest.fixture(name='get_docket')
def fixture_get_docket():
    response = docket_packager.package_docket(TEST_JSON, CLIENT_ID, JOB_ID)
    return response


def test_get_docket(get_docket):
    assert get_docket == {
        'client_id': 1,
        'job_id': 1,
        'data': [{
            'folder_name': "test/123/",
            'file_name': 'docket.json',
            'data': TEST_JSON
            }]
    }


def test_client_id(get_docket):
    assert get_docket['client_id'] == 1


def test_folder_name(get_docket):
    assert get_docket['data'][0]['folder_name'] == 'test/123/'


def test_file_name(get_docket):
    assert get_docket['data'][0]['file_name'] == 'docket.json'


def test_agency(get_docket):
    assert get_docket['data'][0]['data']['agencyAcronym'] == 'test'


def test_docket_id(get_docket):
    assert get_docket['data'][0]['data']['docketId'] == '123'


def test_file_contents(get_docket):
    assert get_docket['data'][0]['data'] == {
        "agencyAcronym": "test",
        "docketId": "123"
    }
