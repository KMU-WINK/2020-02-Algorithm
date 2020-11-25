position = input()

count = 0
row = position[1]
row = int(row)
colcheck = position[0]

Alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(8):
    if(colcheck == Alpha[i]):
        col = i+1
        break


move = [[-1,2],[-2,1],[-1,-2],[-2,-1],[1,2],[2,1],[1,-2],[2,-1]]

for i in range(len(move)):
    if(1 <= col + move[i][0] and col + move[i][0] <= 8):
        if (1 <= row + move[i][1] and row + move[i][1] <= 8):
            count += 1


print(count)