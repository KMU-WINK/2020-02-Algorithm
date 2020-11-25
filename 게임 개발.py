N, M = map(int,input().split())
pos = [0,0]
pos[0], pos[1], d = map(int,input().split())
cnt = 0
Map = []
Map_count = []
for i in range(N):
    Map.append(list(map(int,input().split())))
for i in range(N):
    Map_count_m = [0 for i in range(M)]
    Map_count.append(Map_count_m)
while(True):
    back_count = 0
    d -= 1
    if d == -1:
        d = 3
    try:

        if d == 0:
            if Map[pos[0]-1][pos[1]] == 0 and Map_count[pos[0]-1][pos[1]] == 0:
                pos[0] -= 1
                cnt += 1
                Map_count[pos[0] - 1][pos[1]] = 1
            else:
                back_count += 1

        if d == 1:
            if Map[pos[0]][pos[1]+1] == 0 and Map_count[pos[0]][pos[1]+1] == 0:
                pos[1] += 1
                cnt += 1
                Map_count[pos[0]][pos[1]+1] = 1
            else:
                back_count += 1

        if d == 2:
            if Map[pos[0]+1][pos[1]] == 0 and Map_count[pos[0]+1][pos[1]] == 0:
                pos[0] += 1
                cnt += 1
                Map_count[pos[0] + 1][pos[1]] = 1
            else:
                back_count += 1
        if d == 3:
            if Map[pos[0]][pos[1]-1] == 0 and Map_count[pos[0]][pos[1]-1] == 0:
                pos[1] -= 1
                cnt += 1
                Map_count[pos[0]][pos[1] - 1] = 1
            else:
                back_count += 1

        if back_count == 4:
            if d == 0:
                if Map[pos[0] - 1][pos[1]] == 1:
                    break
                else:
                    back_count = 0
            elif d == 1:
                if Map[pos[0] ][pos[1] + 1] == 1:
                    break
                else:
                    back_count = 0
            elif d == 2:
                if Map[pos[0] +1 ][pos[1]] == 1:
                    break
                else:
                    back_count = 0
            else:
                if Map[pos[0] ][pos[1] - 1] == 1:
                    break
                else:
                    back_count = 0



    except:
        continue
print(cnt)

#구현 실패..

