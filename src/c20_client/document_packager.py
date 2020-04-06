from c20_client import json_jobs_helper


def package_document(document, client_id, job_id):
    folder_name = (document['agencyName']['value'] + "/" +
                   document['docketId']['value'] + "/" +
                   document['documentId']['value'] + "/")
    data = [{
        'folder_name': folder_name,
        'file_name': 'basic_document.json',
        'data': document
    }]

    jobs_list = []
    if 'fileFormats' in document:
        for file in document['fileFormats']:
            jobs_list.append(json_jobs_helper.get_download_from_document(file))

    if 'attachments' in document:
        for attachment in document['attachments']:
            for file in attachment['fileFormats']:
                jobs_list.append(json_jobs_helper.get_download_from_document(file))

    return_document = {
        'client_id': client_id,
        'job_id': job_id,
        'data': data,
        'jobs': jobs_list
    }

    return return_document
