n, m = map(int, input().split())
heights = list(map(int, input().split()))

# 이진 탐색의 시작값과 끝값
start = 0
end = max(heights)

result = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0
    # 떡을 하나하나 잘라서 손님 주는 떡 길이를 sum에 저장
    for i in range(len(heights)):
        cut = heights[i] - mid
        if cut >= 0:
            sum += cut
        else:
            continue
    # sum이 손님한테 줄 조건을 충족했을 때
    if ((sum / m) == 1) and ((sum % m) <= n):
        result = mid
        break
    # sum이 손님한테 줄 길이보다 작을 때. 더 작은 H값을 찾음
    elif sum < m:
        end = mid - 1
        continue
    # 위 두 경우가 아닐 때는 더 큰 H값을 찾음
    else:
        start = mid + 1
        continue

print(result)


