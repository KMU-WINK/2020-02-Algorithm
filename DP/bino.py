def bin(n, r):
    if (r > n // 2):
        r = n - r
    b = [0] * (r + 1)
    b[0] = 1
    for i in range(1, n + 1):
        j = min(i, r)
        while (j > 0):
            b[j] = b[j] + b[j - 1]
            j -= 1
        for n in range(min(i, r) + 1):
            print(b[n], end = " ")
        print()
    return b[r]

print(bin(9, 3))