'''
List Documents from regulations.api
'''
# import json
import requests
from c20_server import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/document.json?api_key="


def list_documents(api_key):

    response = requests.get(URL+api_key)

    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    # if response.status_code == 404:
    #     raise reggov_api_doc_error.BadDocIDException
    # if response.status_code == 400:
    #     raise reggov_api_doc_error.IncorrectIDPatternException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()
