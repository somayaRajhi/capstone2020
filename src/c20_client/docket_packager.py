"""
Packages the docket endpoint to return
to the server as defined in the RESULTS.md
"""

CLIENT_ID = 1


def package_docket(docket):
    """
    Packages the docket endpoint match RESULTS.md
    """
    agency = docket['agencyAcronym']
    docket_id = docket['docketId']
    folder_name = agency + "/" + docket_id + "/"
    return ({
        'client_id': CLIENT_ID,
        'data': [
            {
                'folder_name': folder_name,
                'file_name': 'basic_docket.json',
                'data':
                    {
                        'agency': agency,
                        'docketId': docket_id,
                        'file_contents': docket

                    }
            }]
    })
