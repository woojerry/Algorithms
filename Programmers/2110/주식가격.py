# 10/11
# 큐로 풀었을 때

from collections import deque


def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        price = queue.popleft()
        term = 0
        for i in queue:
            term += 1
            if price > i:
                break
        answer.append(term)

    return answer

# 큐로 안풀었을 때


def solution(prices):
    answer = []
    for i in range(len(prices)):
        term = 0
        for j in range(i+1, len(prices)):  # prices[i+1:]일 때는 시간 초과
            term += 1
            if prices[i] > prices[j]:
                break
        answer.append(term)

    return answer


print(solution([1, 2, 3, 2, 3]))
