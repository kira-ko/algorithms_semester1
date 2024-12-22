import unittest
from io import StringIO
from lab4.task5.src.main import StackWithMax, main

class TestStackWithMax(unittest.TestCase):
    def setUp(self):
        self.stack = StackWithMax()

    def test_push_and_max(self):
        self.stack.push(1)
        self.assertEqual(self.stack.max(), 1)
        self.stack.push(3)
        self.assertEqual(self.stack.max(), 3)
        self.stack.push(2)
        self.assertEqual(self.stack.max(), 3)

    def test_pop_and_max(self):
        self.stack.push(1)
        self.stack.push(3)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.max(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.max(), 1)
        self.stack.pop()
        self.assertIsNone(self.stack.max())

    def test_mixed_operations(self):
        self.stack.push(5)
        self.stack.push(1)
        self.stack.push(5)
        self.assertEqual(self.stack.max(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.max(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.max(), 5)
        self.stack.pop()
        self.assertIsNone(self.stack.max())

class TestMainFunction(unittest.TestCase):
    def run_main(self, input_data):
        output = StringIO()
        main(input_data, output)
        return output.getvalue().strip()

    def test_main_example(self):
        input_data = """5
push 1
push 2
max
pop
max"""
        expected_output = "2\n1"
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_all_pop(self):
        input_data = """4
push 10
push 20
pop
pop"""
        expected_output = ""
        self.assertEqual(self.run_main(input_data), expected_output)

    def test_main_only_max(self):
        input_data = """3
push 5
max
max"""
        expected_output = "5\n5"
        self.assertEqual(self.run_main(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()
