from collections import namedtuple


SavedItem = namedtuple('SavedItem', ['directory_name', 'filename', 'contents'])


class SpyDataRepository:

    def __init__(self):
        self.saved_items = []

    def save_data(self, directory_name, filename, contents):
        item = SavedItem(directory_name=directory_name,
                         filename=filename,
                         contents=contents)

        self.saved_items.append(item)
