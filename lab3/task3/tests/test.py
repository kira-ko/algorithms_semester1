import random
from lab3.task3.src.main import can_sort_scarecrow

def test_case_1():
    assert can_sort_scarecrow(5, 3, [1, 5, 3, 4, 1]) == True

def test_case_2():
    assert can_sort_scarecrow(5, 3, [4, 3, 5, 1, 2]) == False

def test_sorted_array():
    assert can_sort_scarecrow(5, 1, [1, 2, 3, 4, 5]) == True

def test_reverse_sorted_array():
    assert can_sort_scarecrow(5, 1, [5, 4, 3, 2, 1]) == True

def test_random_array():
    n, k = 10, 3
    arr = [random.randint(1, 100) for _ in range(n)]
    result = can_sort_scarecrow(n, k, arr)
    assert result in [True, False]

def test_large_case():
    n, k = 10**5, 5
    arr = [random.randint(1, 10**9) for _ in range(n)]
    result = can_sort_scarecrow(n, k, arr)
    assert result in [True, False]

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_sorted_array()
    test_reverse_sorted_array()
    test_random_array()
    test_large_case()
    print("All tests passed!")