def package_downloads(download_job, client_id, job_id):
    docketid = download_job['docketid']
    documentid = download_job['documentid']
    folder_name = (download_job['agency'] + "/" + docketid + "/"
                   + documentid + "/")
    data = [{
        'folder_name': folder_name,
        # may need to change this
        'file_name': documentid + '.' + download_job['file_type'],
        'data': download_job['data']
    }]

    return_download = {
        'client_id': client_id,
        'job_id': job_id,
        'data': data,
    }
    return return_download
