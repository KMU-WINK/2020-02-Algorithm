import sys

input = lambda: sys.stdin.readline().rstrip()

value = int(input())

def isometricSequence(value):
    if value < 100:
        return value

    numbers = list(range(1, value + 1))
    answer = 0

    for number in numbers:
        termList = []

        for term in str(number):
            termList.append(int(term))

        if len(termList) < 3:
            answer += 1
        else:
            checker = True
            rate = termList[1] - termList[0]
            for i in range(1, len(termList)):
                if termList[i] - termList[i - 1] != rate:
                    checker = False
                    break

            if checker:
                answer += 1

    return answer

print(isometricSequence(value))