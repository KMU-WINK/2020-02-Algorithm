import sys
K,L = map(int, sys.stdin.readline().split())
array = [sys.stdin.readline().rstrip() for x in range(L)]
array.reverse()
def remove_duplicates(array):
    my_set = set()
    nonDupArray =[]
    for i in array:
        if i not in my_set:
            nonDupArray.append(i)
            my_set.add(i)
    return nonDupArray
array = remove_duplicates(array)
N = len(array)
if K<N:
    for i in range(K):
        print(array[-1-i])
else :
    for i in array[::-1]:
        print(i)