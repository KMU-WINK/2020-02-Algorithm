from copy import deepcopy

n, m = list(map(int, input().split()))
maps = [[int(x) for x in input()] for _ in range(n)]
visited = deepcopy(maps)

DIRCT = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0

def DFS(x, y):
    visited[x][y] = 1

    for go_x, go_y in DIRCT:
        go_x, go_y = x + go_x, y + go_y
        if 0 <= go_x < n and 0 <= go_y < m and not visited[go_x][go_y]:
            DFS(go_x, go_y)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            DFS(i, j)
            count += 1

print(count)