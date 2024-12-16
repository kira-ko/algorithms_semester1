import sys
import os

'''Число инверсий'''
def inv_count(array, copy_array, left, middle, right):
    i = left
    j = middle + 1
    k = left
    cnt = 0

    while i <= middle and j <= right:
        if array[i] <= array[j]:
            copy_array[k] = array[i]
            i += 1
        else:
            copy_array[k] = array[j]
            cnt += (middle - i + 1)
            j += 1
        k += 1

    while i <= middle:
        copy_array[k] = array[i]
        i += 1
        k += 1

    while j <= right:
        copy_array[k] = array[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        array[i] = copy_array[i]

    return cnt


def inversions_numbers(array, copy_array, left, right):
    if len(copy_array) < len(array):
        raise ValueError("The Aarray is too small to sort.")

    cnt = 0
    if left < right:
        middle = (left + right) // 2

        cnt += inversions_numbers(array, copy_array, left, middle)
        cnt += inversions_numbers(array, copy_array, middle + 1, right)
        cnt += inv_count(array, copy_array, left, middle, right)

    return cnt


def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    n = int(lines[0])  #
    massive = list(map(int, lines[1].split()))
    massive_copy = massive.copy()

    ans = inversions_numbers(massive, massive_copy, 0, n-1) # Сортируем массив

    output_file.write(str(ans))  # Записываем результат

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