import unittest
from lab2.task8.src.main import multiplication_polynomials

class MyltiplicationPolynomialsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(multiplication_polynomials([8, 9, 10], [10, 12, 2], 3), [80, 186, 224, 138, 20])
        self.assertEqual(multiplication_polynomials([3, 9, 5], [5, 12, 2], 3), [15, 81, 139, 78, 10])

    def test_negative_numbers(self):
        self.assertEqual(multiplication_polynomials([-1, -9, -100], [-1, 12, 2], 3), [1, -3, -10, -1218, -200])
        self.assertEqual(multiplication_polynomials([-1, -2, -5], [-1, -4, 2], 3), [1, 6, 11, 16, -10])

    def test_fifth_degree(self):
        self.assertEqual(multiplication_polynomials([1, -4, -3, -2, -1, -1], [5, 0, 0, -4, 0, 0], 6), [5, -20, -15, -14, 11, 7, 8, 4, 4, 0, 0])
