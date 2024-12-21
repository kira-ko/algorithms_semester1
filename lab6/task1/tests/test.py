import unittest
from lab6.task1.src.main import process_operations

class TestSetOperations(unittest.TestCase):

    def test_add_and_query(self):
        operations = ["A 1", "A 2", "? 1", "? 3"]
        expected = ["Y", "N"]
        self.assertEqual(process_operations(operations), expected)

    def test_add_duplicate_and_query(self):
        operations = ["A 1", "A 1", "? 1", "? 2"]
        expected = ["Y", "N"]
        self.assertEqual(process_operations(operations), expected)

    def test_remove_and_query(self):
        operations = ["A 1", "A 2", "D 1", "? 1", "? 2"]
        expected = ["N", "Y"]
        self.assertEqual(process_operations(operations), expected)

    def test_remove_nonexistent(self):
        operations = ["A 1", "D 2", "? 1", "? 2"]
        expected = ["Y", "N"]
        self.assertEqual(process_operations(operations), expected)

if __name__ == "__main__":
    unittest.main()
