from c20_client import json_jobs_helper


def package_document(document, client_id, job_id):
    folder_name = (document['agencyName']['value'] + "/" +
                   document['docketId']['value'] + "/" +
                   document['documentId']['value'] + "/")
    data = {
        'folder_name': folder_name,
        'file_name': 'basic_document.json',
        'data': document
    }

    jobs_list = []
    if 'fileFormats' in document or 'attachments' in document:
        jobs_list = json_jobs_helper.get_download_from_document(document)

    return_document = {
        'client_id': client_id,
        'job_id': job_id,
        'data': data,
        'jobs': jobs_list
    }

    return return_document
