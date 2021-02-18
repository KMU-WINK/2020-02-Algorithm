import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

root = [x for x in range(1, n+1)]

def find(a):
    if root[a-1] != a:
        return find(root[a-1])
    return a

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    root[rootB-1] = rootA

for i in range(1, n+1):
    routines = list(map(int, sys.stdin.readline().split()))
    for idx_j, j in enumerate(routines):
        if j == 1:
            union(i, idx_j+1)

place = list(map(int, sys.stdin.readline().split()))
result = set([find(i) for i in place])
if len(result) != 1:
    print("NO")
else:
    print("YES")