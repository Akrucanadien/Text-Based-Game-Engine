# Adam Krusic

from pillow import Image as pillow_image


class Image:
    """
    Represents an image
    """

    def __init__(self, image_file_path):
        self.path = image_file_path
        self._get_image_dimensions()

    def _get_image_dimensions(self):
        """
        Returns the dimensions of an image
        """
        with pillow_image.open(self.path) as img:
            width, height = img.size
        
        self.width = width
        self.height = height
