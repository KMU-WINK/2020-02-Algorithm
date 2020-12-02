import sys

N, M = tuple(map(int, sys.stdin.readline().split()))

rice_cake = [int(x) for x in sys.stdin.readline().split()]

rice_cake.sort(reverse = True)

zzal = 0 # 짤린 떡 세기위한 변수
big = rice_cake[0] # 기계가 가지는 최댓

while(zzal < M):
    zzal = 0
    big -= 1
    for i in range(len(rice_cake)):
        if(rice_cake[i] > big):
            zzal += rice_cake[i] - big

print(big)