def change_time(time):
    if "PM" in time:
        return float(time.split("P")[0]) + 12
    else:
        return float(time.split("A")[0])


def solution(time, plans):
    answer = ''

    for plan in plans:
        country, start, arrive = plan[0], plan[1], plan[2]
        # start arrive를 각각 금, 월 기준으로 잘라서 시간계산
        cost = 0
        if 18 - change_time(start) > 0:
            cost += (18 - change_time(start))
        if change_time(arrive) - 13 > 0:
            cost += (change_time(arrive) - 13)

        if time >= cost:
            answer = country

    return answer


print(solution(3.5, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]))
