# 10/10
import math


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)
    print(days)

    count, max = 1, days[0]
    for j in days[1:]:
        if j <= max:
            count += 1
        else:  # j > max:
            answer.append(count)
            max = j
            count = 1
    answer.append(count)  # if에서 끝났을 때 추가

    return answer


#print(solution([93, 30, 55], [1, 30, 5]))
#print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
