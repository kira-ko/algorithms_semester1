import sys
import os


# Функция для вычисления высоты дерева
def calculate_height(tree, node):
    # Если у узла нет детей, его высота 1
    if not tree[node]:
        return 1
    # Рекурсивно вычисляем высоту всех поддеревьев и берем максимальную
    height = 0
    for child in tree[node]:
        height = max(height, calculate_height(tree, child))
    return height + 1


def main(input_data, output_file):

    lines = input_data.strip().split("\n")
    n = int(lines[0])
    parents = list(map(int, lines[1].split()))

    # Строим дерево
    tree = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    # Вычисление высоты дерева
    height = calculate_height(tree, root)

    # Записываем результат в выходной файл
    output_file.write(str(height))


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