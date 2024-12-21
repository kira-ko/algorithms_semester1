import unittest
from io import StringIO

from lab7.task7.src.main import main

class TestPatternMatching(unittest.TestCase):

    def setUp(self):
        self.input_data = ""
        self.output = StringIO()

    def run_main(self, input_data):
        """Запуск основного алгоритма и возврат результата"""
        self.input_data = input_data
        output_file = StringIO()
        main(self.input_data, output_file)
        return output_file.getvalue().strip()

    def test_exact_match(self):
        input_data = """abc
abc"""
        expected_output = "YES"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_wildcard_question_mark(self):
        input_data = """a?c
abc"""
        expected_output = "YES"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_wildcard_star(self):
        input_data = """a*c
abc"""
        expected_output = "YES"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_star_matches_empty_string(self):
        input_data = """*
"""
        expected_output = "YES"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_no_match(self):
        input_data = """a?c
ab"""
        expected_output = "NO"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

