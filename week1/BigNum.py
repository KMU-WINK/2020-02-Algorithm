arrayNum,M,N = input().split()
array = list(map(int,input().split()))
arrayNum,M,N = int(arrayNum), int(M), int(N)

array.sort(reverse=True)

cnt = 0
while(M>0):
    if M>N:
        cnt += int(array[0])*int(N)
        M-=N
    else :
        cnt+=array[1:][0]
        M-=1

print(cnt)