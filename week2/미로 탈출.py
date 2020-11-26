from queue import Queue
from copy import deepcopy

n, m = list(map(int, input().split()))
maps = [[int(x) for x in input()] for _ in range(n)]
visited = deepcopy(maps)

DIRCT = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = -1
q = Queue()
q.put((0, 0))

while True:
    x, y = q.get()
    visited[x][y] = 0

    if x + 1 == n and y + 1 == m:
        break

    count += 1

    for goto_x, goto_y in DIRCT:
        next_x, next_y = x + goto_x, y + goto_y
        # 방문 위치 확인
        if -1 not in [next_x, next_y] and next_x < n and next_y < m and visited[next_x][next_y]:
            q.put((next_x, next_y))

print(count)