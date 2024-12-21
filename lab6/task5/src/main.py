import os
import sys
from collections import defaultdict

def calculate_votes(input_lines):
    """
    Подсчитывает количество голосов для каждого кандидата.
    :param input_lines: Список строк входного файла
    :return: Словарь с подсчетом голосов {кандидат: количество голосов}
    """
    vote_count = defaultdict(int)

    for line in input_lines:
        candidate, votes = line.rsplit(maxsplit=1)
        vote_count[candidate] += int(votes)

    return vote_count


def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")

    # Подсчитываем голоса
    vote_count = calculate_votes(lines)

    # Сортируем кандидатов в лексикографическом порядке и записываем результат
    for candidate in sorted(vote_count):
        output_file.write(f"{candidate} {vote_count[candidate]}\n")


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

