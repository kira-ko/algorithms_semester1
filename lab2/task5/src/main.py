def majority(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for l, m in dic.items():
        if m > len(a) // 2:
            return 1
    return 0

