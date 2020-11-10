n, k = input().split()
n = int(n)
k = int(k)

count = 0

if n > 0 :
    n = n-1
    count += 1

while n >= k:
    n //= k
    count += 1

print(count)