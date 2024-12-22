import os
import importlib.util
import tracemalloc
from time import perf_counter


# Определяем корневую директорию
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def print_separator(text):
    """Печатает разделитель с заголовком."""
    print("\n" + "=" * 40)
    print(f"= {text}")
    print("=" * 40 + "\n")


def print_success(message):
    """Печатает сообщение об успешном завершении."""
    print("\n" + "-" * 40)
    print(f"Успешно: {message}")
    print("-" * 40 + "\n")


def get_lab_path(lab_name):
    """Возвращает абсолютный путь к указанной лабораторной."""
    lab_path = os.path.join(BASE_DIR, lab_name)
    if not os.path.exists(lab_path):
        raise FileNotFoundError(f"Лаборатория '{lab_name}' не найдена.")
    return lab_path


def measure_time(func, *args, repeats=1):
    """Измеряет среднее время выполнения функции."""
    start_time = perf_counter()
    for _ in range(repeats):
        result = func(*args)
    elapsed_time = (perf_counter() - start_time) / repeats
    return result, elapsed_time


def run_task(task_path):
    """Запускает задачу из указанного пути с измерением времени и памяти."""
    try:
        src_path = os.path.join(task_path, "src")
        input_file = os.path.join(task_path, "txtf", "input.txt")
        output_file = os.path.join(task_path, "txtf", "output.txt")

        main_file = os.path.join(src_path, "main.py")
        if not os.path.exists(main_file):
            print(f"  main.py не найден в {src_path}")
            return

        # Динамический импорт main.py
        spec = importlib.util.spec_from_file_location("main", main_file)
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)

        if not hasattr(main_module, "main"):
            print(f"  Функция 'main' отсутствует в {main_file}")
            return

        print(f"  Запуск задачи: {os.path.basename(task_path)}")

        # Чтение входных данных
        with open(input_file, "r") as f:
            input_data = f.read()

        # Измерение времени и памяти выполнения main
        def wrapper():
            with open(output_file, "w") as out_f:
                main_module.main(input_data, out_f)

        tracemalloc.start()  # Начинаем отслеживание памяти
        _, exec_time = measure_time(wrapper, repeats=1)
        current, peak = tracemalloc.get_traced_memory()  # Получаем текущую и пиковую память
        tracemalloc.stop()  # Останавливаем отслеживание памяти

        print(f"    Время выполнения: {exec_time:.5f} сек")
        print(f"    Использование памяти: текущая {current / 1024:.2f} KB, пиковая {peak / 1024:.2f} KB")

    except Exception as e:
        print(f"Ошибка при выполнении задачи: {e}")



def run_lab(lab_name):
    """Запускает задачи для указанной лабораторной."""
    try:
        lab_path = get_lab_path(lab_name)
        print_separator(f"Запуск лабораторной: {lab_name}")
        tasks = [d for d in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, d))]
        for task in sorted(tasks):
            task_path = os.path.join(lab_path, task)
            run_task(task_path)
        print_success(f"Лабораторная {lab_name} выполнена")
    except FileNotFoundError as e:
        print(e)


def run_all_labs():
    """Запускает задачи для всех лабораторных."""
    print_separator("Запуск всех лабораторных")
    labs = [d for d in os.listdir(BASE_DIR) if d.startswith("lab") and os.path.isdir(os.path.join(BASE_DIR, d))]
    for lab in sorted(labs):
        run_lab(lab)
    print_success("Все лабораторные выполнены")


def run_tests_for_task(task_path):
    """Запускает тесты для конкретной задачи."""
    try:
        tests_path = os.path.join(task_path, "tests")
        test_file = os.path.join(tests_path, "test.py")
        if not os.path.exists(test_file):
            print(f"  Тесты не найдены для задачи: {os.path.basename(task_path)}")
            return

        print(f"  Запуск тестов для задачи: {os.path.basename(task_path)}")
        result = os.system(f"python -m unittest {test_file}")
        if result != 0:
            print(f"  Ошибка выполнения тестов в {os.path.basename(task_path)}")
    except Exception as e:
        print(f"  Ошибка при выполнении тестов: {e}")


def run_tests_for_lab(lab_name):
    """Запускает тесты для всех задач в указанной лабораторной."""
    try:
        lab_path = get_lab_path(lab_name)
        print_separator(f"Запуск тестов для лабораторной: {lab_name}")
        tasks = [d for d in os.listdir(lab_path) if os.path.isdir(os.path.join(lab_path, d))]
        for task in sorted(tasks):
            task_path = os.path.join(lab_path, task)
            run_tests_for_task(task_path)
        print_success(f"Тесты лабораторной {lab_name} успешно пройдены")
    except FileNotFoundError as e:
        print(e)


def run_all_tests():
    """Запускает тесты для всех лабораторных."""
    print_separator("Запуск тестов для всех лабораторных")
    labs = [d for d in os.listdir(BASE_DIR) if d.startswith("lab") and os.path.isdir(os.path.join(BASE_DIR, d))]
    for lab in sorted(labs):
        run_tests_for_lab(lab)
    print_success("Все тесты успешно пройдены")


def run_all_tests_and_tasks():
    """Запускает все лабораторные и тесты."""
    print_separator("Запуск всех лабораторных и тестов")
    run_all_tests()
    run_all_labs()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Утилита для управления лабораторными работами")
    parser.add_argument("--lab", type=str, help="Укажите лабораторную для запуска (например, lab1)")
    parser.add_argument("--all", action="store_true", help="Запустить все лабораторные")
    parser.add_argument("--tests", action="store_true", help="Запустить тесты")
    parser.add_argument("--tasks", action="store_true", help="Запустить задачи")
    parser.add_argument("--both", action="store_true", help="Запустить тесты и задачи вместе")

    args = parser.parse_args()

    if args.both:
        run_all_tests_and_tasks()
    elif args.tests:
        if args.lab:
            run_tests_for_lab(args.lab)
        elif args.all:
            run_all_tests()
        else:
            print("Укажите лабораторную (--lab) или запустите все тесты (--all)")
    elif args.tasks:
        if args.lab:
            run_lab(args.lab)
        elif args.all:
            run_all_labs()
        else:
            print("Укажите лабораторную (--lab) или запустите все задачи (--all)")
    else:
        print("Используйте аргументы:")
        print("  --lab <имя лаборатории>    Запустить конкретную лабораторную")
        print("  --all                      Запустить все лабораторные")
        print("  --tests                    Запустить только тесты")
        print("  --tasks                    Запустить только задачи")
        print("  --both                     Запустить тесты и задачи вместе")

