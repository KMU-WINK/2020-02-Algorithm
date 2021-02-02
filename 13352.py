import sys
from collections import Counter

def calSlope(dot1, dot2):
    if dot1[0]-dot2[0] == 0:
        m = 'slopeY'
    elif dot1[1]-dot2[1] == 0:
        m = 'slopeX'
    else :
        m = (dot1[1]-dot2[1]) / (dot1[0]-dot2[0])
    return m

n = int(sys.stdin.readline())

location=[]
for i in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    location.append([x, y])

answer = 'success'
selected=[]
if n >= 5:
    for i in range(5) :
        selected.append(location[i])

    slope=[[],[],[],[],[]]
    selected_slope = []
    slope_idx = 0
    count = 0
    for idx_i,i in enumerate(selected):
        for j in selected:
            m=0
            if i!=j:
                m = calSlope(i, j)
                slope[idx_i].append(m)
            else :
                slope[idx_i].append(' ')
        if len(slope[idx_i]) != len(set(slope[idx_i])):
            selected_slope=slope[idx_i]
            slope_idx=idx_i
            break;
        else:
            count += 1
            if count == 5:
                answer = 'failure'

    if answer == 'success':
        slope_value = ''
        for i in selected_slope:
            num = selected_slope.count(i)
            if num >= 2:
                slope_value = i

        idx_list = [i for i, value in enumerate(selected_slope) if value == slope_value]
        idx_list.append(slope_idx)
        for idx, i in enumerate(location):
            if idx not in idx_list:
                m = calSlope(i, location[idx_list[0]])
                if m == slope_value:
                    idx_list.append(idx)
        first = 0
        for idx, i in enumerate(location):
            if idx not in idx_list:
                first = idx
                break;

        first_slope = ''
        cnt = 0
        for idx, i in enumerate(location):
            if idx not in idx_list and idx != first:
                m = calSlope(i, location[first])
                if first_slope != m:
                    first_slope = m
                    cnt += 1
                    if cnt > 1:
                        answer = 'failure'
                        break;

print(answer)