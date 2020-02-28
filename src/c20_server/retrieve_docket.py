"""
Contains class used to retreive dockets from regulations.gov
"""
import os
import json
import requests


class RetrieveDocket:
    """
    Retrieve the docket in a neat JSON format
    """

    def __jformat(self, obj):
        """
        Create formatted string of JSON object
        """
        formatted = json.dumps(obj, sort_keys=True, indent=4)
        return formatted


    def get_docket(self, docket_id):
        """
        Makes call to regulations.gov and retrieves the docket
        """
        api_key = os.getenv('API_Key')
        response = requests.get("https://api.data.gov:443/regulations/v3/docket" +
                                ".json?api_key=" + api_key + "&docketId=" + docket_id)

        return self.__jformat(response.json())
