import sys
import os

def process_stack(commands):
    stack = []
    result = []

    for command in commands:
        if command.startswith('+'):
            _, num = command.split()
            stack.append(int(num))
        elif command == '-':
            result.append(stack.pop())

    return result


def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    num_commands = int(lines[0].strip())
    commands = [line.strip() for line in lines[1:num_commands + 1]]

    # Проверяем массив
    result = process_stack(commands)

    # Записываем результат в выходной файл
    output_file.write(f"{result}\n")

if __name__ == "__main__":
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
