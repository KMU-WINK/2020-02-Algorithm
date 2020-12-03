import sys

N, M = tuple(map(int, sys.stdin.readline().split()))

money = []

for i in range(N):
    don = int(sys.stdin.readline())
    if(don <= M):
        money.append(don)

check = [-1 for x in range(M+1)]

for i in money:
    check[i] = 1

for i in range(len(check)):
    for j in money:
        if(check[i] == -1 or i+j > M):
            continue

        if(check[i+j] == -1):
            check[i+j] = check[i] + 1

        if(check[i]+1 < check[i+j]):
            check[i+j] = check[i] + 1

print(check[-1])