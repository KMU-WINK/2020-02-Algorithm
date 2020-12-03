n, m = map(int, input().split())
INF = 10001

types = [int(input()) for _ in range(n)]
table = [INF for _ in range(m + 1)]
table[0] = 0
print(table)


for coinType in types:
    for i in range(len(table)):
        if i % coinType == 0:
            table[i] = i / coinType

print(table)


'''
2 15
2
3


3 4
3
5
7


'''