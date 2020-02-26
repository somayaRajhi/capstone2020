from cs334demo import customError
from dotenv import load_dotenv, find_dotenv
import os
import requests


def download_file(URL, api_key, documentId = ""):
    if(documentId == ""):
        data = requests.get(url=URL + api_key + '&rpp=1')
    else:
        data = requests.get(url=URL + api_key + "documentId=" + documentId)
    if data.status_code == 403:
        raise customError.IncorrectApiKey
    if data.status_code == 429:
        raise customError.ThousandCalls
    if data.status_code == 404:
        raise customError.BadID
    document = data.json()
    return document


def main():
    load_dotenv(find_dotenv())
    api_key = os.getenv("API_KEY")
    result = download_file('https://api.data.gov:443/regulations/v3/documents.json?', 'api_key=' + api_key)
    print(result)

if __name__ == "__main__":
    main()
