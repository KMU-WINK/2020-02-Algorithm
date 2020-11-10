n, k = input().split()
n = int(n)
k = int(k)

count = 0

while n >= k:
    if n % k != 0 :
        n -= 1
    else :
        n //= k
    count += 1

print(count)