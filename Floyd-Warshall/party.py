import sys
INF = sys.maxsize
N,M,X = map(int, sys.stdin.readline().split())
party_map = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    start, destination , cost = map(int, sys.stdin.readline().split())
    if party_map[start-1][destination-1]>cost:
        party_map[start-1][destination-1] = cost

#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            if i == j:
                party_map[i][j] = 0 #자기 자신과는 친구가 되지 못한다
            else:
                party_map[i][j] = min(party_map[i][j],
                                       party_map[i][k] + party_map[k][j])


#출력
answer=[]
for i in range(N):
    answer.append(party_map[i][X]+party_map[X][i])
print(max(answer))