import unittest
from io import StringIO



from lab6.task2.src.main import main


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        # Метод setUp() будет запускаться перед каждым тестом
        self.input_data = ""
        self.output = StringIO()

    def run_main(self, input_data):
        """Запуск основного алгоритма и возврат результата"""
        self.input_data = input_data
        # Используем StringIO в качестве файла, не закрываем его сразу
        output_file = StringIO()
        main(self.input_data, output_file)
        return output_file.getvalue().strip()

    def test_add_find(self):
        input_data = """5
add 1234567 John
add 2345678 Alice
find 1234567
find 2345678
find 9876543"""

        expected_output = """John
Alice
not found"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_del(self):
        input_data = """4
add 1234567 John
add 2345678 Alice
del 1234567
find 1234567
find 2345678"""

        expected_output = """not found
Alice"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_multiple_add(self):
        input_data = """3
add 1234567 John
add 1234567 Alice
find 1234567"""

        expected_output = """Alice"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)

    def test_edge_case_empty(self):
        input_data = """1
find 1234567"""

        expected_output = """not found"""

        result = self.run_main(input_data)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()


