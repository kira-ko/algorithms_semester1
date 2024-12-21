import unittest
from lab6.task5.src.main import calculate_votes

class TestCalculateVotes(unittest.TestCase):

    def test_single_candidate(self):
        input_lines = [
            "Smith 10",
            "Smith 20",
            "Smith 30"
        ]
        expected = {"Smith": 60}
        self.assertEqual(calculate_votes(input_lines), expected)

    def test_multiple_candidates(self):
        input_lines = [
            "Smith 10",
            "Johnson 15",
            "Smith 20",
            "Johnson 25",
            "Doe 5"
        ]
        expected = {
            "Smith": 30,
            "Johnson": 40,
            "Doe": 5
        }
        self.assertEqual(calculate_votes(input_lines), expected)

    def test_no_votes(self):
        input_lines = []
        expected = {}
        self.assertEqual(calculate_votes(input_lines), expected)

    def test_lexicographical_order(self):
        input_lines = [
            "Zane 50",
            "Alice 30",
            "Bob 20"
        ]
        result = calculate_votes(input_lines)
        sorted_candidates = sorted(result.keys())
        self.assertEqual(sorted_candidates, ["Alice", "Bob", "Zane"])

if __name__ == "__main__":
    unittest.main()

