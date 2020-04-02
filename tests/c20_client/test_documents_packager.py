from c20_client import compute_jobs, documents_packager
import json

test_json = {
                'documents': [{
                        'agencyAcronym': 'test',
                        'data': 'test Documents',
                        'docketId': '3',
                        'documentId': 'r13'
                    }
                ]
            }


def test_get_documents():
    response = documents_packager.package_documents(test_json)
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

