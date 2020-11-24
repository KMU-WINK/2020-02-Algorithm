import sys
N, M = tuple(map(int, sys.stdin.readline().split()))
map = [list(sys.stdin.readline().rstrip())for x in range(N)]
cnt = 0
def makeIceCream(x,y):
    if x<0 or x>N-1 or y<0 or y>M-1:
        return False
    if map[x][y]=='0':
        map[x][y] = '1'
        makeIceCream(x-1,y)
        makeIceCream(x+1,y)
        makeIceCream(x,y+1)
        makeIceCream(x,y-1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if makeIceCream(i,j) == True:
            cnt+=1
print(cnt)