'''Поиск максимального подмассива'''
def max_subarray(array):
    mx_summ = 0
    summ = 0
    for i in range(len(array)):
        if summ == 0:
            start = i
        summ += array[i]
        if mx_summ < summ:
            mx_summ = summ
            finish = i
        if summ < 0:
            summ = 0
    return array[start:finish + 1]
