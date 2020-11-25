N = int(input())
A =[]
for i in range(N):
    A.append(int(input()))
A.sort(reverse=True)
for i in A:
    print(i,end=" ")