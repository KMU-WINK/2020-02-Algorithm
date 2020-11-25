n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
num_list = list(map(int, input().split()))[:n] #n개의 입력만 받을 수 있게 배열을 슬라이스 처리
answer = 0
cnt = 0

largest_num = int(max(num_list))
num_list.remove(largest_num)
second_num = int(max(num_list))

for i in range(m) :
    if(cnt < k) :
        answer += largest_num
        cnt += 1
    else :
        cnt = 0
        answer += second_num

print(answer)