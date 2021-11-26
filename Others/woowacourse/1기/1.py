def solution(money):
    answer = []
    type = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

    for i in type:
        cnt = 0
        if money // i > 0:
            cnt, money = divmod(money, i)
        answer.append(cnt)

    return answer


print(solution(50237))
print(solution(15000))
