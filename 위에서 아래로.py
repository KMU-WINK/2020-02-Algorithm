N = int(input())
sort_list = []
for i in range(N):
    x = int(input())
    sort_list.append(x)
sort_list.sort()
sort_list.reverse()
print(sort_list)