n = int(input()) # 정사각형 크기
answerX, answerY = 1, 1
movePlans = input().split() # 이동 경로

directionX = [0, 0, -1, 1] # LRUD
directionY = [-1, 1, 0, 0] # LRUD
direction = ['L', "R", "U", "D"] # 좌우상하

for movePlan in movePlans:
    for i in range(len(direction)):
        if movePlan == direction[i]:
            nx = answerX + directionX[i]
            ny = answerY + directionY[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    answerX, answerY = nx, ny

print(answerX, answerY)