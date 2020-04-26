"""
Test class for Job-Queue Class.
"""
import pytest
import fakeredis
from c20_server.job_queue import JobQueue
from c20_server.job \
    import Job, DocumentsJob, DocumentJob, DocketJob, DownloadJob
from c20_server import job_queue_errors


def make_database():
    r_database = fakeredis.FakeStrictRedis()
    return r_database


@pytest.fixture(name='job_queue')
def make_job_queue():
    r_database = make_database()
    return JobQueue(r_database)


@pytest.fixture(name='documents_job')
def make_first_documents_job():
    return DocumentsJob('job01',
                        1000,
                        '2020-1-28',
                        '2020-5-6')


@pytest.fixture(name='document_job')
def make_first_document_job():
    return DocumentJob('job01',
                       'EPA-HQ-OAR-2011-0028-0108')


@pytest.fixture(name='docket_job')
def make_first_docket_job():
    return DocketJob('job01',
                     'EPA-HQ-OAR-2011-0028')


@pytest.fixture(name='download_job')
def make_first_download_job():
    url = "https://.../download?documentId=...&contentType=pdf"
    return DownloadJob('job01',
                       "CMS/CMS-2005/",
                       "title_of_file",
                       "pdf",
                       url)


def test_one_job_added_is_returned_by_get(job_queue):
    job = Job(1234)

    assert job_queue.get_num_unassigned_jobs() == 0
    job_queue.add_job(job)
    assert job_queue.get_num_unassigned_jobs() == 1
    returned_job = job_queue.get_job()
    assert returned_job.job_id == 1234
    assert job_queue.get_num_unassigned_jobs() == 0


def test_add_two_jobs_then_remove_them(job_queue):
    job1 = Job(123411)
    job2 = Job(56722)

    job_queue.add_job(job1)
    job_queue.add_job(job2)
    assert job_queue.get_num_unassigned_jobs() == 2

    first_returned_job = job_queue.get_job()
    second_returned_job = job_queue.get_job()
    assert first_returned_job.job_id == job1.job_id
    assert second_returned_job.job_id == job2.job_id
    assert job_queue.get_num_unassigned_jobs() == 0


def test_get_one_job_from_empty_list(job_queue):
    with pytest.raises(job_queue_errors.NoJobsAvailableException):
        job_queue.get_job()


def test_one_documents_job_added_is_returned_by_get(job_queue, documents_job):
    job_queue.add_job(documents_job)
    assert job_queue.get_num_unassigned_jobs() == 1

    requested_job = job_queue.get_job()
    assert job_queue.get_num_unassigned_jobs() == 0

    assert requested_job.job_id == 'job01'
    assert requested_job.page_offset == 1000
    assert requested_job.start_date == '2020-1-28'
    assert requested_job.end_date == '2020-5-6'


def test_one_document_job_added_is_returned_by_get(job_queue, document_job):
    job_queue.add_job(document_job)
    assert job_queue.get_num_unassigned_jobs() == 1

    requested_job = job_queue.get_job()
    assert job_queue.get_num_unassigned_jobs() == 0

    assert requested_job.job_id == 'job01'
    assert requested_job.document_id == 'EPA-HQ-OAR-2011-0028-0108'


def test_one_docket_job_added_is_returned_by_get(job_queue, docket_job):
    job_queue.add_job(docket_job)
    assert job_queue.get_num_unassigned_jobs() == 1

    requested_docket_job = job_queue.get_job()
    assert requested_docket_job.job_id == 'job01'
    assert requested_docket_job.docket_id == 'EPA-HQ-OAR-2011-0028'


def test_one_download_job_added_is_returned_by_get(job_queue, download_job):
    job_queue.add_job(download_job)
    assert job_queue.get_num_unassigned_jobs() == 1
    requested_download_job = job_queue.get_job()
    url = "https://.../download?documentId=...&contentType=pdf"
    assert requested_download_job.job_id == 'job01'
    assert requested_download_job.url == url
