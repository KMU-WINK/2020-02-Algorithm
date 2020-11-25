import sys

N, M = tuple(map(int, sys.stdin.readline().split()))
mapp = []

for i in range(N):
    line = input()
    row = []
    for x in range(len(line)):
        row = [int(x) for x in line]
    mapp.append(row)

dir = [[1,0],[0,1],[-1,0],[0,-1]]

def dfs(mapp, check, row, col):
    mapp[row][col] = check
    visit = []

    for i in range(4):
        if (row + dir[i][0] < 0 or row + dir[i][0] >= N):
            continue

        if (col + dir[i][1] < 0 or col + dir[i][1] >= M):
            continue

        if (mapp[row + dir[i][0]][col + dir[i][1]] == 0):
            mapp[row + dir[i][0]][col + dir[i][1]] = check
            visit.append((row+dir[i][0],col+dir[i][1]))

    for j in range(len(visit)):
        dfs(mapp, check, visit[j][0], visit[j][1])

check = 2
for i in range(N):
    for j in range(M):
        if(mapp[i][j] == 0):
            dfs(mapp, check, i, j)
            check+= 1


print(check-2)