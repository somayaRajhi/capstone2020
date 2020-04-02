'''
Compute Jobs from regulations.api
'''
# import json
from datetime import date
import requests
from c20_client import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
RESULTS_PER_PAGE = 1000


def get_number_of_docs(response):
    '''
    Return total number of records
    '''
    number_of_docs = response.get("totalNumRecords")
    return number_of_docs

def get_response_from_API(api_key, start_date, end_date):

    crd = start_date + "-" + end_date

    response = requests.get(URL+api_key+"&crd="+crd)

    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()


def compute_jobs(api_key, start_date, end_date):
    '''
    Computing Jobs for Documents endpoint
    '''

    response = get_response_from_API(api_key, start_date, end_date)

    number_of_docs = get_number_of_docs(response)

    return response
