from c20_client.json_jobs_helper import get_download_from_document


def package_document(document, client_id, job_id):
    document_id = document['documentId']['value']
    folder_name = (document['agencyAcronym']['value'] + "/" +
                   document['docketId']['value'] + "/" +
                   document_id + "/")
    data = [{
        'folder_name': folder_name,
        'file_name': 'basic_document.json',
        'data': document
    }]

    jobs_list = []

    if 'attachments' in document:
        jobs_list = get_jobs_list_from_attachments(document, folder_name)

    elif 'fileFormats' in document:
        jobs_list = get_jobs_list_from_file_format(document,
                                                   folder_name, document_id)

    return_document = {
        'client_id': client_id,
        'job_id': job_id,
        'data': data,
        'jobs': jobs_list
    }

    return return_document


def get_jobs_list_from_attachments(document, folder_name):
    jobs_list = []

    for attachment in document['attachments']:
        if 'fileFormats' in attachment:
            title = attachment['title']
            jobs_list += get_jobs_list_from_file_format(attachment,
                                                        folder_name, title)

    return jobs_list


def get_jobs_list_from_file_format(attachment, folder_name, file_name):
    file_formats = []

    for files in attachment['fileFormats']:
        file_formats.append(
            get_download_from_document(files, folder_name, file_name))

    return file_formats
