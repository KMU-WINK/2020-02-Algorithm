import sys
input = lambda: sys.stdin.readline().rstrip()

firstCome, proposer = map(int, input().split())

studentNumber = {}
deStudentNumber = {}
numberList = list(range(proposer))

def studentCode(x):
    c = input()
    studentNumber[c] = x
    deStudentNumber[x] = c


list(map(studentCode, numberList))
answer = list(studentNumber.values())
answer.sort()

for i in answer[:firstCome]:
    print(deStudentNumber[i])

