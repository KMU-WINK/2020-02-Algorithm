N = int(input())
number = []
for i in range(N):
    number.append(int(input()))

for i in range(N):
    for j in range(N-1):
        if(number[j] < number[j+1]):
            tmp = number[j+1]
            number[j+1] = number[j]
            number[j] = tmp

print(number)