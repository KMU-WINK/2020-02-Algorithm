int_input = lambda : list(map(int, input().split()))
n, k = int_input()
a, b = int_input(), int_input()

for i in range(k):
    a_idx, b_idx = a.index(min(a)), b.index(max(b)) # 최소값 최대 값의 위치를 찾아 swap 한다
    a[a_idx], b[b_idx] = b[b_idx], a[a_idx]

print(sum(a))

