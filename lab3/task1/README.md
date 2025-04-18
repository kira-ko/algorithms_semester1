Задание №1 по варианту: улучшение Quick sort
====
Студентка ИТМО, Коновалова Кира Романовна, 472066

Вариант 9
----

Задание
---
Используя псевдокод процедуры Randomized - QuickSort, а так же Partition из презентации к Лекции 3 (страницы 8 и 12), напишите программу быстрой сортировки на Python и проверьте ее, создав несколько рандомных массивов.  
Основное задание. Цель задачи - переделать данную реализацию рандомизированного алгоритма быстрой сортировки, чтобы она работала быстро даже с последовательностями, содержащими много одинаковых элементов. Чтобы заставить алгоритм быстрой сортировки эффективно обрабатывать последовательности с несколькими уникальными элементами, нужно заменить двухстороннее разделение на трехстороннее (смотри в Лекции 3 слайд 17)  

Input / Output
----

| Input     | Output    |
|-----------|-----------|
| 5         | 2 2 2 3 9 |
| 2 3 9 2 2 |           |


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.

Структура проекта:
-------
* task1/ - папка со всеми файлами для задачи
* src/ - исходный код программы
* tests/ - тестирование алгоритма
* txtf / - текстовые файлы с входными и выходными данными

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algoritms_labs/lab3
   ```
3. Запустите все задачи лабораторной:
```bash
   python utils.py --tasks --lab lab3
   ```

## Тестирование
запустите все тесты лабораторной с помощью команды:
```bash
    pytest utils.py --tests --lab lab3
```

