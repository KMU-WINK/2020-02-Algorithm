import sys,heapq
INF = sys.maxsize
N,M,X = (map(int, sys.stdin.readline().split()))
D = [[]*N for _ in range(N)]
heap = []

def dij(x):
    d = [INF]*N
    heapq.heappush(heap, [0, x])
    d[x] = 0
    while heap:
        w, x = heapq.heappop(heap)
        for nw, nx in D[x]:
            nw += w
            if nw < d[nx]:
                d[nx] = nw
                heapq.heappush(heap, [nw, nx])
    return d

for i in range(M):
    x, y, w = map(int, input().split())
    D[x-1].append([w, y-1])

ans = [0]*N
for i in range(N):
    d = dij(i)
    ans[i] += d[X-1]
    d = dij(X-1)
    ans[i] += d[i]
print(max(ans))
