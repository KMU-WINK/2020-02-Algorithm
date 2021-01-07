import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 갈 수 없는 지역을 cost 10억으로 설정한다.

node, edge = map(int, input().split())
start = int(input())

graph = [[] for _ in range(node + 1)]
distance = [INF] * (node + 1)

for _ in range(edge):
    s, a, c = map(int, input().split())  # s : 출발지점, a : 도착지점, c : cost
    graph[s].append((a, c))


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        distanceCost, nowNode = heapq.heappop(heap)

        if distance[nowNode] < distanceCost:  # 이미 방문해서 처리를 끝냈다면 무시한다.
            continue

        for i in graph[nowNode]:
            cost = distanceCost + i[1]  # 0 : 현 도착 지점까지의 코스트, 1 : cost
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(start)

for i in range(1, node + 1):
   if distance[i] == INF:
       print("INF")
   else:
       print(distance[i])