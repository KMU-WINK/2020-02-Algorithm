import sys

n, m = map(int, sys.stdin.readline().split())

rice_list = list(map(int, input().split()))[:n]
rice_list.sort()

def cut_ricecake(start, end):
    lenght = 0

    if start > end:
        return None

    mid = (start + end) // 2

    for i in rice_list :
        if mid < i :
            lenght += i - mid

    if lenght == m :
        return mid
    elif lenght < m :
        end = mid
    else :
        start = mid

    return cut_ricecake(start, end)

print(cut_ricecake(rice_list[0], rice_list[n - 1]))