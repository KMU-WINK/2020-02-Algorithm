case = int(input())
for i in range(case):
    k = int(input())
    n = int(input())
    List = [i for i in range(1, 15)]
    List2 = [i for i in range(1, 15)]
    for _ in range(k):
        for j in range(14):
            cnt = 0
            for h in range(j+1):
                cnt += List[h]
            List2[j] = cnt
        List = list(List2)
    print(List2[n-1])
