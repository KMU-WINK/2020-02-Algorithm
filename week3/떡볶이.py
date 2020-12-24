n, m = map(int, input().split())
riceCake = list(map(int, input().split()))

cutterHeight = {
    'min': 0,
    'max': max(riceCake),
}

while True:
    settingHeight = cutterHeight['min'] + ((cutterHeight['max'] - cutterHeight['min']) // 2) # 비교 높이 설정
    awserLength = sum(map(lambda x: x - settingHeight if x - settingHeight > 0 else 0, riceCake)) # 잘린 떡 합 구하기
    if awserLength < m:
        cutterHeight['max'] = settingHeight - 1
    elif awserLength > m:
        cutterHeight['min'] = settingHeight + 1
    else:
        print(settingHeight)
        break