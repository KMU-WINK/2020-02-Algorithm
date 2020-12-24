import sys

X = int(input())

food = [int(x) for x in sys.stdin.readline().split()]

df = [0 for _ in range(X+1)]

df[1] = food[0]
df[2] = max(food[0],food[1])


for i in range(3,X+1):
    if(food[i-1]+df[i-2] > df[i-1]):
        df[i] = food[i-1]+df[i-2]

    else:
        df[i] = df[i-1]

print(df[X])