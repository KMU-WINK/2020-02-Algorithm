n= input()
row = int(n[1])
col = int(ord(row[0])-96)
cnt =0
moves = [(-2,-1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1)]
for i in moves:
    a= row+i[0]
    b= col+i[1]
    if a>0 and a<9 and b>0 and b<9:
        cnt+=1
print(cnt)