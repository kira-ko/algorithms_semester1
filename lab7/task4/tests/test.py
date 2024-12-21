import unittest
from io import StringIO
from unittest.mock import patch
from lab7.task4.src.main import main

class TestLCS(unittest.TestCase):

    def run_main(self, input_data):
        with patch("sys.stdout", new_callable=StringIO) as output_file:
            main(input_data, output_file)
            return output_file.getvalue().strip()

    def test_lcs(self):
        input_data = """5
                    1 2 3 4 5
                    4
                    2 3 4 5"""
        expected_output = "4"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_lcs_single_element(self):
        input_data = """1
                        1
                        1
                        1"""
        expected_output = "1"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_lcs_no_common_elements(self):
        input_data = """3
                        1 2 3
                        3
                        4 5 6"""
        expected_output = "0"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_lcs_edge_case(self):
        input_data = """5
                        1 2 3 4 5
                        5
                        1 2 3 4 5"""
        expected_output = "5"
        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
