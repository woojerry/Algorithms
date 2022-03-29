def solution(number, k):
    stack = []

    count = 0
    for num in number:
        # 뒤에 이전 숫자보다 큰 숫자가 나오면 stack에서 제거
        while count < k and stack and stack[-1] < num:
            stack.pop()
            count += 1

        stack.append(num)

    while count < k:  # number가 내림차순으로 진행 됐을 때의 처리
        stack.pop()
        count += 1

    print(stack)

    return ''.join(stack)


print(solution("1924", 2))
