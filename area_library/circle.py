import math

from area_library.shape import Shape


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius**2
