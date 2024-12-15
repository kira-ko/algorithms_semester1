import os
import sys


def build_heap(data):
    """
    Преобразует массив data в min-heap.
    Возвращает список сделанных перестановок.
    """
    swaps = []
    n = len(data)

    def sift_down(i):
        """
        Просеивает элемент вниз по правилу min-heap.
        """
        min_index = i
        left = 2 * i + 1
        if left < n and data[left] < data[min_index]:
            min_index = left

        right = 2 * i + 2
        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    # Строим кучу начиная с последнего родителя
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps



def main(input_data, output_file):

    lines = input_data.strip().split("\n")
    n = int(lines[0])
    data = list(map(int, lines[1].split()))

    swaps = build_heap(data)

    output_file.write(f"{len(swaps)}\n")
    for i, j in swaps:
        output_file.write(f"{i} {j}\n")




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
