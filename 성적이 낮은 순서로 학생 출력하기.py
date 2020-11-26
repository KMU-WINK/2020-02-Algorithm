import operator

n = int(input())

students = {}
for i in range(n):
    name, score = input().split()
    students[name] = score

students = sorted(students, key=lambda student: student[1])

for student in students:
    print(student, end=' ')
