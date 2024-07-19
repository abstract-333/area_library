import math

from area_library.shape import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def is_right_triangle(self) -> bool:
        sorted_sides: list[float] = sorted([self.a, self.b, self.c])
        return math.isclose(
            sorted_sides[0] ** 2 + sorted_sides[1] ** 2,
            sorted_sides[2] ** 2,
        )

    def calculate_area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
