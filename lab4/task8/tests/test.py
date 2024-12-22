import unittest
from io import StringIO
from lab4.task8.src.main import evaluate_postfix, main

class TestEvaluatePostfix(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(evaluate_postfix(["5"]), 5)

    def test_simple_addition(self):
        self.assertEqual(evaluate_postfix(["2", "3", "+"]), 5)

    def test_simple_subtraction(self):
        self.assertEqual(evaluate_postfix(["5", "3", "-"]), 2)

    def test_simple_multiplication(self):
        self.assertEqual(evaluate_postfix(["4", "3", "*"]), 12)

    def test_complex_expression(self):
        self.assertEqual(evaluate_postfix(["2", "3", "+", "4", "*"]), 20)  # (2 + 3) * 4
        self.assertEqual(evaluate_postfix(["5", "1", "2", "+", "4", "*", "+", "3", "-"]), 14)  # 5 + ((1 + 2) * 4) - 3

class TestMainFunction(unittest.TestCase):
    def run_main(self, input_data):
        output = StringIO()
        main(input_data, output)
        return output.getvalue().strip()

    def test_main_example(self):
        input_data = """7
2 3 + 4 *"""
        expected_output = "20"
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_large_expression(self):
        input_data = """9
5 1 2 + 4 * + 3 -"""
        expected_output = "14"
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_single_number(self):
        input_data = """1
5"""
        expected_output = "5"
        self.assertEqual(self.run_main(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()
