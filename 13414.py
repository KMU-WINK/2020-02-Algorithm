import sys

n, m = map(int, sys.stdin.readline().split())
numberList=[]
for i in range(m):
    number = sys.stdin.readline().strip()
    numberList.append(number)

numberList.reverse()

newList = []
newSet = set()
for i in numberList:
    if i not in newSet:
        newList.append(i)
        newSet.add(i)

newList.reverse()

if len(newList) >= n :
    for i in range(n):
        print(newList[i])
else:
    for i in range(len(newList)):
        print(newList[i])