"""
Packages the documents endpoint to return
to the server as defined in the RESULTS.md
"""
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
        folder_name = (documents['agencyAcronym'] + "/" +
                       documents['docketId'] + "/" +
                       documents['documentId'] + "/")

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

    return documents
