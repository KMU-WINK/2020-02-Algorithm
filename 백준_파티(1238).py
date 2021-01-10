import sys
import heapq

INF = sys.maxsize

N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, d, t = map(int, input().split())
    arr[s].append([d, t])

def dijkstra(arr, s):
    dist = [INF] * len(arr)
    dist[s] = 0

    heap = []
    heapq.heappush(heap, [0, s])

    while heap:
        time, node = heapq.heappop(heap)

        for i, j in arr[node]:
            next = dist[node] + j

            if next < dist[i] :
                dist[i] = next
                heapq.heappush(heap, [next, i])

    return dist

cost = []
dist_h = dijkstra(arr, X)

for i in range(1, N+1):
    dist = dijkstra(arr, i)
    cost.append(dist[X] + dist_h[i])

print(max(cost))