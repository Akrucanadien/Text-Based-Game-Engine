# Adam Krusic

## text and locations
from model.location import Location
from model.image import Image

class Button:

    def __init__(self, text, x, y, background_image_path):
        location = Location(x, y)
        image = Image(background_image_path)

        self._create(text, location, image)

    def _create(self, text, location, background):
        self.text = text
        self.location = location
        self.background = background

    def wire(self, action):
        self.action = action
