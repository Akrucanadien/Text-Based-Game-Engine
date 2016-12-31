# Adam Krusic

from math import sqrt


class Location:
    """
    Represents an X-Y coordinate
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other_point):
        distance = sqrt(((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2))

        return distance
