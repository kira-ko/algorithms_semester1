import heapq
import sys
import os

def task_scheduler(n, tasks):
    # Очередь с приоритетом для потоков: (время освобождения, индекс потока)
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    result = []
    for task_time in tasks:
        # Достаем поток с минимальным временем освобождения
        free_time, thread_index = heapq.heappop(heap)
        # Добавляем результат
        result.append((thread_index, free_time))
        # Обновляем время освобождения потока и возвращаем его в очередь
        heapq.heappush(heap, (free_time + task_time, thread_index))

    return result


def main(input_data, output_file):

    lines = input_data.strip().split("\n")
    n, m = map(int, lines[0].split())
    tasks = list(map(int, lines[1].split()))

    result = task_scheduler(n, tasks)

    for thread_index, start_time in result:
        output_file.write(f"{thread_index} {start_time}\n")




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