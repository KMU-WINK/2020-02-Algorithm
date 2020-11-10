N, M = input().split()

N = int(N)
M = int(M)

count = 0
mmap = []
dir = [[0,-1], [-1,0], [0,1], [1,0]]

inputed = [int(x) for x in input().split()]

Crow = inputed[0]
Ccol = inputed[1]
direction = inputed[2]

for i in range(N):
    row = [int(x) for x in input().split()]
    mmap.append(row)


def searchMap(row, col, direction):
    count = direction
    answer = 0
    for i in range(4):
        if(mmap[row+dir[count][0]][col+dir[count][1]] == 0):
            answer += 1
            mmap[row + dir[count][0]][col + dir[count][1]] = 1
            answer += searchMap(row+dir[count][0],col+dir[count][1], count)

        if(count == 3):
            count = 0
        else:
            count += 1

    return answer

answer = searchMap(Crow, Ccol, direction)

print(answer)