n, k = map(int, input().split())

answer = 0

while True:
    if n % k == 0:
        n //= k
    else:
        n -= 1

    answer += 1
    if n == 1:
        break

print(answer)
