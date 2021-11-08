

def solution(arr):
    answer = [0] * 3
    storage = [0] * 3
    dic = {}

    for i in arr:
        if i == 1:
            storage[0] += 1
        elif i == 2:
            storage[1] += 1
        elif i == 3:
            storage[2] += 1

    pivot = max(storage)

    for j in range(len(storage)):
        if storage[j] != pivot:
            insert = pivot - storage[j]
            answer[j] = insert

    return answer


#print(solution([2, 1, 3, 1, 2, 1]))
print(solution([3, 3, 3, 3, 3, 3]))
