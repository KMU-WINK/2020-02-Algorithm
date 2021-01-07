import functools

@functools.lru_cache()

def pascal(n, k) :
    if n == k:
        return 1
    elif k == 1 :
        return 1
    else :
        return pascal(n-1, k) + pascal(n-1, k-1)

print(pascal(6, 3))