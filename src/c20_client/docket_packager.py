"""
Packages the docket endpoint to return
to the server as defined in the RESULTS.md
"""


def package_docket(docket, client_id, job_id):
    """
    Packages the docket endpoint match RESULTS.md
    """
    agency = docket['agencyAcronym']
    docket_id = docket['docketId']
    folder_name = agency + "/" + docket_id + "/"
    return ({
        'client_id': client_id,
        'job_id': job_id,
        'data': [{
            'folder_name': folder_name,
            'file_name': 'docket.json',
            'data': docket
            }]
    })
