import sys

N, M = tuple(map(int, sys.stdin.readline().split()))

money = []

for i in range(N):
    money.append(int(sys.stdin.readline()))

money.sort(reverse=True)

result = []

for i in range(len(money)):
    count = 0
    total = M
    check = i

    while(total != 0):
        if(total >= money[check]):
            total -= money[check]
            count += 1

        else:
            check += 1

        if(check == len(money)):
            result.append(-1)
            break

    if(total == 0):
        result.append(count)

small = M # M은 나올수 있는 최댓값.
check2 = 0 # -1로 채워져 있는지 확인

for i in range(len(result)):
    if(result[i] != -1 and small > result[i]):
        check2 = 1
        small = result[i]

print(small if check2 else -1)