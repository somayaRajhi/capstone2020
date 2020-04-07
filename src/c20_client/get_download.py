import requests
from c20_client import status_code_check


def download_file(api_key, url):
    binary_data = requests.get(url + '&api_key=' + api_key)
    status_code_check.check_status(binary_data.status_code)
    return binary_data
