# 첫번째 방법

# import sys
#
# able, total = map(int, sys.stdin.readline().split())
#
# number = {}
# check = {}
#
# for i in range(total):
#     num = sys.stdin.readline().rstrip()
#     number[num] = i
#     check[i] = num
#
# count = 0
#
# while able > 0:
#     if count >= total:
#         break
#
#     if count == number[check[count]]:
#         print(check[count])
#         able -= 1
#
#     count += 1


# 두번째 방법 (더 빠름)

import sys

able, total = map(int, sys.stdin.readline().split())

number = {}

for i in range(total):
    num = sys.stdin.readline().rstrip()
    number[num] = i

answer = sorted(number, key = lambda x : number[x])

for i in range(able):
    if i >= len(answer):
        break
    print(answer[i])

