import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = 1000000000
Lists = [0]*N
for i in range(N):
    L = [INF]*N
    Lists[i] = L
    Lists[i][i] = 0
for i in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    if Lists[a-1][b-1] > c:
        Lists[a - 1][b - 1] = c


for i in range(N):
    for j in range(N):
        for k in range(N):
            if Lists[j][i] + Lists[i][k] < Lists[j][k] :
                Lists[j][k] = Lists[j][i] + Lists[i][k]

for i in Lists:
    print(i)