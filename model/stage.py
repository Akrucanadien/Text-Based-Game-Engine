# Adam Krusic
# Stage in a game
# 12/31/2016

from model.image import Image
from model.button import Button


class Stage:
    """
    Represents a single stage in a game
    One single stage generally translates to a single renderable screen
    """

    def __init__(self, name, background_file_path, button_data, dialogue):
        background = Image(background_file_path)

        buttons = []

        for button in button_data:
            xpos = button["x"]
            ypos = button["y"]
            text = button["text"]
            path = button["path"]

            button = Button(text, xpos, ypos, path)
            buttons.append(button)

        self._create(name, background, buttons, dialogue)


    def _create(self, name, background, buttons, dialogue):
        self.name = name
        self.background = background
        self.buttons = buttons
        self.dialogue = dialogue

