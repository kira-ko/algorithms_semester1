import sys
import os
from bisect import bisect_left, bisect_right

def count_segments(segments, points):
    # Разделяем начала и концы отрезков на два списка
    starts = sorted([a for a, b in segments])
    ends = sorted([b for a, b in segments])

    results = []
    for point in points:
        # Количество отрезков, у которых начало <= точка
        start_count = bisect_right(starts, point)
        # Количество отрезков, у которых конец < точка
        end_count = bisect_left(ends, point)
        # Разница дает количество отрезков, содержащих точку
        results.append(start_count - end_count)

    return results

def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    s, p = map(int, lines[0].split())  # Количество отрезков и точек

    segments = []
    for i in range(1, s + 1):
        a, b = map(int, lines[i].split())
        segments.append((a, b))

    points = list(map(int, lines[s + 1].split()))  # Список точек

    results = count_segments(segments, points)  # Считаем пересечения

    output_file.write(" ".join(map(str, results)) + "\n")  # Записываем результат

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