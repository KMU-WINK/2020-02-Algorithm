import sys

N, M = tuple(map(int, sys.stdin.readline().split()))
mapp = []

for i in range(N):
    line = input()
    row = []
    for x in range(len(line)):
        row = [int(x) for x in line]
    mapp.append(row)

visited = [[0,0]]

dir = [[1,0],[0,1],[-1,0],[0,-1]]

# 상하좌우 중에 1인 부분 리스트에 넣어서 리턴해주는 함수
def bfs(mapp, visited):
    visit = []

    for i in range(len(visited)):
        for j in range(4):
            if(visited[i][0]+dir[j][0] < 0 or visited[i][0]+dir[j][0] >= N):
                continue

            if(visited[i][1]+dir[j][1] < 0 or visited[i][1]+dir[j][1] >= M):
                continue

            if(mapp[visited[i][0]+dir[j][0]][visited[i][1]+dir[j][1]] == 1):
                visit.append((visited[i][0]+dir[j][0],visited[i][1]+dir[j][1]))

    return visit



count = 1
check = 0
while(count < N * M and check == 0):
    visited = bfs(mapp,visited)
    count += 1


    for i in range(len(visited)):
        mapp[visited[i][0]][visited[i][1]] = 0

        if(visited[i][0] == N-1 and visited[i][1] == M-1):
            check = 1
            break

print(count)