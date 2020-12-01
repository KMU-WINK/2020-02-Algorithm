N, K = map(int,input().split())
listA = list(map(int,input().split()))
listB = list(map(int,input().split()))
listA.sort()
listB.sort()
cnt = 0
a = N - 1
b = N - 1
for i in range(N):
    if K > 0:
        if listA[a] > listB[b]:
            cnt += listA[a]
            a -= 1
        else:
            cnt += listB[b]
            b -= 1
            K -= 1
    else:
        cnt += listA[a]
        a -= 1
print(cnt)
