n, m, k = map(int, input().split()) # n: 리스트 원소 수, m: m번 연속으로 더함, k: 가장 큰 수는 k만큼 더함
# input().split()의 결과는 문자열 리스트
# 리스트의 요소를 map(int, x)를 통해 int로 변환 결과는 맵 객체로 나옴
# 맵 객체는 변수 여러개에 저장이 가능함

dongbinList = list(map(int, input().split()))
dongbinList.sort()

bigCost = dongbinList[-1] # 제일 큰 수
secondCost = dongbinList[-2] # 두번째로 큰 수

answer = 0

while True:
    for i in range(k):
        if m == 0:
            break
        answer += bigCost
        m -= 1
    if m == 0:
        break
    answer += secondCost
    m -= 1

print(answer)
