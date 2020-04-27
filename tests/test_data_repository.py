
from unittest.mock import mock_open
from c20_server.data_repository import DataRepository


class DummyMakeDirDataRepository(DataRepository):
    def __init__(self, base_path):
        super().__init__(base_path)
        self.ensure_directory_exists_called = False

    def ensure_directory_exists(self, directory_name):
        self.ensure_directory_exists_called = True


def test_class_saves_data(mocker):
    file_mock = mocker.patch('c20_server.data_repository.open', mock_open())
    data_repo = DummyMakeDirDataRepository('data')
    directory = 'FAA/DOC-ID/'
    filename = 'document.json'
    contents = 'foo\nbar\n'
    data_repo.save_data(directory, filename, contents)

    file_mock.assert_called_once_with('data/FAA/DOC-ID/document.json', 'w')
    file_mock().write.assert_called_once_with(contents)
    assert data_repo.ensure_directory_exists_called
