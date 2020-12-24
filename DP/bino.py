def bino_coef(n, r):
    if r == 0 or r == n:
        return 1
    return bino_coef(n - 1, r) + bino_coef(n - 1, r - 1)

def bino_coef_cache(n, r):
    cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    for i in range(1, n + 1):
        for j in range(1, r + 1):
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]

    return cache[n][r]

print(bino_coef(4, 2))
print(bino_coef_cache(4, 2))
