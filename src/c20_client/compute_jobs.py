'''
Compute Jobs from regulations.api
'''
from datetime import date
import requests
from c20_client import reggov_api_doc_error, documents_packager

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
RESULTS_PER_PAGE = 1000


def get_number_of_docs(response):
    '''
    Return total number of records
    '''
    number_of_docs = response.get("totalNumRecords")
    return number_of_docs


def compute_jobs(api_key, start_date):
    '''
    Computing Jobs for Documents endpoint
    '''

    # Getting current date in mm/dd/yy format
    today = date.today()
    date_now = today.strftime("%m/%d/%y")

    # Test to see if start_date is valid

    crd = start_date + "-" + date_now

    response = requests.get(URL+api_key+"&crd="+crd)

    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    response = response.json()

    #documents_packager.package_documents(response)
    return response
