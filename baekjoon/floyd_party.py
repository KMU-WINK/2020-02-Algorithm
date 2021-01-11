import sys

N, M, X = map(int, sys.stdin.readline().split())

result1 = [[sys.maxsize for _ in range(N+1)] for t in range(N+1)]
result2 = [[sys.maxsize for _ in range(N+1)] for t in range(N+1)]

for i in range(1,N+1):
    result1[i][i] = 0
    result2[i][i] = 0


for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    result1[i][j] = k
    result2[j][i] = k

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

            if(result1[i][j] > result1[i][k] + result1[k][j]):
                result1[i][j] = result1[i][k] + result1[k][j]

            if (result2[i][j] > result2[i][k] + result2[k][j]):
                result2[i][j] = result2[i][k] + result2[k][j]

answer = [0 for _ in range(N+1)]

for i in range(1,N+1):
    answer[i] = result1[i][X]
    answer[i] += result2[i][X]

print(max(answer))