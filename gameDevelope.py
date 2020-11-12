n,m = input().split()
n,m = int(n), int(m)
y,x,d = input().split()
y,x,d = int(y),int(x),int(d)
array = [[int(i) for i in input().split()]for j in range(n)]

def check(x,y,d):
    # if x!=0 and y!=0:
    if array[x][y-1]+array[x][y+1]+array[x+1][y]+array[x-1][y]==4: #사방이 다 가보거나 바다
        return 0
    else :
        return 1

def Move(x,y,d):
    array[x][y] = 1
    while (check(x,y,d)):
        if d==0:
            if array[x][y-1]!=1:
                return Move(x,y-1,(d+3)%4)+1
            elif array[x+1][y]!=1:
                return Move(x+1,y,(d+2)%4)+1
            elif array[x][y+1]!=1:
                return  Move(x,y+1,(d+1)%4)+1
            elif array[x-1][y]!=1:
                return Move(x-1,y,d)+1
        elif d==1:
            if array[x-1][y]!=1:
                return Move(x-1,y,(d+3)%4)+1
            elif array[x][y-1]!=1:
                return Move(x,y-1,(d+2)%4)+1
            elif array[x+1][y]!=1:
                return Move(x+1,y,(d+1)%4)+1
            elif array[x][y+1]!=1:
                return Move(x,y+1,d)+1
        elif d==2:
            if array[x][y+1]!=1:
                return Move(x,y+1,(d+3)%4)+1
            elif array[x-1][y]!=1:
                return Move(x-1,y,(d+2)%4)+1
            elif array[x][y-1]!=1:
                return Move(x,y-1,(d+1)%4)+1
            elif array[x+1][y]!=1:
                return Move(x+1,y,d)+1
        elif d==3:
            if array[x+1][y]!=1:
                return Move(x+1,y,(d+3)%4)+1
            elif array[x][y+1]!=1:
                return Move(x,y+1,(d+2)%4)+1
            elif array[x-1][y]!=1:
                return Move(x-1,y,(d+1)%4)+1
            elif array[x][y-1]!=1:
                return Move(x,y-1,d)+1
    return 0

print(Move(x,y,d)+1)