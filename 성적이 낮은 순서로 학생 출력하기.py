N = int(input())
p_list = {}
for i in range(N):
    name, grade = input().split()
    p_list[name] = grade

sorted(p_list.keys())
for key, value in p_list.items():
    print(key, end=' ')


