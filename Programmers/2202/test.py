import math

def solution(progresses, speeds):
    answer = []
    
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    count, max = 1, days[0]
    for i in days[1:]:
        if i <= max:
            count +=1 
        else:
            answer.append(count)
            count = 1
            max = i
    answer.append(count)
    
    return answer

print(solution([93, 30, 55],[1, 30, 5]))