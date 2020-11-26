n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

sorted_numbers = sorted(numbers, reverse=True)
sorted_numbers = list(map(str, sorted_numbers))
print(' '.join(sorted_numbers))