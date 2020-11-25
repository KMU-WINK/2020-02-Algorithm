n, m = input().split()
n = int(n)
m = int(m)

gameMap = [list(map(int, input().split())) for _ in range(n)]

x = 0
y = 0
arrX = [1, 0, -1, 0]
arrY = [0, 1, 0, -1]

gameMap[x][y] = 2
cnt = 1
while x != m-1 or y != n-1 :
    for i in range(4):
        try:
            if gameMap[y+arrY[i]][x+arrX[i]] == 1:
                gameMap[y+arrY[i]][x+arrX[i]] = 2
                x+=arrX[i]
                y+=arrY[i]
                cnt += 1
                break
        except IndexError: #인덱스 범위 벗어나면 다음 루프를 돌 수 있게
            continue

print(cnt)