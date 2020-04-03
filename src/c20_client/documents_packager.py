"""
Packages the documents endpoint to return
to the server as defined in the RESULTS.md
"""

CLIENT_ID = 1


def package_documents(documents_list):
    """
    Packages the documents endpoint match RESULTS.md
    """
    return_documents = []
    for documents in documents_list['documents']:
        agency = documents['agencyAcronym']
        docket_id = documents['docketId']
        document_id = documents['documentId']
        folder_name = agency + "/" + docket_id + "/" + document_id + "/"

        return_documents.append({
            'client_id': CLIENT_ID,
            'data': [
                {
                    'folder_name': folder_name,
                    'file_name': 'basic_documents.json',
                    'data': documents
                }
            ]
        })
    return return_documents
