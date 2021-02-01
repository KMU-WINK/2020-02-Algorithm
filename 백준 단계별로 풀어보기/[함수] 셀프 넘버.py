originSet = set(range(1, 10000))

initNumber = set()

for nums in originSet:
    for num in str(nums):
        nums += int(num)

    if(nums < 10000):
        initNumber.add(nums)

print(*sorted(originSet.difference(initNumber)), sep="\n")