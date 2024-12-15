import sys
import os

def h_index(citations):
    citations.sort(reverse=True)  # Сортируем список цитирований по убыванию
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

def main(input_data, output_file):
    # Чтение входных данных с учетом запятой
    citations = list(map(int, input_data.strip().split(',')))

    # Вычисление h-индекса
    result = h_index(citations)

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