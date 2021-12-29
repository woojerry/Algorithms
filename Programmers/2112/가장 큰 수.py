def solution(numbers):
    new_numbers = []

    max_num = max(numbers)
    size = len(str(max_num)) + 1  # size +1 해줘야함

    for num in numbers:
        # 튜플로
        new_numbers.append((num, str(num) * size))

    new_numbers.sort(reverse=True, key=lambda x: x[1])
    # 문자열은 앞에서부터 비교하므로
    answer = ''

    for nt in new_numbers:
        answer += str(nt[0])

    if sum(numbers) == 0:  # 모두 0인 경우, 예외처리
        answer = '0'

    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
