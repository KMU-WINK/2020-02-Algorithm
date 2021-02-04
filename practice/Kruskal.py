import sys

def findParent(x, P):
    if P[x] != x:
        return findParent(P[x], P)

    else:
        return x


def isSameParent(x, y, P):
    xP = findParent(x, P)
    yP = findParent(y, P)

    return xP == yP


def union(x, y, P):
    xP = findParent(x, P)
    yP = findParent(y, P)

    if xP > yP:
        P[x] = yP

    else:
        P[y] = xP
        P[yP] = xP


def isfinished(P):
    for i in range(1, len(P)):
        if findParent(i, P) != 1:
            return False

    return True


N, INP = map(int, sys.stdin.readline().split())

edge = []
P = [i for i in range(N+1)]
result = []

for i in range(INP):
    row, col, value = map(int, sys.stdin.readline().split())
    edge.append((value, row, col))

edge.sort()
index = 0

while(not isfinished(P)):
    value, x, y = edge[index]
    if not isSameParent(x, y, P):
        result.append((x, y, value))
        union(x, y, P)

    index += 1


for i in range(len(result)):
    print(result[i])
