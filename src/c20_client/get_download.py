import requests
from c20_client import status_code_check
from c20_client.client_logger import LOGGER


def download_file(api_key, url):
    LOGGER.info('Requesting download from regulations.gov')
    binary_data = requests.get(url + '&api_key=' + api_key)
    status_code_check.check_status(binary_data.status_code)
    LOGGER.info('download has been retrieved')

    return binary_data
