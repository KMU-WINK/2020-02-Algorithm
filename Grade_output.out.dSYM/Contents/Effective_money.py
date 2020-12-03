n, m = map(int, input().split())
val = [int(input()) for _ in range(n)]
print(val)
d = [10001]*10001
d[0] = 0
for v in val:
    for j in range(v, m+1):
        d[j] = min(d[j], d[j-v]+1)
print(d[m])