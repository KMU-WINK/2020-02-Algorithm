import sys

N, K = tuple(map(int, sys.stdin.readline().split()))

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


count = 0
while(count != K):
    A.sort()
    B.sort(reverse=True)

    if(A[0] > B[0]):
        break
    else:
        tmp = A[0]
        A[0] = B[0]
        B[0] = tmp

    count+= 1

answer = 0

for i in range(N):
    answer += A[i]

print(answer)