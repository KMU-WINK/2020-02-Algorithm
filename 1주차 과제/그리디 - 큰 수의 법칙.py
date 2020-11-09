n, m, k = map(int, input().split())
arr = [int(x) for x in input().strip().split()]
arr.sort(reverse=True)
first,second = arr[0],arr[1]

sum =int(first * (k * (m / (k + 1))) + second * (m / (k + 1)) + first * (m % (k + 1)))
print(sum)

