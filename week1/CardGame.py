N, M = input().split()
N,M = int(N), int(M)
array = [[int(x) for x in input().split()]for y in range(N)]

cnt = 0
i= 0
while(i<N):
    if cnt<min(array[i]):
        cnt = min(array[i])
    i+=1

print(cnt)