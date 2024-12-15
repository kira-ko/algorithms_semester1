import unittest
from lab4.task1.src.main import process_stack


class TestStack(unittest.TestCase):
    def test_case_example(self):
        commands = [
            "6",
            "+ 1",
            "+ 10",
            "-",
            "+ 2",
            "+ 1234",
            "-"
        ]
        expected = [10, 1234]
        self.assertEqual(process_stack(commands), expected)


    def test_case_1(self):
        commands = [
            "+ 5",
            "+ 10",
            "-",
            "+ 15",
            "-",
            "-"
        ]
        expected = [10, 15, 5]
        self.assertEqual(process_stack(commands), expected)

    def test_case_2(self):
        commands = [
            "+ 1",
            "+ 2",
            "+ 3",
            "-",
            "-",
            "-"
        ]
        expected = [3, 2, 1]
        self.assertEqual(process_stack(commands), expected)

    def test_case_3(self):
        commands = [
            "+ 100",
            "-",
            "+ 200",
            "+ 300",
            "-",
            "-"
        ]
        expected = [100, 300, 200]
        self.assertEqual(process_stack(commands), expected)

    def test_case_4(self):
        commands = [
            "+ 42",
            "+ 17",
            "-",
            "+ 8",
            "+ 9",
            "-",
            "-",
            "-"
        ]
        expected = [17, 9, 8, 42]
        self.assertEqual(process_stack(commands), expected)


if __name__ == "__main__":
    unittest.main()