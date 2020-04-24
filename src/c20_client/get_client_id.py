"""
File used to check for an environment variable for id and to
get an id form server and assign the id to the enviornment
variable if the environment variable does not yet exist
"""
from os import getenv
import requests


def request_id():
    """
    Ask Moravian server endpoint for id
    Returns an id
    """
    response = requests.get('http://capstone.cs.moravian.edu/get_client_id')
    return response.json()['client_id']


def client_has_id():
    """
    Checks for the client id as a .env variable called CLIENT_ID
    """
    client_id = getenv("CLIENT_ID")

    # Client does not yet have an id
    if client_id is None:
        return False

    # Client has an id assigned
    return True


def save_client_env_variable(client_id):
    """
    Append client id to the environment varibale file
    Will create file if does not already exist
    """
    writer = open('.env', 'a+')
    writer.write("CLIENT_ID=" + str(client_id) + "\n")
    writer.close()
