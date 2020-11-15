N = int(input())
array = input().split()
x,y = 1, 1
for i in array :
    if i =='U':
        if x!=1 :
            x-=1
    elif i=='D':
        if x!=N:
            x+=1
    elif i=='R':
        if y!=N:
            y+=1
    else :
        if y!=1:
            y-=1

print(x,y)