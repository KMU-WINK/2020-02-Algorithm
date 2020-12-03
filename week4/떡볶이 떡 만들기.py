import sys
N,M = (map(int, sys.stdin.readline().split()))
List = list(map(int, sys.stdin.readline().split()))
List.sort()
H = (N-1)//2
cnt =0
def getCnt(H):
    ans = 0
    for x in List:
        ans+=x-H if (x-H>=0) else 0
    return ans

def startEnd(H):
    if H>=0 and H+1<N-1:
        start = getCnt(List[H])
        end = getCnt(List[H+1])
        if start>=M and end<=M:
            return H
        elif start<=M:
            return startEnd(H-1)
        else:
            return startEnd(H+1)
    elif H==0 and getCnt(H)<=M:
        return List[0]

s = startEnd(H)
if s==List[0]:  #getCnt(List[0])<=M일때
    while(cnt<M): #cnt>=M일때까지
        cnt = getCnt(s)
        s-=1
    print(s)
else:
    e = List[s+1]
    for i in range(List[s],e+1):
        cnt= getCnt(i)
        if M<=cnt<M+1:
            print(i)
            break
