from collections import namedtuple
import json
import fakeredis
import pytest
from c20_server.flask_server import create_app
from c20_server.mock_job_manager import MockJobManager
from c20_server.job import DocumentsJob


def make_redis_database():
    r_database = fakeredis.FakeRedis()
    r_database.flushall()
    return r_database


@pytest.fixture(name='manager')
def job_manager_fixture():
    r_database = make_redis_database()
    job_manager = MockJobManager(r_database)
    return job_manager


@pytest.fixture(name='client')
def client_fixture(manager):
    app = create_app(manager, SpyDataRepository())
    app.config['TESTING'] = True
    return app.test_client()


def test_return_result_success(manager):
    mock_job_manager = manager
    app = create_app(mock_job_manager, SpyDataRepository())
    app.config['TESTING'] = True
    client = app.test_client()

    json_data = {
        'client_id': 'client1',
        'job_id': 'job1',
        'data': [
            {
                'folder_name': 'thisisafoldername',
                'file_name': 'thisisafilename',
                'data': {}
            }
        ],
        'jobs': [
            {
                'job_type': 'documents',
                'job_id': 'thisiajobid',
                'page_offset': 'thisiapageoffset',
                'start_date': 'thisisastartdate',
                'end_date': 'thisisanenddate'
            },
        ]
    }
    result = client.post('/return_result', data=json.dumps(json_data),
                         content_type='application/json')
    assert result.status_code == 200
    assert mock_job_manager.add_job_called
    assert mock_job_manager.num_unassigned() == 1


def test_return_result_empty_data(client):
    result = client.post('/return_result', data={})
    assert result.status_code == 400


def test_single_job_return(manager):
    mock_job_manager = manager
    mock_job_manager.add_job(DocumentsJob(job_id=1, page_offset=0,
                                          start_date='03-01-2020',
                                          end_date='04-01-2020'))
    app = create_app(mock_job_manager, SpyDataRepository())
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/get_job')
    assert mock_job_manager.request_job_called
    assert result.data == b'{"job_id": 1,' \
                          b' "page_offset": 0,' \
                          b' "start_date": "03-01-2020",' \
                          b' "end_date": "04-01-2020",' \
                          b' "job_type": "documents"}'


def test_none_job_return_when_no_job(manager):
    mock_job_manager = manager
    app = create_app(mock_job_manager, SpyDataRepository())
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/get_job')
    assert mock_job_manager.request_job_called
    job = json.loads(result.data)
    assert job['job_type'] == 'none'


class DummyJobManager:
    def add_job(self, job):
        pass

    def request_job(self, user):
        pass

    def report_success(self, user):
        pass

    def report_failure(self, user):
        pass

    def reset_stale_job(self, time_to_expire):
        pass

    def num_assigned(self):
        pass

    def num_unassigned(self):
        pass


SavedItem = namedtuple('SavedItem', ['directory_name', 'filename', 'contents'])


class SpyDataRepository:

    def __init__(self):
        self.saved_items = []

    def save_data(self, directory_name, filename, contents):
        item = SavedItem(directory_name=directory_name,
                         filename=filename,
                         contents=contents)

        self.saved_items.append(item)


def test_store_single_data_item():
    data_repository_spy = SpyDataRepository()
    app = create_app(DummyJobManager(), data_repository_spy)
    app.config['TESTING'] = True
    client = app.test_client()

    json_data = {
        'client_id': '1',
        'job_id': '1',
        'data': [
            {
                'folder_name': 'foldername',
                'file_name': 'filename',
                'data': {}
            }
        ],
        'jobs': []
    }

    client.post('/return_result', data=json.dumps(json_data),
                content_type='application/json')

    first_save = data_repository_spy.saved_items[0]

    assert first_save.directory_name == 'foldername'
    assert first_save.filename == 'filename'
    assert first_save.contents == {}


def test_store_multiple_data_items():
    data_repository_spy = SpyDataRepository()
    app = create_app(DummyJobManager(), data_repository_spy)
    app.config['TESTING'] = True
    client = app.test_client()

    json_data = {
        'client_id': '1',
        'job_id': '1',
        'data': [
            {
                'folder_name': 'foldername1',
                'file_name': 'filename1',
                'data': {}
            },
            {
                'folder_name': 'foldername1',
                'file_name': 'filename2',
                'data': {}
            },
            {
                'folder_name': 'foldername2',
                'file_name': 'filename3',
                'data': {}
            }
        ],
        'jobs': []
    }

    client.post('/return_result', data=json.dumps(json_data),
                content_type='application/json')

    first_save = data_repository_spy.saved_items[0]
    assert first_save.directory_name == 'foldername1'
    assert first_save.filename == 'filename1'
    assert first_save.contents == {}

    second_save = data_repository_spy.saved_items[1]
    assert second_save.directory_name == 'foldername1'
    assert second_save.filename == 'filename2'
    assert second_save.contents == {}

    third_save = data_repository_spy.saved_items[2]
    assert third_save.directory_name == 'foldername2'
    assert third_save.filename == 'filename3'
    assert third_save.contents == {}
