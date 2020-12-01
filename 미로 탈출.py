#큐를 이용하는 법을 정말 도저히 모르겠어서 책 저자분의 깃허브를 참고하였습니다...
#하지만 정답 코드를 보고도 이해를 못했습니다...
#주말동안 각성해서 오겠습니다... 분발할게요...

from collections import deque
n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# [상, 하, 좌, 우]로 움직일 때의 좌표 변화
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어났을 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 미로 공간이 0인 경우(괴물을 만났을 경우)
            if maze[nx][ny] == 0:
                continue
            # 미로 공간이 1인 경우(옳은 길일 경우)
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

        return maze[n - 1][m - 1]

print(bfs(0, 0))