from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]


def bfs(v1, v2):
    queue = deque()
    queue.append((v1, v2))

    while queue:
        v1, v2 = queue.popleft()
        for i in range(4):
            nx = v1 + directionX[i]
            ny = v2 + directionY[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[v1][v2] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))
