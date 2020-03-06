from c20_server import regulations_api_errors
import requests


def download_document(api_key, document_id=""):
    """
    downloads a file based on a url, api key and document_id (if given)
    """
    url = "https://api.data.gov:443/regulations/v3/documents.json?"
    if document_id == "":
        data = requests.get(url + api_key + '&rpp=1')
    else:
        data = requests.get(url + api_key + "documentId=" + document_id)
    if data.status_code == 403:
        raise regulations_api_errors.IncorrectApiKey
    if data.status_code == 429:
        raise regulations_api_errors.ThousandCalls
    if data.status_code == 404:
        raise regulations_api_errors.BadID
    document = data.json()
    return document
