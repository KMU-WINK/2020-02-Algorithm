import sys

N, M = map(int, sys.stdin.readline().split())

result = [[sys.maxsize for _ in range(N+1)] for t in range(N+1)]

for _ in range(N+1):
    result[_][_] = 0

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result[i][j] = 1
    result[j][i] = 1


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


# 누가 적은지 확인하기위해 덧셈
answer = [0 for _ in range(N+1)]
answer[0] = sys.maxsize
for i in range(1,N+1):
    for j in range(1,N+1):
        answer[i] += result[i][j]

# 가장 적은 사람 출력
print(answer.index(min(answer)))