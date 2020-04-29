
from collections import namedtuple

Data = namedtuple('Data', ['folder_name', 'file_name', 'contents'])


class MissingDataException(Exception):
    pass


class DataExtractor:

    @staticmethod
    def extract(list_of_data_dicts):
        ret = []

        for data_item in list_of_data_dicts:
            try:
                ret.append(Data(folder_name=data_item['folder_name'],
                                file_name=data_item['file_name'],
                                contents=data_item['data']))
            except TypeError:
                raise MissingDataException()
        return ret
