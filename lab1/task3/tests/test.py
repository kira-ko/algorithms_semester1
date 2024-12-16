import unittest

from lab1.task3.src.main import insertion_descending

class TestInsertionDescendingSort(unittest.TestCase):
    def test_insertion_descending(self):
        self.assertEqual(insertion_descending([31, 41, 59, 26, 41, 58]), [59, 58, 41, 41, 31, 26])

if __name__ == '__main__':
    unittest.main()