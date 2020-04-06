import json
import pytest
from c20_server import job
from c20_server import job_translator
from c20_server import job_translator_errors

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


def test_empty_return():
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
    document_job = job.DocumentsJob("this_is_a_job_id",
                                    "this_is_a_page_offset",
                                    "this_is_a_start_date",
                                    "this_is_an_end_date")
    assert job_translator.json_to_job(json_example) == document_job


def test_handle_single_job():
    job_list = [
        job.DocumentsJob(
            job_id='this_is_a_job_id',
            page_offset='this_is_a_page_offset',
            start_date='this_is_a_start_date',
            end_date='this_is_an_end_date')
    ]
    assert job_translator.handle_jobs(JSON_RESULT_EXAMPLE) == job_list
