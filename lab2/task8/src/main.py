def multiplication_polynomials(a, b, n):
    result = [0] * (n + n - 1)
    for cof_a in range(n):
        for cof_b in range(n):
            result[cof_a + cof_b] += a[cof_b] * b[cof_a]
    return result