import sys
import os

'''Бинарный поиск'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


'''
if __name__ == '__main__':

    data_n, data_k = open_file("../txtf/input.txt")
    n = int(data_n[0])
    mass = data_n[1:]

    k = int(data_k[0])
    mass_f = data_k[1:]

    write_file("", "../txtf/output.txt", mode="w")
    for i in mass_f:
        ans = binary_search(mass, i)
        write_file(f"{ans} ", "../txtf/output.txt", mode='a')
'''

def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    data_n = list(map(int, lines[0].split()))
    data_k = list(map(int, lines[1].split()))

    n = int(data_n[0])
    mass1 = data_n[1:]

    k = int(data_k[0])
    mass2 = data_k[1:]

    for i in mass2:
        ans = binary_search(mass1, i)

        output_file.write(str(ans) + ' ')

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