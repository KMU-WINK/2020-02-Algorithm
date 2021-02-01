t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    floorList = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            floorList[i] += floorList[i-1]
    print(floorList[-1])