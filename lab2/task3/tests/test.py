import unittest
from lab2.task3.src.main import inversions_numbers



class TestInversionsNumbers(unittest.TestCase):

    def test_inversions(self):
        array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        self.assertEqual(inversions_numbers(array, [0] * len(array), 0, len(array) -1 ), 17)
        self.assertEqual(inversions_numbers([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0, 4), 0)
        self.assertEqual(inversions_numbers([5, 4, 3, 2, 1], [5, 4, 3, 2, 1], 0, len([5, 4, 3, 2, 1])-1), 10)

    def test_empty_array(self):
        self.assertEqual(inversions_numbers([], [], 0, len([])-1 ), 0)


if __name__ == '__main__':
    unittest.main()