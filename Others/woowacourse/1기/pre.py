def solution(v):
    answer = []
    x = {}
    y = {}
    for i in v:
        x[i[0]] = x.get(i[0], 0) + 1
        y[i[1]] = y.get(i[1], 0) + 1

    for j in x:
        if x[j] == 1:
            answer.append(j)

    for k in y:
        if y[k] == 1:
            answer.append(k)

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))
