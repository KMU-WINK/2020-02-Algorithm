import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 갈 수 없는 지역을 time 10억으로 설정한다.

def dijkstra(partyPlace, graph):
    heap = []
    distance = [INF] * (student + 1)
    heapq.heappush(heap, (0, partyPlace))
    distance[partyPlace] = 0
    while heap:
        distanceTime, nowstudent = heapq.heappop(heap)

        if distance[nowstudent] < distanceTime:  # 이미 방문해서 처리를 끝냈다면 무시한다.
            continue

        for i in graph[nowstudent]:
            time = distanceTime + i[1]  # 0 : 현 도착 지점까지의 시간, 1 : time
            if time < distance[i[0]]:
                distance[i[0]] = time
                heapq.heappush(heap, (time, i[0]))

    return distance

student, edge, partyPlace = map(int, input().split())

returnGraph = [[] for _ in range(student + 1)]
goGraph = [[] for _ in range(student + 1)]

for _ in range(edge):
    s, a, t = map(int, input().split())  # s : 출발지점, a : 도착지점, t : 걸리는 시간
    returnGraph[s].append((a, t)) # 집으로 돌아가는 그래프
    goGraph[a].append((s, t)) # 파티 장소로 가는 그래프

distance = dijkstra(partyPlace, returnGraph) # 집으로 돌아가는 코스트
timeTable = distance # 집으로 돌아가는 코스트 저장

distance = dijkstra(partyPlace, goGraph) # 파티 장소로 가는 코스트

totalTime = [x + y for x, y in zip(timeTable[1:student + 1], distance[1:student + 1])] # 집으로 돌아가는 코스트와 파티 장소로 가는 코스트를 더한다
print(max(totalTime))


