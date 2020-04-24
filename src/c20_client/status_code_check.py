"""
Function to check status code against regulations.gov api errors
"""
from c20_client import reggov_api_doc_error
from c20_client.client_logger import LOGGER


def check_status(status_code):
    if status_code == 400:
        LOGGER.error('The given ID is incorrect')
        raise reggov_api_doc_error.IncorrectIDPatternException
    if status_code == 403:
        LOGGER.error('The given API key is incorrect')
        raise reggov_api_doc_error.IncorrectApiKeyException
    if status_code == 404:
        LOGGER.error('The given Doc ID was bad')
        raise reggov_api_doc_error.BadDocIDException
    if status_code == 429:
        LOGGER.error('The 1000 call an hour limit has been exceeded')
        raise reggov_api_doc_error.ExceedCallLimitException
