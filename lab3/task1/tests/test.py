import unittest
from lab3.task1.src.main import randomized_quicksort

class TestQuickSort(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_random_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2]
        expected = [1, 1, 2, 3, 4, 5, 9]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_single_element_array(self):
        arr = [42]
        expected = [42]
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_empty_array(self):
        arr = []
        expected = []
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_large_array(self):
        arr = list(range(1000, 0, -1))  # От 1000 до 1
        expected = list(range(1, 1001))  # От 1 до 1000
        randomized_quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()
