with open("../txtf/input.txt", 'r') as f:
    n = int(f.readline())
f.close()

with open("../txtf/output.txt", "w") as f:
    if 0 <= n <= 10**7:
        if n <= 1:
            f.write(str(n))
        else:
            a, b = 0, 1
            s = 0
            for i in range(1, n):
                s = (a+b)%10
                a, b = b, s
            f.write(str(s))
    else:
        print('Числа не подходят по диапазону')
        f.write('out of range')
f.close()