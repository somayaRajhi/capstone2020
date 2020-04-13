import json
import pytest
from c20_server import job
from c20_server import job_translator
from c20_server import job_translator_errors
from c20_server.job import DocumentsJob, DocumentJob, DocketJob, DownloadJob


def test_handle_job_empty_json():
    assert job_translator.handle_jobs({}) == {}


def test_throw_invalid_job_type_exception():
    json_example = {
        "job_type": "invalid",
        "job_id": "this_is_a_job_id"
    }
    with pytest.raises(job_translator_errors.UnrecognizedJobTypeException):
        job_translator.json_to_job(json_example)


def test_documents_job_to_json():
    job_example = DocumentsJob("this_is_a_job_id",
                               "this_is_a_page_offset",
                               "this_is_a_start_date",
                               "this_is_an_end_date")

    job_json = job_translator.job_to_json(job_example)

    job_json_expected = {"job_id": "this_is_a_job_id",
                         "page_offset": "this_is_a_page_offset",
                         "start_date": "this_is_a_start_date",
                         "end_date": "this_is_an_end_date",
                         "job_type": "documents"}
    job_json_expected = json.dumps(job_json_expected)
    assert job_json == job_json_expected


def test_document_job_to_json():
    job_example = DocumentJob("this_is_a_job_id",
                              "this_is_a_document_id")

    job_json = job_translator.job_to_json(job_example)

    job_json_expected = {"job_id": "this_is_a_job_id",
                         "document_id": "this_is_a_document_id",
                         "job_type": "document"}
    job_json_expected = json.dumps(job_json_expected)
    assert job_json == job_json_expected


def test_docket_job_to_json():
    job_example = DocketJob("this_is_a_job_id",
                            "this_is_a_docket_id")

    job_json = job_translator.job_to_json(job_example)

    job_json_expected = {"job_id": "this_is_a_job_id",
                         "docket_id": "this_is_a_docket_id",
                         "job_type": "docket"}
    job_json_expected = json.dumps(job_json_expected)
    assert job_json == job_json_expected


def test_download_job_to_json():
    job_example = DownloadJob("this_is_a_job_id",
                              "this_is_a_url")

    job_json = job_translator.job_to_json(job_example)

    job_json_expected = {"job_id": "this_is_a_job_id",
                         "url": "this_is_a_url",
                         "job_type": "download"}
    job_json_expected = json.dumps(job_json_expected)
    assert job_json == job_json_expected


def test_single_documents_json_to_job():
    json_example = {
        "job_type": "documents",
        "job_id": "this_is_a_job_id",
        "page_offset": "this_is_a_page_offset",
        "start_date": "this_is_a_start_date",
        "end_date": "this_is_an_end_date"
    }
    test_job = job_translator.json_to_job(json_example)
    documents_job = job.DocumentsJob(test_job[0],
                                     "this_is_a_page_offset",
                                     "this_is_a_start_date",
                                     "this_is_an_end_date")
    assert test_job == documents_job


def test_single_document_json_to_job():
    json_example = {
        "job_type": "document",
        "job_id": "this_is_a_job_id",
        "document_id": "this_is_a_document_id"
    }
    test_job = job_translator.json_to_job(json_example)
    document_job = job.DocumentJob(test_job[0],
                                   "this_is_a_document_id")
    assert test_job == document_job


def test_single_docket_json_to_job():
    json_example = {
        "job_type": "docket",
        "job_id": "this_is_a_job_id",
        "docket_id": "this_is_a_docket_id"
    }
    test_job = job_translator.json_to_job(json_example)
    docket_job = job.DocketJob(test_job[0],
                               "this_is_a_docket_id")
    assert test_job == docket_job


def test_single_download_json_to_job():
    json_example = {
        "job_type": "download",
        "job_id": "this_is_a_job_id",
        "url": "this_is_a_url"
    }
    test_job = job_translator.json_to_job(json_example)
    download_job = job.DownloadJob(test_job[0],
                                   "this_is_a_url")
    assert test_job == download_job


def test_handle_single_job():
    json_result_sample = \
        {
            "Data": [
                {
                    "folder_name": "this_is_a_folder_name",
                    "file_name": "this_is_a_file_name",
                    "contents": {}
                }
            ],
            "jobs": [
                {
                    "job_type": "documents",
                    "job_id": "this_is_a_job_id",
                    "page_offset": "this_is_a_page_offset",
                    "start_date": "this_is_a_start_date",
                    "end_date": "this_is_an_end_date"
                },
            ]
        }
    json_result_sample = json.dumps(json_result_sample)

    test_job = job_translator.handle_jobs(json_result_sample)

    job_list = [
        job.DocumentsJob(
            job_id=test_job[0][0],
            page_offset="this_is_a_page_offset",
            start_date="this_is_a_start_date",
            end_date="this_is_an_end_date")
    ]
    assert test_job == job_list


def test_handle_documents_return_data():
    json_documents_return_data = \
        {
            "Data": [
                {
                    "folder_name": "this_is_a_folder_name",
                    "file_name": "this_is_a_file_name",
                    "contents": {}
                }
            ],
            "jobs": [
                {
                    "job_type": "document",
                    "job_id": "this_is_a_job_id",
                    "document_id": "this_is_a_document_id"
                },
                {
                    "job_type": "docket",
                    "job_id": "this_is_a_job_id",
                    "docket_id": "this_is_a_docket_id"
                },
                {
                    "job_type": "document",
                    "job_id": "this_is_a_job_id",
                    "document_id": "this_is_a_second_document_id"
                },
                {
                    "job_type": "docket",
                    "job_id": "this_is_a_job_id",
                    "docket_id": "this_is_a_second_docket_id"
                }
            ]
        }
    json_documents_return_data = json.dumps(json_documents_return_data)

    test_job = job_translator.handle_jobs(json_documents_return_data)

    job_list = [
        job.DocumentJob(
            job_id=test_job[0][0],
            document_id="this_is_a_document_id"),
        job.DocketJob(
            job_id=test_job[1][0],
            docket_id="this_is_a_docket_id"),
        job.DocumentJob(
            job_id=test_job[2][0],
            document_id="this_is_a_second_document_id"),
        job.DocketJob(
            job_id=test_job[3][0],
            docket_id="this_is_a_second_docket_id")
    ]

    assert test_job == job_list


def test_handle_document_return_data():
    json_document_return_data = \
        {
            "Data": [
                {
                    "folder_name": "this_is_a_folder_name",
                    "file_name": "this_is_a_file_name",
                    "contents": {}
                }
            ],
            "jobs": [
                {
                    "job_type": "download",
                    "job_id": "this_is_a_job_id",
                    "url": "this_is_a_url"
                },
                {
                    "job_type": "download",
                    "job_id": "this_is_a_second_job_id",
                    "url": "this_is_a_second_url"
                },
                {
                    "job_type": "download",
                    "job_id": "this_is_a_third_job_id",
                    "url": "this_is_a_third_url"
                },

            ]
        }
    json_document_return_data = json.dumps(json_document_return_data)

    test_job = job_translator.handle_jobs(json_document_return_data)

    job_list = [
        job.DownloadJob(
            job_id=test_job[0][0],
            url="this_is_a_url"),
        job.DownloadJob(
            job_id=test_job[1][0],
            url="this_is_a_second_url"),
        job.DownloadJob(
            job_id=test_job[2][0],
            url="this_is_a_third_url")
    ]
    assert test_job == job_list
