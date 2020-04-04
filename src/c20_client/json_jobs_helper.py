"""
Returns a single job for the various endpoints of the JSON from regulations.gov
"""

def get_jobs_from_documents(document):
    """
    Get the job from a single piece of the overall data in the documents endpoint
    """

    jobs = {
        'job_type': 'document',
        'document_id': document['documentId']
    }, {
        'job_type': 'docket',
        'docket_id': document['docketId']
    }

    return jobs


def get_jobs_from_document(document):
    """
    Get the job from the data in the document endpoint
    """
    jobs = document
    jobs = {
        'job_type': 'download',
        "fileFormats": ['urls']
    }

    return jobs
