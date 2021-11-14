# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    dic = {}

    for i in A:
        dic[i] = dic.get(i, 0) + 1

    answer = 0

    for j in dic:
        # if j == dict[j] 할거없음
        if j != dic[j]:
            if abs(j - dic[j]) < dic[j]:
                answer += abs(j - dic[j])
            elif abs(j - dic[j]) >= dic[j]:
                answer += dic[j]

    return answer


print(solution([1, 1, 3, 4, 4, 4]))
