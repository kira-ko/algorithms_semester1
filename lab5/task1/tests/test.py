import unittest
from io import StringIO
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(base_dir, '..', 'src')

sys.path.append(src_dir)

from lab5.task1.src.main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        """Настроим стандартный вывод, чтобы можно было проверить вывод в файле"""
        self.sio = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.sio

    def tearDown(self):
        """Возвращаем стандартный вывод после выполнения теста"""
        sys.stdout = self.saved_stdout

    def test_heap_valid(self):
        """Тест для случая, когда массив является неубывающей пирамидой"""
        input_data = "7\n1 3 6 5 9 8 12\n"
        main(input_data, self.sio)
        output = self.sio.getvalue().strip()
        self.assertEqual(output, "YES")

    def test_heap_invalid(self):
        """Тест для случая, когда массив не является неубывающей пирамидой"""
        input_data = "7\n1 3 6 7 9 8 4\n"
        main(input_data, self.sio)
        output = self.sio.getvalue().strip()
        self.assertEqual(output, "NO")

    def test_single_element(self):
        """Тест для массива с одним элементом, который всегда является пирамидой"""
        input_data = "1\n5\n"
        main(input_data, self.sio)
        output = self.sio.getvalue().strip()
        self.assertEqual(output, "YES")

    def test_two_elements(self):
        """Тест для массива с двумя элементами, который является пирамидой"""
        input_data = "2\n5 8\n"
        main(input_data, self.sio)
        output = self.sio.getvalue().strip()
        self.assertEqual(output, "YES")


    def test_large_valid_heap(self):
        """Тест для большого массива, который является пирамидой"""
        input_data = "10\n1 3 5 7 9 8 6 10 11 12\n"
        main(input_data, self.sio)
        output = self.sio.getvalue().strip()
        self.assertEqual(output, "YES")

if __name__ == "__main__":
    unittest.main()