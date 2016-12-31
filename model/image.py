# Adam Krusic

class Image:
    """
    Represents an image
    """

    def __init__(self, image_file_path):
        self.path = image_file_path
        self._get_image_dimensions()

    def _get_image_dimensions(self):
        pass
        # TODO: Get dimensions of the image
