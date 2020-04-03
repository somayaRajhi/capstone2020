"""
Contains class used to retreive documents from regulations.gov
"""
import json
import requests
from c20_client import reggov_api_doc_error


def jformat(obj):
    """
    Create formatted string from a JSON object
    """
    formatted = json.dumps(obj, sort_keys=True, indent=4)
    return formatted


def get_documents_data(api_key, offset, date):
    """
    Makes call to regulations.gov and retrieves the documents data
    """
    response = requests.get('https://api.data.gov:443/regulations' +
                            '/v3/documents.json?api_key=' + api_key +
                            '&po=' + str(offset) + '&crd=' + date)

    if response.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()


def get_data_string(api_key, offset, date):
    """
    Return the JSON object as a easy to read string
    """
    return jformat(get_data_json(api_key, offset, date))


def get_data_json(api_key, offset, date):
    """
    Returns the JSON object under the key job
    """
    return get_documents_data(api_key, offset, date)


def get_documents(api_key, offset, start_date, end_date):
    """
    Returns the docket in the format of a JSON file with the current job
    and the data for the current job
    """
    date = start_date + '-' + end_date
    return get_data_json(api_key, offset, date)
