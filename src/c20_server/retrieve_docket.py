"""
Contains class used to retreive dockets from regulations.gov
"""
import json
import requests

def jformat(obj):
    """
    Create formatted string of JSON object
    """
    formatted = json.dumps(obj, sort_keys=True, indent=4)
    return formatted


def get_docket(api_key, docket_id):
    """
    Makes call to regulations.gov and retrieves the docket
    """
    response = requests.get("https://api.data.gov:443/regulations/v3/docket.json?api_key=" +
                            api_key +
                            "&docketId=" +
                            docket_id)

    return jformat(response.json())
