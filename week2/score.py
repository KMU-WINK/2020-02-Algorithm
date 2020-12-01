N = int(input())
numlist = []

for i in range(N):
    student, score = input().split()
    score = int(score)
    numlist.append((student,score))

for i in range(N):
    for j in range(N-1):
        if(int(numlist[j][1]) > int(numlist[j+1][1])):
            tmp = numlist[j+1]
            numlist[j+1] = numlist[j]
            numlist[j] = tmp


for i in range(N):
    print(numlist[i][0], end=' ') #옆으로 이어서 출력