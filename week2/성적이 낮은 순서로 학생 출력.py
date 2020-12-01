func = lambda x : (x[0], int(x[1])) # 형 변환
data = [func(input().split()) for i in range(int(input()))]
data.sort(key=lambda x : x[1])

[print(item[0], end=' ') for item in data]