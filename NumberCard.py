n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
max=0
for i in range(n):
    if max<sorted(a[i])[0]:
        max=sorted(a[i])[0]
print(max)