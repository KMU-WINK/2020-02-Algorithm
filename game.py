n, m = map(int, input().split())
a, b, d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
Map[a][b] = 1
move = 1
turn_cnt=0

def spin():
    global d
    d -= 1
    if d < 0:
        d = 3


while True:
    spin()
    row = a + dx[d]
    col = b + dy[d]
    if Map[row][col] == 0:
        Map[row][col] = 1
        a = row
        b = col
        move += 1
        turn_cnt=0
        continue
    else:
        turn_cnt+=1
    if turn_cnt ==4:
        row = a-dx[d]
        col = b-dy[d]
        if Map[row][col]==0:
            a = row
            b = col
        else:
            break
        turn_cnt =0

print(move)
