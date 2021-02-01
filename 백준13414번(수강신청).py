K, L = map(int, input().split())

students = []

for n in range(L):
    classNumber = int(input())
    students.append(classNumber)

for i in range(len(students)-1):
    for j in range(i+1, len(students)-1):
        if students[i] == students[j]:
            del students[i]

for i in range(K):
    print(students[i])