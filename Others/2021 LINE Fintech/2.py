import math


def solution(arr):
    answer = 0
    cand_list = []
    pre, post = 0, 1
    dir = False
    start, end = 0, 0

    while start < len(arr) - 2:
        for end in range(start, len(arr) - 1):
            if not dir:
                if arr[end] > arr[end+1]:
                    dir = True
                    if end == (len(arr) - 2):
                        cand_list.append(pre * post)
                elif arr[end] < arr[end+1]:
                    pre += 1
                else:
                    pre = 0
                    start = end + 1
                    break
                if end == (len(arr) - 2):
                    start = len(arr) - 2
                    break
            else:  # dir == True
                if arr[end] > arr[end+1]:
                    post += 1
                    if end == (len(arr) - 2):
                        cand_list.append(pre * post)
                        start = len(arr) - 1
                        break
                else:
                    cand_list.append(pre * post)
                    pre, post = 0, 1
                    dir = False
                    start = end
                    break

    for j in cand_list:
        answer += j

    answer = answer % (math.pow(10, 9) + 7)
    return int(answer)


#print(solution([0, 1, 2, 5, 3, 7]))
# print(solution([1, 2, 3, 2, 1]))
print(solution([1, 2, 3, 2, 1, 4, 3, 2, 2, 1]))
#print(solution([1, 2, 1, 2, 1]))
