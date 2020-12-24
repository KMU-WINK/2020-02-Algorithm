import sys

N, M = tuple(map(int, sys.stdin.readline().split()))

rice_cake = [int(x) for x in sys.stdin.readline().split()]

small = 0 # 짤린 떡 세기위한 변수
big = max(rice_cake) # 기계가 가지는 최댓
total = 0

while(True):

    middle = int((small + big)/2)
    total = 0
    for i in rice_cake:
        if(i > middle):
            total += i - middle
        else:
            continue

    if total > M:
        small = middle
    elif total < M:
        big = middle
    else:
        middle = int((small + big)/2)
        break

print(middle)