import unittest
from lab4.task9.src.main import process_requests

class TestPolyclinicQueue(unittest.TestCase):
    def test_example1(self):
        commands = ["7", "+ 1", "+ 2", "-", "+ 3", "+ 4", "-", "-"]
        expected = [1, 2, 3]
        self.assertEqual(process_requests(commands), expected)

    def test_example2(self):
        commands = ["10", "+ 1", "+ 2", "* 3", "-", "+ 4", "* 5", "-", "-", "-", "-"]
        expected = [1, 3, 2, 5, 4]
        self.assertEqual(process_requests(commands), expected)


    def test_simple_case(self):
        commands = ["+ 1", "+ 2", "* 3", "-", "-"]
        expected = [1, 3]
        self.assertEqual(process_requests(commands), expected)

    def test_only_end_and_serve(self):
        commands = ["+ 10", "+ 20", "+ 30", "-", "-", "-"]
        expected = [10, 20, 30]
        self.assertEqual(process_requests(commands), expected)

    def test_large_case(self):
        commands = ["+ 1"] * 1000 + ["-"] * 1000
        expected = [1] * 1000
        self.assertEqual(process_requests(commands), expected)


if __name__ == "__main__":
    unittest.main()