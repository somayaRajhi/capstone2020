from c20_server import customError
import requests


def download_file(url, api_key, document_id=""):
    """
    downloads a file based on a url, api key and document_id (if given)
    """
    if document_id == "":
        data = requests.get(url + api_key + '&rpp=1')
    else:
        data = requests.get(url + api_key + "documentId=" + document_id)
    if data.status_code == 403:
        raise customError.IncorrectApiKey
    if data.status_code == 429:
        raise customError.ThousandCalls
    if data.status_code == 404:
        raise customError.BadID
    document = data.json()
    return document



