import sys,copy

N, M = tuple(map(int, sys.stdin.readline().split()))
map = [list(sys.stdin.readline().rstrip())for x in range(N)]

move = [ #오른쪽 아래 왼쪽 위
    [0,1],
    [1,0],
    [0,-1],
    [-1,0]
]
stack =[(0,0)]
def maze(x,y):
    if not (x==N-1 and y==M-1):  #도착지점이 아니면 canMove로 ㄱㄱ
        return canMove(x,y)
    else :       #도착
        return len(stack)

def canMove(x,y):
    for i in move:
        if (N>x+i[0]and x+i[0]>=0) and (M>(y+i[1]) and y+i[1]>=0):
            if (x==N-2 and y==M-1) or(x==N-1 and y==M-2):  #도착지점의 인근블럭일경우
                stack.append([N-1,M-1])    #도착지점 추가
                return maze(N-1,M-1)       #도착인걸 나타내도록 ~
            if (map[x+i[0]][y+i[1]]=='1'):  #갈수 있는길
                if [x+i[0],y+i[1]] in stack :  # 스택에 이미 있다면 와본 곳이라는뜻
                    map[x][y] ='0'   #되돌아가서 이 길은 막힌길이라는걸로
                    stack.pop()     #스택에서 빼주기
                    return maze(stack[-1][0],stack[-1][1])  #제일 마지막경로로 되돌아가기
                else:              #안와본 길
                    stack.append([x+i[0],y+i[1]])   #길에 추가
                    return maze(x+i[0],y+i[1])


print(maze(0,0))