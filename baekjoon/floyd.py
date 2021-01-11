import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

result = [[sys.maxsize for _ in range(N+1)] for t in range(N+1)]

for _ in range(N+1):
    result[_][_] = 0

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    if(result[i][j] > k):
        result[i][j] = k


for k in range(1, N+1):
    # k는 거쳐가는 친구

    for i in range(1, N+1):
        # i 는 시작
        if(i == k):
            continue

        for j in range(1, N+1):
            # j는 끝나는 친구
            if(j == i):
                continue

            if(result[i][j] > result[i][k] + result[k][j]):
                result[i][j] = result[i][k] + result[k][j]


for i in range(1,N+1):
    for j in range(1,N+1):
        if(result[i][j] == sys.maxsize):
            continue
        print(result[i][j], end=' ')
    print()