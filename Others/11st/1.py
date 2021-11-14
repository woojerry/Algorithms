# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # 홀,짝 정수 중 가장 큰 것의 합
    pass
    odd_max = 0
    even_max = 0

    for i in A:
        if i % 2 == 0:
            if even_max == 0:
                even_max = i
            else:
                if even_max < i:
                    even_max = i

        else:
            if odd_max == 0:
                odd_max = i
            else:
                if odd_max < i:
                    odd_max = i

    answer = odd_max + even_max

    return answer


print(solution([5, 3, 10, 6, 11]))
