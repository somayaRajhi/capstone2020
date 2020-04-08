from c20_client import json_jobs_helper


def package_document(document, client_id, job_id):
    folder_name = (document['agencyAcronym']['value'] + "/" +
                   document['docketId']['value'] + "/" +
                   document['documentId']['value'] + "/")
    data = [{
        'folder_name': folder_name,
        'file_name': 'basic_document.json',
        'data': document
    }]

    jobs_list = get_jobs_list(document)

    return_document = {
        'client_id': client_id,
        'job_id': job_id,
        'data': data,
        'jobs': jobs_list
    }

    return return_document


def get_jobs_list(document):
    jobs_list = []
    if 'fileFormats' in document:
        for files in document['fileFormats']:
            jobs_list.append(
                json_jobs_helper.get_download_from_document(files))

    if 'attachments' in document:
        for attachment in document['attachments']:
            for files in attachment['fileFormats']:
                jobs_list.append(
                    json_jobs_helper.get_download_from_document(files))

    return jobs_list
