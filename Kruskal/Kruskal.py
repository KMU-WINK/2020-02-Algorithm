import sys
M,N = map(int, sys.stdin.readline().split()) # M = 지점갯수, N = 주어질 루트 갯수
kruskal_input = []
for _ in range(N):
    S,D,L = map(int, sys.stdin.readline().split())
    kruskal_input.append([S-1,D-1,L])
kruskal_input.sort(key=lambda x:x[2],reverse=True) #cost가 큰 순으로 정렬-> pop으로꺼내기
checked = [[] for _ in range(M)]
def checkCycle(root):  # cycle이 만들어지는지 검사 True=> 사이클x, False=>사이클o Root[0] 첫번째에서 다른곳으로 경유 후 Root[1]로 오면 사이클
    if checked[root[0]] ==[] and checked[root[1]]==[]:
        return True
    for n in checked[root[0]]:
        if n[0] == root[1]:
            return False
        for i in checked[n[0]]:
            for j in checked[i[0]]:
                if i[0] == root[1] or j[0]==root[1]:
                    return False
    return True


root = kruskal_input.pop()
checked[root[0]].append([root[1],root[2]])
checked[root[1]].append([root[0],root[2]])
cnt = root[2]
for _ in range(N-1):
    root = kruskal_input.pop()
    # root추가했을때 사이클 도는지 안도는지 확인 후
    if (checkCycle(root)) : # 사이클이 돌면 추가 X
    # 사이클이 돌지 않으면 checked에 추가
        checked[root[0]].append([root[1],root[2]])
        checked[root[1]].append([root[0],root[2]])
        cnt+=root[2]

print(checked)
print(cnt)