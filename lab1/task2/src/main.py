import sys
import os

"""Задание 2. Сортировка вставкой +"""
def insertion_sort(list_arr):
    index_result = [1]
    for i in range(1, len(list_arr)):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)
    return index_result, list_arr


def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    n = int(lines[0])  # Число элементов
    arr = list(map(int, lines[1].split()))  # Массив чисел

    index, array = insertion_sort(arr) # Сортируем массив

    output_file.write((" ".join(map(str, index))) + '\n' ) # Записываем результат
    output_file.write(" ".join(map(str, array)))

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