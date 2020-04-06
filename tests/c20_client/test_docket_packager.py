import pytest
from c20_client import docket_packager

TEST_JSON = {
    "agencyAcronym": "test",
    "docketId": "123",
}


@pytest.fixture(name='get_docket')
def fixture_get_docket():
    response = docket_packager.package_docket(TEST_JSON)
    return response


def test_get_docket(get_docket):
    assert get_docket == {
        'client_id': 1,
        'data': [{
            'folder_name': 'test/123/',
            'file_name': 'basic_docket.json',
            'data': {
                'agency': 'test',
                'docketId': '123',
                'file_contents': {
                    "agencyAcronym": "test",
                    "docketId": "123"
                }
            }
        }]
    }


def test_client_id(get_docket):
    assert get_docket['client_id'] == 1


def test_folder_name(get_docket):
    assert get_docket['data'][0]['folder_name'] == 'test/123/'


def test_file_name(get_docket):
    assert get_docket['data'][0]['file_name'] == 'basic_docket.json'


def test_agency(get_docket):
    assert get_docket['data'][0]['data']['agency'] == 'test'


def test_docket_id(get_docket):
    assert get_docket['data'][0]['data']['docketId'] == '123'


def test_file_contents(get_docket):
    assert get_docket['data'][0]['data']['file_contents'] == {
        "agencyAcronym": "test",
        "docketId": "123"
    }
