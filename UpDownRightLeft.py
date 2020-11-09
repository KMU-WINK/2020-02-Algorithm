n = int(input())
arr = input().split()
x,y=1,1
for i in range(len(arr)):
    if arr[i]=='L' and x>1:
        x-=1
    elif arr[i]=='U' and y>1:
        y-=1
    elif arr[i]=='R':
        x+=1
    elif arr[i]=='D':
        y+=1
print(x,y)