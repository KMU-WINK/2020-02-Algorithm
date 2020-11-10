n, m = input().split()
n = int(n)
m = int(m)

arr = [list(map(int, input().split())) for _ in range(n)]


answer = 0
for i in range(len(arr)):
    min_number = min(arr[i])
    if(answer < min_number):
        answer = min_number

print(answer)