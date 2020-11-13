num=0
n,m,k = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort(reverse=True)
a=arr[0]
b=arr[1]
if a==b:
    num=a*m
    print(num)
else:
    c= int(m/k)*k
    d= m-c
    num = a*c
    num += b*d
    print(num)