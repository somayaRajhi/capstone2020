"""
Test the retrieve_docket.py file
"""
import os
import json
import requests

from c20_server.retrieve_docket import RetrieveDocket

def create_an_instance_of_object():
    a_test = RetrieveDocket()
    assert a_test is not None

def test_good_docket():
    a_test = RetrieveDocket()

    api_key = os.getenv('API_Key')
    response = requests.get("https://api.data.gov:443/regulations/v3/docket" +
                            ".json?api_key=" + api_key + "&docketId=EPA-HQ-OAR-2011-0028")

    formatted = json.dumps(response.json(), sort_keys=True, indent=4)
    assert a_test.get_docket('EPA-HQ-OAR-2011-0028') == formatted
