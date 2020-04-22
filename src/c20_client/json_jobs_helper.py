"""
Returns a single job for the various
endpoints of the JSON from regulations.gov
"""


def get_docket_from_documents(document):
    """
    Get the docket job from a single piece of
    the overall data in the documents endpoint
    """
    job = {
        'job_type': 'docket',
        'docket_id': document['docketId']
    }

    return job


def get_document_from_documents(document):
    """
    Get the document job from a single piece of
    the overall data in the documents endpoint
    """
    job = {
        'job_type': 'document',
        'document_id': document['documentId']
    }

    return job


def get_download_from_document(file, folder_name, file_name):
    """
    Get the download job from the data in the document endpoint
    """
    url = file.split('contentType=')

    jobs = {
        'job_type': 'download',
        'file_name': file_name,
        'file_type': url[1],
        'folder_name': folder_name,
        'url': file
    }

    return jobs
