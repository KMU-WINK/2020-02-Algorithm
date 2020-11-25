N, M = input().split()

N = int(N)
M = int(M)

num_list = []
result = []

for _ in range(N):
    num = [int(x) for x in input().split()]
    num_list.append(num)

for i in range(N):
    small = 10001
    for j in range(M):
        if(num_list[i][j] < small):
            small = num_list[i][j]

    result.append(small)

result.sort(reverse=True)

print(result[0])