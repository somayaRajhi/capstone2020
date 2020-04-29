import requests
from c20_client import status_code_check
from c20_client.client_logger import LOGGER


def download_document(api_key, document_id):
    """
    downloads a file based on a url, api key and document_id (if given)
    """
    api_key = "&api_key=" + api_key
    document_id = "&documentId=" + document_id
    url = "https://api.data.gov:443/regulations/v3/document.json?"
    LOGGER.info('Requesting document from regulations.gov')
    data = requests.get(url + api_key + document_id)
    status_code_check.check_status(data.status_code)
    LOGGER.info('document has been retrieved')
    document = data.json()
    return document
