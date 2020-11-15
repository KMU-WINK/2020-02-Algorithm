import sys
N,K = (map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort(), B.sort(reverse=True)
answer = sum(A[K:])
print(answer+sum(B[:K]))