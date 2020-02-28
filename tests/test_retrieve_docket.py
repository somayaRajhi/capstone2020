"""
Test the retrieve_docket.py file
"""
import os
from dotenv import load_dotenv, find_dotenv
import json
import requests
import requests_mock
from c20_server.retrieve_docket import get_docket

URL = "https://api.data.gov:443/regulations/v3/docket.json?api_key="
load_dotenv(find_dotenv())
API_KEY = os.getenv("API_KEY")
DOCKET_ID = "EPA-HQ-OAR-2011-0028"

def test_mock_server():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY + "&docketID=" + DOCKET_ID, json='resp')
        response = get_docket(API_KEY, DOCKET_ID)

        assert response == '"resp"'


def test_good_docket_id():

    response = requests.get("https://api.data.gov:443/regulations/v3/docket" +
                            ".json?api_key=" + API_KEY + "&docketId=EPA-HQ-OAR-2011-0028")

    formatted = json.dumps(response.json(), sort_keys=True, indent=4)
    assert get_docket('EPA-HQ-OAR-2011-0028') == formatted

def test_bad_docket_id():
    pass
