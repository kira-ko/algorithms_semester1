import unittest
from lab2.task4.src.main import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binarysearch1(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 8), -1)

    def test_binarysearch2(self):
        self.assertEqual(binary_search([], 1), -1)