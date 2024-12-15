from collections import deque
import os
import sys

class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()

    def push(self, value):
        self.queue.append(value)
        while self.min_queue and self.min_queue[-1] > value:
            self.min_queue.pop()
        self.min_queue.append(value)

    def pop(self):
        if self.queue:
            value = self.queue.popleft()
            if value == self.min_queue[0]:
                self.min_queue.popleft()

    def get_min(self):
        if self.min_queue:
            return self.min_queue[0]


def process_commands(commands):
    queue = MinQueue()
    results = []

    for command in commands:
        if command.startswith("+"):
            _, value = command.split()
            queue.push(int(value))
        elif command == "-":
            queue.pop()
        elif command == "?":
            results.append(queue.get_min())

    return results


def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    m = int(lines[0].strip())
    commands = [line.strip() for line in lines[1:m + 1]]

    results = process_commands(commands)


    output_file.write("\n".join(map(str, results)) + "\n")

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


