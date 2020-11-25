import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
print(max([min(list(map(int, sys.stdin.readline().split()))) for i in range(n)]))