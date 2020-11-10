a = input()
location = list(a)

location[0] = ord(location[0]) -96
location[1] = int(location[1])

cnt = 0

if location[0] <= 6 :
    cnt += 2
    if location[1] == 1 or location[1] == 8 :
        cnt -= 1
if location[0] >= 3 :
    cnt += 2
    if location[1] == 1 or location[1] == 8 :
        cnt -= 1
if location[1] <= 6 :
    cnt += 2
    if location[0] == 1 or location[0] == 8 :
        cnt -= 1
if location[1] >= 3 :
    cnt += 2
    if location[0] == 1 or location[0] == 8 :
        cnt -= 1

print(cnt)