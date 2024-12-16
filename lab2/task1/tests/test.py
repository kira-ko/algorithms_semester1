import unittest

from lab2.task1.src.main import merge_sort

class TestMergeSort(unittest.TestCase):
    def test1(self):
        self.assertEqual(merge_sort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])

    def test2(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test3(self):
        self.assertEqual(merge_sort([8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test4(self):
        self.assertEqual(merge_sort([3]), [3])

    def test_5(self):
        self.assertEqual(merge_sort([]), [])

    def test6(self):
        array = [1000000000, 999999999, 999999998]
        self.assertEqual(merge_sort(array), [999999998, 999999999, 1000000000])


if __name__ == '__main__':
    unittest.main()