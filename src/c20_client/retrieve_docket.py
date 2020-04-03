"""
Contains class used to retreive dockets from regulations.gov
"""
import json
import requests
from c20_client.status_code_check import check_status


def jformat(obj):
    """
    Create formatted string from a JSON object
    """
    formatted = json.dumps(obj, sort_keys=True, indent=4)
    return formatted


def get_docket_data(api_key, docket_id):
    """
    Makes call to regulations.gov and retrieves the docket data
    """
    response = requests.get("https://api.data.gov:443/" +
                            "regulations/v3/docket.json?api_key=" +
                            api_key +
                            "&docketId=" +
                            docket_id)

    check_status(response.status_code)

    return response.json()


def get_data_string(api_key, docket_id):
    """
    Return the JSON object as a easy to read string
    """
    return jformat(get_data_json(api_key, docket_id))


def get_data_json(api_key, docket_id):
    """
    Returns the JSON object under the key job
    """
    docket_information = get_docket_data(api_key, docket_id)
    return {"data": docket_information}


def get_job_string(docket_id):
    """
    Returns the current job as a formatted easy to read string
    """
    return jformat(get_job_json(docket_id))


def get_job_json(docket_id):
    """
    Returns the current job as a JSON with the keys type and id
    """
    return {"job": {"job_type": "docket", "url": docket_id}}


def get_docket(api_key, docket_id):
    """
    Returns the docket in the format of a JSON file with the current job
    and the data for the current job
    """
    job = get_job_string(docket_id)
    data = get_data_string(api_key, docket_id)
    docket = job[:-1] + ',' + data[1:]
    return json.loads(docket)
