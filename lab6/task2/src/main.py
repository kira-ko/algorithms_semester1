import os
import sys


def process_queries(input_data):
    phonebook = {}
    result = []

    for line in input_data.strip().split("\n"):
        parts = line.split()
        command = parts[0]

        if command == "add":
            number = parts[1]
            name = parts[2]
            phonebook[number] = name

        elif command == "del":
            number = parts[1]
            if number in phonebook:
                del phonebook[number]

        elif command == "find":
            number = parts[1]
            if number in phonebook:
                result.append(phonebook[number])
            else:
                result.append("not found")

    return result


def main(input_data, output_file):
    results = process_queries(input_data)

    # Записываем результаты в выходной файл
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


