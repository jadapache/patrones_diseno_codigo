import json
from abc import ABC


class BaseRepository(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        with open(self.filename, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
