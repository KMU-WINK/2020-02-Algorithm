N, M = map(int,input().split())
cnt = 0

ice = []
for i in range(N):
  ice.append(list(map(int, input())))


def solve(x,y):
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False
    if int(ice[x][y]) == 0:
        ice[x][y] = 1

        solve(x-1,y)
        solve(x, y-1)
        solve(x, y+1)
        solve(x+1, y)

        return True

    return False




for height in range(N):
    for width in range(M):
        int(ice[height][width])
        if solve(height,width) == True:
            cnt += 1

print(cnt)

