N = int(input())
List = list(map(str,input().split()))
StarPo = [1,1]
for i in range(len(List)):
    if List[i] == 'R':
        StarPo[1] += 1
    elif List[i] == 'L':
        StarPo[1] -= 1
    elif List[i] == 'U':
        StarPo[0] -= 1
    else:
        StarPo[0] += 1

    if StarPo[0] == 0:
        StarPo[0] = 1
    if StarPo[1] == 0:
        StarPo[1] = 1
    if StarPo[0] == N+1:
        StarPo[0] = N
    if StarPo[1] == N+1:
        StarPo[1] = N
print("{} {}".format(StarPo[0],StarPo[1]))