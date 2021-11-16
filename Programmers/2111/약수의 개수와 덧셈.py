# 11/16

def find(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count


def solution(left, right):
    answer = 0

    for j in range(left, right + 1):
        if find(j) % 2 == 0:
            answer += j
        else:
            answer -= j

    return answer
