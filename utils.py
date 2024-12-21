import os
import time
import importlib.util
from time import perf_counter

# Определяем корневую директорию (где находится utils.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_lab_path(lab_name):
    """
    Возвращает абсолютный путь к указанной лабораторной.
    """
    lab_path = os.path.join(BASE_DIR, lab_name)
    if not os.path.exists(lab_path):
        raise FileNotFoundError(f"Лаборатория '{lab_name}' не найдена в '{BASE_DIR}'")
    return lab_path


def measure_time(func, *args, repeats=1):
    """
    Измеряет среднее время выполнения функции func с переданными аргументами.
    """
    start_time = perf_counter()
    for _ in range(repeats):
        result = func(*args)
    elapsed_time = (perf_counter() - start_time) / repeats
    return result, elapsed_time


def run_task(task_path):
    """
        Запускает конкретную задачу из указанного пути.
        """
    try:
        src_path = os.path.join(task_path, "src")
        tests_path = os.path.join(task_path, "tests")
        input_file = os.path.join(task_path, "txtf", "input.txt")
        output_file = os.path.join(task_path, "txtf", "output.txt")

        main_file = os.path.join(src_path, "main.py")
        if not os.path.exists(main_file):
            raise FileNotFoundError(f"Файл main.py не найден в папке '{src_path}'")

        # Динамический импорт test1.py
        spec = importlib.util.spec_from_file_location("main", main_file)
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)

        # Проверяем наличие функции main
        if not hasattr(main_module, "main"):
            raise AttributeError(f"В файле main.py отсутствует функция 'main'")

        print(f"  Запуск задачи: {os.path.basename(task_path)}")
        os.chdir(src_path)  # Переключаемся в директорию задачи

        # Читаем входные данные
        with open(input_file, "r") as f:
            input_data = f.read()

        # Измеряем время выполнения main
        def wrapper():
            with open(output_file, "w") as out_f:
                main_module.main(input_data, out_f)

        _, exec_time = measure_time(wrapper, repeats=1)

        print(f"    Время выполнения: {exec_time:.5f} сек")
        os.chdir(BASE_DIR)  # Возвращаемся в корневую директорию
    except Exception as e:
        print(f"Ошибка при выполнении задачи: {e}")


def run_lab(lab_name):
    """
    Запускает все задачи из указанной лабораторной.
    """
    try:
        lab_path = get_lab_path(lab_name)
        print(f"Запуск лабораторной: {lab_name}")
        tasks = [d for d in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, d))]
        for task in sorted(tasks):
            task_path = os.path.join(lab_path, task)
            run_task(task_path)
    except FileNotFoundError as e:
        print(e)


def run_all_labs():
    """
    Запускает все лабораторные.
    """
    print("Запуск всех лабораторных...")
    labs = [d for d in os.listdir(BASE_DIR) if d.startswith("lab") and os.path.isdir(os.path.join(BASE_DIR, d))]
    for lab in sorted(labs):
        run_lab(lab)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Утилита для запуска лабораторных работ")
    parser.add_argument("--lab", type=str, help="Укажите лабораторную для запуска (например, lab5)")
    parser.add_argument("--all", action="store_true", help="Запустить все лабораторные")

    args = parser.parse_args()

    if args.all:
        run_all_labs()
    elif args.lab:
        run_lab(args.lab)
    else:
        print("Укажите аргумент --lab <имя лаборатории> или --all для запуска всех лабораторных.")
