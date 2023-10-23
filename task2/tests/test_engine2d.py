import sys

import pyasn1_modules.rfc5275
import pytest
from contextlib import nullcontext as does_not_raise

from task2.src.figures.figure import Figure
from task2.src.figures.triangle import Triangle
from task2.src.figures.circle import Circle
from task2.src.figures.rectangle import Rectangle
from task2.src.engine2d.engine2d import Engine2D


class TestEngine2D:
    # @pytest.fixture(params=[[[255, 200, 255], does_not_raise()],
    #                         [(0, 0, 0), does_not_raise()],
    #                         [[2312, 323, 32], pytest.raises(ValueError)]
    #                         [[15.5, 100.25, 23.56], pytest.raises(TypeError)],
    #                         [[255, 255], pytest.raises(ValueError)],
    #                         ["string", pytest.raises(TypeError)]])
    # def get_params(self, request):
    #     return request.param

    @pytest.fixture
    def get_engine2d(self):
        return Engine2D([255, 255, 255])

    def test_get_color(self, get_engine2d):
        assert get_engine2d.color == [255, 255, 255]

    @pytest.mark.parametrize("new_color, expectation", [[[176, 223, 244], does_not_raise()],
                                                        [(5, 5, 5), does_not_raise()],
                                                        [[4223, 34223, 52], pytest.raises(ValueError)],
                                                        [[234.5, 122.25, 33.56], pytest.raises(TypeError)],
                                                        [[100, 100], pytest.raises(ValueError)],
                                                        ["string2", pytest.raises(TypeError)]])
    def test_set_color(self, get_engine2d, new_color, expectation):
        with expectation:
            get_engine2d.set_color(new_color)
            assert get_engine2d.color == new_color

    def test_get_canvas(self, get_engine2d):
        assert get_engine2d.canvas == []

    @pytest.mark.parametrize("new_elemnt, expectation", [[Circle((2, 2), 5), does_not_raise()],
                                                         [Triangle([(2, 2), (5, 5), (2, 5)]), does_not_raise()],
                                                         [Rectangle([(0, 0), (1, 0), (1, 1), (0, 1)]), does_not_raise()],
                                                         ["string", pytest.raises(TypeError)],
                                                         [[54, 23], pytest.raises(TypeError)]])
    def test_add_element(self, get_engine2d, new_elemnt, expectation):
        with expectation:
            get_engine2d.add_element(Circle((100, 100), 50))
            get_engine2d.add_element(new_elemnt)
            assert len(get_engine2d.canvas) == 2

    @pytest.mark.parametrize("idx, expectation", [[0, does_not_raise()],
                                                  [2, does_not_raise()],
                                                  [5, pytest.raises(IndexError)]])
    def test_delete_element(self, get_engine2d, expectation, idx):
        with expectation:
            get_engine2d.add_element(Circle((100, 100), 50))
            get_engine2d.add_element(Circle((2, 2), 5))
            get_engine2d.add_element(Triangle([(2, 2), (5, 5), (2, 5)]))
            get_engine2d.add_element(Rectangle([(0, 0), (1, 0), (1, 1), (0, 1)]))
            old_num_of_elements = len(get_engine2d.canvas)
            get_engine2d.delete_element(idx)
            new_num_of_elements = len(get_engine2d.canvas)
            assert old_num_of_elements-new_num_of_elements == 1

    def test_draw(self, get_engine2d, capfd):
        get_engine2d.add_element(Circle((100, 100), 50))
        get_engine2d.add_element(Rectangle([(0, 0), (1, 0), (1, 1), (0, 1)]))
        old_canvas_len = len(get_engine2d.canvas)
        get_engine2d.draw()
        get_engine2d.set_color([100, 100, 0])
        get_engine2d.add_element(Circle((100, 100), 30))
        get_engine2d.add_element(Rectangle([(0, 0), (1, 0), (1, 1), (0, 1)]))
        get_engine2d.draw()
        new_canvas_len = len(get_engine2d.canvas)
        captured = capfd.readouterr()
        assert old_canvas_len == 2 and new_canvas_len == 0 and \
               captured.out == "Current color is [255, 255, 255]: Drawing Circle: center in (100, 100) " \
                               "and radius 50\nCurrent color is [255, 255, 255]: Drawing Rectangle: " \
                               "vertices in (0, 0), (1, 0), (1, 1), (0, 1)\nCurrent color is [100, 100, 0]: " \
                               "Drawing Circle: center in (100, 100) and radius 30\nCurrent color is [100, 100, 0]: " \
                               "Drawing Rectangle: vertices in (0, 0), (1, 0), (1, 1), (0, 1)\n"




