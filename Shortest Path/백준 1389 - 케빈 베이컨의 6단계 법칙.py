infTemp = int(1e9)

n, m = map(int, input().split())

graph = [[infTemp] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    sum = 0;
    for b in range(1, n + 1):
        sum += graph[a][b];

    if(sum < infTemp):
        infTemp = sum;
        answer = a

print(answer)