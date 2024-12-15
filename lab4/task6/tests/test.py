import unittest
from lab4.task6.src.main import process_commands


class TestQueueWithMin(unittest.TestCase):
    def test_example(self):
        commands = ["7", "+ 1", "?", "+ 10", "?", "-", "?", "-"]
        expected = [1, 1, 10]
        self.assertEqual(process_commands(commands), expected)

    def test_all_push(self):
        commands = ["+ 5", "+ 2", "+ 8", "+ 1", "?"]
        expected = [1]
        self.assertEqual(process_commands(commands), expected)

    def test_alternating_commands(self):
        commands = ["+ 10", "?", "+ 5", "?", "-", "?", "-"]
        expected = [10, 5, 5]
        self.assertEqual(process_commands(commands), expected)

    def test_large_input(self):
        commands = ["+ 1"] * 1000 + ["?"] * 500 + ["-"] * 500
        expected = [1] * 500
        self.assertEqual(process_commands(commands), expected)


if __name__ == "__main__":
    unittest.main()