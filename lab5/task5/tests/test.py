import unittest
from lab5.task5.src.main import task_scheduler

class TestTaskScheduler(unittest.TestCase):
    def test_case_1(self):
        n, tasks = 2, [1, 2, 3, 4, 5]
        expected = [
            (0, 0),
            (1, 0),
            (0, 1),
            (1, 2),
            (0, 4)
        ]
        self.assertEqual(task_scheduler(n, tasks), expected)

    def test_case_2(self):
        n, tasks = 4, [1, 1, 1, 1, 1, 1, 1, 1]
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
        ]
        self.assertEqual(task_scheduler(n, tasks), expected)

    def test_case_3(self):
        n, tasks = 1, [10, 5, 15]
        expected = [
            (0, 0),
            (0, 10),
            (0, 15),
        ]
        self.assertEqual(task_scheduler(n, tasks), expected)

    def test_case_4(self):
        n, tasks = 3, [3, 3, 3, 3, 3]
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 3),
            (1, 3),
        ]
        self.assertEqual(task_scheduler(n, tasks), expected)

if __name__ == "__main__":
    unittest.main()