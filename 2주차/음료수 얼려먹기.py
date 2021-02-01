import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(v1, v2):
    if v1 < 0 or v1 >= n or v2 < 0 or v2 >= m:
        return False

    if not graph[v1][v2]:
        graph[v1][v2] = 1
        dfs(v1 + 1, v2)
        dfs(v1, v2 + 1)
        dfs(v1 - 1, v2)
        dfs(v1, v2 - 1)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
