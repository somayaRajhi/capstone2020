'''
List Documents from regulations.api
'''
# import json
import requests
from c20_client import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
RESULTS_PER_PAGE = 1000


def compute_jobs(api_key):

    response = requests.get(URL+api_key)

    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()
