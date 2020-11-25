n, m, k= map(int,input().split())
List = list(map(int,input().split()))
max_list1 = max(List)
List.remove(max_list1)
max_list2 = max(List)
answer = 0
while(True):
    for i in range(k):
        answer += max_list1
        m -= 1
        if(m == 0):
            break
    if(m == 0):
        break
    answer += max_list2
    m -= 1
    if(m == 0):
        break

print(answer)
