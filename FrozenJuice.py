n, m = input().split()
n = int(n)
m = int(m)

map = [list(map(int, input().split())) for _ in range(n)]

answer = 0
def checkICE(y, x) :
    global answer
    if y == n or x == m or y < 0 or x < 0 :
        return False
    else :
        if map[y][x] == 0 :
            map[y][x] = 1
            checkICE(y+1, x)
            checkICE(y, x-1)
            checkICE(y-1, x)
            checkICE(y, x+1)
            return True
        else :
            return False

for i in range(n) :
    for j in range(m) :
        if checkICE(i, j) == True :
            answer += 1
print(answer)