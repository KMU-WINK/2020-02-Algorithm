N, M = map(int,input().split())
aver = 0
for i in range(N):
    List = list(map(int,input().split()))
    min_num = min(List)
    if aver < min_num:
        aver = min_num
print(min_num)