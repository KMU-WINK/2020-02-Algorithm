n = int(input())
arr = {}
for i in range(n):
    n, k = input().split()
    k = int(k)
    arr[n] = k

answer = sorted(arr.items(), key = lambda item: item[1])

for key,value in answer:
    print(key, end = ' ') #공백으로 구분해 출력