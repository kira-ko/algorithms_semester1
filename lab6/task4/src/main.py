import os
import sys

class ThreadedMap:
    def __init__(self):
        self.map = {}
        self.order = []

    def put(self, key, value):
        if key not in self.map:
            self.order.append(key)
        self.map[key] = value

    def delete(self, key):
        if key in self.map:
            del self.map[key]
            self.order.remove(key)

    def get(self, key):
        return self.map.get(key, "<none>")

    def prev(self, key):
        if key not in self.map:
            return "<none>"
        idx = self.order.index(key)
        return self.map[self.order[idx - 1]] if idx > 0 else "<none>"

    def next(self, key):
        if key not in self.map:
            return "<none>"
        idx = self.order.index(key)
        return self.map[self.order[idx + 1]] if idx < len(self.order) - 1 else "<none>"


def process_operations(operations):
    """
    Выполняет операции над прошитым ассоциативным массивом.
    :param operations: Список строк операций
    :return: Список результатов для операций "get", "prev", "next"
    """
    result = []
    threaded_map = ThreadedMap()

    for operation in operations:
        parts = operation.split()
        command, key = parts[0], parts[1]

        if command == "put":
            value = parts[2]
            threaded_map.put(key, value)
        elif command == "delete":
            threaded_map.delete(key)
        elif command == "get":
            result.append(threaded_map.get(key))
        elif command == "prev":
            result.append(threaded_map.prev(key))
        elif command == "next":
            result.append(threaded_map.next(key))

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