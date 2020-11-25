N = int(input())

num = [x for x in input().split()]

row = 1
col = 1

for i in range(len(num)):
    if(num[i] == 'U'):
        if(row == 1):
            continue
        else:
            row -= 1

    elif(num[i] == 'D'):
        if(row == N):
            continue
        else:
            row += 1

    elif(num[i] == 'L'):
        if(col == 1):
            continue
        else:
            col -= 1

    elif(num[i] == 'R'):
        if(col == N):
            continue
        else:
            col += 1

print(row, col)