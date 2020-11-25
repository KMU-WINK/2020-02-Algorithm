# 너무 어려워서... gg칩니다...
# while문 안의 if gameMap[(A - 1 , B)] == 0 and (A - 1, B) in gabongot == False: 에서 KeyError가 발생하는데...
# 어떻게 해결해야할지 모르겠습니다... Help me please...

N, M = map(int, input().split()) # 3 <= N, M <= 50
A, B, d = map(int, input().split()) # d = 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽

# N x M 좌표계 생성
map_coordinate = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        coordinate = (i, j)
        map_coordinate.append(coordinate)

# 육지, 바다 맵 생성
map_element = []
for i in range(N):
    map_element.append(list(map(int, input().split()))) # 0:육지, 1:바다
map_element = sum(map_element, [])

# {좌표 : 육지바다값} 딕셔너리 생성
gameMap = {name:value for name, value in zip(map_coordinate, map_element)}
print(gameMap)

gabongot = [] # 가본 곳 저장리스트
gabongot.append((A, B)) # 시작 위치를 가본 곳에 저장

# 왼쪽으로 돌기
def turn_left():
    global d
    if d == 0: #북쪽 -> 서쪽
        d = 3
    elif d == 1: #동쪽 -> 북쪽
        d = 0
    elif d == 2: #남쪽 -> 동쪽
        d = 1
    elif d == 3: #서쪽 -> 남쪽
        d = 2

num_gabongot = 1 #방문한 칸의 수
while True:
    turn_left()
    if d == 0:
        if gameMap[(A, B - 1)] == 0 and (A, B - 1) in gabongot == False:
            B -= 1
            num_gabongot += 1
        else:
            if (A, B + 1) == 0:
                B += 1
            else:
                break
    elif d == 1:
        if gameMap[(A + 1, B)] == 0 and (A + 1, B) in gabongot == False:
            A += 1
            num_gabongot += 1
        else:
            if (A - 1, B) == 0:
                A -= 1
            else:
                break
    elif d == 2:
        if gameMap[(A, B + 1)] == 0 and (A, B + 1) in gabongot == False:
            B += 1
            num_gabongot += 1
        else:
            if (A, B - 1) == 0:
                B -= 1
            else:
                break
    elif d == 3:
        if gameMap[(A - 1 , B)] == 0 and (A - 1, B) in gabongot == False:
            A -= 1
            num_gabongot += 1
        else:
            if (A + 1, B) == 0:
                A += 1
            else:
                break

print(num_gabongot)