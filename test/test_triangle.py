from contextlib import nullcontext as does_not_raise

import pytest

from area_library import Triangle


class TestTriangle:

    @pytest.mark.parametrize(
        argnames="a, b, c, res, expectation",
        argvalues=[
            (1, 2, 1.5, 0.7261843774138906, does_not_raise()),
            (10, 9, 12, 44.039045175843675, does_not_raise()),
        ],
    )
    def test_calculate_area(self, a, b, c, res, expectation):
        with expectation:
            assert Triangle(a, b, c).calculate_area() == res

    @pytest.mark.parametrize(
        argnames="a, b, c, res, expectation",
        argvalues=[
            (5, 5, 7.0710678118654752440084436210485, True, does_not_raise()),
            (5, 5, 6, False, does_not_raise()),
        ],
    )
    def test_is_right_triangle(self, a, b, c, res, expectation):
        with expectation:
            assert Triangle(a, b, c).is_right_triangle() == res
