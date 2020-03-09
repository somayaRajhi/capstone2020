"""
Contains class used to retreive dockets from regulations.gov
"""
import json
import requests
from c20_server import reggov_api_docket_error


def jformat(obj):
    """
    Create formatted string of JSON object
    """
    formatted = json.dumps(obj, sort_keys=True, indent=4)
    return formatted


def get_docket(api_key, docket_id):
    """
    Makes call to regulations.gov and retrieves the docket
    """
    response = requests.get("https://api.data.gov:443/" +
                            "regulations/v3/docket.json?api_key=" +
                            api_key +
                            "&docketId=" +
                            docket_id)

    if response.status_code == 400:
        raise reggov_api_docket_error.IncorrectIDPattern
    if response.status_code == 403:
        raise reggov_api_docket_error.IncorrectApiKey
    if response.status_code == 404:
        raise reggov_api_docket_error.BadDocketID
    if response.status_code == 429:
        raise reggov_api_docket_error.ExceedCallLimit

    return jformat(response.json())
