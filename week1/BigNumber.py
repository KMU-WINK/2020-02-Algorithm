N, M, K = input().split()

N = int(N)
M = int(M)
K = int(K)

answer = 0

num = list(input().split())

for i in range(len(num)):
    num[i]= int(num[i])

num.sort(reverse = True)

for i in range(1,M+1):
    if(i%(K+1) !=0):
        answer += int(num[0])
    else:
        answer += int(num[1])

print(answer)
