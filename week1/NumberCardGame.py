import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
matrix = [min(list(map(int, sys.stdin.readline().split()))) for i in range(n)]

print(max(matrix))