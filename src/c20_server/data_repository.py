import os
from pathlib import Path


class DataRepository:

    def __init__(self, base_path):
        self.base_path = base_path

    def save_data(self, directory_name, filename, contents):
        self.ensure_directory_exists(directory_name)
        path = os.path.join(self.base_path, directory_name, filename)
        with open(path, 'w') as file:
            file.write(contents)

    def ensure_directory_exists(self, directory_name):
        Path(os.path.join(self.base_path, directory_name))\
            .mkdir(parents=True, exist_ok=True)
