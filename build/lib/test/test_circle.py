from contextlib import nullcontext as does_not_raise

import pytest

from area_library import Circle


class TestTriangle:

    @pytest.mark.parametrize(
        argnames="radius, res, expectation",
        argvalues=[
            (10, 314.1592653589793, does_not_raise()),
            (3, 28.274333882308138, does_not_raise()),
        ],
    )
    def test_calculate_area(self, radius, res, expectation):
        with expectation:
            assert Circle(radius).calculate_area() == res
