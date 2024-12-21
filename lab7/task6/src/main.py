import sys
import os
import bisect


def lis(sequence):
    """
    Функция для нахождения наибольшей возрастающей подпоследовательности (LIS).
    :param sequence: Список целых чисел (последовательность).
    :return: Кортеж из длины LIS и самой LIS.
    """
    n = len(sequence)
    if n == 0:
        return 0, []

    # Массив для хранения минимальных концов возрастающих подпоследовательностей
    # длины i+1 в arr[i]
    lis_ends = []
    # Массив для восстановления самой последовательности
    prev_idx = [-1] * n
    indices = [-1] * n

    for i in range(n):
        # Используем бинарный поиск для нахождения места вставки
        pos = bisect.bisect_left(lis_ends, sequence[i])

        # Если pos == len(lis_ends), то добавляем новый элемент
        if pos == len(lis_ends):
            lis_ends.append(sequence[i])
        else:
            lis_ends[pos] = sequence[i]

        # Сохраняем индекс для восстановления последовательности
        indices[pos] = i
        if pos > 0:
            prev_idx[i] = indices[pos - 1]

    # Восстанавливаем саму последовательность
    lis_seq = []
    idx = indices[len(lis_ends) - 1]
    while idx != -1:
        lis_seq.append(sequence[idx])
        idx = prev_idx[idx]

    # Лист нужно перевернуть, так как мы восстанавливаем его с конца
    lis_seq.reverse()

    return len(lis_ends), lis_seq


def main(input_data, output_file):
    """
    Основная функция для запуска задачи.
    :param input_data: Строка с содержимым входного файла.
    :param output_file: Объект файла для записи вывода.
    """
    lines = input_data.strip().split("\n")
    n = int(lines[0])
    sequence = list(map(int, lines[1].split()))

    # Получаем результат
    length, subsequence = lis(sequence)

    # Записываем результат в выходной файл
    output_file.write(f"{length}\n")
    output_file.write(" ".join(map(str, subsequence)) + "\n")


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
