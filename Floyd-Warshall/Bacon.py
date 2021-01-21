import sys
N, M = map(int, sys.stdin.readline().split())
friend_map = [[N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    friend_A, friend_B = map(int, sys.stdin.readline().split())
    friend_map[friend_A-1][friend_B-1] = 1
    friend_map[friend_B-1][friend_A-1] = 1


#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            if i == j:
                friend_map[i][j] = 0 #자기 자신과는 친구가 되지 못한다
            else:
                friend_map[i][j] = min(friend_map[i][j],
                                       friend_map[i][k] + friend_map[k][j])


#출력
answer = []
for row in friend_map:
    answer.append(sum(row))
print(answer.index(min(answer)) + 1)