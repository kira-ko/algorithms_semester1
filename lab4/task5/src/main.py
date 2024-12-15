import os
import sys

class StackWithMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        # Если стек с максимумами пуст или текущий элемент >= текущего максимума
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return
        # Если удаляемый элемент равен текущему максимуму, удаляем его и из max_stack
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]



def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    n = int(lines[0].strip())  # Число строк
    commands = [line.strip() for line in lines[1:n + 1]]

    stack = StackWithMax()
    results = []

    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            stack.push(int(value))
        elif command == "pop":
            stack.pop()
        elif command == "max":
            results.append(stack.max())

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