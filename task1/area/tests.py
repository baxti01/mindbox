import unittest
from math import pi
from figures import Circle, Triangle


class TestCircle(unittest.TestCase):

    def test_area_positive(self):
        self.assertAlmostEqual(Circle.get_area(5), pi * 25)

    def test_area_zero_radius(self):
        self.assertEqual(Circle.get_area(0), 0)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle.get_area(-5)


class TestTriangle(unittest.TestCase):

    def test_area_positive(self):
        self.assertAlmostEqual(Triangle.get_area(3, 4, 5), 6)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle.get_area(1, 1, 2)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle.get_area(-3, 4, 5)

    def test_is_right_triangle_positive(self):
        self.assertEqual(Triangle.is_right_triangle(3, 4, 5), True)

    def test_is_right_triangle_negative(self):
        self.assertEqual(Triangle.is_right_triangle(5, 4, 5), False)

    def test_is_right_triangle_invalid(self):
        with self.assertRaises(ValueError):
            Triangle.is_right_triangle(-5, 4, 5)


if __name__ == '__main__':
    unittest.main()
