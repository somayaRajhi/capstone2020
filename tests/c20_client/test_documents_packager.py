from c20_client import documents_packager

TEST_JSON = {
    'documents': [{
        'agencyAcronym': 'test',
        'data': 'test Documents',
        'docketId': 'docket-number-3',
        'documentId': 'document-number-15'
    }]
}


def test_get_documents():
    response = documents_packager.package_documents(TEST_JSON)
    assert response == {
        'client_id': 1,
        'data': [{
            'folder_name': 'test/docket-number-3/document-number-15/',
            'file_name': 'basic_documents.json',
            'data': {
                'agencyAcronym': 'test',
                'data': 'test Documents',
                'docketId': 'docket-number-3',
                'documentId': 'document-number-15'
            }
        }]
    }


def test_client_id():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['client_id'] == 1


def test_folder_name():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['data'][0]['folder_name'] ==\
        'test/docket-number-3/document-number-15/'


def test_file_name():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['data'][0]['file_name'] == 'basic_documents.json'


def test_agency_acronym():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['data'][0]['data']['agencyAcronym'] == 'test'


def test_data():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['data'][0]['data']['data'] == 'test Documents'


def test_docket_id():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['data'][0]['data']['docketId'] == 'docket-number-3'


def test_document_id():
    response = documents_packager.package_documents(TEST_JSON)
    assert response['data'][0]['data']['documentId'] == 'document-number-15'
