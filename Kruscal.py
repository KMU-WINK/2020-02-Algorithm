import sys
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n) :
    start, end, distance = map(int, sys.stdin.readline().split())
    graph.append([start, end, distance])

cycle = [i for i in range(1, m+1)]

graph.sort(key = lambda x:x[2])

def find(a):
    if a != cycle[a-1]:
        cycle[a-1] = find(cycle[a-1])
    return cycle[a-1]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    cycle[rootB-1] = rootA

cost = 0
cnt = 0
tree = []
for i in graph:
    if cnt == m-1:
        break
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        cost += i[2]
        cnt += 1
        tree.append([i[0], i[1]])

print(cost)
print(tree)