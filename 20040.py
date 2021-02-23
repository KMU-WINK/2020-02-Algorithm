import sys
sys.setrecursionlimit(1500)

n, m = map(int, sys.stdin.readline().split())

root = [x for x in range(n)]

def get(a):
    if root[a] == a:
        return a
    p = get(root[a])
    root[a] = p
    return p

def find(a):
    if root[a] != a:
        return find(root[a])
    return a

def union(a, b):
    rootA = get(a)
    rootB = get(b)
    root[rootB] = rootA

answer = 0
for i in range(m):
    dotA, dotB = map(int, sys.stdin.readline().split())
    if find(dotA) != find(dotB):
        union(dotA, dotB)
    else :
        answer = i+1
        break

print(answer)