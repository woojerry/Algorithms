# 10/11
from collections import deque


def solution(priorities, location):
    answer = 0
    printer = []
    queue = deque((p, i) for i, p in enumerate(priorities))

    while True:
        J = queue.popleft()

        if len(queue) == 0:
            printer.append(J)
            answer += 1
            break

        if J[0] >= max(queue)[0]:
            print(max(queue))
            printer.append(J)
            answer += 1
            if J[1] == location:
                break
        else:
            queue.append(J)

    return answer


print(solution([2, 1, 3, 2], 2))
