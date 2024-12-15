import heapq
import math
import os
import sys


def k_closest_points_to_origin(n, K, points):
    # Используем кучу для хранения точек с наименьшим расстоянием
    max_heap = []

    for x, y in points:
        # Расстояние до начала координат
        distance = math.sqrt(x ** 2 + y ** 2)
        # Добавляем точку в кучу
        heapq.heappush(max_heap, (-distance, (x, y)))  # Отрицательное расстояние для макс-кучи
        # Если кучи больше K, удаляем самую дальнюю точку
        if len(max_heap) > K:
            heapq.heappop(max_heap)

    # Извлекаем точки из кучи и сортируем их
    closest_points = [point for _, point in max_heap]
    closest_points.sort(key=lambda point: math.sqrt(point[0] ** 2 + point[1] ** 2))

    return closest_points


def main(input_data, output_file):
    # Чтение входных данных
    lines = input_data.strip().split("\n")
    n, k = map(int, lines[0].split())  # n - количество точек, k - количество ближайших
    points = [tuple(map(int, line.split())) for line in lines[1:]]  # Считываем точки

    # Получаем K ближайших точек
    closest_points = k_closest_points_to_origin(n, k, points)

    # Записываем результат в выходной файл
    output_file.write(f"[{', '.join(f'({x}, {y})' for x, y in closest_points)}]\n")


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
