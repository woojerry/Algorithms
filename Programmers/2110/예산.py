# 10/07

def solution(d, budget):
    d.sort()
    answer = 0

    for i in d:
        if(budget >= i):
            budget -= i
            answer += 1
    return answer
