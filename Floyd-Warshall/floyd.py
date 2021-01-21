import sys
INF = sys.maxsize
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus_map = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    start, destination , cost = map(int, sys.stdin.readline().split())
    if bus_map[start-1][destination-1]>cost:
        bus_map[start-1][destination-1] = cost

#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            if i == j:
                bus_map[i][j] = 0 #자기 자신과는 친구가 되지 못한다
            else:
                bus_map[i][j] = min(bus_map[i][j],
                                       bus_map[i][k] + bus_map[k][j])


#출력
for i in bus_map :
    for j in i :
        if j==INF:
            print(0,end=' ')
        else: print(j,end=' ')
    print()