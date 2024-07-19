from area_library.circle import Circle
from area_library.shape import Shape
from area_library.triangle import Triangle


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, *args) -> Shape:
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "triangle":
            return Triangle(*args)
        else:
            raise TypeError(f"Unknown shape type: {shape_type}")
