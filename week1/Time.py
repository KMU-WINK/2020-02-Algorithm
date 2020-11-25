N = int(input())

onetime = 0

three = [3, 13, 23, 33, 43, 53, 30, 31, 32, 34, 35, 36, 37, 38, 39]

answer = 0

for i in range(60):
    for j in range(60):
        if ((i in three) or (j in three)):
            onetime += 1

for i in range(N+1):
    if(i == 3 or i == 13 or i == 23):
        answer += 60 * 60

    else:
        answer += onetime

print(answer)