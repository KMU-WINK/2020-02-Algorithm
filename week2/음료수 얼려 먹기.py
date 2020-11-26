from copy import deepcopy


n, m = list(map(int, input().split()))
maps = [[int(x) for x in input()] for _ in range(n)]
visited = deepcopy(maps)


DIRCT = [(-1, 0), (0, 1), (1, 0), (0, -1)]
location = {'x': 0, 'y': 0}

def DFS(x, y):
    pass


for i in range(n):
    for j in range(m):
        if not visited[n][m]:
            DFS(i, j)