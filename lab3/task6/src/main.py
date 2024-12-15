import sys
import os
from lab3.task1.src.main import randomized_quicksort

def sum_of_every_tenth_product(array1, array2):
    product_list = []
    for b in array2:
        for a in array1:
            product_list.append(a * b)

    randomized_quicksort(product_list, 0, len(product_list) - 1)
    result = sum(product_list[i] for i in range(0, len(product_list), 10))

    return result



def main(input_data, output_file):
    # Чтение входных данных
    lines = input_data.strip().split("\n")
    n, m = map(int, lines[0].split())  # Размеры массивов
    A = list(map(int, lines[1].split()))  # Массив A
    B = list(map(int, lines[2].split()))  # Массив B

    # Вычисление суммы каждого десятого элемента
    result = sum_of_every_tenth_product(A, B)

    # Запись результата в выходной файл
    output_file.write(f"{result}\n")


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