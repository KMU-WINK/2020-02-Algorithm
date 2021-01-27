n, m = map(int, input().split())

relation = [[0] * n for i in range(n)]

for i in range(m):
    start, end = map(int, input().split())
    relation[start - 1][end - 1] = 1
    relation[end - 1][start - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif relation[i][k] and relation[k][j]:
                if relation[i][j] == 0:
                    relation[i][j] = relation[i][k] + relation[k][j]
                else:
                    relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

total = 1e9
answer = 0
for i in relation:
    listTotal = 0
    for j in i:
        listTotal += j
    if total > listTotal:
        total = listTotal
        answer = relation.index(i)

print(answer+1)