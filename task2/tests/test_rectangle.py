import sys
import pytest
from contextlib import nullcontext as does_not_raise

from task2.src.figures.rectangle import Rectangle


class TestRectangle:
    @pytest.fixture(params=[[[(5, -5), (2, -2), (5, 1), (8, -2)], does_not_raise()],
                            [[(0, 0), (1, 0), (1, 1), (0, 1)], does_not_raise()],
                            [[[0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5]], does_not_raise()],
                            [[(3, 3), (3, 3), (3, 3), (3, 3)], pytest.raises(Exception)],
                            [[(0, 0), (1, 0), (1, 1), (2, 1)], pytest.raises(Exception)],
                            [[(0, 0), (1, 0), (1, 1), ("str", 1)], pytest.raises(TypeError)],
                            [[(0, 0), (1, 0), (1, 1)], pytest.raises(ValueError)],
                            ['str', pytest.raises(ValueError)],
                            [["str1", "str2", "str3", "str4"], pytest.raises(TypeError)],
                            [[(0, 0), (1, 0), (1, 1), (0, 1, 2)], pytest.raises(ValueError)]])
    def get_params(self, request):
        return request.param

    @pytest.fixture
    def get_rectangle(self, get_params):
        return Rectangle(get_params[0])

    def test_get_coords(self, get_params, get_rectangle):
        assert get_rectangle.coords == get_params[0]

    @pytest.mark.parametrize("new_coords", [[(10, -5), (7, -2), (10, 1), (13, -2)],
                                            [(2, 0), (2, 2), (0, 2), (0, 0)],
                                            [(2.5, 0.5), (2.5, 2.5), (0.5, 2.5), (0.5, 0.5)],
                                            [[2, 0], [2, 2], [0, 2], [0, 0]]])
    def test_set_coords(self, get_rectangle, new_coords):
        get_rectangle.coords = new_coords
        assert get_rectangle.coords == new_coords

    def test_draw(self, get_rectangle, get_params, capfd):
        expectation = get_params[1]
        with expectation:
            get_rectangle.draw()
            a = get_rectangle.coords[0]
            b = get_rectangle.coords[1]
            c = get_rectangle.coords[2]
            d = get_rectangle.coords[3]
            captured = capfd.readouterr()
            assert captured.out == f"Drawing Rectangle: vertices in {a}, {b}, {c}, {d}\n"
