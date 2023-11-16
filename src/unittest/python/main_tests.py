import numpy as np
import unittest

from main import bezier_curve, binomial_coefficient, visualisation


class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.points = np.array([[1, 9], [8, 16], [16, 8], [8, 1], [1, 7], [8, 9]])

    def test_binomial(self):
        expected = 10.0
        result = binomial_coefficient(5, 2)
        self.assertEqual(result, expected)

    def test_bezier_curve(self):
        expected = [[1.0, 9.0],
                    [5.984426874999999, 11.402976562499997],
                    [9.537729375000001, 9.3035703125],
                    [9.1875, 6.96875],
                    [6.520340000000001, 5.876250000000001],
                    [5.4540106250000004, 7.1022421875],
                    [8.0, 9.0]]
        result = bezier_curve(self.points, num_samples=7)
        self.assertEqual(result.tolist(), expected)
        self.assertIsInstance(result, type(self.points))

    def test_visualisation(self):
        result = visualisation(bezier_curve(self.points, num_samples=7), self.points)
        self.assertIsNone(result)
