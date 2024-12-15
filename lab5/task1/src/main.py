import os
import sys

def is_heap(array):
    """
    Проверяет, является ли массив неубывающей пирамидой (кучей).
    :param array: Список целых чисел
    :return: True, если массив является кучей, иначе False
    """
    n = len(array)
    for i in range(n):
        if 2 * i + 1 < n and array[i] > array[2 * i + 1]:
            return False
        if 2 * i + 2 < n and array[i] > array[2 * i + 2]:
            return False
    return True


def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    n = int(lines[0])
    array = list(map(int, lines[1].split()))

    # Проверяем массив
    result = "YES" if is_heap(array) else "NO"

    # Записываем результат в выходной файл
    output_file.write(result + "\n")


if __name__ == '__main__':
    # Указываем пути для входного и выходного файлов
    input_path = sys.argv[1] if len(sys.argv) > 1 else "../txtf/input.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "../txtf/output.txt"

    # Проверка, существуют ли файлы в указанной директории
    if not os.path.exists(input_path):
        print(f"Ошибка: файл '{input_path}' не найден!")
        sys.exit(1)

    try:
        # Чтение входных данных
        with open(input_path, "r") as input_file:
            input_data = input_file.read()

        # Запись результата
        with open(output_path, "w") as output_file:
            main(input_data, output_file)

        print(f"Результат успешно записан в файл '{output_path}'")
    except Exception as e:
        print(f"Ошибка при обработке: {e}")
