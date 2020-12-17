X = int(input())

df = [0 for i in range(X+1)]

state = [2,3,5]

for i in state:
    df[i] += 1

for i in range(1,X):
    for j in state:
        if(i * j > X):
            continue

        if(df[i*j] == 0):
            df[i*j] = df[i]+1

        elif(df[i*j] > df[i]+1):
            df[i*j] = df[i]+1

    if(df[i+1] == 0 or df[i+1] > df[i] + 1):
        df[i+1] = df[i] + 1


print(df[X])