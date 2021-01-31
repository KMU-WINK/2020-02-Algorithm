import sys
from functools import reduce
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

def loserSearch(avr, scores):
    temp = 0
    for score in scores:
        if (avr < score):
            temp += 1

    return temp

while T > 0:
    n, *scoreList = map(int, input().split())

    avrScore = reduce(lambda x, y: x + y, scoreList) / n
    loser = loserSearch(avrScore, scoreList)
    print('%0.3f' % ((loser / n) * 100) + '%')

    T -= 1
