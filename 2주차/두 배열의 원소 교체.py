import sys

n, m = map(int, sys.stdin.readline().split())

smallList = sorted(list(map(int, input().split())))
bigList = sorted(list(map(int, input().split())), reverse=True)

for i in range(m):
    if smallList[i] < bigList[i]:
        smallList[i] = bigList[i]

print(sum(smallList))