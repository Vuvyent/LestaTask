import sys
import pytest
from contextlib import nullcontext as does_not_raise

from task2.src.figures.triangle import Triangle


class TestTriangle:
    @pytest.fixture(params=[[[(2, 2), (3, 3), (1, 0)], does_not_raise()],
                            [[(3, 3), (3, 3), (3, 3)], pytest.raises(Exception)],
                            [[(2, 2), (3, 3), (1, 1)], pytest.raises(Exception)],
                            [[[2, 2], [3, 3], [1, 0]], does_not_raise()],
                            [[(2.2, 2.5), (3.8, 3.9), (1.9, 0.2)], does_not_raise()],
                            [[(2, 2), (3, "str"), (1, 0)], pytest.raises(TypeError)],
                            [[(2.2, 2.5), (3.8, 3.9)], pytest.raises(ValueError)],
                            ['str2', pytest.raises(ValueError)],
                            [["str1", "str2", "str3"], pytest.raises(TypeError)],
                            [[(2.2, 2.5, 3), (3.8, 3.9), (1.9, 2.3, 4.5)], pytest.raises(ValueError)]])
    def get_params(self, request):
        return request.param

    @pytest.fixture
    def get_triangle(self, get_params):
        return Triangle(get_params[0])

    def test_get_coords(self, get_params, get_triangle):
        assert get_triangle.coords == get_params[0]

    @pytest.mark.parametrize("new_coords", [[(3, 3), (4, 4), (5, 0)],
                                            [(3, 3), (4, 4), (5, 5)],
                                            [[3, 3], [4, 4], [5, 0]],
                                            [(3.2, 3.5), (3.6, 4.9), (2.9, 2.2)]])
    def test_set_coords(self, get_triangle, new_coords):
        get_triangle.coords = new_coords
        assert get_triangle.coords == new_coords

    def test_draw(self, get_triangle, get_params, capfd):
        expectation = get_params[1]
        with expectation:
            get_triangle.draw()
            a = get_triangle.coords[0]
            b = get_triangle.coords[1]
            c = get_triangle.coords[2]
            captured = capfd.readouterr()
            assert captured.out == f"Drawing Triangle: vertices in {a}, {b}, {c}\n"
