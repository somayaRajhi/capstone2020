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
    jobs_list += find_file_formats(document)

    if 'attachments' in document:
        for attachment in document['attachments']:
            jobs_list += find_file_formats(attachment)

    return jobs_list


def find_file_formats(attachment):
    file_formats = []
    if 'fileFormats' in attachment:
        for files in attachment['fileFormats']:
            file_formats.append(
                json_jobs_helper.get_download_from_document(files))
    return file_formats
