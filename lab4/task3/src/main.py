import os
import sys

def is_correct_sequence(sequence):
    stack = []
    matching_brackets = {')': '(', ']': '['}

    for char in sequence:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return "NO"

    return "YES" if not stack else "NO"


def process_sequences(sequences):
    return [is_correct_sequence(seq) for seq in sequences]

def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    n = int(lines[0].strip())  # Число строк
    sequences = [line.strip() for line in lines[1:n + 1]]

    results = process_sequences(sequences)


    output_file.write("\n".join(results) + "\n")

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
