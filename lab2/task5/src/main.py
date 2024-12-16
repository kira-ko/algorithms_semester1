import sys
import os

def majority(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for l, m in dic.items():
        if m > len(a) // 2:
            return 1
    return 0


def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    n = int(lines[0])  # Число элементов
    arr = list(map(int, lines[1].split()))  # Массив чисел

    result = majority(arr) # Сортируем массив

    output_file.write(str(result))  # Записываем результат

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