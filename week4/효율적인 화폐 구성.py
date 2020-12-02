import sys
N,M = (map(int, sys.stdin.readline().split()))
money = [list(map(int, sys.stdin.readline().rstrip('\n'))) for _ in range(N)]  # [[2,],[3]]
money.sort(reverse=True)
money.append(0)
def count(change):
    for i in money[:N-1]:
        if change%i[0]==0:
            print(money.index(i),i[0])
            change-=i[0]
            money[-1]+=1
            return change
    return -1
while M!=0:
    if M==-1:
        print(-1)
        break
    M=count(M)
    if M==0:
        print(money[-1])
        break