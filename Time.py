N = int(input())
minute = range(60)
second = range(60)

count = 0
for i in range(N + 1):
    for j in minute:
        for k in second:
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)