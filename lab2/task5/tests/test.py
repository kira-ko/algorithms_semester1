import unittest
from lab2.task5.src.task5 import majority

class TestMajorityElement(unittest.TestCase):

    def test_majority1(self):
        self.assertEqual(majority([2, 3, 9, 2, 2]), 1)
        self.assertEqual(majority([1, 2, 3, 4]), 0)

    def test_majority2(self):
        self.assertEqual(majority([1]), 1)
