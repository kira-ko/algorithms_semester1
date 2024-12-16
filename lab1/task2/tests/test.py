import unittest

from lab1.task2.src.main import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_index(self):
        ind, arr = insertion_sort([1, 8, 4, 2, 3, 7, 5, 6, 9, 0])
        self.assertEqual(arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(ind, [1, 2, 2, 2, 3, 5, 5, 6, 9, 1])


if __name__ == '__main__':
    unittest.main()