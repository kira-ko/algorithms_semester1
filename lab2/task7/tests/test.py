import unittest
from lab2.task7.src.main import max_subarray

class TestMaxSubarray(unittest.TestCase):
    def test1(self):
        self.assertEqual(max_subarray([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(max_subarray([-1, 2, 3, -9]), [2, 3])

    def test_one_element(self):
        self.assertEqual(max_subarray([-1, 2, 3, -9, 11]), [11])
        self.assertEqual(max_subarray([100, -9, 2, -3, 5]), [100])

    def test_single_array(self):
        self.assertEqual(max_subarray([6]), [6])
        self.assertEqual(max_subarray([1]), [1])