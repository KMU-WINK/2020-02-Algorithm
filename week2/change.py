import sys

N, K = tuple(map(int, sys.stdin.readline().split()))

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort(reverse=True)

count = 0
while(count != K):

    if(A[count] < B[count]):
        A[count] = B[count]
    # else:
    #     tmp = A[0]
    #     A[0] = B[0]
    #     B[0] = tmp

    count+= 1

answer = 0

for i in range(N):
    answer += A[i]

print(answer)