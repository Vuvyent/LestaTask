import sys
import pytest
from contextlib import nullcontext as does_not_raise

from task2.src.figures.circle import Circle


class TestCircle:
    @pytest.fixture(params=[[[(2, 2), 3], does_not_raise()],
                            [[[2, 2], 3], does_not_raise()],
                            [[(2.5, 2.5), 2.6], does_not_raise()],
                            [((2, 2), 3), does_not_raise()],
                            [["str1", "str2"], pytest.raises(TypeError)],
                            [[("str1", "str2"), 2], pytest.raises(TypeError)],
                            [[(2, 2), "str1"], pytest.raises(TypeError)],
                            [[(2, 2, 2), 3], pytest.raises(ValueError)],
                            [[(2, 2), 0], pytest.raises(ValueError)]])
    def get_params(self, request):
        return request.param

    @pytest.fixture
    def get_circle(self, get_params):
        return Circle(get_params[0][0], get_params[0][1])

    def test_get_center(self, get_params, get_circle):
        assert get_circle.center == get_params[0][0]

    def test_get_r(self, get_params, get_circle):
        assert get_circle.r == get_params[0][1]

    @pytest.mark.parametrize("new_center", [[3, 3],
                                            (3, 3),
                                            (3.0, 3.0)])
    def test_set_center(self, get_circle, new_center):
        get_circle.center = new_center
        assert get_circle.center == new_center

    @pytest.mark.parametrize("new_r", [2, 2.3])
    def test_set_r(self, get_circle, new_r):
        get_circle.r = new_r
        assert get_circle.r == new_r

    def test_draw(self, get_circle, get_params, capfd):
        expectation = get_params[1]
        with expectation:
            get_circle.draw()
            r = get_circle.r
            center = get_circle.center
            captured = capfd.readouterr()
            assert captured.out == f"Drawing Circle: center in {center} and radius {r}\n"
