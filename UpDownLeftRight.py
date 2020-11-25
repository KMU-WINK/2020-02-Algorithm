n = int(input())
num_list = list(input().split())
answer = [1, 1]

for i in num_list:
    if i == 'R' :
        if answer[1] != n :
            answer[1] += 1
        print(answer)
    elif i == 'U' :
        if answer[0] != 1 :
            answer[0] -= 1
        print(answer)
    elif i == 'D' :
        if answer[0] != n :
            answer[0] += 1
        print(answer)
    else :
        if answer[1] != 1 :
            answer[1] -= 1
        print(answer)