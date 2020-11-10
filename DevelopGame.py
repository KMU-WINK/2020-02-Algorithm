n, m = input().split()
n = int(n)
m = int(m)

a, b, d = input().split()
a = int(a)
b = int(b)
d = int(d)
gameMap = [list(map(int, input().split())) for _ in range(n)]

gameMap[a][b] = 2

def main() :
    global a, b, d
    end = False
    checkAround = 0
    cnt = 0
    arrA = [0, 1, 0, -1]
    arrB = [-1, 0, 1, 0]
    while end == False:
        for i in range(4) :
            if d == i :
                if gameMap[a+arrA[i]][b+arrB[i]] == 0:
                    checkAround = 0
                    gameMap[a+arrA[i]][b+arrB[i]] = 2
                    cnt += 1
                    a += arrA[i]
                    b += arrB[i]
                if gameMap[a+arrA[i]][b+arrB[i]] == 1 or gameMap[a+arrA[i]][b+arrB[i]] == 2 :
                    if d == 0:
                        d = 3
                    else :
                        d -= 1
                    checkAround += 1
                    if checkAround == 4 :
                        if gameMap[a-arrB[i]][b-arrA[i]] != 1 :
                            checkAround = 0
                            gameMap[a-arrB[i]][b-arrA[i]] = 2
                            cnt += 1
                            a -= arrB[i]
                            b -= arrA[i]
                        else :
                            end = True
    return cnt

answer = main()
print(answer)