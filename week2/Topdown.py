N = int(input())
number = []
for i in range(N):
    number.append(int(input()))

for i in range(N-1):
    for j in range(i,N-1):
        if(number[i] < number[i+1]):
            tmp = number[i+1]
            number[i+1] = number[i]
            number[i] = tmp

print(number)