# 10/28

def solution(sizes):
    answer = 0
    weights = []
    heights = []

    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i].reverse()

    for w, h in sizes:
        weights.append(w)
        heights.append(h)

    answer = max(weights) * max(heights)

    return answer


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
