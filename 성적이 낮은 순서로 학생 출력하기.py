N = int(input())
p_list = {}
for i in range(N):
    name, grade = input().split()
    p_list[name] = grade

p_list = dict(sorted(p_list.items(),key=lambda x:x[1]))
for key, value in p_list.items():
    print(key, end=' ')


