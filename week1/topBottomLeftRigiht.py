import sys, operator

n = int(sys.stdin.readline())
plan = list(sys.stdin.readline().split())

position = [1, 1]
moveValues = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}

for moveTo in plan:
    for i in range(2):
        if position[i] + moveValues[moveTo][i]: # 0 이상일때
            position[i] += moveValues[moveTo][i]

print(position)