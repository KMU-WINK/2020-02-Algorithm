n = int(input())

hours = list(map(str, list(range(n + 1))))
minutes = list(map(str, list(range(60))))
seconds = list(map(str, list(range(60))))

cnt = 0

for i in hours :
    for j in minutes :
        for k in seconds :
            if '3' in j or '3' in k or '3' in i:
                cnt += 1
                
print(cnt)