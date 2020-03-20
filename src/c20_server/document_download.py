import requests
from c20_server import reggov_api_doc_error
import os
from dotenv import load_dotenv, find_dotenv


def extract_file_formats(document):
    if 'fileFormats' in document:
        file_formats = document['fileFormats']
        return file_formats
    return None


def extract_attachments(document):
    attachments = []
    temp = []
    if 'attachments' in document:
        for i in document['attachments']:
            attachments.append(i['fileFormats'])
            for num in attachments:
                temp += num
        return temp
    return None


def download_document(api_key, document_id=""):
    """
    downloads a file based on a url, api key and document_id (if given)
    """
    api_key = "&api_key=" + api_key
    document_id = "&documentId=" + document_id

    url = "https://api.data.gov:443/regulations/v3/document.json?"
    data = requests.get(url + api_key + document_id)

    print(data.json())

    if data.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if data.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if data.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if data.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException
    document = data.json()
    file_formats = extract_file_formats(document)
    file_attachments = extract_attachments(document)
    if file_formats:
        return document, file_formats
    return document, file_attachments



def main():
    load_dotenv(find_dotenv())
    api_key = os.getenv("API_KEY")
    doc_id = "BIS-2018-0006-47983" #fileformats[]
    #doc_id = "CMS-2005-0001-0001"  #one fileformat no attachments[]
    #doc_id = "FMCSA-1997-2350-21654" #one fileformats[] multiple entries
    result1 = download_document(api_key, doc_id)
    print(result1[1])
    #print(result2)


if __name__ == '__main__':
    main()
