a = input()
location = list(a)

location[0] = ord(location[0]) -96
location[1] = int(location[1])

cnt = 0

def setCnt(idx) :
    global cnt
    cnt += 2
    if location[idx] == 1 or location[idx] == 8 :
        cnt -= 1
    
if location[0] <= 6 :
    setCnt(1)
if location[0] >= 3 :
    setCnt(1)
if location[1] <= 6 :
    setCnt(0)
if location[1] >= 3 :
    setCnt(0)

print(cnt)