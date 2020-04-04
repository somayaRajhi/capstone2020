"""
Packages the documents endpoint to return
to the server as defined in the RESULTS.md
"""
import requests
from c20_client.json_jobs_helper import (
    get_docket_from_documents,
    get_document_from_documents
)


def package_documents(documents_list, client_id, job_id):
    """
    Packages the documents endpoint match RESULTS.md
    """
    documents_data_list = []
    jobs_list = []
    for documents in documents_list['documents']:
        agency = documents['agencyAcronym']
        docket_id = documents['docketId']
        document_id = documents['documentId']
        folder_name = agency + "/" + docket_id + "/" + document_id + "/"

        documents_data_list.append(
            {
                'folder_name': folder_name,
                'file_name': 'basic_document.json',
                'data': documents
            }
        )

        jobs_list.append(get_document_from_documents(documents))
        jobs_list.append(get_docket_from_documents(documents))

    documents = {
        'client_id': client_id,
        'job_id': job_id,
        'data': documents_data_list,
        'jobs': jobs_list
    }

    requests.post('http://capstone.cs.moravian.edu', documents)
    # Necessary for tests
    return documents
