def R(x,y):
    cnt=0
    if (x+2<8):
        if (y-1>=0):
            cnt+=1
        if  (y+1<8):
            cnt+=1
    return cnt
def L(x,y):
    cnt=0
    if (x-2)>=0:
        if (y-1>=0):
            cnt+=1
        if  (y+1<8):
            cnt+=1
    return cnt
def U(x,y):
    cnt=0
    if (y-2>=0):
        if (x-1>=0):
            cnt+=1
        if (x+1<8):
            cnt+=1
    return cnt
def D(x,y):
    cnt=0
    if (y+2<8):
        if (x-1>=0):
            cnt+=1
        if (x+1<8):
            cnt+=1
    return cnt

def knight(x, y): #udlr 로 4개로나눠서 함수구현
    return U(x,y)+D(x,y)+R(x,y)+L(x,y)

xy = input()
row = ['a','b','c','d','e','f','g','h']
x= row.index(xy[0])
y = int(xy[1])-1
print(knight(x,y))