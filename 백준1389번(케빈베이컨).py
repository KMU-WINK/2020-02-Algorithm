n, m = map(int, input().split())

s = [[0] * n for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif s[i][k] and s[k][j]:
                if s[i][j] == 0:
                    s[i][j] = s[i][k] + s[k][j]
                else:
                    s[i][j] = min(s[i][j], s[i][k] + s[k][j])

result = 100000000
for i in range(n):
    sum = 0
    for j in range(n):
        sum += s[i][j]
    if result > sum:
        result = sum
        p = i

print(p + 1)