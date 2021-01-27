import sys

def checkpeople(k, n):
    apart = [i for i in range(n+1)]
    for i in range(k):
        for j in range(2,n+1):
            apart[j] = apart[j-1] + apart[j]

    return apart[n]


T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(checkpeople(k,n))