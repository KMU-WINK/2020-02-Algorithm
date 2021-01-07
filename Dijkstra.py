import sys
from heapq import heappush, heappop
r = sys.stdin.readline
INF = 1e9


def dijkstra(n, x, ro):
    dist = [INF] * n
    dist[x] = 0
    q = []
    heappush(q, [0, x])

    while q:
        cost, pos = heappop(q)

        for p, c in ro[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])

    return dist


N, M, X = map(int, r().split())
road = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, r().split())
    road[u-1].append([v-1, t])

answer = [0] * N
for i in range(N):
    ret = dijkstra(N, i, road)

    if i == X-1:
        for idx, r in enumerate(ret):
            answer[idx] += r
    else:
        answer[i] += ret[X-1]
print(max(answer))