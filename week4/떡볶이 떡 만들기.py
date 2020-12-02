import sys
N,M = (map(int, sys.stdin.readline().split()))
List = list(map(int, sys.stdin.readline().split()))
List.sort()
H = List[(N-1)//2]
h=H
cnt =0

def getCnt(h):
    ans = 0
    for l in List:
        if l>=h:
            ans += l - h
    return ans

while(cnt!=M):
    cnt = getCnt(h)
    if h>List[-1]:
        h = H-1
    else:
        h+=1
        cnt=getCnt(h)
print(h)