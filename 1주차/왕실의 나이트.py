knightPoint = input()
row = int(knightPoint[1])
col = int(ord(knightPoint[0])) - int(ord('a')) + 1
# 기사의 col은 알파벳이므로 아스키 코드 값을 Int로 받고 시작점인 a의 아스키코드를 빼고 1을 더하면 col도 숫자로 나타낼 수 있다.

ableDirections = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
answer = 0

for ableDirection in ableDirections:
    nextRow = row + ableDirection[0]
    nextCol = col + ableDirection[1]

    if nextRow >= 1 and nextRow <= 8 and nextCol >= 1 and nextCol <= 8:
        answer += 1

print(answer)