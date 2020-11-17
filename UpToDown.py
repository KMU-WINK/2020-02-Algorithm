n = int(input())
arr = []
for i in range(n):
    value = int(input())
    arr.append(value)

arr.sort(reverse=True)

for i in arr:
    print(i, end = ' ') #공백으로 구분해 출력