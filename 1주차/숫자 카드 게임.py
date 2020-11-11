n, m = map(int, input().split())

answer = -10001

for i in range(n):
    card = list(map(int, input().split()))
    answer = max(answer, min(card))

print(answer)