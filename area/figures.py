import math
from abc import ABC
from math import pi

from area.interface import BaseFigure


class Circle(BaseFigure):
    @staticmethod
    def get_area(radius: float, *args) -> float:
        if radius < 0:
            raise ValueError('The radius cannot be negative')

        return pi * radius ** 2


class Triangle(BaseFigure):
    @staticmethod
    def get_area(a: float, b: float, c: float, *args) -> float:
        Triangle.is_triangle(a, b, c)
        p = (a + b + c) / 2
        s = p * (p - a) * (p - b) * (p - c)

        return math.sqrt(s)

    @staticmethod
    def is_right_triangle(a: float, b: float, c: float) -> bool:
        Triangle.is_triangle(a, b, c)
        arr = [a, b, c]
        arr.sort(reverse=True)
        condition = arr[0] ** 2 == arr[1] ** 2 + arr[2] ** 2

        return condition

    @staticmethod
    def is_triangle(a: float, b: float, c: float) -> None:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('The sides of a triangle cannot be negative or equal to zero')

        if a + b <= c:
            raise ValueError('These sides do not form a triangle')
