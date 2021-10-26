# 10/26
# 9375 패션왕 신해빈

t = int(input())

for _ in range(1, t+1):
    dict = {}
    for i in range(int(input())):
        wear, type = input().split()
        dict[type] = dict.get(type, 0) + 1

    answer = 1
    for j in dict.values():
        answer *= j+1  # null까지해서 +1한 뒤, combinations 중 1개를 고르는 것이므로
    print(answer-1)  # 알몸인경우 제외
