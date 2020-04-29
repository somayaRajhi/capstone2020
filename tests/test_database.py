import pytest
from c20_server.job import Job
from c20_server.database import MockDatabase
from c20_server.mock_job_manager import MockJobManager


def test_no_redis_connection():
    r_database = MockDatabase(is_connected=False)
    assert not r_database.connect()


def test_with_redis_server_connection():
    r_database = MockDatabase(is_connected=True)
    assert r_database.connect()


@pytest.fixture(name='job1')
def make_first_job():
    return Job(job_id=1)


def test_adding_one_job_with_redis_server_connection(job1):
    r_database = MockDatabase(is_connected=True)
    mock_job_manager = MockJobManager(r_database.fake_redis)
    mock_job_manager.add_job(job1)
    assert mock_job_manager.add_job_called
    assert mock_job_manager.num_unassigned() == 1


def test_trying_add_job_with_no_redis_connection(job1):
    r_database = MockDatabase(is_connected=False)
    mock_job_manager = MockJobManager(r_database.fake_redis)
    with pytest.raises(Exception):
        mock_job_manager.add_job(job1)
    assert not r_database.connect()
