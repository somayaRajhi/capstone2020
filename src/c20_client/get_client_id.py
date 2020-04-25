"""
File used to check for an environment variable for id and to
get an id form server and assign the id to the enviornment
variable if the environment variable does not yet exist
"""
from os import getenv
import requests
from dotenv import load_dotenv
from c20_client.connection_error import NoConnectionError

load_dotenv()

class IdManager():
    """
    Manages id functions for getting, saving, and
    checking the existence of an id
    """

    def check(self):
        """
        Checks for an id, if not exist the Manager makes
        the request for an id and saves it
        """
        # If client does not have an id
        if not self.client_has_id():
            self.save_client_env_variable(self.request_id)


    def request_id(self):
        """
        Ask Moravian server endpoint for id
        Returns an id
        """
        try:
            response = requests.get('http://capstone.cs.moravian.edu/get_user_id')
        except Exception:
            raise NoConnectionError

        return response.json()['user_id']


    def client_has_id(self):
        """
        Checks for the client id as a .env variable called CLIENT_ID
        """
        print('checking')
        client_id = self.get_id()
        print('HAS IT')
        print(client_id)
        print('^^^^^^^^^^^^^')
        # Client does not yet have an id
        if client_id is None:
            return False

        # Client has an id assigned
        return True


    def save_client_env_variable(self, client_id):
        """
        Append client id to the environment varibale file
        Will create file if does not already exist
        """
        writer = open('.env', 'a+')
        writer.write("CLIENT_ID=" + str(client_id) + "\n")
        writer.close()

    def get_id(self):
        """
        Gets the id from the env variable
        """
        print ('------>' + str(getenv("CLIENT_ID")) + '<---------')
        return getenv("CLIENT_ID")
