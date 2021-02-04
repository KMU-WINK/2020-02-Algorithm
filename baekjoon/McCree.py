import sys

N = int(sys.stdin.readline())
result = "success"
dots = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append([x, y])


def checkline(a, b, x, y):
    check = False

    if a == sys.maxsize and x == b:
        check = True

    if y == a * x + b:
        check = True

    return check


def findgra(dots):
    x1, y1 = dots[0][0], dots[0][1]

    gradient = {}
    count = 1
    check = 1

    while True:
        x2, y2 = dots[count][0], dots[count][1]

        if x1 == x2 and y1 == y2:
            count += 1
            continue

        gra = sys.maxsize if (x1 == x2) else (y2 - y1) / (x2 - x1)

        if gra in gradient:
            break

        gradient[gra] = 1
        count += 1

        if count == len(dots):
            x1, y1 = dots[check][0], dots[check][1]
            gradient = {}
            count = 0
            check += 1

        if check == len(dots):
            gra = "F"
            break

    return gra


def removedot(dots, a, b):
    dot = []
    for i in range(0, N):
        x, y = dots[i][0], dots[i][1]
        if not checkline(a, b, x, y):
            dot.append([x, y])

    return dot


def solve(dots):
    slope = findgra(dots)
    if slope == "F":
        print("failure")
        return
    b1 = dots[0][0] if slope == sys.maxsize else dots[0][1] - slope * dots[0][0]

    dot = removedot(dots, slope, b1)
    if len(dot) < 3:
        print("success")
        return
    slope2 = findgra(dot)
    if slope2 == "F":
        print("failure")
        return
    b2 = dot[0][0] if slope2 == sys.maxsize else dot[0][1] - slope2 * dot[0][0]
    result = "success"

    for i in range(N):
        x, y = dots[i][0], dots[i][1]
        if not(checkline(slope, b1, x, y) or checkline(slope2, b2, x, y)):
            result = "failure"
            break

    print(result)

if N < 5:
    print("success")

else:
    solve(dots)