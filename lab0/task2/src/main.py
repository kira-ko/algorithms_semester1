with open("../txtf/input.txt", "r") as f:
    n = int(f.readline())
f.close()

with open("../txtf/output.txt", "w") as f:
    if 0 <= n <= 45:
        if n <= 1:
            f.write(str(n))
        else:
            a = [0, 1]
            for i in range(1, n):
                a.append((a[i-1] + a[i]))
            print(*a)
            f.write(str(a[n]))
    else:
        print('Числа не подходят по диапазону')
        f.write('out of range')
f.close()