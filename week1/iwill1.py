import sys
args = list(map(int, sys.stdin.readline().split()))

n, k, count = args[0], args[1], 0

while n > 1:
    count += 1
    n = n / k if n % k == 0 else n - 1

print(count)