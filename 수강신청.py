import sys

a, b = map(int, input().split())
s = []
m = {}

for i in range(b):
    s.append(sys.stdin.readline().rstrip())
k = 0
for i in s:
    m[i] = k
    k += 1


def sortkey(z):
    return z[1]


sortedlist = sorted(m.items(), key=sortkey)
for i in sortedlist[:a]:
    print(i[0])