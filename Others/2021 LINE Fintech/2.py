import itertools


def solution(arr):
    answer = 0
    sub_list = []

    changed = False
    change_i = 0
    after = 0
    for i in range(1, len(arr) - 2):

        if not changed:
            if arr[i] > arr[i+1]:
                changed = True
                change_i = i+1
        else:
            if arr[i] < arr[i+1]:
                after = i - change_i

                break
    print(after * (change_i - 2))
    return answer


print(solution([0, 1, 2, 5, 3, 7]))
