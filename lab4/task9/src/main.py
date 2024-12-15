from collections import deque
import os
import sys

class PolyclinicQueue:
    def __init__(self):
        self.queue = deque()
        self.middle_index = 0

    def add_end(self, patient_id):
        self.queue.append(patient_id)

    def add_middle(self, patient_id):
        self.middle_index = (len(self.queue) + 1) // 2
        self.queue.insert(self.middle_index, patient_id)

    def serve_patient(self):
        return self.queue.popleft()

def process_requests(commands):
    queue = PolyclinicQueue()
    results = []

    for command in commands:
        if command.startswith("+"):
            _, patient_id = command.split()
            queue.add_end(int(patient_id))
        elif command.startswith("*"):
            _, patient_id = command.split()
            queue.add_middle(int(patient_id))
        elif command == "-":
            results.append(queue.serve_patient())

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

    results = process_requests(commands)


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
