import sys
from copy import deepcopy

n, m = tuple(map(int, sys.stdin.readline().split()))
location = list(map(int, sys.stdin.readline().split()))
DIRECT = [[0, -1], [1, 0], [0, 1], [-1, 0]]

maps = [list(map(int, sys.stdin.readline().split())) for x in range(n)]
visited = deepcopy(maps)
visited[location[0]][location[1]] = 1
visited_count, rotate_count = 1, 0

while True:
    location[2] = len(DIRECT) - 1 if location[2] == 0 else location[2] - 1 # 방향 변경
    next_x_idx, next_y_idx = location[0] + DIRECT[location[2]][0], location[1] + DIRECT[location[2]][1] # 다음 좌표

    if visited[next_x_idx][next_y_idx] == 0: # 방문할 수 있는 곳이면
        location[0], location[1] = next_x_idx, next_y_idx # 방향 변경
        visited[location[0]][location[1]] = 1 # 방문 처리
        visited_count += 1 # 방문 카운트
    elif rotate_count < 4:
        rotate_count += 1 # 돌려돌려 돌림판
    else:
        break

print(visited_count)