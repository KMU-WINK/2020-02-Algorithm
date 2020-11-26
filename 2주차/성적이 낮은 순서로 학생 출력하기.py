[print(i[0], end=" ") for i in sorted(dict([int(x) if i else x for i,x in enumerate(input().split())] for k in range(int(input()))).items(), key=lambda x: x[1])]
