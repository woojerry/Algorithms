# 10/17
# 문제파악 주의
# 효율성 때문에 확인할 때 해시 사용
def solution(phone_book):
    answer = True
    dict = {}
    for i in phone_book:
        dict[i] = dict.get(i, 0) + 1
    for phone_numbers in phone_book:
        tmp = ''
        for numbers in phone_numbers:
            tmp += numbers
            if tmp in dict and tmp != phone_numbers:
                answer = False

    return answer


print(solution(["119", "97674223", "1195524421"]))
