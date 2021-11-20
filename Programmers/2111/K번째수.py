import copy


def solution(array, commands):
    answer = []

    for command in commands:
        start, end, k = command
        tmp = copy.deepcopy(array)
        cal = sorted(tmp[start-1:end])
        result = cal[k-1]
        answer.append(result)

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
