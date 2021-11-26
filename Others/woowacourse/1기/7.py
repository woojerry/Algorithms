from collections import deque


def solution(cryptogram):
    answer = ''
    alphabets = []
    filtered = []

    for i in cryptogram:
        alphabets.append(i)

    queue = deque(alphabets)

    tmp = queue.popleft()
    filtered.append(tmp)
    while(queue):
        el = queue.popleft()
        if el == tmp:
            filtered.pop()
            if len(filtered) > 0:
                tmp = filtered.pop()
                filtered.append(tmp)
            else:
                tmp = ''
        else:
            tmp = el
            filtered.append(el)

    for j in filtered:
        answer += j

    return answer


print(solution("browoanoommnaon"))
print(solution("zyelleyz"))
