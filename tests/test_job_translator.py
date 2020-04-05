import pytest
import json
from c20_server import job
from c20_server import job_translator
from c20_server import job_translator_errors


json_result_example = \
    {
        "Data": [
            "..."
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
json_result_example = json.dumps(json_result_example)


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
    assert job_translator.json_to_job(json_example) == \
        job.DocumentsJob("this_is_a_job_id", "this_is_a_page_offset", "this_is_a_start_date", "this_is_an_end_date")
