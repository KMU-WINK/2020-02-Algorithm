import sys
sys.setrecursionlimit(1500)
n, m = map(int, sys.stdin.readline().split())
numberList=[]
for i in range(m):
    cal, a, b = map(int, sys.stdin.readline().split())
    numberList.append([cal, a, b])

parent = [x for x in range(n+1)]

def get(a):
    if parent[a] == a:
        return a
    p = get(parent[a])
    parent[a] = p
    return p

def find(a):
    if parent[a] != a:
        return find(parent[a])
    return a

def union(a, b):
    rootA = get(a)
    rootB = get(b)
    parent[rootB] = rootA

for i in numberList:
    if i[0] == 0:
        union(i[1], i[2])
    if i[0] == 1:
        if find(i[1]) == find(i[2]):
            print("YES")
        else:
            print("NO")