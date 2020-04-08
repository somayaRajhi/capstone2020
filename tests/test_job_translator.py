import json
import pytest
from c20_server import job
from c20_server import job_translator
from c20_server import job_translator_errors
from c20_server.job import DocumentsJob

JSON_RESULT_EXAMPLE = \
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
JSON_RESULT_EXAMPLE = json.dumps(JSON_RESULT_EXAMPLE)


def test_job_is_json():
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


def test_handle_job_empty_json():
    assert job_translator.handle_jobs({}) == {}


def test_throw_invalid_job_type_exception():
    json_example = {
        "job_type": "invalid",
        "job_id": "this_is_a_job_id"
    }
    with pytest.raises(job_translator_errors.UnrecognizedJobTypeException):
        job_translator.json_to_job(json_example)


def test_single_job():
    json_example = {
        "job_type": "documents",
        "job_id": "this_is_a_job_id",
        "page_offset": "this_is_a_page_offset",
        "start_date": "this_is_a_start_date",
        "end_date": "this_is_an_end_date"
    }
    test_job = job_translator.json_to_job(json_example)
    print(test_job[0])
    document_job = job.DocumentsJob(test_job[0],
                                    "this_is_a_page_offset",
                                    "this_is_a_start_date",
                                    "this_is_an_end_date")
    assert test_job == document_job


def test_handle_single_job():
    test_job = job_translator.handle_jobs(JSON_RESULT_EXAMPLE)
    job_list = [
        job.DocumentsJob(
            job_id=test_job[0][0],
            page_offset="this_is_a_page_offset",
            start_date="this_is_a_start_date",
            end_date="this_is_an_end_date")
    ]
    assert test_job == job_list
