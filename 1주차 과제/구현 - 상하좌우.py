n = int(input())
way = input().split()
x,y = 1,1
for i in range(len(way)):
    if way[i] == 'R' :
        if x+1 == n+1:  continue
        x += 1
    elif way[i] == 'L':
        if x-1 == 0:    continue
        x -= 1
    elif way[i] == 'U':
        if y-1 == 0:    continue
        y -= 1
    elif way[i] == 'D':
        if y+1 == n+1:  continue
        y += 1

print(y,x)