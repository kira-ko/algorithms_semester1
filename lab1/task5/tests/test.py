import unittest

from lab1.task5.src.main import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()