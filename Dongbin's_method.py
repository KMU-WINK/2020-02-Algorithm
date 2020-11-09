N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
numbers.reverse()

i = 1
j = 1
sum = 0
while i <= M:
    if j <= K:
        sum += numbers[0]
    else:
        sum += numbers[1]
        j = 1
    i += 1
    j += 1

print(sum)

