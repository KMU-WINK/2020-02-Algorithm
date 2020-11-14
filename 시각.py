N = int(input())
Hour = 0
Min = 0
sec = 0
cnt = 0
while(True):
    sec += 1
    if sec//10 == 3 or sec % 10 == 3 or Min //10 == 3 or Min % 10 == 3 or Hour // 10 == 3 or Hour % 10 == 3:
        cnt += 1
    if sec == 60:
        sec = 0
        Min += 1
    if Min == 60:
        Min = 0
        Hour += 1
    if Hour == N and Min == 59 and sec == 59:
        break
print(cnt)