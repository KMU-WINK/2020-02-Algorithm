N = int(input())
cnt= 0
threeN =0
for i in range(N):
    if '3' in str(i):
        threeN+=1
for i in range(59):
    if '3' in str(i):
        cnt+=1
num=0
num=cnt*(60-cnt+60)*(N-threeN+1)  #3이 포함되는 수 X
num+=threeN*(60*60)  #3, 13, 23시
print(num)
