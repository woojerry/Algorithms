# 11/17

def solution(nums):
    answer = 0

    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1

    if len(dic) >= len(nums) / 2:
        answer = len(nums) // 2
    else:
        answer = len(dic)

    return answer


print(solution([3, 1, 2, 3]))
