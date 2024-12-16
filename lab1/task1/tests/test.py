import unittest

from lab1.task1.src.main import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()