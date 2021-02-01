T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    residents = [x for x in range(1, n+1)]
    for j in range(k):
        for a in range(1, n):
            residents[a] += residents[a-1]
    print(residents[-1])