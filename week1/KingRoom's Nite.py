import sys

moveValues = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
args = sys.stdin.readline()
location = [ord('a') - ord(args[0]) + 1, int(args[1])]

count = 0
for moveTo in moveValues:
    if location[0] + moveTo[0] > 0 and location[1] + moveTo[1] > 0:
        count += 1

print(count)