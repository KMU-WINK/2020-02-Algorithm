N = int(input())
movingPlan = list(input().split())
coordinate = [1, 1]

for i in range(len(movingPlan)):
    if movingPlan[i] == 'L':
        if coordinate[1] == 1:
            pass
        else:
            coordinate[1] -= 1
    elif movingPlan[i] == 'R':
        if coordinate[1] == N:
            pass
        else:
            coordinate[1] += 1
    elif movingPlan[i] == 'U':
        if coordinate[0] == 1:
            pass
        else:
            coordinate[0] -= 1
    elif movingPlan[i] == 'D':
        if coordinate[0] == N:
            pass
        else:
            coordinate[0] += 1
    else:
        print("Please input correct plan")

print(coordinate[0], coordinate[1])