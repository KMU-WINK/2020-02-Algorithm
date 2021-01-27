# 이게 맞는지는 모르겠는데... 일단 파스칼 삼각형을 출력해보았습니다...

row = int(input()) + 1

for rowNumber in range(row):
    list = 1
    PList = [list]
    print('1', end=" ")

    for i in range(rowNumber):
        list = list * (rowNumber-i) * i / (i+1)
        PList.append(int(list))
        print(str(int(list)).rjust(3), end=" ")
    print()