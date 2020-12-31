cache = [0] * 100

def fib_cache(n):
    if n == 1 or n == 2: return 1
    if cache[n] != 0:
        return cache[n]

    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7))
print(fib_cache(7))
