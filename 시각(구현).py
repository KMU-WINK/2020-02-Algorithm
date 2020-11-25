N  = input()
count = 0

for i in range(0, int(N)+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
