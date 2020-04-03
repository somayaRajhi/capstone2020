"""
Function to check status code against regulations.gov api errors
"""
from c20_client import reggov_api_doc_error


def check_status(status_code):
    if status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException
