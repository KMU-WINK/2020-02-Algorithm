N, M = map(int, input().split())
route = []
posX,posY = 0,0
cnt = 1
for i in range(N):
    x = input()
    route.append(x)

while(True):
    try:
        if route[posX][posY+1] == '0':
            posX += 1
            cnt += 1

        else:
            posY += 1
            cnt += 1
        if posX == N-1 and posY == M-1:
            break
    except:
        if posX == N:
            posY += 1
            cnt += 1
        else:
            posX += 1
            cnt += 1
        if posX == N-1 and posY == M-1:
            break

print(cnt)

