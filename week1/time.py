import sys

n = int(sys.stdin.readline())

three = [i for i in range(60) if str(3) in str(i)]
count = 0

## 하 코드가 너무 마음에 안 든다..
for i in range(60):
    for j in range(60):
        if i in three or j in three:
            count += 1

count_ms = count

for i in range(n):
    count += 60 ** 2  if i in three else count_ms

print(count)