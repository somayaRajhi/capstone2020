from c20_client import documents_packager

TEST_JSON = {
    'documents': [{
        'agencyAcronym': 'test',
        'data': 'test Documents',
        'docketId': '3',
        'documentId': 'r13'
    }]
}


def test_get_documents():
    response = documents_packager.package_documents(TEST_JSON)
    assert response == {
        'client_id': 1,
        'data': [{
            'folder_name': 'test/3/r13/',
            'file_name': 'basic_documents.json',
            'data': {
                'agencyAcronym': 'test',
                'data': 'test Documents',
                'docketId': '3',
                'documentId': 'r13'
            }
        }]
    }
