import os
import sys

def can_sort_scarecrow(n, k, arr):
    """
    Определяет, можно ли отсортировать массив с помощью "сортировки пугалом".

    :param n: Число матрешек.
    :param k: Размах рук (шаг перемещения).
    :param arr: Список размеров матрешек.
    :return: "ДА", если сортировка возможна, иначе "НЕТ".
    """
    if n == 0 or k <= 0:
        return 'Нет'

    # Разделяем элементы по индексам с одинаковым остатком от деления на k
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(arr[i])

    # Сортируем каждую группу и проверяем общий порядок
    for group in groups:
        group.sort()

    # Собираем массив из отсортированных групп
    sorted_arr = []
    for i in range(n):
        sorted_arr.append(groups[i % k].pop(0))

    # Проверяем, является ли итоговый массив отсортированным
    return sorted_arr == sorted(arr)



def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла
    :param output_file: Объект файла для записи вывода
    """
    lines = input_data.strip().split("\n")
    n, k = map(int, lines[0].split())
    array = list(map(int, lines[1].split()))

    if can_sort_scarecrow(n, k, array):
        result = 'Yes'
    else:
        result = 'No'

    output_file.write(result + "\n")


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


