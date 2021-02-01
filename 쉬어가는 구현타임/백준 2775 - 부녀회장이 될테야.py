import sys

input = lambda: sys.stdin.readline().rstrip()

def countCitizen(k, n):
    if (n == 1): return 1
    if (k == 0): return n

    return countCitizen(k - 1, n) + countCitizen(k, n - 1)

tc = int(input())

for _ in range(tc):
    k = int(input())
    n = int(input())
    print(countCitizen(k, n))




