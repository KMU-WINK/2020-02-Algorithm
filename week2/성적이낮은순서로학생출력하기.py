N = int(input())
array = [[str(x) for x in input().split()]for y in range(N)]

array.sort(key=lambda x:x[1])
for i in array :
    print(i[0],end=" ")