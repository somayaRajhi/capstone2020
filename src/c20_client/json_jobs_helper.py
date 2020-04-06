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


def get_download_from_document(document):
    """
    Get the download job from the data in the document endpoint
    """
    file_formats = find_formats(document)

    jobs = {
        'job_type': 'download',
        'fileFormats': file_formats
    }
    return jobs


def find_formats(document):
    if 'attachments' in document:
        file_formats = []
        for formats in document['attachments']:
            file_formats += formats['fileFormats']
    else:
        file_formats = document['fileFormats']
    return file_formats
