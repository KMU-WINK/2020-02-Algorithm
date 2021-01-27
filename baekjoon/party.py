import heapq
import sys

def X_to_dijkstra(X, adjust):
    distance = adjust[X]
    queue = []
    for i in range(1, len(distance)):
        if (distance[i] != sys.maxsize):
            heapq.heappush(queue, (distance[i], i))

    while queue:
        weight, X = heapq.heappop(queue)
        important = adjust[X]
        for i in range(1, len(important)):
            if (important[i] == sys.maxsize):
                continue

            if (important[i] + distance[X] < distance[i]):
                distance[i] = important[i] + distance[X]
                heapq.heappush(queue, (distance[i], i))

    return distance[1:]

N, M, X = map(int, sys.stdin.readline().split())

adjust = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
adjust2 = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if(i == j):
            adjust[i][j] = 0
            adjust2[i][j] = 0

for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split())
    adjust[i][j] = w
    adjust2[j][i] = w

result1 = X_to_dijkstra(X, adjust)
result2 = X_to_dijkstra(X, adjust2)


for i in range(1,len(result1)):
    result1[i] = result1[i] + result2[i]

print(max(result1))