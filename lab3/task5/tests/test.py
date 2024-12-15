import unittest
from lab3.task5.src.main import h_index

class TestHIndex(unittest.TestCase):
    def test_case_1(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        self.assertEqual(h_index(citations), expected)

    def test_case_2(self):
        citations = [1, 3, 1]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_case_3(self):
        citations = [0, 0, 0]
        expected = 0
        self.assertEqual(h_index(citations), expected)

    def test_case_4(self):
        citations = [10, 8, 5, 4, 3]
        expected = 4
        self.assertEqual(h_index(citations), expected)

    def test_case_5(self):
        citations = [25, 8, 5, 3, 3]
        expected = 3
        self.assertEqual(h_index(citations), expected)

if __name__ == "__main__":
    unittest.main()