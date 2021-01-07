N = int(input())

r = int(input())

if(r > N):
    print("error")

df = [1 for _ in range(N+1)]

for i in range(0,N+1):
    tmp2 = df[0]
    for j in range(1,i):
        tmp = df[j]
        df[j] = tmp2 + df[j]
        tmp2 = tmp

print(df[r])
