import json

client_ID = 1


def package_documents(documents_list):
    for documents in documents_list['documents']:
        agency = documents['agencyAcronym']
        docket_ID = documents['docketId']
        document_ID = documents['documentId']
        folder_name = agency + "/" + docket_ID + "/" + document_ID + "/"

        return_documents = {
            'client_id': client_ID,
            #'job_id': 'job1',
            'data': [
                {
                    'folder_name': folder_name,
                    'file_name': 'basic_documents.json',
                    'data': documents
                }
            ]
        }
    return return_documents