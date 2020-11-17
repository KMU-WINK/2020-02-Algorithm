n, k = input().split()
n = int(n)
k = int(k)
arr1 = list(map(int, input().split()))[:n] #n개의 입력만 받을 수 있게 배열을 슬라이스 처리
arr2 = list(map(int, input().split()))[:n]
answer = 0

for i in range(k):
    arr1_num_idx = arr1.index(min(arr1))
    arr2_num_idx = arr2.index(max(arr2))
    arr1[arr1_num_idx] = max(arr2)
    arr2[arr2_num_idx] = min(arr1)

for i in arr1 :
    answer += i

print(answer)