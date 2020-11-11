N, K = map(int, input().split())
attempt = 0

while N > 1:
    if N % K == 0:
        M = N // K
        N = M
    else:
        N -= 1
    attempt += 1

print(attempt)