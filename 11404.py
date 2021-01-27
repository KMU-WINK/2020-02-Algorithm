n = int(input())
m = int(input())

inf = 1e9

distance = [[inf] * n for i in range(n)]

for i in range(m):
    start, end, cost = map(int, input().split())
    if distance[start - 1][end - 1] > cost:
        distance[start - 1][end - 1] = cost

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                
for i in distance:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()