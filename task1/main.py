from typing import Type

from area.figures import Circle, Triangle
from area.interface import BaseFigure


def get_figure_area(figure: Type[BaseFigure], *args):
    print(figure.get_area(*args))


if __name__ == '__main__':
    get_figure_area(Circle, 5)
    get_figure_area(Triangle, 3, 4, 5)
    get_figure_area(Triangle, 5, 4, 5)

    print(Triangle.is_right_triangle(3, 4, 5))
    print(Triangle.is_right_triangle(5, 4, 5))
