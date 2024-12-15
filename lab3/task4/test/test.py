import unittest

from lab3.task4.src.main import count_segments  # Импортируйте вашу функцию из исходного кода


class TestCountSegments(unittest.TestCase):

    def test_single_segment_single_point(self):
        segments = [(1, 5)]
        points = [3]
        expected = [1]
        result = count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_example1(self):
        segments = [(2, 3), (0, 5), (7, 10)]
        points = [1, 6, 11]
        expected = [1, 0, 0]
        result = count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_no_points_inside_segments(self):
        segments = [(1, 5), (6, 10)]
        points = [0, 11]
        expected = [0, 0]
        result = count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_example2(self):
        segments = [(1, 3), (-10, 10)]
        points = [-100, 100, 0]
        expected = [0, 0, 1]
        result = count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        segments = []
        points = []
        expected = []
        result = count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_no_segments(self):
        segments = []
        points = [1, 2, 3]
        expected = [0, 0, 0]
        result = count_segments(segments, points)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()