N, M  = map(int,input().split())
INF = 1000000000
Lists = [0]*N
for i in range(N):
    L = [INF]*N
    Lists[i] = L
    Lists[i][i] = 0
for i in range(M):
    a, b = map(int,input().split())
    Lists[a-1][b-1] = 1
    Lists[b-1][a-1] = 1

cnt = INF

for i in range(N):
    for j in range(N):
        for k in range(N):
            if Lists[j][i] + Lists[i][k] < Lists[j][k] :
                Lists[j][k] = Lists[j][i] + Lists[i][k]

for i in range(N):
    if cnt > sum(Lists[i]):
        cnt = sum(Lists[i])
        k = i
print(k+1)