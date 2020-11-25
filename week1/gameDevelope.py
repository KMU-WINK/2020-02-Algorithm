n,m = input().split()
n,m = int(n), int(m)
y,x,d = input().split()
y,x,d = int(y),int(x),int(d)
array = [[int(i) for i in input().split()]for j in range(n)]
xlist = [0,1,0,-1] #왼쪽 아래 오른쪽 위
ylist = [-1,0,1,0]
def check(x,y): # 사방이 다 막혀있는지 확인
    for i in range(4) :
        if array[x+xlist[i]][y+ylist[i]]!=1:
            return 1
    return 0
def back(x,y,d): #방향유지, 한칸뒤로
    if (n<x or x<0) or (m<y or y<0) :
        return 0
    else :
        if d%2==0:
            return Move(x+xlist[d+1],y+ylist[d+1],d)
        else :
            return Move(x+xlist[(d+3)%4],y+ylist[(d+3)%4],d)
def Move(x,y,d):
    array[x][y] = 1
    while (check(x,y)):
        if d%2==0:
            if array[x+xlist[d]][y+ylist[d]]!=1:
                return Move(x+xlist[d],y+ylist[d],(d+3)%4)+1
            elif array[x+xlist[(d+1)%4]][y+ylist[(d+1)%4]]!=1:
                return Move(x+xlist[(d+1)%4],y+ylist[(d+1)%4],(d+2)%4)+1
            elif array[x+xlist[(d+2)%4]][y+ylist[(d+2)%4]]!=1:
                return Move(x+xlist[(d+2)%4],y+ylist[(d+2)%4],(d+1)%4)+1
            elif array[x+xlist[(d+3)%4]][y+ylist[(d+3)%4]]!=1:
                return Move(x+xlist[(d+3)%4],y+ylist[(d+3)%4],d)+1
        else :
            if array[x+xlist[(d+2)%4]][y+ylist[(d+2)%4]]!=1:
                return Move(x+xlist[(d+2)%4],y+ylist[(d+2)%4],(d+3)%4)+1
            elif array[x+xlist[(d+3)%4]][y+ylist[(d+3)%4]]!=1:
                return Move(x+xlist[(d+3)%4],y+ylist[(d+3)%4],(d+2)%4)+1
            elif array[x+xlist[d]][y+ylist[d]]!=1:
                return Move(x+xlist[d],y+ylist[d],(d+1)%4)+1
            if array[x+xlist[(d+3)%4]][y+ylist[(d+3)%4]]!=1:
                return Move(x+xlist[(d+3)%4],y+ylist[(d+3)%4],d)+1
    return back(x,y,d)
print(Move(x,y,d)+1)
