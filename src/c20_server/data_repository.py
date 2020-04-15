import os


class DataRepository:

    @staticmethod
    def save_data(directory_name, filename, contents):
        path = os.path.join('data', directory_name, filename)
        with open(path, 'w') as file:
            file.write(contents)
