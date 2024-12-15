import unittest
from lab4.task3.src.main import is_correct_sequence, process_sequences


class TestBracketSequence(unittest.TestCase):
    def test_valid_sequences(self):
        self.assertEqual(is_correct_sequence("()"), "YES")
        self.assertEqual(is_correct_sequence("[]"), "YES")
        self.assertEqual(is_correct_sequence("()[]"), "YES")
        self.assertEqual(is_correct_sequence("(())"), "YES")
        self.assertEqual(is_correct_sequence("([])"), "YES")
        self.assertEqual(is_correct_sequence("[([])]"), "YES")

    def test_invalid_sequences(self):
        self.assertEqual(is_correct_sequence(")("), "NO")
        self.assertEqual(is_correct_sequence("["), "NO")
        self.assertEqual(is_correct_sequence("])"), "NO")
        self.assertEqual(is_correct_sequence("(("), "NO")
        self.assertEqual(is_correct_sequence("([)]"), "NO")
        self.assertEqual(is_correct_sequence("[(])"), "NO")

    def test_process_sequences(self):
        sequences = ["()", "([])", "[([)])", "((()))", "(]", "[()]"]
        expected = ["YES", "YES", "NO", "YES", "NO", "YES"]
        self.assertEqual(process_sequences(sequences), expected)


if __name__ == "__main__":
    unittest.main()