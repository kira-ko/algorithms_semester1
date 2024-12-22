import unittest
from io import StringIO
from lab5.task2.src.main import calculate_height, main

class TestCalculateHeight(unittest.TestCase):
    def test_single_node(self):
        tree = [[]]
        self.assertEqual(calculate_height(tree, 0), 1)

    def test_linear_tree(self):
        tree = [[1], [2], [3], []]  # 0 -> 1 -> 2 -> 3
        self.assertEqual(calculate_height(tree, 0), 4)

    def test_binary_tree(self):
        tree = [[1, 2], [3, 4], [], [], []]  # 0 -> {1, 2}, 1 -> {3, 4}
        self.assertEqual(calculate_height(tree, 0), 3)

    def test_unbalanced_tree(self):
        tree = [[1], [2], [3, 4], [5], [], []]  # Unbalanced tree structure
        self.assertEqual(calculate_height(tree, 0), 5)

class TestMainFunction(unittest.TestCase):
    def run_main(self, input_data):
        output = StringIO()
        main(input_data, output)
        return output.getvalue().strip()

    def test_main_example(self):
        input_data = """5
-1 0 4 0 3"""
        expected_output = "4"
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_single_node(self):
        input_data = """1
-1"""
        expected_output = "1"
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_linear_tree(self):
        input_data = """4
-1 0 1 2"""
        expected_output = "4"
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_binary_tree(self):
        input_data = """5
-1 0 0 1 1"""
        expected_output = "3"
        self.assertEqual(self.run_main(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()