# Adam Krusic

from model.image import Image
from model.location import Location


class Dialogue:

    def __init__(self, text, x, y, background_file_path):
        location = Location(x, y)
        background = Image(background_file_path)
        self._create(text, location, background)

    def _create(self, text, location, background):
        self.text = text
        self.location = location
        self.background = background
