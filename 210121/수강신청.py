import sys
K,L = map(int, sys.stdin.readline().split())
array = [sys.stdin.readline().rstrip() for x in range(L)]
nonDupArray =[]
for i in array: #중복 검사
    if (i not in nonDupArray) :
        nonDupArray.append(i)
    else :
        nonDupArray.remove(i)
        nonDupArray.append(i)
for i in nonDupArray[:K]:
    print(i)
    #시간초과나서 set으로 다시한번 풀어볼 예정~