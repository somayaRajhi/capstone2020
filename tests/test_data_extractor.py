
import pytest
from c20_server.data_extractor import DataExtractor, MissingDataException


@pytest.fixture(name='extractor')
def make_extractor():
    return DataExtractor()


def test_empty_data(extractor):
    results = extractor.extract([])
    assert results == []


def make_dict_item(number):
    return {'folder_name': 'the/directory/{}'.format(number),
            'file_name': 'filename{}.json'.format(number),
            'data': 'file{}\ncontents\n'.format(number)}


def test_extract_single_item(extractor):
    dict_item = make_dict_item(1)
    results = extractor.extract([dict_item])

    assert len(results) == 1
    data_item = results[0]
    assert data_item.folder_name == 'the/directory/1'
    assert data_item.file_name == 'filename1.json'
    assert data_item.contents == 'file1\ncontents\n'


def assert_data_item(data_item, number):
    assert data_item.folder_name == 'the/directory/{}'.format(number)
    assert data_item.file_name == 'filename{}.json'.format(number)
    assert data_item.contents == 'file{}\ncontents\n'.format(number)


def test_extract_multiple_items(extractor):
    dict_item1 = make_dict_item(1)
    dict_item2 = make_dict_item(2)
    results = extractor.extract([dict_item1, dict_item2])

    assert len(results) == 2
    assert_data_item(results[0], 1)
    assert_data_item(results[1], 2)


def test_missing_field_gives_exception(extractor):
    missing_data = {'folder_name': 'the/directory/',
                    'file_name': 'filename{}.json'
                    }
    with pytest.raises(MissingDataException):
        extractor.extract(missing_data)
