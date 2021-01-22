from pathlib import Path


class ImageLoader():

    def __init__(self, url, get_file_method):
        self.url = url
        self.get_file_method = get_file_method

    def load(self, name):
        return Path(self.get_file_method(name, origin=self.url, untar=True))
