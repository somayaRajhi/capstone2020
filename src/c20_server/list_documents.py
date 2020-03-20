'''
List Documents from regulations.api
'''
# import json
import requests
from c20_server import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="


def list_docket_ids():
    response = "Successfully got docket IDs"
    return response


def list_document_ids():
    response = "Successfully got document IDs"
    return response


def list_documents(api_key):

    response = requests.get(URL+api_key)

    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    # document_ids = list_document_ids(response)

    return response.json()
