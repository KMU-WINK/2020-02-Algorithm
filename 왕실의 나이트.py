pos = input()
pos_List = [ord(pos[:1])-96, int(pos[1:])]
cnt = 0
List = [[1,2],[-1,2],[-2,-1],[-2,1],[-1,-2],[1,-2],[2,1],[2,-1]]
for i in range(len(List)):
    if 8>= pos_List[0] + List[i][0] >=1 and 8>= pos_List[1] +List[i][1] >= 1:
        cnt += 1

print(cnt)

