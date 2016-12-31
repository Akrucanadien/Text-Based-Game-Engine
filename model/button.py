# Adam Krusic

## text and locations
from model.location import Location
from model.image import Image

class Button:

    def __init__(self, text, x, y, background_image_path):
        self.create(text, Location(x, y), Image(background_image_path))

    def create(self, text, location, background):
        self.text = text
        self.location = location
        self.background = background
