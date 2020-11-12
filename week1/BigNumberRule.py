import sys


n, m, k = tuple(map(int, sys.stdin.readline().split()))
args = list(map(int, sys.stdin.readline().split()))
args.sort(reverse=True)

count = 0
max_count = 0
for i in range(m):
    if max_count < k:
        count += args[0]
        max_count += 1
    else:
        count += args[1]
        max_count = 0

print(count)