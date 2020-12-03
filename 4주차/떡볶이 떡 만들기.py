import sys
n, m = map(int, sys.stdin.readline().split())

rice_cakes = list(map(int, sys.stdin.readline().split()))
max_tteok = max(rice_cakes)
min_tteok = 0

def cutting(rice_cakes, cutting_value):
    value = 0
    for rice_cake in rice_cakes:
        if rice_cake < cutting_value:
            continue
        else:
            value += rice_cake - cutting_value

    return value

while True:
    cut_length = (max_tteok + min_tteok) // 2
    answer = cutting(rice_cakes, cut_length)

    if answer == m:
        print(cut_length)
        break
    elif answer > m:
        min_tteok = cut_length
    elif answer < m :
        max_tteok = cut_length