import unittest
from io import StringIO


# Импортируем основную функцию из main.py
from lab7.task6.src.main import main  # Убедитесь, что путь правильный


class TestLIS(unittest.TestCase):

    def setUp(self):
        # Метод setUp() будет запускаться перед каждым тестом
        self.input_data = ""
        self.output = StringIO()

    def run_main(self, input_data):
        """Запуск основного алгоритма и возврат результата"""
        self.input_data = input_data
        output_file = StringIO()
        main(self.input_data, output_file)
        return output_file.getvalue().strip()

    def test_basic(self):
        input_data = """6
1 3 2 3 4 5"""

        expected_output = """5
1 2 3 4 5"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_edge_case_single_element(self):
        input_data = """1
5"""

        expected_output = """1
5"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_edge_case_all_equal(self):
        input_data = """5
5 5 5 5 5"""

        expected_output = """1
5"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)




if __name__ == "__main__":
    unittest.main()
