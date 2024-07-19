from contextlib import nullcontext as does_not_raise

import pytest

from area_library import ShapeFactory, Triangle, Circle


class TestShapeFactory:

    @pytest.mark.parametrize(
        argnames="shape_type, a, b, c, res, expectation",
        argvalues=[
            (
                "triangle",
                1,
                2,
                1.5,
                Triangle(
                    1,
                    2,
                    1.5,
                ),
                does_not_raise(),
            ),
            ("rectangle", 1, 2, 1.5, Triangle(1, 2, 1.5), pytest.raises(TypeError)),
            ("circle", 1, 2, 1.5, Triangle(1, 2, 1.5), pytest.raises(TypeError)),
        ],
    )
    def test_create_shape_triangle(self, shape_type, a, b, c, res, expectation):
        with expectation:
            assert type(ShapeFactory.create_shape(shape_type, a, b, c)) == type(res)

    @pytest.mark.parametrize(
        argnames="shape_type, radius, res, expectation",
        argvalues=[
            ("circle", 1, Circle(1), does_not_raise()),
            ("triangle", 1, Circle(1), pytest.raises(TypeError)),
            ("square", 1, Circle(1), pytest.raises(TypeError)),
        ],
    )
    def test_create_shape_circle(self, shape_type, radius, res, expectation):
        with expectation:
            assert type(ShapeFactory.create_shape(shape_type, radius)) == type(res)
