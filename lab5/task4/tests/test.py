import unittest
from lab5.task4.src.main import build_heap

class TestBuildHeap(unittest.TestCase):
    def test_example_1(self):
        data = [5, 4, 3, 2, 1]
        swaps = build_heap(data)
        self.assertEqual(data, [1, 2, 3, 5, 4])
        self.assertTrue(len(swaps) <= 4 * len(data))

    def test_example_2(self):
        data = [1, 2, 3, 4, 5]
        swaps = build_heap(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])
        self.assertEqual(len(swaps), 0)

    def test_large_case(self):
        data = [i for i in range(1000, 0, -1)]
        swaps = build_heap(data)
        self.assertTrue(len(swaps) <= 4 * len(data))

if __name__ == "__main__":
    unittest.main()