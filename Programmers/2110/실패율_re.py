# 10/15

def solution(N, stages):
    answer = []
    list = []

    fail_rates = []
    users = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)
        if users == 0:  # 스테이지에 도달한 유저가 없는 경우
            fail_rate = 0
        else:
            fail_rate = count / users

        fail_rates.append(fail_rate)
        users -= count

    for index, value in enumerate(fail_rates):
        list.append((index + 1, value))

    list = sorted(list, key=lambda x: x[1], reverse=True)

    for j in (list):
        answer.append(j[0])
    return answer

#solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
#solution(8, [1, 2, 3, 4, 5, 6, 7])
