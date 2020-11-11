N, M = map(int, input().split())

largeNumbers = []
for i in range(N):
    number = list(map(int, input().split()))
    minValue = number[0]
    for j in range(len(number)):
        if minValue > number[j]:
            minValue = number[j]
    largeNumbers.append(minValue)

maxValue = largeNumbers[0]
for i in range(len(largeNumbers)):
    if maxValue < largeNumbers[i]:
        maxValue = largeNumbers[i]

print(maxValue)