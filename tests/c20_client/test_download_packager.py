from c20_client import download_packager

DOWNLOAD_DATA = download_packager.package_downloads(
    {'data': 'test data', 'file_name': 'test_file',
     'file_type': 'pdf', 'folder_name': 'abc/docket-id-3/document-id-7/'},
    1, 2)

DOWNLOAD_HTML_DATA = download_packager.package_downloads(
    {'data': 'test data', 'file_name': 'test html file',
     'file_type': 'htm', 'folder_name': 'abc/docket-id-3/document-id-7/'},
    1, 2)

DOWNLOAD_EXCEL_DATA = download_packager.package_downloads(
    {'data': 'test data', 'file_name': 'test_excel file',
     'folder_name': 'abc/docket-id-3/document-id-7/', 'file_type': 'xlsx'},
    1, 2)


def test_client_id():
    assert DOWNLOAD_DATA['client_id'] == 1


def test_job_id():
    assert DOWNLOAD_DATA['job_id'] == 2


def test_folder_name():
    assert DOWNLOAD_DATA['data'][0]['folder_name'] ==\
           'abc/docket-id-3/document-id-7/'


def test_file_name():
    assert DOWNLOAD_DATA['data'][0]['file_name'] == 'test_file.pdf'


def test_html_file_name():
    assert DOWNLOAD_HTML_DATA['data'][0]['file_name'] == 'test_html_file.htm'


def test_excel_file_name():
    assert DOWNLOAD_EXCEL_DATA['data'][0]['file_name'] ==\
           'test_excel_file.xlsx'


def test_data():
    assert DOWNLOAD_DATA['data'][0]['data'] == 'test data'
