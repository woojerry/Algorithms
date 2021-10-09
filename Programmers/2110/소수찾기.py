# 10/07
import math


def solution(n):
    answer = 0
    numbers = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if numbers[i] == True:
            j = 2
            while i*j <= n:
                numbers[i*j] = False
                j += 1

    for i in range(2, n+1):
        if numbers[i] == True:
            answer += 1

    return answer


print(solution(5))
