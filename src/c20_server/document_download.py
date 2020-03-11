import requests
from c20_server import reggov_api_doc_error


def download_document(api_key, document_id=""):
    """
    downloads a file based on a url, api key and document_id (if given)
    """
    url = "https://api.data.gov:443/regulations/v3/documents.json?"
    if document_id == "":
        response = requests.get(url + api_key + '&rpp=1')
    else:
        response = requests.get(url + api_key + "documentId=" + document_id)
    if response.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException
    document = response.json()
    return document
