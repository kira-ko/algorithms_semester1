import os
import sys

def process_operations(operations):
    """
    Выполняет операции над множеством.
    :param operations: Список строк операций
    :return: Список результатов для операций "? x"
    """
    result = []
    custom_set = set()

    for operation in operations:
        op_type, x = operation.split()
        x = int(x)

        if op_type == "A":
            custom_set.add(x)
        elif op_type == "D":
            custom_set.discard(x)
        elif op_type == "?":
            result.append("Y" if x in custom_set else "N")

    return result


def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    n = int(lines[0])
    operations = lines[1:]

    # Обрабатываем операции
    results = process_operations(operations)

    # Записываем результаты в файл
    output_file.write("\n".join(results) + "\n")


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
