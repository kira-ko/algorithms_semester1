import sys
import os

def multiplication_polynomials(a, b, n):
    result = [0] * (n + n - 1)
    for cof_a in range(n):
        for cof_b in range(n):
            result[cof_a + cof_b] += a[cof_b] * b[cof_a]
    return result


def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    data = list(map(int, lines[0].split()))
    n = data[0]
    a = data[1:]

    b = list(map(int, lines[1].split()))

    result = multiplication_polynomials(a, b, n)

    output_file.write(" ".join(map(str, result)))  # Записываем результат

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