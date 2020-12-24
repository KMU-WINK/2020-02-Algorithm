# 강의 영상을 보았으나... 저 공식을 이해하지 못했습니다...
# 내 머리가 너무나 나빠서...
# 다이나믹 프로그래밍... 이름 깐지나요 멋있다...
n, m = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(money[i], m + 1):
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
    
